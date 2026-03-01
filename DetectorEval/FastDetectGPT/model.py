# Copyright (c) Guangsheng Bao.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree. 
# Modified 2026.
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import time
import os

def from_pretrained(cls, model_name, kwargs, cache_dir):
    # use local model if it exists
    local_path = os.path.join(cache_dir, 'local.' + model_name.replace("/", "_"))
    if os.path.exists(local_path):
        return cls.from_pretrained(local_path, **kwargs)
    return cls.from_pretrained(model_name, **kwargs, cache_dir=cache_dir)

# predefined models
model_fullnames = { 
                    'llama3-8b': 'meta-llama/Meta-Llama-3.1-8B',
                    'llama3-8b-instruct': 'meta-llama/Meta-Llama-3.1-8B-Instruct',
                    'falcon-7b': 'tiiuae/falcon-7b',
                    'falcon-7b-instruct': 'tiiuae/falcon-7b-instruct',
                    }
float16_models = ['llama3-8b', 'llama3-8b-instruct', 'falcon-7b', 'falcon-7b-instruct']

def get_model_fullname(model_name):
    return model_fullnames[model_name] if model_name in model_fullnames else model_name

def load_model(model_name, device, cache_dir):
    model_fullname = get_model_fullname(model_name)
    print(f'Loading model {model_fullname}...')
    model_kwargs = {}
    if model_name in float16_models:
        model_kwargs.update(dict(torch_dtype=torch.float16))
    if 'gpt-j' in model_name:
        model_kwargs.update(dict(revision='float16'))
    model = from_pretrained(AutoModelForCausalLM, model_fullname, model_kwargs, cache_dir)
    print('Moving model to GPU...', end='', flush=True)
    start = time.time()
    model.to(device)
    print(f'DONE ({time.time() - start:.2f}s)')
    return model

def load_tokenizer(model_name, cache_dir):
    model_fullname = get_model_fullname(model_name)
    optional_tok_kwargs = {}
    optional_tok_kwargs['padding_side'] = 'right'
    base_tokenizer = from_pretrained(AutoTokenizer, model_fullname, optional_tok_kwargs, cache_dir=cache_dir)
    if base_tokenizer.pad_token_id is None:
        base_tokenizer.pad_token_id = base_tokenizer.eos_token_id
        if '13b' in model_fullname:
            base_tokenizer.pad_token_id = 0
    return base_tokenizer