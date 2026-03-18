## (1) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2016/test/286674e3082feb7e5afb92777e48821f/level4/gemma-3-27b-it/level4@NAV:::3.txt
### Human review:

The manuscript presents a set of algorithms for clustering over graphs, and for testing whether two cluster assignments are similar. As mentioned above, although the algorithms themselves are clear, their motivation and the reason why they appear as a list of algorithms is not well explained. The algorithms themselves are modifications of existing ones, and the only novelty is the constraints presented at the end.

### Polished review:

The manuscript details algorithms for graph clustering and a method for comparing the similarity of different clusterings. While the algorithmic descriptions are readily understandable, the overarching motivation connecting these algorithms—and the rationale for presenting them as a collection—remains unclear. The presented work largely builds upon established algorithms, with the primary novelty residing in the constraints introduced towards the conclusion of the paper.





## (2) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2016/test/286674e3082feb7e5afb92777e48821f/level4/meta-llama-Llama-3.1-70B-Instruct-AWQ-INT4/level4@NAV:::6.txt
### Human review:

In the paper the authors try to come up with a theory which works for graph clustering in model free framework. However, the result is naive and unconvincing. In the paper the authors try to come up with a theory which works for graph clustering in model free framework. However, the result is naive and unconvincing. The authors pretend to construct a new theory but theit theory is just a naive handwaving. Just to give a couple of examples: Theorem 1 (Generic Theorem) ... "which also fits G well is close to C" ... Proposition 3 (Informal) ... "under standard recovery conditions" ...

### Polished review:

The authors attempt to develop a theory for graph clustering within a model-free framework. Unfortunately, their result falls short, appearing overly simplistic and unconvincing. Rather than presenting a genuinely novel theory, the authors seem to be relying on unsubstantiated claims. For instance, Theorem 1 (Generic Theorem) contains vague assertions, such as "...which also fits G well is close to C". Similarly, Proposition 3 (Informal) lacks rigor, relying on ambiguous "standard recovery conditions".

## (3) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2016/test/286674e3082feb7e5afb92777e48821f/level4/meta-llama-Llama-3.1-70B-Instruct-AWQ-INT4/level4@NAV:::3.txt
### Human review:

The manuscript presents a set of algorithms for clustering over graphs, and for testing whether two cluster assignments are similar. As mentioned above, although the algorithms themselves are clear, their motivation and the reason why they appear as a list of algorithms is not well explained. The algorithms themselves are modifications of existing ones, and the only novelty is the constraints presented at the end.

### Polished review:

This manuscript introduces a collection of algorithms designed for graph-based clustering and evaluating the similarity between cluster assignments. However, the underlying motivation for these algorithms and the rationale behind presenting them as a series of distinct methods remains unclear. Upon closer examination, it becomes apparent that the algorithms themselves are adaptations of existing techniques, with the primary innovation being the constraints introduced in the later sections.

## (4) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2016/test/286674e3082feb7e5afb92777e48821f/level4/gemini-2.5-pro/level4@NAV:::6.txt
### Human review:

In the paper the authors try to come up with a theory which works for graph clustering in model free framework. However, the result is naive and unconvincing. In the paper the authors try to come up with a theory which works for graph clustering in model free framework. However, the result is naive and unconvincing. The authors pretend to construct a new theory but theit theory is just a naive handwaving. Just to give a couple of examples: Theorem 1 (Generic Theorem) ... "which also fits G well is close to C" ... Proposition 3 (Informal) ... "under standard recovery conditions" ...

### Polished review:

The authors propose a theoretical framework for model-free graph clustering. However, the theoretical development lacks the necessary rigor, and the results are not sufficiently substantiated. The paper puts forward a new theory, but the core arguments rely more on high-level intuition than on precise mathematical definitions and formal proofs.

This lack of precision is evident in several key statements. For instance:
*   In Theorem 1 (Generic Theorem), the phrase "...which also fits G well is close to C..." is used without formally defining the concepts of "fits well" or the metric for being "close."
*   Similarly, Proposition 3 (Informal) is presented "...under standard recovery conditions..." without explicitly stating which conditions are being assumed, making the claim difficult to verify or build upon.

## (5) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2016/test/286674e3082feb7e5afb92777e48821f/level4/Qwen3-30B-A3B-Thinking-2507-FP8/level4@NAV:::3.txt
### Human review:

The manuscript presents a set of algorithms for clustering over graphs, and for testing whether two cluster assignments are similar. As mentioned above, although the algorithms themselves are clear, their motivation and the reason why they appear as a list of algorithms is not well explained. The algorithms themselves are modifications of existing ones, and the only novelty is the constraints presented at the end.

### Polished review:



The manuscript introduces a collection of algorithms for graph clustering and for assessing the similarity between cluster assignments. While the algorithms themselves are clearly presented, their underlying motivation and the rationale for presenting them as a distinct set are inadequately justified. The proposed methods constitute adaptations of existing approaches, with the sole novelty residing in the constraints introduced at the conclusion.

## (6) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2015/test/310dcbbf4cce62f762a2aaa148d556bd/level4/meta-llama-Llama-3.1-70B-Instruct-AWQ-INT4/level4@NAV:::4.txt
### Human review:

Since this is a short review, I only ask one question: what is the reason that boundary cases have to be analyzed differently? It doesn't seem that rho = q_j appears anyhow special, especially for j > 1. This paper analyzes contextual bandits against a stronger baseline: one that uses adaptive linear programming to decide to pass on certain percent of suboptimal rounds (what the authors call budget). It has interesting setup and unique solutions.

### Polished review:

The authors present an intriguing analysis of contextual bandits in comparison to a more robust baseline that employs adaptive linear programming to strategically opt out of a predetermined percentage of suboptimal rounds, referred to as the 'budget'. This setup is notable, and the proposed solutions are distinct and worthy of consideration. However, one aspect that warrants further clarification is the rationale behind the disparate treatment of boundary cases. Specifically, it is unclear what makes the value rho = q_j uniquely significant, particularly for j greater than 1.

## (7) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2015/test/15de21c670ae7c3f6f3f1f37029303c9/level4/meta-llama-Llama-3.1-70B-Instruct-AWQ-INT4/level4@NAV:::1.txt
### Human review:

I think that the main issue of the manuscript is a lack of awareness of the literature on the topic. The authors' algorithm is strongly related to the Monte Carlo EM algorithm (and in fact the general class of stochastic approximation algorithms with markovian dynamic which have been proposed in various forms to optimize intractable likelihood functions). There is a well developed literature on the topic and the authors should compare what they have been doing to existing work. A theory which includes some of the authors' results already exists and covers much more general scenarios. For example the Markov chains are not required to be uniformly ergodic and there is no need to reinitialise the Markov chain at a fixed distribution r at each iteration (the authors acknowledge that they do this in order to simplify their analysis, but this is not sufficient--in addition reinitializing with the previous sample may be a better idea, as discussed at the end of the manuscript, and these algorithms have also been extensively analysed previously). The presentation of the results is far from optimal : for example for Theorem 1 and 2 it is not clear what the assumptions are? One can refer to the text before and after, but the reader should not have to do that. Note also that there is no need for the strong assumptions used in order to develop results such as those of Theorem 6 (see for example Benveniste, Metivier and Priouret for more general results). I think that the authors lack awareness of the literature and the results are only marginally novel.

### Polished review:

The primary concern with this manuscript is its apparent lack of engagement with the existing literature on the topic. The authors' algorithm bears a strong resemblance to the Monte Carlo EM algorithm, as well as the broader class of stochastic approximation algorithms with Markovian dynamics that have been proposed to optimize intractable likelihood functions. A thorough review of the literature would reveal that the authors' work has been preceded by a well-established theoretical framework that encompasses many of their results and extends to more general scenarios. Notably, the requirement for uniformly ergodic Markov chains and the reinitialization of the Markov chain at a fixed distribution r at each iteration are not necessary, as demonstrated by existing research. In fact, reinitializing with the previous sample, as mentioned in the manuscript, has been extensively analyzed in prior studies. The presentation of the results could be improved, particularly in theorems 1 and 2, where the assumptions are not clearly stated and require the reader to refer to surrounding text. Furthermore, the strong assumptions used to derive results like Theorem 6 are unnecessary, as more general results have been established in the literature (e.g., Benveniste, Metivier, and Priouret). Overall, the authors' lack of familiarity with the existing literature diminishes the novelty of their results, which are only marginally new.

## (8) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2013/test/24681928425f5a9133504de568f5f6df/level4/meta-llama-Llama-3.1-70B-Instruct-AWQ-INT4/level4@NAV:::2.txt
### Human review:

This paper presents a method for learning the structure as well as the parameters of stochastic AND-OR grammars. Such grammars contain AND rules and OR rules and can be used to represent several recursive phenomena, including natural language and even grammars. The authors present a nice method for unsupervised structure learning of these grammars by introducing new AND-OR fragments at consecutive steps, and measuring the likelihood and prior gains of their model. 
The authors present experiments on two tasks: learning event grammars and learning image grammars. In both they achieve results that are competitive with prior art. 
I liked the overall paper as it seems to be a tractable way of learning stochastic grammars that can be modeled using AND and OR rules. My criticism of the paper stems from the following observations: 
1) The authors do not mention how tractable the learning algorithm is. Will it scale to thousands of datapoints? 
2) I would have liked to seen experiments on natural language sentences as natural language is the most obvious application of such grammars. Will it be even possible to learn using the presented methods on the Penn Treebank dataset for example, on which previous work has focused on (say, Klein and Manning)? This paper presents a way of estimating the structure and parameters of stochastic AND-OR grammars and presents nice results on two tasks; I would have liked to see more experiments, especially on natural language data.

### Polished review:

This paper proposes a novel approach to learning the structure and parameters of stochastic AND-OR grammars, which are capable of modeling recursive phenomena such as natural language and images through the use of AND and OR rules. The authors introduce a method for unsupervised structure learning by iteratively incorporating new AND-OR fragments and evaluating the model's likelihood and prior gains. 

Experimental results are presented for two tasks: event grammar learning and image grammar learning, where the proposed method achieves competitive performance with existing state-of-the-art approaches. 

Overall, the paper presents a promising framework for learning stochastic AND-OR grammars using AND and OR rules. However, there are some limitations that need to be addressed. 

Two major concerns arise from the paper: 
1) The authors do not provide an assessment of the learning algorithm's scalability. It is unclear whether the method can be efficiently applied to large datasets with thousands of data points. 
2) The paper would benefit from additional experiments, particularly on natural language data, which represents a more intuitive application of stochastic AND-OR grammars. For instance, evaluating the method on the Penn Treebank dataset, which has been used in previous studies (e.g., Klein and Manning), would provide valuable insights into its performance on real-world natural language processing tasks. While the paper demonstrates the effectiveness of the proposed approach on two tasks, further experimentation is necessary to fully explore its capabilities.

## (9) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/iclr_2017/test/333/level4/gemma-3-27b-it/level4@NAV:::2.txt
### Human review:

This paper provides an interesting analysis of the conditions which enable generation of natural looking textures. The results is quite surprising, and analysis is quite thorough. 
I do think the evaluation methods require more work, but as other reviewers mentioned this could be an interesting line of work moving forwards and does not take too much from this current paper which, I think, should be accepted.

### Polished review:

This paper presents a compelling analysis of the factors governing the generation of realistic textures. The findings are noteworthy and the analysis is comprehensive. 

While the evaluation methodologies could benefit from further development – a point also raised by other reviewers – this work represents a promising direction for future research. This does not significantly detract from the current contribution, which I recommend accepting.





## (10) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/iclr_2017/test/333/level4/meta-llama-Llama-3.1-70B-Instruct-AWQ-INT4/level4@NAV:::2.txt
### Human review:

This paper provides an interesting analysis of the conditions which enable generation of natural looking textures. The results is quite surprising, and analysis is quite thorough. 
I do think the evaluation methods require more work, but as other reviewers mentioned this could be an interesting line of work moving forwards and does not take too much from this current paper which, I think, should be accepted.

### Polished review:

This manuscript presents an intriguing examination of the conditions that facilitate the generation of visually authentic textures. The findings are unexpected, and the analysis is comprehensive. 

Although I believe the evaluation methodologies could benefit from further refinement, as noted by other reviewers, this study has the potential to be an exciting area of future research. However, this limitation does not detract from the current paper's contributions, and I recommend its acceptance.

## (11) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/iclr_2017/test/333/level4/gemini-2.5-pro/level4@NAV:::2.txt
### Human review:

This paper provides an interesting analysis of the conditions which enable generation of natural looking textures. The results is quite surprising, and analysis is quite thorough. 
I do think the evaluation methods require more work, but as other reviewers mentioned this could be an interesting line of work moving forwards and does not take too much from this current paper which, I think, should be accepted.

### Polished review:

This paper presents an insightful study of the conditions required for generating natural-looking textures. The results are unexpected, and the analysis is commendably thorough.

While the evaluation protocol could be improved, this represents a promising avenue for future work and does not significantly detract from the contributions of this paper. In my opinion, this work warrants acceptance.

## (12) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2016/test/286674e3082feb7e5afb92777e48821f/level4/Qwen3-30B-A3B-Thinking-2507-FP8/level4@P1NOPDF:::2.txt
### Human review:

The paper gives a relationship between different distances of clustering. The paper considers the network models such as Preference Frame Model (PFM) and Stochastic Block Model (SBM) and proves a locally convex-like property for clustering. It is shown that for any two clusterings, which estimate the parameters of the model fitted to the network data equally well, are also near each other in terms of mis-classification distance measures. The paper gives a nice property of clusterings in network data. The property of equivalence between the different measures of distance of clusterings for network data has been stated and proved in the paper. The paper gives both theoretical and experimental validations of the results stated in the paper. The results given in the paper are novel, but there has been recently some works of similar flavor in network literature like Peng, Sun and Zanetti (COLT, 2015), Chao, Lu, Ma, Zhou (Arxiv, 2015). The theoretical parts of the paper are also quite simple extensions of well-known results. As mentioned in the paper, the work can have some applications in detecting clusterability, but the formal results in that regard were not provided in the paper. The paper is well-written and explains the core ideas of the paper quite lucidly.

### Polished review:



This paper establishes a relationship between different distance metrics for clustering in network data, focusing on models like the Preference Frame Model (PFM) and Stochastic Block Model (SBM). The authors prove a local convexity property for clustering: for any two clusterings that estimate model parameters equally well, they must also be close in terms of misclassification distance. This equivalence between different distance measures for network clustering is a notable contribution, rigorously established and supported by both theoretical analysis and experimental validation.

While the results are novel, the work builds on recent literature with similar themes, including Peng et al. (COLT 2015) and Chao et al. (arXiv 2015). The theoretical framework, however, relies on straightforward extensions of well-known results rather than substantial new mathematical insights. The paper also suggests potential applications in clusterability detection, but fails to provide formal results or analysis in this direction, leaving the practical utility somewhat underdeveloped.

The writing is clear and well-structured, with the core ideas effectively articulated. The experimental section adequately supports the theoretical claims. However, the novelty claim requires careful contextualization against existing work on network clustering distances. The absence of concrete applications or formal guarantees for clusterability detection represents a missed opportunity to strengthen the contribution's impact. Despite these limitations, the paper presents a coherent and technically sound argument for the equivalence of distance measures in the specified network models.

## (13) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2015/test/2f25f6e326adb93c5787175dda209ab6/level4/Qwen3-30B-A3B-Thinking-2507-FP8/level4@P1NOPDF:::3.txt
### Human review:

The paper proposes approximate inference techniques for determinantal point process (DPP) that do not require spectral knowledge of the kernel defining the DPP. Instead, inducing inputs are utilized to bound the likelihood, which reduces the computational cost. Both variational inference and approximate Markov chain Monte Carlo (MCMC) techniques are described and their efficiency is demonstrated empirically.
 I believe there is merit to this paper, however I found the method description rather rough and empirical evaluation not thorough enough. A few points that may help clarify:
 1) How does the computational complexity and overall compute time of the two proposed methods compare?
2) How do the proposed methods compare to other alternatives, both approximate and exact, in terms of quality of approximation and computation time?
3) Empirical results on the toy data in Section 5.1 show that parameter estimation error using variational inference is too large, and resorts to approximate MCMC instead. In what settings does the proposed variational inference expected to work and when is it expected to fail? Why?
4) A 13-point sample is generated for the toy example. How do the methods perform when the inducing inputs are actually these sampled points?
5) Is there a rule of thumb to follow when selecting a) the number of inducing points, b) placing the initial inducing points?
Minor comments:
The matrices K and L are referred to throughout the introduction without explaining what they are. Briefly mentioning the marginal kernel and L-ensembles may make it easier to follow for an uninformed reader.
 There is discussion about the advantages of directly learning the marginal kernel parameters throughout the paper, but this is not the approach taken. I believe some of it could be cut back since it does not contribute to the rest of the paper.
  Inducing inputs are utilized to bound the DPP likelihood, which reduces the computational cost. Both variational inference and approximate Markov chain Monte Carlo (MCMC) techniques are described and their efficiency is demonstrated empirically.I believe there is merit to this paper, however I found the method description rather rough and empirical evaluation not thorough enough. If accepted, I strongly encourage the authors to improve the write-up.

### Polished review:



The paper introduces approximate inference techniques for determinantal point processes (DPPs) that bypass the need for spectral knowledge of the defining kernel. Instead, it leverages inducing inputs to bound the DPP likelihood, thereby reducing computational cost. Both variational inference and approximate Markov chain Monte Carlo (MCMC) methods are proposed and empirically validated. While the approach holds potential, the method description is somewhat underdeveloped, and the empirical evaluation lacks sufficient depth. To strengthen the paper, the authors should address the following points:  

1. **Computational comparison**: Provide a clear analysis of the computational complexity and actual runtime for both proposed methods. How do they scale with problem size relative to each other?  
2. **Benchmark against alternatives**: Systematically compare the proposed methods to both exact and approximate baselines in terms of approximation quality (e.g., log-likelihood, sample diversity) and computational efficiency.  
3. **Variational inference limitations**: In Section 5.1, variational inference yields substantial parameter estimation errors on the toy dataset, necessitating a switch to approximate MCMC. Clarify the conditions under which variational inference is expected to succeed versus fail, and justify this behavior.  
4. **Inducing inputs and data alignment**: The toy example uses a 13-point dataset. How do the methods perform when the inducing inputs exactly coincide with the observed data points?  
5. **Practical guidelines**: Offer concrete heuristics for selecting (a) the number of inducing points and (b) the initial placement of these points.  

Minor comments:  
- The introduction references matrices *K* and *L* without definition. Briefly clarify their roles (e.g., as the marginal kernel and L-ensemble parameters) to aid readers unfamiliar with DPPs.  
- The paper repeatedly emphasizes the benefits of directly learning marginal kernel parameters, yet this approach is not adopted. Trim these sections, as they do not align with the proposed method and distract from the core contribution.  

The core idea is promising, but the current presentation requires significant refinement to demonstrate its full value. The method description and empirical analysis need greater rigor to convince readers of its practical utility.

## (14) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2015/test/1ee3dfcd8a0645a25a35977997223d22/level4/Qwen3-30B-A3B-Thinking-2507-FP8/level4@P1NOPDF:::4.txt
### Human review:

The paper proposes a new framework for spectral regularized embedding, applied to graph transduction. The framework itself, and in particular the benefits for having an orthonormal embedding might be described more convincingly, but this is not a serious issue.
The authors then propose an interesting and elegant algorithm to solve the SEER problem approximately. This is an original contribution and it seems to provide a good alternative to solve the complex learning problem.
 Experimental results tend to demonstrate the benefits of the proposed solution. It would be great to show results that demonstrate the benefits of the SEER framework, or of the orthonormal representation defined by (3) at first, and also to show the approximation accuracy of the IIP solution to the SEER problem. This is not visible in the current results, and it would be of high interest to position the actual contribution in a more global context.
 The multiple graph transduction is unfortunately described at a very high level. It is definitely an interesting extension, but more details, motivation and intuitions are necessary to understand clearly how and why the proposed method is also interesting for multiple graph, and especially to understand how that algorithm is implement in such settings. In the current form, it is difficult to grasp the main ideas in the multiple graph case, and especially to really appreciate the experimental results in this case. In that respect, the last column of Table 4 (noisy case) is not very intuitive - it seems that one graph is better than multiple ones, which would contradict the motivation for dealing with multiple graphs.
 Finally, the paper is not always easy to read and pretty dense at places. It also refers at too many places to the supplementary material. It is probably a sign that the authors wants to give too much information in a single paper, which actually penalises the accessibility and probably visibility of the work.  The paper proposes a new framework, SEER for orthonormal embeddings that is applied to graph transduction. An interesting algorithm based on IIP is proposed to solve the learning problem in SEER, and relatively convincing results are proposed.

### Polished review:



The paper introduces a novel framework, SEER (Spectral Embedding with orthonormal Embeddings and Regularization), for graph transduction via spectral regularization. The core idea of orthonormal embeddings merits stronger justification; while the framework itself is conceptually sound, its specific advantages over non-orthonormal alternatives are not convincingly established. This is a notable weakness in the presentation but not a fundamental flaw.

The proposed IIP-based algorithm for approximately solving the SEER problem represents a clear and elegant technical contribution. It effectively addresses the computational complexity of the underlying optimization, offering a practical alternative to exact methods. This algorithmic innovation is original and well-motivated.

The experimental evaluation demonstrates the proposed method's efficacy on standard benchmarks, but key gaps limit its impact. Crucially, the results do not isolate the contribution of the SEER framework itself or the specific benefits of the orthonormal embedding (defined in Equation 3). To properly position the work, the authors should include ablation studies showing: (1) the performance gain from using SEER versus a non-orthonormal baseline, and (2) the accuracy of the IIP approximation relative to the exact SEER solution. Without these, the paper cannot convincingly attribute improvements to the core framework or its key components.

The extension to multiple graph transduction is introduced at a high level and lacks sufficient detail. While the idea is promising, the paper fails to provide clear motivation for why the method is particularly suited to multiple graphs or intuitive explanations of its operation in this setting. The algorithm description is too terse, making it difficult to assess how the approach scales or adapts to multiple graphs. This is especially problematic for Table 4 (noisy case), where the result—showing a single graph outperforming multiple graphs—directly contradicts the stated motivation for handling multiple graphs. This counterintuitive finding requires explicit discussion to avoid undermining the paper's central claim.

The writing is dense in places, and the frequent reliance on supplementary material suggests the main text attempts to cover too much. This overloading reduces accessibility and risks obscuring the paper's key contributions. The supplementary material should support, not substitute for, the main narrative.

In summary, the paper presents a promising framework (SEER) and a valuable algorithmic solution (IIP) for graph transduction. However, the current presentation lacks sufficient justification for the orthonormal embedding, omits critical ablation studies to validate the framework's core contributions, and inadequately develops the multiple graph extension—where the experimental results themselves seem contradictory. Addressing these points would significantly strengthen the paper's impact and clarity. The technical core is sound, but the presentation needs refinement to fully convey its significance.

## (15) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2014/test/57aeee35c98205091e18d1140e9f38cf/level4/Qwen3-30B-A3B-Thinking-2507-FP8/level4@P1NOPDF:::2.txt
### Human review:

This paper proposes a new approach to derive the bound of the average causal effect (ACE) from a variable X to another Y. Its main principles is the use of Entner's Rule 1 in its inverse direction, the relaxation of the faithfulness assumption to introduce possibility of the path-cancellation at some degree, and the introduction of assumptions represented by some inequality constraints. A computation scheme of the ACE bound are formulated by using linear programing under these principles. Though the authors have not optimized the algorithm to derive the bounds yet, the resulted bounds seem very narrow and accurate in comparison with the other approaches in state of the art.
Quality
The authors tried to establish a novel method to derive more accurate bound of ACE than the state of the art. They combined several feasible principles and succeeded to provide the tighter bounds. In this regard, the content of the paper is very interesting. 
However, some criteria to define the bounds are not comprehensively explained. Particularly, the validity of the use of Entner's Rule 1 in the inverse direction is not clearly discussed. For its use in the inverse direction, the authors should explicitly assume the structure depicted in Fig.2. This should be clearly explained and discussed.
In addition, the generic criteria to choose appropriate parameters for relaxation are not provided. Since these affect the result of the bounds significantly, the principle to determine the parameters should be more investigated and included in the work.
Clarity
The explanation of the paper on the theoretical part seems basically comprehensive except the essential discussion I pointed out above. 
However, the demonstration of the experimental results are not well described. As I pointed out above, the actual implementation of the algorithm is not comprehensively explained. The definition of the parameters shown in Table 1 (Table 5?) are not clearly given.
In addition, I see some typos. For example;
"The full algorithm is shown in Table 1." on page 6=> I do not see any table of algorithm.
"Results are summarized in Table 5." on page 8=> I do not see Table 5 (maybe Table 1).
Originality
The problem setting of this paper has been addressed by some earlier work as the authors pointed out. In this regard, the scope of this paper does not have very string originality. 
The idea to combine the three ideas in a unified shape contains some originality. But, as I pointed out above, the validity of the combination is not very clearly discussed.
Significance
In terms of deriving the tighter bounds of ACE, this method shows some significance. However, its performance has been check by quite limited experiments. It generality in both theory and wide experiments has not been strictly assessed. The paper addresses an important problem which is to evaluate the bound of the strength of causal relations. However, the validity of the presented idea should be more well described in both theory and experiments.

### Polished review:



This paper introduces a novel method for deriving tight bounds on the average causal effect (ACE) from a variable X to Y. The approach leverages three key principles: applying Entner's Rule 1 in reverse, relaxing the faithfulness assumption to permit partial path cancellation, and incorporating inequality constraints. The authors formulate a linear programming scheme to compute these ACE bounds. While the algorithm has not yet been optimized, the resulting bounds appear significantly tighter and more accurate than state-of-the-art methods.

**Quality**  
The paper presents an interesting contribution by synthesizing feasible principles to derive sharper ACE bounds. However, two critical gaps undermine the argument’s rigor. First, the justification for applying Entner's Rule 1 in reverse is insufficient. The authors must explicitly justify this reversal by referencing and discussing the structural assumptions depicted in Figure 2. Second, the paper lacks a principled framework for selecting relaxation parameters—these critically influence bound quality, yet their determination remains arbitrary. The authors should provide clear criteria for parameter selection and demonstrate its impact on results.

**Clarity**  
The theoretical exposition is generally comprehensive but omits essential justification for the inverse application of Entner’s Rule 1. Experimental sections suffer from poor description: the algorithm’s implementation details are incomplete, and parameter definitions in Table 1 (referenced as Table 5 on page 8) are ambiguous. Additionally, page 6 states "The full algorithm is shown in Table 1," yet no such table exists; similarly, page 8 references "Table 5" where only Table 1 appears. These inconsistencies require correction. Minor typos also disrupt readability.

**Originality**  
While the paper’s problem setting overlaps with prior work (as acknowledged by the authors), the integration of three distinct concepts—reverse Entner’s Rule, relaxed faithfulness, and inequality constraints—represents a novel framework. However, this integration lacks sufficient theoretical justification. The authors fail to rigorously demonstrate why this combination yields improved bounds, weakening the claimed novelty.

**Significance**  
The method demonstrates potential for tighter ACE bounds, addressing a fundamental challenge in causal inference. Yet its significance is limited by two factors: (1) the experimental validation is constrained to a few synthetic scenarios, with insufficient evaluation of generalizability; and (2) theoretical claims about bound quality are not robustly supported by diverse empirical evidence. The paper would gain substantial impact if it expanded both the theoretical justification and experimental scope to address these limitations.

In summary, the paper offers a promising direction for ACE bound estimation but requires deeper theoretical grounding and more thorough experimental validation to justify its claims. The core ideas are compelling, but current presentation leaves critical gaps in justification and implementation details. Addressing these would significantly strengthen the contribution.

## (16) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2017/test/2131f8ecf18db66a758f718dc729e00e/level4/Qwen3-30B-A3B-Thinking-2507-FP8/level4@P1NOPDF:::3.txt
### Human review:

This is an interesting paper. I enjoyed reading it. In the paper, the authors consider the task of clustering data points via crowdsourcing wherein the problem is of recovering original labels of data points based on the answers to similar cluster queries. The authors propose bounds on the number of queries required to recover the labels considering noisy as well as noiseless answers for the queries. The main contribution of the paper is theoretical, along with some empirical simulations. The paper is well written, making it easy to understand the theoretical contributions for a general machine learning audience. Especially, the connection w.r.t. Information theory for deriving the bounds is explained nicely. 
I have the following concerns, in regards to improving the paper.
(1) While the idea of AND queries is interesting theoretically, it seems to conflict with the original motivation for crowdsourcing. In the case of an AND query, effectively, the label of the cluster is also given as part of the answer rather than just answering if the data points of interest belong to same cluster or not. If this is the case indeed, as I interpret from the paper, why would one even need to ask those similarity queries ? Why not ask the label for a data point itself ? This is my primary confusion w.r.t. the contributions in this paper.
(2) Is it possible to simplify the expressions for the bounds in Theorems 1,2,3,4, while keeping the essence.
(3) In the experiments, it seems that only AND queries are considered. If so, the experimental study is in question unless the above point (1) is clarified.
I am satisfied with the response of the authors for my questions above. So, voting for the acceptance of this paper.

### Polished review:



This paper presents an interesting theoretical approach to clustering via crowdsourcing, where the goal is to recover true data labels using answers to similarity queries. The authors derive theoretical bounds on the number of queries needed for label recovery under both noisy and noiseless settings, supported by empirical simulations. The paper is well-structured and accessible to a general machine learning audience, with a particularly clear information-theoretic justification for the bounds.  

I have three key concerns that would strengthen the paper:  

(1) **Theoretical motivation for AND queries requires clarification.** The paper’s use of AND queries (e.g., "Do points A and B belong to the same cluster as point C?") appears to contradict the core crowdsourcing premise. If the worker must know the cluster label of point C to answer such a query (as implied by the query structure), the query effectively reveals the label directly—making direct label requests to workers unnecessary. This undermines the paper’s motivation for using similarity queries. The authors should explicitly address why AND queries are preferable to simply asking for labels directly, especially given that the query design seems to leak label information.  

(2) **Simplification of theoretical bounds.** The expressions for the bounds in Theorems 1–4 are complex. While the derivations are sound, simplifying these expressions (e.g., through asymptotic approximations or tighter characterizations) without losing the core insights would improve readability and practical interpretation for readers.  

(3) **Experimental evaluation scope.** The experiments only consider AND queries (as noted in Section 5), but without resolving concern (1), the empirical study lacks justification. If AND queries are indeed the only considered approach, the experimental results cannot validate the paper’s central claim about similarity-based crowdsourcing. Clarification on whether other query types (e.g., standard pairwise similarity queries) were explored or why they were excluded is essential.  

I have reviewed the authors’ response to these points and find their clarifications satisfactory. The theoretical contributions are novel and well-motivated, and the paper makes a valuable addition to the literature on crowdsourced clustering. I recommend acceptance.

## (17) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2017/test/34ed066df378efacc9b924ec161e7639/level4/Qwen3-30B-A3B-Thinking-2507-FP8/level4@P1NOPDF:::2.txt
### Human review:

The paper proposes a human image generator conditioned on appearance and human pose. The proposed generation is based on adversarial training architecture where two-step generative networks that produces high resolution image to feed into a discriminator. In the generator part, the first generator produce a coarse image using a U-shape network given appearance and pose map, then the second generator takes the coarse input with the original appearance to predict residual to refine the coarse image. The paper utilizes the DeepFashion dataset for evaluation.
The paper proposes a few important ideas.
* Task novelty: introducing the idea of conditioning on appearance and pose map for human image generation
* Techniques: stacked architecture that predicts difference map rather than direct upsampling, and loss design
The paper can improve in terms of the following points to stand out.
* Still needs quality improvement
* Significance: the paper could be seen one of yet-another GAN architecture
* Problem domain: good vision/graphics application, but difficult to generalize to other learning problems
The paper is well organized to convey the key aspects of the proposed architecture. Conditioned on appearance and pose information, the proposed generator stacks two networks to adopt a coarse-to-fine strategy. This paper effectively utilize the generation strategy in the dressing problem. The proposed approach looks appropriate to the concerned problem scenario. The difference map generation also looks a small but nice technique in generating higher resolution images.
Probably the major complaints to the paper is that the generated results contain visible artifacts and still requires a lot of improvement for application perspective. For example, patterns in ID346 of Fig 4 results in black dots in the final result. Even though the second generator mitigates the blurry image from the first generator, it seems the model is still insufficient to recover high-frequency components in the target appearance.
Another possible but not severe concern is that some might say the proposed approach is an application of conditional GANs. Conditioning or stacking of generators for adversarial training have been proposed in the past; e.g., below, though they are arXiv papers. The paper includes application-specific challenges, but this might not appeal to large number of audiences.
* Han Zhang, Tao Xu, Hongsheng Li, Shaoting Zhang, Xiaolei Huang, Xiaogang Wang, Dimitris Metaxas, "StackGAN: Text to Photo-realistic Image Synthesis with Stacked Generative Adversarial Networks", arXiv:1612.03242.
* Xun Huang, Yixuan Li, Omid Poursaeed, John Hopcroft, Serge Belongie, Stacked Generative Adversarial Networks, arXiv:1612.04357.
In overall, the paper successfully proposed a solution to the pose-conditioned image problem, and properly conducts evaluation. The proposed approach sufficiently presents technical novelty. The resulting images still needs quality improvement, but the proposed model at least generate something visually consistent images. My initial rating is accept.

### Polished review:



This paper introduces a human image generator conditioned on appearance and pose maps, using a two-stage generative architecture. The first generator produces a coarse image via a U-shaped network using appearance and pose inputs, while the second generator refines it by predicting a residual map from the coarse output and original appearance. The approach leverages the DeepFashion dataset for evaluation and demonstrates a coarse-to-fine strategy well-suited to dressing applications. Key contributions include: (1) task novelty in conditioning on both appearance and pose for human image synthesis, and (2) technical innovations in the stacked architecture (predicting residual maps instead of direct upsampling) and loss design.

The paper is well-structured and clearly conveys its methodology. The coarse-to-fine generation strategy effectively addresses the problem scope, and the residual-based refinement is a thoughtful technical addition for high-resolution output. However, several critical points require attention to strengthen the work's impact.

First, the generated image quality remains a significant limitation. Results exhibit visible artifacts, particularly in high-frequency details (e.g., pattern inconsistencies in ID346 of Figure 4 manifest as unwanted black dots). While the second generator reduces blurriness from the first stage, the model still struggles to recover fine texture details, limiting practical applicability. This issue demands substantial improvement before the work can be considered robust for real-world use.

Second, the novelty claim warrants careful consideration. The core approach—stacking generators for conditional synthesis—builds directly on established conditional GAN frameworks. For instance, StackGAN (Zhang et al., arXiv:1612.03242) and Stacked GANs (Huang et al., arXiv:1612.04357) already demonstrate similar generator stacking for text-to-image and general synthesis tasks. While the paper incorporates application-specific challenges (e.g., pose-guided dressing), this may not resonate broadly with the wider machine learning community, potentially positioning the work as a specialized application rather than a generalizable advancement.

Third, the significance is somewhat diminished by the incremental nature of the contributions. The field has seen numerous conditional GAN variants, and the paper’s approach, while functional, does not clearly articulate a compelling new direction beyond existing paradigms. The evaluation focuses on qualitative results without rigorous quantitative metrics (e.g., FID, LPIPS) or ablation studies to isolate the impact of the residual refinement strategy, weakening the case for technical novelty.

Despite these concerns, the work is technically sound and addresses a meaningful problem in computer vision. The architecture is appropriately designed for the task, and the results—while imperfect—do produce visually coherent outputs. The paper’s organization and clarity effectively communicate its core ideas.

In summary, the paper presents a functional solution to pose-conditioned human image generation with a logical architecture. However, the lack of substantial quality improvements in the generated outputs, the incremental novelty relative to existing stacked GAN work, and the limited generalizability of the approach prevent it from standing out significantly. To strengthen the contribution, the authors should prioritize artifact reduction, provide deeper quantitative validation, and better contextualize the novelty against prior stacked GAN literature.

I recommend acceptance, as the work is technically valid and addresses a relevant problem, but the current version requires more substantial improvements to fully justify its contribution.

## (18) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2013/test/24681928425f5a9133504de568f5f6df/level4/Qwen3-30B-A3B-Thinking-2507-FP8/level4@P1NOPDF:::2.txt
### Human review:

This paper presents a method for learning the structure as well as the parameters of stochastic AND-OR grammars. Such grammars contain AND rules and OR rules and can be used to represent several recursive phenomena, including natural language and even grammars. The authors present a nice method for unsupervised structure learning of these grammars by introducing new AND-OR fragments at consecutive steps, and measuring the likelihood and prior gains of their model. 
The authors present experiments on two tasks: learning event grammars and learning image grammars. In both they achieve results that are competitive with prior art. 
I liked the overall paper as it seems to be a tractable way of learning stochastic grammars that can be modeled using AND and OR rules. My criticism of the paper stems from the following observations: 
1) The authors do not mention how tractable the learning algorithm is. Will it scale to thousands of datapoints? 
2) I would have liked to seen experiments on natural language sentences as natural language is the most obvious application of such grammars. Will it be even possible to learn using the presented methods on the Penn Treebank dataset for example, on which previous work has focused on (say, Klein and Manning)? This paper presents a way of estimating the structure and parameters of stochastic AND-OR grammars and presents nice results on two tasks; I would have liked to see more experiments, especially on natural language data.

### Polished review:



This paper introduces a method for jointly learning the structure and parameters of stochastic AND-OR grammars, which incorporate both AND and OR rules to model recursive phenomena such as natural language. The authors propose a tractable approach for unsupervised structure learning by incrementally introducing new AND-OR fragments and evaluating their likelihood and prior gains.  

The method is evaluated on two tasks: learning event grammars and image grammars, where it achieves competitive results relative to prior work. The core idea is compelling, offering a practical framework for modeling grammars with AND/OR structure. However, two key limitations warrant attention:  

First, the paper does not address the computational scalability of the learning algorithm. Specifically, it remains unclear whether the approach can efficiently handle datasets with thousands of instances—a critical consideration for real-world applications. Without empirical or theoretical analysis of time/space complexity, the practical utility of the method for large-scale problems is uncertain.  

Second, the absence of experiments on natural language data is a significant gap. Given that natural language is the most prominent application domain for such grammars, the lack of results on standard benchmarks like the Penn Treebank (e.g., replicating the setup of Klein and Manning’s work) weakens the paper’s broader relevance. The authors should clarify whether their method is feasible for learning syntactic structures from sentences, as this would directly validate its intended use case.  

While the results on event and image grammars are promising, these omissions limit the paper’s impact. The authors should either extend their experiments to natural language or explicitly discuss the challenges of applying their method to such data. A more thorough scalability analysis would also strengthen the contribution. Overall, the approach is well-motivated and technically sound, but the missing evidence on scalability and natural language applicability prevents the work from fully demonstrating its potential.

## (19) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/iclr_2017/test/330/level4/Qwen3-30B-A3B-Thinking-2507-FP8/level4@P1NOPDF:::3.txt
### Human review:

This paper proposes learning document embeddings as a sum of the constituent word embeddings, which are jointly learned and randomly dropped out ('corrupted') during training. While none of the pieces of this model are particularly novel, the result is an efficient learning algorithm for document representation with good empirical performance.
Joint training of word and document embeddings is not a new idea, nor is the idea of enforcing the document to be represented by the sum of its word embeddings (see, e.g. '"The Sum of Its Parts": Joint Learning of Word and Phrase Representations with Autoencoders' by Lebret and Collobert). Furthermore, the corruption mechanism is nothing other than traditional dropout on the input layer. Coupled with the word2vec-style loss and training methods, this paper offers little on the novelty front.
On the other hand, it is very efficient at generation time, requiring only an average of the word embeddings rather than a complicated inference step as in Doc2Vec. Moreover, by construction, the embedding captures salient global information about the document -- it captures specifically that information that aids in local-context prediction. For such a simple model, the performance on sentiment analysis and document classification is quite encouraging.
Overall, despite the lack of novelty, the simplicity, efficiency, and performance of this model make it worthy of wider readership and study, and I recommend acceptance.

### Polished review:



This paper proposes learning document embeddings as the sum of constituent word embeddings, with word embeddings jointly trained and randomly masked ("corrupted") during training. While the individual components of this approach are not novel, the resulting method offers an efficient algorithm for document representation with strong empirical results.

Joint training of word and document embeddings is well-established, as demonstrated in prior work such as Lebret and Collobert's "The Sum of Its Parts: Joint Learning of Word and Phrase Representations with Autoencoders." Similarly, the constraint that a document must be represented as the sum of its word embeddings has appeared in earlier literature. The proposed corruption mechanism is effectively equivalent to standard input-layer dropout, and the use of a word2vec-inspired loss function further limits novelty. Consequently, the paper contributes little new on the theoretical or methodological front.

However, the method excels in practical efficiency. At inference time, it requires only a simple average of word embeddings, avoiding the complex inference procedures needed in models like Doc2Vec. Crucially, the embedding inherently captures the global semantic structure of the document—specifically, the information most relevant for predicting local context. For such a straightforward architecture, the performance on sentiment analysis and document classification tasks is notably strong.

Despite the limited novelty, the model's simplicity, computational efficiency, and competitive results make it a compelling contribution. It offers a robust baseline that could inform future work in document representation. I recommend acceptance for its clear utility and strong empirical validation.

## (20) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2013/test/24681928425f5a9133504de568f5f6df/level4/gemini-2.5-pro/level4@P1NOPDF:::2.txt
### Human review:

This paper presents a method for learning the structure as well as the parameters of stochastic AND-OR grammars. Such grammars contain AND rules and OR rules and can be used to represent several recursive phenomena, including natural language and even grammars. The authors present a nice method for unsupervised structure learning of these grammars by introducing new AND-OR fragments at consecutive steps, and measuring the likelihood and prior gains of their model. 
The authors present experiments on two tasks: learning event grammars and learning image grammars. In both they achieve results that are competitive with prior art. 
I liked the overall paper as it seems to be a tractable way of learning stochastic grammars that can be modeled using AND and OR rules. My criticism of the paper stems from the following observations: 
1) The authors do not mention how tractable the learning algorithm is. Will it scale to thousands of datapoints? 
2) I would have liked to seen experiments on natural language sentences as natural language is the most obvious application of such grammars. Will it be even possible to learn using the presented methods on the Penn Treebank dataset for example, on which previous work has focused on (say, Klein and Manning)? This paper presents a way of estimating the structure and parameters of stochastic AND-OR grammars and presents nice results on two tasks; I would have liked to see more experiments, especially on natural language data.

### Polished review:

This paper presents a method for learning both the structure and parameters of stochastic AND-OR grammars. The proposed framework learns in an unsupervised manner, incrementally adding new AND-OR fragments to the grammar based on improvements to the data likelihood and a model prior. The authors demonstrate their approach on two tasks—learning event grammars and image grammars—achieving results that are competitive with prior work.

The primary contribution of this work is a seemingly tractable approach to the challenging problem of grammar induction. The incremental, data-driven method for structure learning is well-motivated. However, the evaluation and analysis could be strengthened in two key areas.

First, the paper lacks a discussion of the algorithm's tractability and scalability. It is unclear whether the proposed learning procedure can scale to datasets containing thousands of examples. An analysis of the computational complexity or empirical runtime would be a valuable addition.

Second, while the experiments on event and image grammars are interesting, the paper would be more compelling with an evaluation on natural language. Natural language parsing is a canonical application for such grammars, and its omission is conspicuous. For instance, applying the method to a standard benchmark like the Penn Treebank would not only demonstrate its applicability to a key domain but also enable direct comparison with a large body of previous work on grammar induction (e.g., Klein and Manning). The current experiments showcase the method's potential, but a more thorough validation, particularly on natural language data, is needed to fully assess its contributions.

## (21) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/iclr_2017/test/333/level4/gemini-2.5-pro/level4@P1NOPDF:::2.txt
### Human review:

This paper provides an interesting analysis of the conditions which enable generation of natural looking textures. The results is quite surprising, and analysis is quite thorough. 
I do think the evaluation methods require more work, but as other reviewers mentioned this could be an interesting line of work moving forwards and does not take too much from this current paper which, I think, should be accepted.

### Polished review:

This paper presents a thorough and insightful analysis of the conditions required for generating natural-looking textures. The findings are quite surprising, and the analysis is comprehensive.

While the evaluation methods could be strengthened, this limitation does not significantly detract from the paper's core contributions. Further development of the evaluation framework represents a promising direction for future work. Given the novelty of the findings and the quality of the analysis, I believe this paper should be accepted.

## (22) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2016/test/01931a6925d3de09e5f87419d9d55055/level4/gemini-2.5-pro/level4@P2PURE:::6.txt
### Human review:

In this paper the authors present a locally adaptive normal distribution. Instead of measuring distances via a Euclidean distance they define a Riemannian metric M(x) which varies smoothly across the data set. Given the R. Metric M(x) geodesic distances along the manifold can be calculated via the exponential and logarithmic map. The authors use the Euler-Lagrange equations which define a set of ordinary differential equations for estimating the geodesic distances. The logarithm map takes points from the manifold (y) into the tangent plane (at x) such that the length of the resulting vector is the geodesic distance from x to y along the manifold. The authors then apply a normal distribution computing a Mahalanobis distance on points mapped by the logarithm map. This inner product is used to compute distances from a point x to the mean instead of Euclidean distances. The authors then derive estimators for the mean and covariance via maximum likelihood. Since the solutions are not available in closed form they present a steepest descent algorithm for estimating them. Finally, since the normalization constant is also not available in closed form the authors present a Monte-Carlo approximation method. They apply this method to synthetic data generated on a manifold as well as in a clustering task. They compare to the standard mixture of Gaussians. Overall I feel that the paper provides an interesting and useful extension of the normal distribution which adapts to local manifold structure. The authors combine work in metric estimation, computing geodesic distances, and learning distributions. I believe this work is worthy of publication. I have a few comments on my scores for the above: Technical quality Comments: The manifold techniques (using Euler-Lagrange equations, estimating logarithm maps) are sound and well explained. The Monte-Carlo estimation of the normalization constant and steepest descent algorithms are clever and well described. Analysis of the applications is lacking (sigma parameter appears to be picked by optimizing on training data?). Explanation of the usefulness of the learned distribution is also somewhat lacking. Novelty Comments: It appears the main contribution of this paper is combining previous work (using Kernels for a metric M(x), estimating geodesic distances via Euler-Lagrange, applying a normal distribution) and providing an algorithm for estimating the parameters (mean, covariance, normalization constant). Potential Impact Comments: The authors provide a fair evaluation of the GMM and LAND in the synthetic data (looking at log-likelihood on data generated by the learned distributions) but it's not clear how they chose the sigma parameter. The authors show that the LAND fits well on data generated along a manifold but don't show how well it compares to a GMM when data is generated according to a single normal distribution or GMM. In the real life (clustering) data they appear to choose the sigma value for the LAND via optimizing the F measure and then present that same F measure. What they should have done (or if they did made this clearer) is provide the F measure on a held-out test set to be fair. It is, therefore, hard to see if there is or is not a problem with over-fitting. It also would have been nice to examine very high dimensional data. One potentially useful application that the authors present is that the LAND could be used as a generative model for manifold data, however, they make the rather unusual manifold assumption that the data X is observed in D dimensions and the manifold dimension is also D (that is, points on the tangent plane are D-dimensional and the Metric M(x) is full rank). In manifold learning we're usually interested in data that lie on a d-dimensional manifold embedded into a D-dimensional Euclidean space where D is much larger than d. Clarity Comments: There's one particular notation point I found confusing: the overloading of the Sigma notation. In particular they say M = Sigma^-1 but then estimate it via a (local) diagonal Kernel matrix. Is this Simga also the same as the (fitted) covariance matrix? If so, is the kernel just an initialization? This would be strange since M(x) should vary with x but the fitted covariance matrix is a single parameter. In the proof of the steepest decent they explicitly say say that "in our case M = Sigma^-1" and use that substitution. Clarification here would be nice. In Sec 4.2 they don't state but I assume cluster membership was chosen by picking 2 clusters and computing closest (geodesic?) distance to the cluster means. Overall I felt the manifold introduction was well explained (at least for someone familiar with Riemannian manifolds).

### Polished review:

This paper introduces a locally adaptive normal distribution by replacing the standard Euclidean distance with a geodesic distance defined on a Riemannian manifold. The authors define a smoothly varying metric M(x) and compute geodesic distances by solving the Euler-Lagrange equations. The logarithmic map projects points from the manifold to a local tangent space, where a normal distribution is then defined. Specifically, the model uses the Mahalanobis distance in this tangent space to measure the deviation from the mean. The authors derive maximum likelihood estimators for the distribution's mean and covariance, which, lacking a closed-form solution, are optimized using a steepest descent algorithm. As the normalization constant is also intractable, they propose a Monte-Carlo approximation. The proposed method is evaluated on synthetic manifold data and a real-world clustering task, with comparisons made to a standard Gaussian Mixture Model.

Overall, this paper presents an interesting and useful extension of the normal distribution that adapts to local manifold structure. The authors effectively combine techniques from metric estimation, geodesic distance computation, and distributional learning. I believe this work is worthy of publication, though I have several comments and concerns detailed below.

**Technical Quality**
The technical contributions of the paper are sound. The use of manifold techniques, such as the Euler-Lagrange equations and the logarithmic map, is well-motivated and clearly explained. Similarly, the proposed steepest descent algorithm and the Monte-Carlo estimation of the normalization constant are clever and well-described solutions to the challenges of the model. However, the analysis of the applications is somewhat lacking, and the paper could better explain the practical usefulness of the learned distribution.

**Novelty**
The primary contribution appears to be the synthesis of several existing lines of work—namely, using kernels to define a metric M(x), estimating geodesic distances via the Euler-Lagrange equations, and applying a normal distribution in the resulting tangent space. The novelty lies in integrating these concepts and developing a coherent algorithm for estimating the model parameters (mean, covariance, and normalization constant).

**Potential Impact**
The experimental evaluation raises several concerns that limit the paper's impact:
1.  **Parameter Selection and Evaluation:** The method for selecting the kernel width parameter (`sigma`) is not clearly specified for the synthetic experiments. In the real-world clustering experiment, it appears that `sigma` was chosen to optimize the F-measure on the same data that the F-measure is reported on. This is a significant methodological flaw. To demonstrate generalization and avoid overfitting, performance should be reported on a held-out test set after tuning hyperparameters on a separate validation set.
2.  **Comparative Evaluation:** The comparison with Gaussian Mixture Models (GMMs) is one-sided. While the paper shows that the proposed LAND model performs well on manifold-structured data, it does not evaluate how it compares to a GMM when the data is genuinely generated from a single Gaussian or a GMM. This would be a crucial baseline to understand the model's robustness and potential drawbacks.
3.  **Manifold Assumption:** The authors make the unusual assumption that the manifold dimension `d` is equal to the ambient data dimension `D`. A primary motivation for manifold learning is typically to model low-dimensional structures (`d << D`) embedded in high-dimensional spaces. This `d=D` assumption, where M(x) is full-rank, significantly limits the applicability of the proposed method to the more common manifold learning scenario. It would also have been valuable to see experiments on very high-dimensional data.

**Clarity**
1.  **Overloaded Notation:** The notation for `Sigma` is a significant source of confusion. The authors state that the metric `M(x) = Sigma^-1`, but they also estimate `M(x)` using a local, diagonal kernel matrix, which varies with `x`. Simultaneously, they estimate a single, global covariance matrix `Sigma` for the distribution. It is unclear how a locally varying metric can be the inverse of a single global covariance matrix. The proof of the steepest descent algorithm explicitly uses this substitution. The authors should clarify the relationship between the local metric `M(x)` and the learned covariance `Sigma`. Is the kernel definition of M(x) merely an initialization?
2.  **Missing Experimental Details:** In Section 4.2 (the clustering experiment), the paper does not specify how cluster assignments were made. I assume membership was determined by assigning each point to the cluster with the minimum geodesic distance to its mean, but this should be stated explicitly.

## (23) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2016/test/286674e3082feb7e5afb92777e48821f/level4/gpt-5/level4@P2PURE:::3.txt
### Human review:

The manuscript presents a set of algorithms for clustering over graphs, and for testing whether two cluster assignments are similar. As mentioned above, although the algorithms themselves are clear, their motivation and the reason why they appear as a list of algorithms is not well explained. The algorithms themselves are modifications of existing ones, and the only novelty is the constraints presented at the end.

### Polished review:

The manuscript introduces a collection of algorithms for graph-based clustering and for evaluating whether two cluster assignments are similar. While the algorithms are clearly described, their motivation is insufficiently justified, and it is unclear why they are presented as a list rather than within a unified framework. Moreover, the methods appear to be modifications of existing approaches, with the only apparent novelty being the constraints introduced at the end.

## (24) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2016/test/286674e3082feb7e5afb92777e48821f/level4/gemma-3-27b-it/level4@P2PURE:::3.txt
### Human review:

The manuscript presents a set of algorithms for clustering over graphs, and for testing whether two cluster assignments are similar. As mentioned above, although the algorithms themselves are clear, their motivation and the reason why they appear as a list of algorithms is not well explained. The algorithms themselves are modifications of existing ones, and the only novelty is the constraints presented at the end.

### Polished review:

The manuscript introduces algorithms for graph clustering and for quantifying the similarity between two cluster assignments. While the algorithms are clearly presented, their overarching motivation and the rationale for presenting them as a collection of distinct methods remain unclear. These algorithms largely build upon existing approaches, with the primary novelty lying in the constraints detailed towards the end of the paper.

## (25) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2016/test/286674e3082feb7e5afb92777e48821f/level4/gemma-3-27b-it/level4@P3PURE:::3.txt
### Human review:

The manuscript presents a set of algorithms for clustering over graphs, and for testing whether two cluster assignments are similar. As mentioned above, although the algorithms themselves are clear, their motivation and the reason why they appear as a list of algorithms is not well explained. The algorithms themselves are modifications of existing ones, and the only novelty is the constraints presented at the end.

### Polished review:

The manuscript presents a set of algorithms for graph clustering and for assessing the similarity between two cluster assignments. While the algorithms are clearly described, their overall motivation and the rationale for presenting them as a collection remain unclear. The proposed methods largely consist of modifications to existing techniques, and the primary novelty appears to reside in the constraints introduced at the conclusion of the paper.





## (26) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2016/test/286674e3082feb7e5afb92777e48821f/level4/meta-llama-Llama-3.1-70B-Instruct-AWQ-INT4/level4@P2PURE:::3.txt
### Human review:

The manuscript presents a set of algorithms for clustering over graphs, and for testing whether two cluster assignments are similar. As mentioned above, although the algorithms themselves are clear, their motivation and the reason why they appear as a list of algorithms is not well explained. The algorithms themselves are modifications of existing ones, and the only novelty is the constraints presented at the end.

### Polished review:

The manuscript proposes a set of algorithms for clustering over graphs and for assessing the similarity between two cluster assignments. However, the motivation behind these algorithms and the rationale for presenting them as a collection are not adequately explained. Although the algorithms themselves are well-defined, they are essentially modifications of existing methods, with the only novel contribution being the constraints introduced at the end.

## (27) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2016/test/286674e3082feb7e5afb92777e48821f/level4/meta-llama-Llama-3.1-70B-Instruct-AWQ-INT4/level4@P3PURE:::3.txt
### Human review:

The manuscript presents a set of algorithms for clustering over graphs, and for testing whether two cluster assignments are similar. As mentioned above, although the algorithms themselves are clear, their motivation and the reason why they appear as a list of algorithms is not well explained. The algorithms themselves are modifications of existing ones, and the only novelty is the constraints presented at the end.

### Polished review:

The manuscript presents a set of algorithms for clustering over graphs and for testing the similarity between two cluster assignments. However, the motivation behind these algorithms and the rationale for presenting them as a list is not well-explained. Although the algorithms themselves are clearly described, they are essentially modifications of existing methods, with the primary novelty lying in the constraints presented at the end.

## (28) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2016/test/286674e3082feb7e5afb92777e48821f/level4/Qwen3-30B-A3B-Thinking-2507-FP8/level4@P3PURE:::6.txt
### Human review:

In the paper the authors try to come up with a theory which works for graph clustering in model free framework. However, the result is naive and unconvincing. In the paper the authors try to come up with a theory which works for graph clustering in model free framework. However, the result is naive and unconvincing. The authors pretend to construct a new theory but theit theory is just a naive handwaving. Just to give a couple of examples: Theorem 1 (Generic Theorem) ... "which also fits G well is close to C" ... Proposition 3 (Informal) ... "under standard recovery conditions" ...

### Polished review:



The authors claim to develop a novel theoretical framework for graph clustering in a model-free setting. However, the proposed theory is unsubstantiated and fails to deliver meaningful theoretical insights. The argument amounts to unsubstantiated assertions rather than a rigorous derivation. For instance: Theorem 1 (Generic Theorem) states "...which also fits G well is close to C," which lacks mathematical precision. Similarly, Proposition 3 (Informal) invokes "under standard recovery conditions" without specifying the conditions or demonstrating their validity in the context of the model. These elements undermine the paper's core contribution and render the theoretical claims unconvincing.

## (29) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2016/test/286674e3082feb7e5afb92777e48821f/level4/Qwen3-30B-A3B-Thinking-2507-FP8/level4@P3PURE:::3.txt
### Human review:

The manuscript presents a set of algorithms for clustering over graphs, and for testing whether two cluster assignments are similar. As mentioned above, although the algorithms themselves are clear, their motivation and the reason why they appear as a list of algorithms is not well explained. The algorithms themselves are modifications of existing ones, and the only novelty is the constraints presented at the end.

### Polished review:



The manuscript presents algorithms for graph clustering and for testing similarity between cluster assignments. While the algorithms themselves are clearly described, the motivation for their development and the rationale for presenting them as a distinct list of methods are not well articulated. The algorithms constitute modifications of existing approaches, and the only novel contribution is the set of constraints introduced at the end of the paper.

## (30) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2016/test/144a3f71a03ab7c4f46f9656608efdb2/level4/meta-llama-Llama-3.1-70B-Instruct-AWQ-INT4/level4@P2PURE:::5.txt
### Human review:

This paper considers the problem of finding an optimal Bayesian network configuration. In particular the authors show how to incorporate non-decomposable constraints (and in particular ancestral constrains) into the structure learning approach of Chen et al. [2015, 2016]. Empirical evaluation of the proposed approach against ILP based approaches shows orders of magnitude improvements. The authors rephrase the problem as a MaxSAT problem with specific constraints. While my expertise in with this approach is limited the results (runtime comparison) seem quite impressive. Specifically the authors show a runtime reduction by orders of magnitude relative to alternative methods.

### Polished review:

This paper addresses the problem of finding an optimal Bayesian network configuration, focusing on the incorporation of non-decomposable constraints, particularly ancestral constraints, into the structure learning approach of Chen et al. [2015, 2016]. The authors' empirical evaluation demonstrates that their proposed approach achieves orders of magnitude improvements over ILP-based methods. By reformulating the problem as a MaxSAT problem with specific constraints, the authors obtain impressive results, showing a significant reduction in runtime compared to alternative methods. Although my familiarity with this approach is limited, the runtime comparison suggests substantial improvements, with the authors reporting a runtime reduction of orders of magnitude relative to existing methods.

## (31) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2016/test/144a3f71a03ab7c4f46f9656608efdb2/level4/meta-llama-Llama-3.1-70B-Instruct-AWQ-INT4/level4@P3PURE:::5.txt
### Human review:

This paper considers the problem of finding an optimal Bayesian network configuration. In particular the authors show how to incorporate non-decomposable constraints (and in particular ancestral constrains) into the structure learning approach of Chen et al. [2015, 2016]. Empirical evaluation of the proposed approach against ILP based approaches shows orders of magnitude improvements. The authors rephrase the problem as a MaxSAT problem with specific constraints. While my expertise in with this approach is limited the results (runtime comparison) seem quite impressive. Specifically the authors show a runtime reduction by orders of magnitude relative to alternative methods.

### Polished review:

This paper addresses the problem of finding an optimal Bayesian network configuration, focusing on the incorporation of non-decomposable constraints, specifically ancestral constraints, into the structure learning approach of Chen et al. [2015, 2016]. The authors empirically evaluate their proposed approach against ILP-based methods, demonstrating improvements of several orders of magnitude. By reformulating the problem as a MaxSAT problem with specific constraints, the authors achieve notable results, particularly in runtime comparisons. Although my expertise with this approach is limited, the reported improvements appear impressive, showing a runtime reduction of several orders of magnitude compared to alternative methods.

## (32) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2016/test/144a3f71a03ab7c4f46f9656608efdb2/level4/Qwen3-30B-A3B-Thinking-2507-FP8/level4@P2PURE:::5.txt
### Human review:

This paper considers the problem of finding an optimal Bayesian network configuration. In particular the authors show how to incorporate non-decomposable constraints (and in particular ancestral constrains) into the structure learning approach of Chen et al. [2015, 2016]. Empirical evaluation of the proposed approach against ILP based approaches shows orders of magnitude improvements. The authors rephrase the problem as a MaxSAT problem with specific constraints. While my expertise in with this approach is limited the results (runtime comparison) seem quite impressive. Specifically the authors show a runtime reduction by orders of magnitude relative to alternative methods.

### Polished review:



This paper addresses the problem of finding an optimal Bayesian network configuration by incorporating non-decomposable constraints, specifically ancestral constraints, into the structure learning framework of Chen et al. [2015, 2016]. The authors reformulate the problem as a MaxSAT problem with tailored constraints. Empirical evaluation demonstrates orders-of-magnitude runtime reductions compared to ILP-based approaches. While my expertise in this specific approach is limited, the reported runtime improvements appear highly impressive.

## (33) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2015/test/15de21c670ae7c3f6f3f1f37029303c9/level4/gemma-3-27b-it/level4@P3PURE:::1.txt
### Human review:

I think that the main issue of the manuscript is a lack of awareness of the literature on the topic. The authors' algorithm is strongly related to the Monte Carlo EM algorithm (and in fact the general class of stochastic approximation algorithms with markovian dynamic which have been proposed in various forms to optimize intractable likelihood functions). There is a well developed literature on the topic and the authors should compare what they have been doing to existing work. A theory which includes some of the authors' results already exists and covers much more general scenarios. For example the Markov chains are not required to be uniformly ergodic and there is no need to reinitialise the Markov chain at a fixed distribution r at each iteration (the authors acknowledge that they do this in order to simplify their analysis, but this is not sufficient--in addition reinitializing with the previous sample may be a better idea, as discussed at the end of the manuscript, and these algorithms have also been extensively analysed previously). The presentation of the results is far from optimal : for example for Theorem 1 and 2 it is not clear what the assumptions are? One can refer to the text before and after, but the reader should not have to do that. Note also that there is no need for the strong assumptions used in order to develop results such as those of Theorem 6 (see for example Benveniste, Metivier and Priouret for more general results). I think that the authors lack awareness of the literature and the results are only marginally novel.

### Polished review:

The primary weakness of this manuscript is a limited engagement with relevant prior work. The authors’ algorithm bears a strong resemblance to the Monte Carlo EM algorithm, and more broadly falls within the well-established class of stochastic approximation algorithms with Markovian dynamics used for optimizing intractable likelihood functions. A significant body of literature exists in this area, and the authors should thoroughly compare their approach to existing methods. Indeed, a theoretical framework encompassing the authors’ results already exists and addresses more general scenarios. Specifically, the requirement of uniform ergodicity for the Markov chains is unnecessarily restrictive, and the practice of reinitializing the Markov chain from a fixed distribution *r* at each iteration – acknowledged by the authors as a simplification for analysis – is suboptimal. Reinitializing with the previous sample, as discussed in the manuscript, may be a preferable strategy, and algorithms employing such approaches have been extensively analyzed previously. 

The presentation of the results also requires improvement. For example, the assumptions underlying Theorems 1 and 2 are not explicitly stated within the theorems themselves; readers are forced to cross-reference the surrounding text. Furthermore, the strong assumptions employed to derive results like those in Theorem 6 are not necessary, as more general results are available (e.g., Benveniste, Metivier, and Priouret). 

Overall, the manuscript demonstrates a lack of awareness of the existing literature, and the contributions, while technically sound, are only marginally novel.





## (34) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2015/test/2f25f6e326adb93c5787175dda209ab6/level4/gemini-2.5-pro/level4@P2PURE:::3.txt
### Human review:

The paper proposes approximate inference techniques for determinantal point process (DPP) that do not require spectral knowledge of the kernel defining the DPP. Instead, inducing inputs are utilized to bound the likelihood, which reduces the computational cost. Both variational inference and approximate Markov chain Monte Carlo (MCMC) techniques are described and their efficiency is demonstrated empirically.
 I believe there is merit to this paper, however I found the method description rather rough and empirical evaluation not thorough enough. A few points that may help clarify:
 1) How does the computational complexity and overall compute time of the two proposed methods compare?
2) How do the proposed methods compare to other alternatives, both approximate and exact, in terms of quality of approximation and computation time?
3) Empirical results on the toy data in Section 5.1 show that parameter estimation error using variational inference is too large, and resorts to approximate MCMC instead. In what settings does the proposed variational inference expected to work and when is it expected to fail? Why?
4) A 13-point sample is generated for the toy example. How do the methods perform when the inducing inputs are actually these sampled points?
5) Is there a rule of thumb to follow when selecting a) the number of inducing points, b) placing the initial inducing points?
Minor comments:
The matrices K and L are referred to throughout the introduction without explaining what they are. Briefly mentioning the marginal kernel and L-ensembles may make it easier to follow for an uninformed reader.
 There is discussion about the advantages of directly learning the marginal kernel parameters throughout the paper, but this is not the approach taken. I believe some of it could be cut back since it does not contribute to the rest of the paper.
  Inducing inputs are utilized to bound the DPP likelihood, which reduces the computational cost. Both variational inference and approximate Markov chain Monte Carlo (MCMC) techniques are described and their efficiency is demonstrated empirically.I believe there is merit to this paper, however I found the method description rather rough and empirical evaluation not thorough enough. If accepted, I strongly encourage the authors to improve the write-up.

### Polished review:

This paper introduces approximate inference techniques for determinantal point processes (DPPs) that avoid the need for spectral decomposition of the DPP kernel. The proposed approach utilizes inducing points to construct a tractable bound on the likelihood, thereby reducing computational complexity. The authors present methods based on both variational inference and approximate Markov chain Monte Carlo (MCMC) and provide empirical results to demonstrate their efficiency.

While the proposed direction is promising, the paper in its current form suffers from a lack of clarity in the methodological description and an insufficiently thorough empirical evaluation. The core ideas have merit, but the following points should be addressed to strengthen the paper:

1.  The paper would benefit from a direct comparison of the computational complexity and empirical runtimes of the two proposed methods (variational inference and MCMC).

2.  A crucial component missing from the evaluation is a comparison against other approximate and exact DPP inference methods. This comparison should analyze both the quality of the approximation and the computational time.

3.  The authors note in the toy example (Section 5.1) that the parameter estimation error for variational inference is high, leading them to use the MCMC approach instead. This raises an important question that the paper should address: under what conditions is the proposed variational approach expected to perform well, and when and why is it expected to fail? A deeper analysis of the limitations of the VI method is needed.

4.  For the toy example, where a 13-point sample is generated, it would be insightful to see how the methods perform when these 13 sampled points are themselves used as the set of inducing points.

5.  The paper currently lacks practical guidance on selecting the inducing points. The authors should provide recommendations or a rule of thumb for choosing a) the number of inducing points and b) their initial placement.

**Minor Comments:**

*   The introduction refers to matrices K and L without defining them. To improve readability for readers not deeply familiar with DPPs, the authors should briefly introduce the concepts of the marginal kernel and L-ensembles when these terms first appear.
*   The paper discusses the advantages of directly learning the marginal kernel parameters, but this is not the approach ultimately taken. This discussion detracts from the main contributions of the paper and could be streamlined or removed to improve focus.

If the paper is accepted, the authors are strongly encouraged to improve the write-up to address these clarity and evaluation concerns.

## (35) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2015/test/2f25f6e326adb93c5787175dda209ab6/level4/gemini-2.5-pro/level4@P3PURE:::1.txt
### Human review:

Determinantal point processes (DPPs) have been receiving a significant amount of recent attention in the machine learning literature, due to their ability to model repulsion within realizations of a set of points.
This repulsion is specified via a positive definite kernel function.
One challenge, however, is learning the appropriate parameters of this kernel, given example point realizations.
This estimation is difficult due to a difficult-to-compute normalization constant that, in effect, sums over all possible cardinalities and point configurations.
A recent proposal [7] has provided a way to do this by observing that the spectrum can be estimated and used to provide incremental upper and lower bounds, resulting in a provably-correct scheme for "retrospective" Markov chain Monte Carlo (MCMC) of the kernel parameters.
The present paper proposes a different type of bound that can also be used for MCMC inference, but that does not require estimation of the eigenvalues.
This approach also lends itself to a variational approach to learning, and the paper draws connections to inducing-point methods to scalable inference in Gaussian process models.
This is a technically strong and well-written paper.
I was not aware of the inequality that provides the lower bound in Proposition 1 and it seems like an excellent fit for this problem.
It is a clever way to avoid the estimation issues of [7].
I love the connections to GP inducing points, as well as the ability to now perform variational inference.
Overall this paper was a pleasure to read.
I have two technical concerns that I would like to see addressed, however.
First, although I like this approach very much, I do not find it all that compelling that it is a huge computational win to replace power iterations with nonlinear optimization problems of increasing dimension.
Second, it is not obvious to me that simple increasing of the cardinality is guaranteed to result in convergence of the bounds, because of the coupled optimization problem.
Although I am not certain, I believe this optimization is highly non-convex and so one needs to increase cardinality and also ensure that a global minimum is achieved.
This is something that should be addressed directly, because it seems that a local minimum could prevent the procedure from being able to bound away the Bernoulli threshold and make it impossible to take an MCMC step.
Presentation Issues:
 - P7 Figure 1: Please include axis labels for the figures.
 - The proof of the proposition is the main thing that makes this
 paper possible and is the central insight.
I would've liked to see
 it in the main body of the paper and not the index.
- P7 L361: "... the variational lower is ..."  A nice paper that uses a clever trick to bound the partition function of a determinantal point process, leading to potentially faster inference and connections to other kinds of models.

### Polished review:

### Summary

This paper addresses the challenging problem of learning the kernel parameters for determinantal point processes (DPPs). Parameter estimation in DPPs is difficult due to the intractable normalization constant of the likelihood function, which involves a sum over all possible point configurations and cardinalities. While recent work [7] introduced a retrospective Markov chain Monte Carlo (MCMC) scheme using bounds derived from eigenvalue estimates, this paper proposes an alternative approach. The authors introduce a novel bound on the normalization constant that circumvents the need for eigenvalue estimation. This method not only facilitates MCMC inference but also naturally extends to a variational learning framework, drawing insightful connections to inducing-point methods for scalable Gaussian process models.

### Strengths

The paper is technically strong, well-motivated, and clearly written. The central contribution, a novel inequality providing a lower bound on the normalization constant (Proposition 1), is an elegant and effective solution to the problem. This approach cleverly avoids the estimation issues associated with the method in [7]. Furthermore, the connections drawn to GP inducing-point methods are insightful, and the extension to variational inference is a significant advantage that broadens the applicability of the method. Overall, the paper presents a valuable contribution and was a pleasure to review.

### Concerns

Despite the strengths of the work, I have two technical concerns that I would like to see addressed:

1.  **Computational Advantage:** While the proposed method successfully avoids power iterations for eigenvalue estimation, it is not immediately clear that it offers a significant computational advantage over [7]. The method replaces eigenvalue estimation with a sequence of non-linear optimization problems of increasing dimensionality. The paper would be strengthened by a more direct discussion of the computational trade-offs involved in this exchange.

2.  **Convergence of Bounds:** A more significant concern relates to the convergence guarantees of the bounds. The procedure relies on solving a coupled optimization problem while incrementally increasing the cardinality of a set. It is not obvious that simply increasing the cardinality guarantees convergence of the bounds, particularly because the optimization problem is likely highly non-convex. There is a risk that the algorithm could become trapped in a local minimum, which could prevent the bounds from tightening sufficiently to make a decision on the MCMC accept/reject step. This potential failure mode should be addressed directly, as it could make it impossible to take an MCMC step.

### Presentation Issues

-   **Figure 1 (Page 7):** The figures are missing axis labels.
-   **Proof of Proposition 1:** The proof of the main proposition is the central insight that enables this work. Given its importance, it would be more appropriate to include it, or at least a proof sketch, in the main body of the paper rather than relegating it to the appendix.
-   **Typo (Page 7, Line 361):** There is a minor typo: "... the variational lower is ..."

### Conclusion

In summary, this is a high-quality paper that introduces a clever and valuable technique for inference in DPPs. The proposed bound on the partition function enables new MCMC and variational inference schemes and creates interesting links to other machine learning models. While there are some concerns regarding the practical computational trade-offs and the convergence properties of the optimization, the core ideas are novel and significant.

## (36) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2015/test/1ee3dfcd8a0645a25a35977997223d22/level4/gemini-2.5-pro/level4@P3PURE:::4.txt
### Human review:

The paper proposes a new framework for spectral regularized embedding, applied to graph transduction. The framework itself, and in particular the benefits for having an orthonormal embedding might be described more convincingly, but this is not a serious issue.
The authors then propose an interesting and elegant algorithm to solve the SEER problem approximately. This is an original contribution and it seems to provide a good alternative to solve the complex learning problem.
 Experimental results tend to demonstrate the benefits of the proposed solution. It would be great to show results that demonstrate the benefits of the SEER framework, or of the orthonormal representation defined by (3) at first, and also to show the approximation accuracy of the IIP solution to the SEER problem. This is not visible in the current results, and it would be of high interest to position the actual contribution in a more global context.
 The multiple graph transduction is unfortunately described at a very high level. It is definitely an interesting extension, but more details, motivation and intuitions are necessary to understand clearly how and why the proposed method is also interesting for multiple graph, and especially to understand how that algorithm is implement in such settings. In the current form, it is difficult to grasp the main ideas in the multiple graph case, and especially to really appreciate the experimental results in this case. In that respect, the last column of Table 4 (noisy case) is not very intuitive - it seems that one graph is better than multiple ones, which would contradict the motivation for dealing with multiple graphs.
 Finally, the paper is not always easy to read and pretty dense at places. It also refers at too many places to the supplementary material. It is probably a sign that the authors wants to give too much information in a single paper, which actually penalises the accessibility and probably visibility of the work.  The paper proposes a new framework, SEER for orthonormal embeddings that is applied to graph transduction. An interesting algorithm based on IIP is proposed to solve the learning problem in SEER, and relatively convincing results are proposed.

### Polished review:

This paper proposes SEER, a new framework for spectral regularized embedding applied to graph transduction. The authors then introduce an interesting and elegant algorithm to solve the SEER optimization problem approximately. While the core algorithm is an original and valuable contribution, the paper has several weaknesses in its current form regarding motivation, experimental analysis, and presentation.

The primary strength of the paper is the novel algorithm proposed to solve the SEER problem. It appears to be an elegant and effective alternative for this complex learning task.

However, several aspects of the paper could be significantly improved:

1.  **Framework Motivation:** The motivation for the SEER framework itself, and particularly the benefits of enforcing an orthonormal embedding as defined by (3), could be described more convincingly. While not a major flaw, a stronger justification would improve the paper's foundation.

2.  **Experimental Analysis:** The experimental results demonstrate the overall benefit of the final proposed solution, but they do not disentangle the individual contributions. To better position the work in a broader context, it would be highly valuable to see results that: a) specifically demonstrate the benefits of the SEER framework over alternatives, b) isolate the impact of the orthonormal representation, and c) evaluate the approximation accuracy of the proposed IIP solution with respect to the original SEER problem. The current results do not offer this level of insight.

3.  **Multiple Graph Transduction:** The extension to multiple graphs is unfortunately described at a very high level. It lacks the necessary detail, motivation, and intuition to clearly understand how the method is implemented and why it is advantageous in this setting. This lack of clarity makes it difficult to interpret and appreciate the corresponding experimental results. For example, the result in the last column of Table 4 (the noisy case) is counter-intuitive, as it seems to suggest that a single graph outperforms multiple graphs, which would contradict the motivation for the extension.

4.  **Clarity and Presentation:** The paper is dense and not always easy to read. It also refers to the supplementary material too frequently for core details. This suggests an attempt to include too much information in a single paper, which ultimately penalizes the accessibility and potential impact of the work.

In summary, the paper introduces a new framework and a promising algorithm for graph transduction. However, weaknesses in the experimental validation, the high-level description of the multi-graph extension, and overall clarity currently limit its contribution.

## (37) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2015/test/1ee3dfcd8a0645a25a35977997223d22/level4/Qwen3-30B-A3B-Thinking-2507-FP8/level4@P3PURE:::4.txt
### Human review:

The paper proposes a new framework for spectral regularized embedding, applied to graph transduction. The framework itself, and in particular the benefits for having an orthonormal embedding might be described more convincingly, but this is not a serious issue.
The authors then propose an interesting and elegant algorithm to solve the SEER problem approximately. This is an original contribution and it seems to provide a good alternative to solve the complex learning problem.
 Experimental results tend to demonstrate the benefits of the proposed solution. It would be great to show results that demonstrate the benefits of the SEER framework, or of the orthonormal representation defined by (3) at first, and also to show the approximation accuracy of the IIP solution to the SEER problem. This is not visible in the current results, and it would be of high interest to position the actual contribution in a more global context.
 The multiple graph transduction is unfortunately described at a very high level. It is definitely an interesting extension, but more details, motivation and intuitions are necessary to understand clearly how and why the proposed method is also interesting for multiple graph, and especially to understand how that algorithm is implement in such settings. In the current form, it is difficult to grasp the main ideas in the multiple graph case, and especially to really appreciate the experimental results in this case. In that respect, the last column of Table 4 (noisy case) is not very intuitive - it seems that one graph is better than multiple ones, which would contradict the motivation for dealing with multiple graphs.
 Finally, the paper is not always easy to read and pretty dense at places. It also refers at too many places to the supplementary material. It is probably a sign that the authors wants to give too much information in a single paper, which actually penalises the accessibility and probably visibility of the work.  The paper proposes a new framework, SEER for orthonormal embeddings that is applied to graph transduction. An interesting algorithm based on IIP is proposed to solve the learning problem in SEER, and relatively convincing results are proposed.

### Polished review:



The paper introduces a novel framework for spectral regularized embedding (SEER) applied to graph transduction, with a focus on orthonormal embeddings. While the framework's benefits for orthonormal embeddings could be more convincingly articulated, this remains a minor concern. The proposed IIP-based algorithm for approximately solving the SEER problem represents a clear original contribution and provides a compelling alternative for addressing the underlying learning challenge.  

However, the experimental evaluation lacks critical comparisons to fully position the contribution. Specifically, it would be valuable to demonstrate: (1) the benefits of the SEER framework itself or the orthonormal representation defined in Equation (3), and (2) the approximation accuracy of the IIP solution relative to the exact SEER problem. These comparisons are absent in the current results, hindering a clear understanding of the method's relative strengths.  

The extension to multiple graph transduction is described at a high level and appears underdeveloped. While the idea is promising, the paper lacks sufficient detail, motivation, and intuition to clarify *how* and *why* the method is advantageous for multiple graphs. This is especially problematic for interpreting the experimental results in this setting. For instance, the "noisy case" column in Table 4 (last column) shows superior performance for a single graph over multiple graphs, which contradicts the stated motivation for handling multiple graphs and lacks clear justification.  

Additionally, the paper is occasionally dense and over-reliant on supplementary material, which impedes readability and accessibility. This suggests the authors may have attempted to include excessive detail in the main text, ultimately diminishing the work's visibility and impact. Overall, the SEER framework and its IIP-based solution are promising, but the current presentation requires significant refinement to clearly establish the methodological contributions and experimental validity.

## (38) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2014/test/57aeee35c98205091e18d1140e9f38cf/level4/gemini-2.5-pro/level4@P2PURE:::2.txt
### Human review:

This paper proposes a new approach to derive the bound of the average causal effect (ACE) from a variable X to another Y. Its main principles is the use of Entner's Rule 1 in its inverse direction, the relaxation of the faithfulness assumption to introduce possibility of the path-cancellation at some degree, and the introduction of assumptions represented by some inequality constraints. A computation scheme of the ACE bound are formulated by using linear programing under these principles. Though the authors have not optimized the algorithm to derive the bounds yet, the resulted bounds seem very narrow and accurate in comparison with the other approaches in state of the art.
Quality
The authors tried to establish a novel method to derive more accurate bound of ACE than the state of the art. They combined several feasible principles and succeeded to provide the tighter bounds. In this regard, the content of the paper is very interesting. 
However, some criteria to define the bounds are not comprehensively explained. Particularly, the validity of the use of Entner's Rule 1 in the inverse direction is not clearly discussed. For its use in the inverse direction, the authors should explicitly assume the structure depicted in Fig.2. This should be clearly explained and discussed.
In addition, the generic criteria to choose appropriate parameters for relaxation are not provided. Since these affect the result of the bounds significantly, the principle to determine the parameters should be more investigated and included in the work.
Clarity
The explanation of the paper on the theoretical part seems basically comprehensive except the essential discussion I pointed out above. 
However, the demonstration of the experimental results are not well described. As I pointed out above, the actual implementation of the algorithm is not comprehensively explained. The definition of the parameters shown in Table 1 (Table 5?) are not clearly given.
In addition, I see some typos. For example;
"The full algorithm is shown in Table 1." on page 6=> I do not see any table of algorithm.
"Results are summarized in Table 5." on page 8=> I do not see Table 5 (maybe Table 1).
Originality
The problem setting of this paper has been addressed by some earlier work as the authors pointed out. In this regard, the scope of this paper does not have very string originality. 
The idea to combine the three ideas in a unified shape contains some originality. But, as I pointed out above, the validity of the combination is not very clearly discussed.
Significance
In terms of deriving the tighter bounds of ACE, this method shows some significance. However, its performance has been check by quite limited experiments. It generality in both theory and wide experiments has not been strictly assessed. The paper addresses an important problem which is to evaluate the bound of the strength of causal relations. However, the validity of the presented idea should be more well described in both theory and experiments.

### Polished review:

This paper proposes a new method for deriving bounds on the Average Causal Effect (ACE) between two variables, X and Y. The approach is based on three main principles: the inverse application of Entner's Rule 1, the relaxation of the faithfulness assumption to permit a degree of path-cancellation, and the introduction of assumptions framed as inequality constraints. Using these principles, the authors formulate a linear program to compute the ACE bounds. Although the algorithm has not yet been optimized, the initial results suggest that the derived bounds are significantly narrower and more accurate compared to other state-of-the-art approaches.

### Quality

The authors aim to establish a novel method for deriving tighter ACE bounds than existing techniques. By combining several plausible principles, they succeed in this goal, making the paper's contribution interesting.

However, the justification for some of the core components is not sufficiently explained. Specifically, the validity of applying Entner's Rule 1 in the inverse direction is not clearly discussed. To justify this inverse application, the authors must explicitly assume the causal structure depicted in Figure 2. This assumption and its implications should be clearly stated and thoroughly discussed.

Furthermore, the paper provides no generic criteria for selecting the parameters that govern the relaxation of the faithfulness assumption. Since these parameters significantly impact the resulting bounds, the principles for determining their values should be investigated more thoroughly and included in the work.

### Clarity

The theoretical exposition is largely comprehensive, aside from the critical omissions noted above.

However, the presentation of the experimental results is not well-described. The paper does not provide a comprehensive explanation of the algorithm's implementation. The definitions for the parameters shown in the results table (referred to as Table 1, but perhaps Table 5) are not clearly provided. Additionally, there are several typographical errors and incorrect references. For instance:
-   On page 6, the text states, "The full algorithm is shown in Table 1," but no such table is present.
-   On page 8, the text says, "Results are summarized in Table 5," which likely refers to Table 1.

### Originality

The problem of bounding ACE has been addressed in prior work, as the authors acknowledge. In this respect, the problem setting of the paper is not highly original.

The originality lies in the synthesis of the three core ideas—inverse rule application, faithfulness relaxation, and inequality constraints—into a unified framework. However, as previously mentioned, the validity and theoretical soundness of this combination are not rigorously discussed, which tempers the novelty of the contribution.

### Significance

The proposed method demonstrates potential significance in its ability to derive tighter ACE bounds. However, its performance has only been validated with a limited set of experiments. The method's generality has not been strictly assessed, either theoretically or through broader experimental evaluation. While the paper addresses the important problem of quantifying the strength of causal relationships, the validity of the proposed ideas must be better substantiated with both stronger theoretical arguments and more comprehensive experiments before its full significance can be determined.

## (39) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2014/test/57aeee35c98205091e18d1140e9f38cf/level4/gemini-2.5-pro/level4@P3PURE:::2.txt
### Human review:

This paper proposes a new approach to derive the bound of the average causal effect (ACE) from a variable X to another Y. Its main principles is the use of Entner's Rule 1 in its inverse direction, the relaxation of the faithfulness assumption to introduce possibility of the path-cancellation at some degree, and the introduction of assumptions represented by some inequality constraints. A computation scheme of the ACE bound are formulated by using linear programing under these principles. Though the authors have not optimized the algorithm to derive the bounds yet, the resulted bounds seem very narrow and accurate in comparison with the other approaches in state of the art.
Quality
The authors tried to establish a novel method to derive more accurate bound of ACE than the state of the art. They combined several feasible principles and succeeded to provide the tighter bounds. In this regard, the content of the paper is very interesting. 
However, some criteria to define the bounds are not comprehensively explained. Particularly, the validity of the use of Entner's Rule 1 in the inverse direction is not clearly discussed. For its use in the inverse direction, the authors should explicitly assume the structure depicted in Fig.2. This should be clearly explained and discussed.
In addition, the generic criteria to choose appropriate parameters for relaxation are not provided. Since these affect the result of the bounds significantly, the principle to determine the parameters should be more investigated and included in the work.
Clarity
The explanation of the paper on the theoretical part seems basically comprehensive except the essential discussion I pointed out above. 
However, the demonstration of the experimental results are not well described. As I pointed out above, the actual implementation of the algorithm is not comprehensively explained. The definition of the parameters shown in Table 1 (Table 5?) are not clearly given.
In addition, I see some typos. For example;
"The full algorithm is shown in Table 1." on page 6=> I do not see any table of algorithm.
"Results are summarized in Table 5." on page 8=> I do not see Table 5 (maybe Table 1).
Originality
The problem setting of this paper has been addressed by some earlier work as the authors pointed out. In this regard, the scope of this paper does not have very string originality. 
The idea to combine the three ideas in a unified shape contains some originality. But, as I pointed out above, the validity of the combination is not very clearly discussed.
Significance
In terms of deriving the tighter bounds of ACE, this method shows some significance. However, its performance has been check by quite limited experiments. It generality in both theory and wide experiments has not been strictly assessed. The paper addresses an important problem which is to evaluate the bound of the strength of causal relations. However, the validity of the presented idea should be more well described in both theory and experiments.

### Polished review:

This paper introduces a novel method to derive bounds for the average causal effect (ACE) between two variables, X and Y. The approach is based on three core principles: the application of Entner's Rule 1 in the inverse direction, a relaxation of the faithfulness assumption to permit a degree of path-cancellation, and the introduction of additional assumptions formulated as inequality constraints. Using these principles, the authors formulate the computation of the ACE bounds as a linear programming problem. Although the algorithm has not yet been optimized, preliminary results suggest that the method can produce significantly narrower and more accurate bounds compared to state-of-the-art approaches.

### Quality and Significance

The paper addresses the important problem of evaluating the strength of causal relations and attempts to establish a new method for deriving more accurate ACE bounds than existing techniques. The combination of several feasible principles to achieve tighter bounds is an interesting contribution. The preliminary results, which show narrow and accurate bounds, indicate the potential significance of this work.

However, the paper has several weaknesses that undermine its contributions.

1.  **Insufficient Theoretical Justification:** The criteria for defining the bounds are not comprehensively explained. A major concern is the lack of a clear discussion on the validity of applying Entner's Rule 1 in the inverse direction. This application appears to implicitly require a specific causal structure, such as the one depicted in Figure 2. This should be stated as an explicit assumption, and its implications must be thoroughly discussed to validate the theoretical foundation of the method.

2.  **Lack of Guidance on Parameter Selection:** The proposed method relies on parameters for relaxing the faithfulness assumption, which significantly affect the final bounds. However, the paper provides no generic criteria or a principled method for selecting these parameters. This is a critical omission that limits the practical applicability and reproducibility of the work. The authors should investigate and include principles for determining these parameters.

3.  **Limited Empirical Evaluation:** The method's performance has been evaluated in a limited experimental setting. Its generality has not been strictly assessed, making it difficult to judge its robustness and performance across a wider range of scenarios.

### Clarity

While the theoretical explanations are generally comprehensible, the paper's clarity is hampered by the critical theoretical omissions mentioned above.

Furthermore, the presentation of the experimental results is not well-described. The paper does not comprehensively explain the actual implementation of the algorithm, making it difficult to reproduce the results. The definitions of the parameters shown in Table 1 are not clearly provided. The manuscript also contains several typographical errors and incorrect cross-references that should be corrected. For example:
*   On page 6: "The full algorithm is shown in Table 1." An algorithm table does not appear to be present.
*   On page 8: "Results are summarized in Table 5." This likely refers to Table 1.

### Originality

The problem of ACE bounding is well-established, and the paper builds on prior work in this area. The main originality lies in the novel combination of three distinct ideas—inverse Entner's Rule, relaxed faithfulness, and inequality constraints—within a unified framework. However, as noted, the validity of this combination is not rigorously discussed, which currently weakens the originality of the contribution.

### Conclusion

This paper presents a promising approach for deriving tighter ACE bounds. However, the validity of the proposed ideas needs to be much better substantiated, both theoretically and empirically. The authors should provide a more rigorous justification for their methodological choices, offer clear guidance on parameter selection, and conduct a more thorough experimental evaluation to demonstrate the generalizability of their method.

## (40) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2017/test/024d7f84fff11dd7e8d9c510137a2381/level4/gemini-2.5-pro/level4@P2PURE:::3.txt
### Human review:

In this paper, the authors present an accelerated variant of the Min-Sum message-passing protocol for solving consensus problems in distributed optimization. The authors use the reparametrization techniques proposed in [Ruozzi and Tatikonda, 2013] and establish rates of convergence for the Min-Sum Splitting algorithm for solving consensus problems with quadratic objective functions. The main tool used for the analysis is the construction of an auxiliary linear process that tracks the evolution of the Min-Sum Splitting algorithm.
The main contributions of the paper can be summarized as follows: (i) provide analysis for the Min-Sum splitting algorithm using a new proof technique based on the introduction of an auxiliary process, (ii) design a Min-Sum protocol for consensus problems that achieves better convergence than previously established results, and (iii) show the connection between the proposed method, and lifted Markov chains and multi-step methods in convex optimization.
The motivation and contributions of the paper are clear. The paper is well written and easy to follow, however, it does contain several typos and grammatical mistakes (listed below). The proofs of Propositions 1 and 2, and Theorem 1 appear to be correct.
Typos and Grammatical errors:
- Line 34: "…with theirs neighbors…" -> "…with their neighbors…"
- Line 174: "double-stochastic" -> "doubly-stochastic"
- Line 183: "… can be casted as…" -> "… can be cast as…"
- Line 192: "…class of graph with…" -> "…class of graphs with…"
- Line 197: "…which seems to…" -> "…which seem to…"
- Line 206: "…additional overheads…" -> "…additional overhead…"
- Line 225: "…pugging…" -> "…plugging…"
- Line 238: "…are seen to…" -> "…are able to…"
- Line 240: "…both type of…" -> "…both types of…"
- Line 248: "…also seen to…" -> "…also shown to…"
- Line 279-280: "…to convergence to…" -> "…to converge to…"
- Line 300: "…,which scales like…" -> "…,which scale like…"
- Line 302: "…for the cycle,…" -> "…for cycle graphs,…"
Other minor comments:
- Lines 220 and 221: Do you mean "Lagrangian" and "Lagrange multipliers" instead of "Laplacian" and "Laplace multipliers"?
- The authors present 3 algorithms, and the quantities involved are not always explained or described. For example, what is R{vw} and r{vw} in Algorithm 2? Also, in Algorithm 2, the quantities \hat{R}^0 and \hat{r}^0 do not appear to be initialized. Moreover, since the auxiliary linear process is key to the analysis and the central idea of the paper, the authors show clearly state which variables correspond to this in Algorithm 3.
The paper also appears to be missing several references. More specifically:
- Lines 41 and 43: (Sub)gradient methods for consensus optimization. There are several more references that could be included:
-- Bertsekas and Tsitsiklis, Parallel and distributed computation: numerical methods, 1989
-- Sundhar Ram Srinivasan et. al., Incremental stochastic subgradient algorithms for convex optimization, 2009
-- Wei Shi, Extra: An exact first-order algorithm for decentralized consensus optimization, 2015
(and, of course, many more)
- Line 170: "The original literature…"
- Line 229: work by Polyak (Heavy-ball)
- Line 232: work by Nesterov
It would be interesting and useful if the authors could answer/comment and address in the paper the following:
- Although the paper is a theoretical paper, the authors should comment on the practicality of the method, and when such a method should be used as opposed to other distributed methods for consensus optimization. 
- What are the limitations of the Min-Sum Splitting method? 
- What is the intuition behind using the auxiliary process in the Min-Sum Splitting method?
- The results provided in this paper are for consensus problems with quadratic objective functions. Can this framework be extended to solve more general consensus problems that often arise in Machine Learning? 
- The authors should also clearly state why such an approach is of interest in the context of Machine Learning and for the Machine Learning community.
In summary, this paper is a purely theoretical paper in which the authors establish rates of convergence using a new proof technique and show the connections between their method and well-established methods in the literature. Overall, the ideas presented in this paper are interesting, however, the practicality of the method and intuition behind the results are missing, as well as some justification for the importance of this result for the Machine Learning community.

### Polished review:

This paper introduces an accelerated variant of the Min-Sum message-passing protocol, termed the Min-Sum Splitting algorithm, for solving distributed consensus optimization problems. Leveraging reparametrization techniques from [Ruozzi and Tatikonda, 2013], the authors establish convergence rates for problems with quadratic objective functions. The core of their analysis is a novel proof technique based on an auxiliary linear process designed to track the algorithm's evolution.

The main contributions are: (1) an analysis of the Min-Sum splitting algorithm via the novel auxiliary process proof technique; (2) a new Min-Sum protocol for consensus that demonstrates improved convergence rates over existing results; and (3) an exposition of the connections between the proposed method, lifted Markov chains, and multi-step methods in convex optimization.

The paper is well-written, with clear motivation and contributions. The technical arguments, including the proofs for Propositions 1 and 2 and Theorem 1, appear to be sound. However, the manuscript contains several typos and would benefit from clarification on a few points.

**Typos and Grammatical Errors:**
*   Line 34: "…with theirs neighbors…" should be "…with their neighbors…"
*   Line 174: "double-stochastic" should be "doubly-stochastic"
*   Line 183: "… can be casted as…" should be "… can be cast as…"
*   Line 192: "…class of graph with…" should be "…class of graphs with…"
*   Line 197: "…which seems to…" should be "…which seem to…"
*   Line 206: "…additional overheads…" should be "…additional overhead…"
*   Line 225: "…pugging…" should be "…plugging…"
*   Line 238: "…are seen to…" should be "…are able to…"
*   Line 240: "…both type of…" should be "…both types of…"
*   Line 248: "…also seen to…" should be "…also shown to…"
*   Lines 279-280: "…to convergence to…" should be "…to converge to…"
*   Line 300: "…,which scales like…" should be "…,which scale like…"
*   Line 302: "…for the cycle,…" should be "…for cycle graphs,…"

**Other Minor Comments:**
*   Lines 220 and 221: Should "Laplacian" and "Laplace multipliers" be "Lagrangian" and "Lagrange multipliers"?
*   The paper presents three algorithms, but the quantities involved are not always clearly defined. For example, R{vw} and r{vw} in Algorithm 2 are not explained. Furthermore, the quantities \hat{R}^0 and \hat{r}^0 do not appear to be initialized in Algorithm 2. Since the auxiliary linear process is central to the paper's analysis, the authors should explicitly state which variables in Algorithm 3 correspond to this process.

**Missing References:**
The paper appears to be missing citations in several key areas:
*   Lines 41 and 43: For (sub)gradient methods in consensus optimization, several foundational references could be included, such as:
    *   Bertsekas and Tsitsiklis, "Parallel and distributed computation: numerical methods," 1989
    *   Sundhar Ram et al., "Incremental stochastic subgradient algorithms for convex optimization," 2009
    *   Wei Shi et al., "Extra: An exact first-order algorithm for decentralized consensus optimization," 2015
*   Line 170: "The original literature…" requires a citation.
*   Line 229: The work of Polyak on the heavy-ball method should be cited.
*   Line 232: Nesterov's work on accelerated methods should be cited.

While the theoretical contributions are strong, the paper would be significantly improved by addressing the following points:
*   **Practicality:** A discussion on the practical implications of the proposed method is needed. When should practitioners choose this algorithm over other distributed methods for consensus optimization?
*   **Limitations:** The authors should elaborate on the potential limitations of the Min-Sum Splitting method.
*   **Intuition:** The intuition behind using an auxiliary process, a central element of the analysis, could be explained more thoroughly to benefit the reader.
*   **Generalization:** The analysis is currently restricted to quadratic objective functions. The authors should discuss the potential for extending this framework to the more general convex problems that are common in machine learning.
*   **Relevance to Machine Learning:** Crucially, the paper needs to more explicitly justify the relevance of these results to the machine learning community. Why is this specific approach of interest for NIPS?

In summary, this is a strong theoretical paper that introduces an interesting method with a novel proof technique and establishes connections to important concepts in optimization. However, its current impact is limited by a lack of discussion on the method's practical applications, limitations, and underlying intuition. To strengthen the paper, the authors should provide a clearer justification for the importance of this work to the machine learning community.

## (41) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2017/test/194cf6c2de8e00c05fcf16c498adc7bf/level4/Qwen3-30B-A3B-Thinking-2507-FP8/level4@P3PURE:::3.txt
### Human review:

The paper proposes a new approach to the study of eye movements. The authors correctly summarize the current state of the art (as far as I understand it, but I admit from the outset I am not an expert in perception or eye movements). Basically these approaches are based on a saliency map that is defined over an image and fixations points are selected in a optimization/maximization approach. This model (EYMOL) works according to a different assumption and instead is defined directly on trajectories of gaze according to a "Least Action Principle." The details of some of the math were beyond my ability to evaluate because I don't have the necessary physics background (particularly the extensive appendix). However, even still I was able to understand the key elements of the approach and how it differs from past models. The model is helpfully applied to real data set of eye-movements and is compared against a variety of alternative models. While it doesn't dominate on every measure, the results are favorable for the new approach and demonstrate that it has some validity.
I think the paper might be of interest to some people in the vision science community (e.g., attendees of VSS). I'm not quite as convinced this makes a great contribution to NIPS, however I think that should be evaluated against other reviewer's opinions who are more expert. I think it likely advances a new and interesting theory that could inspire further empirical research, and so has both novelty and merit for perception sciences.

### Polished review:



The paper introduces a novel framework for modeling eye movements, EYMOL, which diverges from prevailing approaches by operating directly on gaze trajectories via a "Least Action Principle" rather than relying on saliency maps and fixation point optimization. While I acknowledge my limited expertise in perception science and eye movement research (and thus cannot fully assess the physics-heavy mathematical details in the appendix), I found the core conceptual distinction and methodology clearly articulated. The authors effectively demonstrate that EYMOL offers a distinct theoretical foundation compared to existing models. The approach is rigorously evaluated on real eye-movement datasets and benchmarked against multiple alternative models. Although EYMOL does not consistently outperform all baselines across every metric, the results provide favorable evidence supporting its validity and potential utility.  

The work presents a conceptually novel and theoretically grounded contribution to vision science, likely to interest researchers at venues like VSS. However, I am not fully convinced this constitutes a substantial advancement for NIPS, as the primary contribution aligns more closely with empirical perception science than with core machine learning or computational neuroscience challenges addressed by the conference. Its significance for NIPS should be weighed against the assessment of reviewers with deeper expertise in vision science. That said, the paper advances an interesting theoretical perspective that could inspire future empirical work, establishing clear novelty and merit within its domain.

## (42) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2017/test/34ed066df378efacc9b924ec161e7639/level4/gemini-2.5-pro/level4@P3PURE:::2.txt
### Human review:

The paper proposes a human image generator conditioned on appearance and human pose. The proposed generation is based on adversarial training architecture where two-step generative networks that produces high resolution image to feed into a discriminator. In the generator part, the first generator produce a coarse image using a U-shape network given appearance and pose map, then the second generator takes the coarse input with the original appearance to predict residual to refine the coarse image. The paper utilizes the DeepFashion dataset for evaluation.
The paper proposes a few important ideas.
* Task novelty: introducing the idea of conditioning on appearance and pose map for human image generation
* Techniques: stacked architecture that predicts difference map rather than direct upsampling, and loss design
The paper can improve in terms of the following points to stand out.
* Still needs quality improvement
* Significance: the paper could be seen one of yet-another GAN architecture
* Problem domain: good vision/graphics application, but difficult to generalize to other learning problems
The paper is well organized to convey the key aspects of the proposed architecture. Conditioned on appearance and pose information, the proposed generator stacks two networks to adopt a coarse-to-fine strategy. This paper effectively utilize the generation strategy in the dressing problem. The proposed approach looks appropriate to the concerned problem scenario. The difference map generation also looks a small but nice technique in generating higher resolution images.
Probably the major complaints to the paper is that the generated results contain visible artifacts and still requires a lot of improvement for application perspective. For example, patterns in ID346 of Fig 4 results in black dots in the final result. Even though the second generator mitigates the blurry image from the first generator, it seems the model is still insufficient to recover high-frequency components in the target appearance.
Another possible but not severe concern is that some might say the proposed approach is an application of conditional GANs. Conditioning or stacking of generators for adversarial training have been proposed in the past; e.g., below, though they are arXiv papers. The paper includes application-specific challenges, but this might not appeal to large number of audiences.
* Han Zhang, Tao Xu, Hongsheng Li, Shaoting Zhang, Xiaolei Huang, Xiaogang Wang, Dimitris Metaxas, "StackGAN: Text to Photo-realistic Image Synthesis with Stacked Generative Adversarial Networks", arXiv:1612.03242.
* Xun Huang, Yixuan Li, Omid Poursaeed, John Hopcroft, Serge Belongie, Stacked Generative Adversarial Networks, arXiv:1612.04357.
In overall, the paper successfully proposed a solution to the pose-conditioned image problem, and properly conducts evaluation. The proposed approach sufficiently presents technical novelty. The resulting images still needs quality improvement, but the proposed model at least generate something visually consistent images. My initial rating is accept.

### Polished review:

This paper proposes a generative model for synthesizing human images conditioned on a target pose and an appearance encoding. The method is based on a generative adversarial network (GAN) architecture that employs a two-stage, coarse-to-fine generator. The first generator, a U-Net-like network, produces a coarse image from the input appearance and pose map. The second generator then takes this coarse output, along with the original appearance information, and predicts a residual map to refine the initial image, adding higher-frequency details. The model is trained and evaluated on the DeepFashion dataset.

**Strengths:**

*   **Task Novelty:** The paper introduces a novel and interesting task: generating realistic human images by explicitly conditioning on both appearance and pose. This is a challenging problem with clear applications in vision and graphics.
*   **Technical Contributions:** The proposed architecture includes several valuable ideas. The stacked, coarse-to-fine generator is an effective strategy for this task. Furthermore, having the second stage predict a difference (residual) map, rather than directly upsampling or generating the final image, is a simple yet effective technique for improving high-resolution synthesis.
*   **Clarity and Organization:** The paper is well-organized and clearly conveys the key aspects of the proposed architecture and methodology. The approach is well-suited for the target problem.

**Weaknesses:**

*   **Image Quality and Artifacts:** A major weakness is that the quality of the generated images requires significant improvement from an application perspective. The results contain visible artifacts. For instance, as seen in Figure 4 (ID346), complex patterns on clothing can degrade into black dots in the final generated image. While the second generator is intended to mitigate blurriness from the first stage, the model still appears insufficient for recovering high-frequency components from the target appearance.
*   **Incremental Novelty:** The contribution could be viewed as an application-specific extension of existing conditional GAN frameworks. The core ideas of conditioning a generator and stacking multiple generators for adversarial training have been explored in prior work (e.g., Zhang et al., "StackGAN", arXiv:1612.03242; Huang et al., "Stacked Generative Adversarial Networks", arXiv:1612.04357). While the paper addresses application-specific challenges, this focus may limit its appeal to a broader machine learning audience.
*   **Limited Generalizability:** The proposed solution is highly tailored to a specific computer vision and graphics problem. This makes it difficult to see how the techniques would generalize to other learning domains.

**Conclusion:**

Overall, the paper successfully proposes a novel solution to the challenging problem of pose-conditioned human image generation and provides a proper evaluation of its method. The proposed approach presents sufficient technical novelty, particularly in its coarse-to-fine architecture and use of a residual map for refinement. While the quality of the resulting images needs further improvement, the model generates visually consistent results that represent a solid step forward. My initial recommendation is to accept the paper.

## (43) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2017/test/34ed066df378efacc9b924ec161e7639/level4/Qwen3-30B-A3B-Thinking-2507-FP8/level4@P2PURE:::2.txt
### Human review:

The paper proposes a human image generator conditioned on appearance and human pose. The proposed generation is based on adversarial training architecture where two-step generative networks that produces high resolution image to feed into a discriminator. In the generator part, the first generator produce a coarse image using a U-shape network given appearance and pose map, then the second generator takes the coarse input with the original appearance to predict residual to refine the coarse image. The paper utilizes the DeepFashion dataset for evaluation.
The paper proposes a few important ideas.
* Task novelty: introducing the idea of conditioning on appearance and pose map for human image generation
* Techniques: stacked architecture that predicts difference map rather than direct upsampling, and loss design
The paper can improve in terms of the following points to stand out.
* Still needs quality improvement
* Significance: the paper could be seen one of yet-another GAN architecture
* Problem domain: good vision/graphics application, but difficult to generalize to other learning problems
The paper is well organized to convey the key aspects of the proposed architecture. Conditioned on appearance and pose information, the proposed generator stacks two networks to adopt a coarse-to-fine strategy. This paper effectively utilize the generation strategy in the dressing problem. The proposed approach looks appropriate to the concerned problem scenario. The difference map generation also looks a small but nice technique in generating higher resolution images.
Probably the major complaints to the paper is that the generated results contain visible artifacts and still requires a lot of improvement for application perspective. For example, patterns in ID346 of Fig 4 results in black dots in the final result. Even though the second generator mitigates the blurry image from the first generator, it seems the model is still insufficient to recover high-frequency components in the target appearance.
Another possible but not severe concern is that some might say the proposed approach is an application of conditional GANs. Conditioning or stacking of generators for adversarial training have been proposed in the past; e.g., below, though they are arXiv papers. The paper includes application-specific challenges, but this might not appeal to large number of audiences.
* Han Zhang, Tao Xu, Hongsheng Li, Shaoting Zhang, Xiaolei Huang, Xiaogang Wang, Dimitris Metaxas, "StackGAN: Text to Photo-realistic Image Synthesis with Stacked Generative Adversarial Networks", arXiv:1612.03242.
* Xun Huang, Yixuan Li, Omid Poursaeed, John Hopcroft, Serge Belongie, Stacked Generative Adversarial Networks, arXiv:1612.04357.
In overall, the paper successfully proposed a solution to the pose-conditioned image problem, and properly conducts evaluation. The proposed approach sufficiently presents technical novelty. The resulting images still needs quality improvement, but the proposed model at least generate something visually consistent images. My initial rating is accept.

### Polished review:



The paper introduces a human image generator conditioned on both appearance and pose information. The approach employs an adversarial training framework featuring a two-step generative architecture that produces high-resolution images for the discriminator. Specifically, the first generator (a U-shaped network) creates a coarse image from appearance and pose maps, while the second generator refines this output by predicting a residual map using the coarse image and original appearance. The method is evaluated on the DeepFashion dataset.

The paper presents several significant contributions:
* **Task novelty:** Introducing conditioning on appearance and pose maps for human image generation.
* **Technical innovations:** A stacked architecture that predicts residual maps rather than direct upsampling, along with a novel loss design.

To strengthen its impact, the paper should address the following limitations:
* **Quality improvement:** Current results exhibit visible artifacts and require substantial refinement for practical use.
* **Significance:** The work risks being perceived as merely another GAN architecture without clear differentiation.
* **Generalizability:** While highly applicable to vision/graphics tasks like dressing, the approach lacks broader relevance to other learning domains.

The paper is well-structured and clearly conveys its core methodology. The coarse-to-fine strategy, leveraging appearance and pose conditioning, is well-suited for the dressing problem. The residual-based refinement technique is a thoughtful contribution to high-resolution generation.

The primary concern is the persistent visual artifacts in generated images. For instance, Figure 4 (ID 346) shows black dots resulting from pattern inconsistencies. Although the second generator reduces blur from the first, the model remains inadequate for recovering high-frequency details in target appearances.

A secondary, less critical concern is that the stacked generator approach builds on prior work in conditional GANs. Similar concepts (e.g., stacked generators for adversarial training) have appeared in recent literature, such as:
* Zhang et al., "StackGAN: Text to Photo-realistic Image Synthesis with Stacked Generative Adversarial Networks" (arXiv:1612.03242)
* Huang et al., "Stacked Generative Adversarial Networks" (arXiv:1612.04357)

While the paper addresses application-specific challenges, this may limit its appeal to a wider audience beyond the vision/graphics community.

Overall, the paper successfully proposes a solution to pose-conditioned human image generation with appropriate evaluation. It demonstrates sufficient technical novelty and produces visually consistent outputs. Despite quality limitations, the core approach is sound. My initial rating is accept.

## (44) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2017/test/34ed066df378efacc9b924ec161e7639/level4/Qwen3-30B-A3B-Thinking-2507-FP8/level4@P3PURE:::2.txt
### Human review:

The paper proposes a human image generator conditioned on appearance and human pose. The proposed generation is based on adversarial training architecture where two-step generative networks that produces high resolution image to feed into a discriminator. In the generator part, the first generator produce a coarse image using a U-shape network given appearance and pose map, then the second generator takes the coarse input with the original appearance to predict residual to refine the coarse image. The paper utilizes the DeepFashion dataset for evaluation.
The paper proposes a few important ideas.
* Task novelty: introducing the idea of conditioning on appearance and pose map for human image generation
* Techniques: stacked architecture that predicts difference map rather than direct upsampling, and loss design
The paper can improve in terms of the following points to stand out.
* Still needs quality improvement
* Significance: the paper could be seen one of yet-another GAN architecture
* Problem domain: good vision/graphics application, but difficult to generalize to other learning problems
The paper is well organized to convey the key aspects of the proposed architecture. Conditioned on appearance and pose information, the proposed generator stacks two networks to adopt a coarse-to-fine strategy. This paper effectively utilize the generation strategy in the dressing problem. The proposed approach looks appropriate to the concerned problem scenario. The difference map generation also looks a small but nice technique in generating higher resolution images.
Probably the major complaints to the paper is that the generated results contain visible artifacts and still requires a lot of improvement for application perspective. For example, patterns in ID346 of Fig 4 results in black dots in the final result. Even though the second generator mitigates the blurry image from the first generator, it seems the model is still insufficient to recover high-frequency components in the target appearance.
Another possible but not severe concern is that some might say the proposed approach is an application of conditional GANs. Conditioning or stacking of generators for adversarial training have been proposed in the past; e.g., below, though they are arXiv papers. The paper includes application-specific challenges, but this might not appeal to large number of audiences.
* Han Zhang, Tao Xu, Hongsheng Li, Shaoting Zhang, Xiaolei Huang, Xiaogang Wang, Dimitris Metaxas, "StackGAN: Text to Photo-realistic Image Synthesis with Stacked Generative Adversarial Networks", arXiv:1612.03242.
* Xun Huang, Yixuan Li, Omid Poursaeed, John Hopcroft, Serge Belongie, Stacked Generative Adversarial Networks, arXiv:1612.04357.
In overall, the paper successfully proposed a solution to the pose-conditioned image problem, and properly conducts evaluation. The proposed approach sufficiently presents technical novelty. The resulting images still needs quality improvement, but the proposed model at least generate something visually consistent images. My initial rating is accept.

### Polished review:



The paper proposes a human image generation framework conditioned on appearance and pose information. The approach employs an adversarial training architecture featuring a two-step generative network: the first generator produces a coarse image via a U-shaped network using appearance and pose maps, while the second generator refines this output by predicting a residual map (using the coarse image and original appearance map) to reconstruct high-resolution details. The method is evaluated on the DeepFashion dataset.

The paper makes several noteworthy contributions.  
* **Task novelty**: Introducing appearance and pose conditioning for human image synthesis.  
* **Technical innovations**: A stacked architecture that generates a difference map (rather than direct upsampling) and a carefully designed loss function.  

However, the paper requires significant improvements to strengthen its impact:  
* **Quality limitations**: Generated images exhibit visible artifacts (e.g., black dots in ID346 of Figure 4), indicating insufficient recovery of high-frequency details despite the residual refinement step. The model remains inadequate for practical applications.  
* **Significance concern**: The work may be perceived as a routine extension of conditional GANs rather than a broadly impactful advancement.  
* **Domain specificity**: While well-suited for vision/graphics tasks like dressing synthesis, the approach lacks clear generalizability to other learning domains.  

The paper is well-organized and effectively communicates the coarse-to-fine generation strategy. The use of appearance and pose conditioning is appropriate for the problem, and the residual-based refinement constitutes a notable technical contribution for high-resolution synthesis.  

A key limitation is the persistent quality gap in generated outputs, as artifacts persist even after residual refinement. Additionally, while the method addresses application-specific challenges, the core technique overlaps with prior work on stacked generators for adversarial training. For instance:  
* Zhang et al. ("StackGAN," arXiv:1612.03242) and Huang et al. ("Stacked Generative Adversarial Networks," arXiv:1612.04357) have previously explored stacked generator architectures for conditional synthesis. The current work’s novelty is largely confined to the specific application domain.  

Overall, the paper successfully addresses the pose-conditioned human image generation problem with a technically sound approach and appropriate evaluation. While the generated images remain visually consistent, they require significant quality improvements. The technical novelty is sufficient for acceptance, though the work’s broader significance warrants stronger justification. I recommend acceptance.

## (45) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2017/test/34ed066df378efacc9b924ec161e7639/level4/Qwen3-30B-A3B-Thinking-2507-FP8/level4@P3PURE:::3.txt
### Human review:

This paper develops a GAN-type system to generate a novel-view person images guided by a target skeleton (represented as keypoints). The system contains mostly known techniques such as DCGANs, U-nets, so the contribution is about the specific computer vision application. 
Pros:
* The proposed idea is interesting, the writing is easy to follow, and empirical experiments show that it is able to synthesize images that are realistic-looking at some level.
Cons:
* As this work is application oriented, it is important to achieve good results. My main complain is 
	 there is no quantitative evaluation. For example, is it possible to organize user studies to evaluate how many times the generated images can trick human eyes.
	 the empirical results are not visually appealing. Take fig.1 for example, the generated images are too small to see. Even this way, there are many noticeable visual errors when comparing the results to the targets. It is thus a bit discouraging to conclude that the results so far are of good quality or close to real images. The same issue stays for almost all the results including the supplementary figures. Personally I feel the authors are at the right direction and the work is promising, while it is yet to stop and declare victory at this stage.
After rebuttal:
I am still not convinced after reading the authors' feedback. In particular, it has also been pointed by other reviewers that there are still issues regarding quantitative as well as qualitative results, all is important for such a practical oriented work. The rebuttal shows some attempts but they still do not address these concerns to a satisfied degree. I feel it may not be ready to be well presented in a venue like NIPS.

### Polished review:



This paper proposes a GAN-based framework for generating novel-view person images conditioned on skeletal keypoints. While the system integrates established components (e.g., DCGANs, U-Nets), the primary contribution lies in its application-specific design for pose-guided image synthesis.  

**Strengths:**  
The core idea is compelling and well-motivated, the exposition is clear and accessible, and preliminary experiments demonstrate moderate realism in synthesized outputs.  

**Major Concerns:**  
The work lacks essential evaluation rigor for a practical application. Crucially, there is no quantitative assessment of output quality (e.g., no user studies measuring perceptual realism or human deception rates). The qualitative results further undermine confidence: Figure 1’s generated images are too low-resolution for meaningful analysis, and visible artifacts (e.g., inconsistent body parts, pose misalignment) persist when comparing outputs to targets. These issues extend to all presented results, including supplementary figures. The authors’ claim of "high-quality" synthesis appears premature given these limitations.  

**Post-Rebuttal Assessment:**  
Despite the authors’ response, the core concerns remain unaddressed. As noted by other reviewers, both quantitative and qualitative deficiencies persist, which are critical for a venue like NIPS. The rebuttal’s attempts to mitigate these issues fall short of resolving the evaluation gaps. The work shows promise but remains insufficiently validated for publication at this stage.

## (46) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2017/test/34ed066df378efacc9b924ec161e7639/level4/Qwen3-30B-A3B-Thinking-2507-FP8/level4@P3PURE:::1.txt
### Human review:

Summary:
The paper proposes an architecture for generating a images containing a person that combines the appearance of a person in an input image and a specified input pose (using heat maps).
Strengths:
+ the proposed task is novel
+ novel two stage coarse-to-fine architecture
+ well written
+ while the results contain discernible artifacts, they are promising
+ extensive evaluation of design decisions
Weaknesses:
- the quantitative evaluation is generally weak; this is understandable (and not a major weakness) given that no suitable evaluation metrics exist
Comments:
Given the iterative refinement nature of the proposed architecture, it is suggested that some recent work on iterative refinement using cascaded networks be included in the related work, e.g., [a,b]:
[a] J. Carreira, P. Agrawal, K. Fragkiadaki, and J. Malik. H man pose estimation with iterative error feedback. In IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2016.
[b] A. Newell, K. Yang, and J. Deng. Stacked hourglass networks for human pose estimation. In European Conference on Computer Vision (ECCV), 2016.
- line 110: "we find that using residual blocks as basic component improves the generation performance" In what way? Please elaborate.
While the evaluation is generally extensive, I was left curious how using the Stage 2 network with the inputs for Stage 1 and trained adversarially would perform. Is the blurring observed with Stage 1 + GAN due to the intermediate fully connected layer?
Overall rating:
Based on the novelty of the problem and approach I am confidently recommending that the paper be accepted.
Rebuttal:
While this reviewer appreciates the attempt at a user study, given its very preliminary nature, I do not find it convincing and thus am discount it in my review rating. The authors are urged to include a substantive human evaluation in their revision. Nonetheless, my positive review of the work still stands.

### Polished review:



Summary:  
This paper introduces a novel architecture for generating images of persons by synthesizing appearance from an input image with a specified pose (encoded via heatmaps).  

Strengths:  
+ The task definition is novel and addresses a meaningful gap in person image synthesis.  
+ The proposed two-stage coarse-to-fine architecture is innovative and well-motivated.  
+ The paper is clearly written and technically sound.  
+ Despite visible artifacts in results, the generated images demonstrate promising quality.  
+ The evaluation includes extensive ablation studies on design choices.  

Weaknesses:  
- Quantitative evaluation is limited due to the absence of established metrics for this task; this is understandable and not a major weakness.  

Comments:  
1. Given the iterative refinement nature of the architecture, the related work section should incorporate recent advances in iterative refinement via cascaded networks, such as:  
   [a] Carreira et al., "Human Pose Estimation with Iterative Error Feedback," CVPR 2016.  
   [b] Newell et al., "Stacked Hourglass Networks for Human Pose Estimation," ECCV 2016.  

2. Line 110 states, "we find that using residual blocks as the basic component improves generation performance." Please elaborate on *how* residual blocks specifically enhance performance (e.g., stability, artifact reduction, or fidelity metrics).  

3. The evaluation is comprehensive, but it leaves unresolved curiosity: How would Stage 2 perform when initialized with Stage 1 outputs and trained adversarially? Is the blurring observed in Stage 1 + GAN results attributable to the intermediate fully connected layer?  

Overall Rating:  
The novelty of the problem and approach, coupled with the promising results and thorough design evaluation, warrant a confident recommendation for acceptance.  

Rebuttal:  
While the authors include a preliminary user study, its limited scope renders it inconclusive. This will not factor into the final rating. The authors are strongly encouraged to replace it with a rigorous human evaluation in revision. Nevertheless, the paper’s technical merits remain compelling, and the recommendation for acceptance stands.

## (47) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2013/test/24681928425f5a9133504de568f5f6df/level4/gemini-2.5-pro/level4@P2PURE:::2.txt
### Human review:

This paper presents a method for learning the structure as well as the parameters of stochastic AND-OR grammars. Such grammars contain AND rules and OR rules and can be used to represent several recursive phenomena, including natural language and even grammars. The authors present a nice method for unsupervised structure learning of these grammars by introducing new AND-OR fragments at consecutive steps, and measuring the likelihood and prior gains of their model. 
The authors present experiments on two tasks: learning event grammars and learning image grammars. In both they achieve results that are competitive with prior art. 
I liked the overall paper as it seems to be a tractable way of learning stochastic grammars that can be modeled using AND and OR rules. My criticism of the paper stems from the following observations: 
1) The authors do not mention how tractable the learning algorithm is. Will it scale to thousands of datapoints? 
2) I would have liked to seen experiments on natural language sentences as natural language is the most obvious application of such grammars. Will it be even possible to learn using the presented methods on the Penn Treebank dataset for example, on which previous work has focused on (say, Klein and Manning)? This paper presents a way of estimating the structure and parameters of stochastic AND-OR grammars and presents nice results on two tasks; I would have liked to see more experiments, especially on natural language data.

### Polished review:

This paper proposes a method for the unsupervised learning of both the structure and parameters of stochastic AND-OR grammars. These grammars, which utilize both AND and OR rules, are capable of representing various recursive phenomena. The proposed learning algorithm iteratively introduces new AND-OR fragments, which are accepted based on improvements to the data likelihood and a model prior.

The authors demonstrate their method on two tasks—learning event grammars and image grammars—achieving results that are competitive with previous work.

The paper's main strength is its presentation of a seemingly tractable approach for learning these expressive grammars. However, my assessment is tempered by two primary concerns:

1.  The computational tractability and scalability of the learning algorithm are not discussed. It is unclear whether the method can scale effectively to datasets containing thousands of data points.

2.  The paper omits experiments on natural language, which is one of the most natural and significant applications for such grammatical models. It would be highly informative to assess the method's performance on a standard benchmark like the Penn Treebank, which has been the focus of related prior work (e.g., Klein and Manning). While the results on event and image tasks are valuable, including experiments on language data would more convincingly establish the general utility and capabilities of the proposed approach.

## (48) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/nips_2013-2017/2013/test/24681928425f5a9133504de568f5f6df/level4/gemini-2.5-pro/level4@P3PURE:::2.txt
### Human review:

This paper presents a method for learning the structure as well as the parameters of stochastic AND-OR grammars. Such grammars contain AND rules and OR rules and can be used to represent several recursive phenomena, including natural language and even grammars. The authors present a nice method for unsupervised structure learning of these grammars by introducing new AND-OR fragments at consecutive steps, and measuring the likelihood and prior gains of their model. 
The authors present experiments on two tasks: learning event grammars and learning image grammars. In both they achieve results that are competitive with prior art. 
I liked the overall paper as it seems to be a tractable way of learning stochastic grammars that can be modeled using AND and OR rules. My criticism of the paper stems from the following observations: 
1) The authors do not mention how tractable the learning algorithm is. Will it scale to thousands of datapoints? 
2) I would have liked to seen experiments on natural language sentences as natural language is the most obvious application of such grammars. Will it be even possible to learn using the presented methods on the Penn Treebank dataset for example, on which previous work has focused on (say, Klein and Manning)? This paper presents a way of estimating the structure and parameters of stochastic AND-OR grammars and presents nice results on two tasks; I would have liked to see more experiments, especially on natural language data.

### Polished review:

This paper proposes a method for the unsupervised learning of both the structure and parameters of stochastic AND-OR grammars. These grammars, which utilize AND and OR production rules, are capable of representing a variety of recursive phenomena, including natural language and compositional visual scenes. The authors introduce an effective approach for structure learning that iteratively proposes new AND-OR fragments and evaluates them based on the resulting increase in data likelihood and the model prior.

The method is evaluated on two tasks: learning event grammars from video and learning image grammars. On both tasks, the reported results are competitive with those of prior work.

Overall, the paper presents a promising and seemingly tractable approach for learning a powerful class of stochastic grammars. However, my primary criticisms are as follows:

1.  The scalability of the learning algorithm is not discussed. The paper provides no analysis of the method's computational complexity or its performance on larger datasets, leaving it unclear whether it can scale to problems involving thousands of data points.

2.  The paper lacks experiments on natural language, which is a primary and motivating application for this type of grammar. It would be valuable to see if the proposed method can be applied to standard benchmarks like the Penn Treebank, which has been the focus of related grammar induction research (e.g., Klein and Manning). The absence of such experiments makes it difficult to assess the broader applicability of the approach.

In summary, while this paper introduces a compelling method and presents encouraging results on two tasks, it would be significantly strengthened by an analysis of the algorithm's scalability and an empirical evaluation on natural language data.

## (49) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/iclr_2017/test/330/level4/meta-llama-Llama-3.1-70B-Instruct-AWQ-INT4/level4@P2PURE:::3.txt
### Human review:

This paper proposes learning document embeddings as a sum of the constituent word embeddings, which are jointly learned and randomly dropped out ('corrupted') during training. While none of the pieces of this model are particularly novel, the result is an efficient learning algorithm for document representation with good empirical performance.
Joint training of word and document embeddings is not a new idea, nor is the idea of enforcing the document to be represented by the sum of its word embeddings (see, e.g. '"The Sum of Its Parts": Joint Learning of Word and Phrase Representations with Autoencoders' by Lebret and Collobert). Furthermore, the corruption mechanism is nothing other than traditional dropout on the input layer. Coupled with the word2vec-style loss and training methods, this paper offers little on the novelty front.
On the other hand, it is very efficient at generation time, requiring only an average of the word embeddings rather than a complicated inference step as in Doc2Vec. Moreover, by construction, the embedding captures salient global information about the document -- it captures specifically that information that aids in local-context prediction. For such a simple model, the performance on sentiment analysis and document classification is quite encouraging.
Overall, despite the lack of novelty, the simplicity, efficiency, and performance of this model make it worthy of wider readership and study, and I recommend acceptance.

### Polished review:

This paper proposes a document embedding model that learns to represent documents as a sum of their constituent word embeddings, which are jointly learned and randomly dropped out ('corrupted') during training. Although the individual components of this model are not particularly novel, the resulting algorithm is efficient for learning document representations and achieves good empirical performance.

The idea of jointly training word and document embeddings is not new, and the concept of representing documents as the sum of their word embeddings has been explored previously (e.g., 'The Sum of Its Parts': Joint Learning of Word and Phrase Representations with Autoencoders' by Lebret and Collobert). Moreover, the corruption mechanism employed in this paper is essentially traditional dropout applied to the input layer. When combined with word2vec-style loss and training methods, this paper does not offer significant novelty.

However, the model has the advantage of being very efficient at generation time, requiring only the average of word embeddings, as opposed to a more complex inference step as in Doc2Vec. Furthermore, by design, the embedding captures salient global information about the document, specifically the information that aids in local-context prediction. Given the simplicity of the model, its performance on sentiment analysis and document classification tasks is quite encouraging.

Overall, despite the lack of novelty, the model's simplicity, efficiency, and performance make it worthy of wider readership and study. Therefore, I recommend acceptance.

## (50) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/iclr_2017/test/330/level4/gemini-2.5-pro/level4@P2PURE:::3.txt
### Human review:

This paper proposes learning document embeddings as a sum of the constituent word embeddings, which are jointly learned and randomly dropped out ('corrupted') during training. While none of the pieces of this model are particularly novel, the result is an efficient learning algorithm for document representation with good empirical performance.
Joint training of word and document embeddings is not a new idea, nor is the idea of enforcing the document to be represented by the sum of its word embeddings (see, e.g. '"The Sum of Its Parts": Joint Learning of Word and Phrase Representations with Autoencoders' by Lebret and Collobert). Furthermore, the corruption mechanism is nothing other than traditional dropout on the input layer. Coupled with the word2vec-style loss and training methods, this paper offers little on the novelty front.
On the other hand, it is very efficient at generation time, requiring only an average of the word embeddings rather than a complicated inference step as in Doc2Vec. Moreover, by construction, the embedding captures salient global information about the document -- it captures specifically that information that aids in local-context prediction. For such a simple model, the performance on sentiment analysis and document classification is quite encouraging.
Overall, despite the lack of novelty, the simplicity, efficiency, and performance of this model make it worthy of wider readership and study, and I recommend acceptance.

### Polished review:

This paper presents a method for learning document embeddings by summing the embeddings of their constituent words. These word representations are learned jointly, with a random dropout mechanism (termed 'corruption') applied during training. While the model's individual components are not novel, the resulting algorithm for learning document representations is both efficient and empirically effective.

The joint training of word and document embeddings is not a new concept, nor is the approach of composing a document vector from the sum of its word vectors (e.g., Lebret and Collobert, "The Sum of Its Parts"). Furthermore, the proposed corruption mechanism is functionally equivalent to applying standard dropout to the input layer. When combined with a word2vec-style loss and training methodology, the paper's contribution in terms of novelty is limited.

On the other hand, the model possesses significant practical advantages. It is highly efficient at inference time, requiring only an average of word embeddings rather than a complex optimization step, as is necessary for models like Doc2Vec. By construction, the document embedding captures salient global information—specifically, the information that aids in the prediction of local word contexts. For such a straightforward model, its performance on sentiment analysis and document classification tasks is quite encouraging.

In summary, despite the limited novelty, the model's simplicity, efficiency, and strong performance make it a valuable contribution worthy of wider readership and further study. I therefore recommend acceptance.

## (51) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/iclr_2017/test/330/level4/gemini-2.5-pro/level4@P3PURE:::3.txt
### Human review:

This paper proposes learning document embeddings as a sum of the constituent word embeddings, which are jointly learned and randomly dropped out ('corrupted') during training. While none of the pieces of this model are particularly novel, the result is an efficient learning algorithm for document representation with good empirical performance.
Joint training of word and document embeddings is not a new idea, nor is the idea of enforcing the document to be represented by the sum of its word embeddings (see, e.g. '"The Sum of Its Parts": Joint Learning of Word and Phrase Representations with Autoencoders' by Lebret and Collobert). Furthermore, the corruption mechanism is nothing other than traditional dropout on the input layer. Coupled with the word2vec-style loss and training methods, this paper offers little on the novelty front.
On the other hand, it is very efficient at generation time, requiring only an average of the word embeddings rather than a complicated inference step as in Doc2Vec. Moreover, by construction, the embedding captures salient global information about the document -- it captures specifically that information that aids in local-context prediction. For such a simple model, the performance on sentiment analysis and document classification is quite encouraging.
Overall, despite the lack of novelty, the simplicity, efficiency, and performance of this model make it worthy of wider readership and study, and I recommend acceptance.

### Polished review:

This paper proposes a method for learning document embeddings by summing the embeddings of their constituent words. These word and document embeddings are learned jointly, with a random subset of words dropped out from each document during training. While the individual components of the model are not novel, the resulting algorithm is an efficient and empirically effective method for learning document representations.

The paper's contribution in terms of novelty is limited. The core ideas—jointly training word and document vectors, and representing a document as a sum of its word embeddings—have been explored previously (e.g., Lebret and Collobert, "The Sum of Its Parts": Joint Learning of Word and Phrase Representations with Autoencoders). Furthermore, the proposed "corruption" mechanism is equivalent to applying standard dropout to the input word vectors. When combined with a word2vec-style objective and training procedure, the overall framework presents a combination of existing techniques rather than a fundamentally new approach.

Despite its limited novelty, the model's primary strengths are its simplicity and efficiency. At inference time, generating a document embedding requires only a simple averaging of its word vectors, a significant advantage over methods like Doc2Vec that necessitate a more complex inference step. By construction, the resulting document embedding captures salient global information, specifically the information that is most useful for predicting words in a local context. Given its simplicity, the model achieves encouraging performance on downstream tasks such as sentiment analysis and document classification.

In summary, while the paper lacks significant novelty, its proposed model is simple, efficient, and performs well. These practical strengths make the work a valuable contribution that is worthy of study by the community. Therefore, I recommend acceptance.

## (52) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/iclr_2017/test/330/level4/Qwen3-30B-A3B-Thinking-2507-FP8/level4@P3PURE:::1.txt
### Human review:

This paper discusses a method for computing vector representations for documents by using a skip-gram style learning mechanism with an added regularizer in the form of a global context vector with various bits of drop out. While none of the individual components proposed in this paper are new, I believe that the combination in this fashion is. Further, I appreciated the detailed analysis of model behaviour in section 3.
The main downside to this submission is in its relative weakness on the empirical front. Arguably there are more interesting tasks than sentiment analysis and k-way classification! Likewise, why waste 2/3 of a page on t-sne projections rather than use that space for further analysis?
While I am a bit disappointed by this reduced evaluation and agree with the other reviewers concerning soft baselines, I think this paper should be accepted: it's an interesting algorithm, nicely composed and very efficient, so it's reasonable to assume that other readers might have use for some of the ideas presented here.

### Polished review:



This paper proposes a method for computing document vector representations using a skip-gram style learning mechanism enhanced with a global context vector regularizer and various dropout variants. While the individual components are not novel, the specific combination represents a meaningful contribution. I particularly appreciate the detailed behavioral analysis presented in Section 3.  

The primary weakness of this submission lies in its empirical evaluation. The experimental scope is limited to sentiment analysis and k-way classification tasks, which are relatively narrow compared to more challenging or diverse document understanding benchmarks. Furthermore, dedicating two-thirds of a page to t-SNE visualizations—rather than expanding the analysis of model performance or comparing against additional baselines—reduces the paper's empirical impact. Although I share other reviewers' concerns regarding the comparison to soft baselines, the method's conceptual novelty, clear exposition, and computational efficiency justify its acceptance. The approach offers a practical and efficient framework that could benefit a broader audience, making it a valuable contribution to the field despite the limited empirical evaluation.

## (53) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/iclr_2017/test/363/level4/Qwen3-30B-A3B-Thinking-2507-FP8/level4@P3PURE:::1.txt
### Human review:

This paper proposed a compare-aggregate model for the NLP tasks that require semantically comparing the text sequences, such as question answering and textual entailment.
The basic framework of this model is to apply a convolutional neural network (aggregation) after a element-wise operation (comparison) over the attentive outputs of the LSTMs. 
The highlighted part is the comparison, where this paper compares several different methods for matching text sequences, and the element-wise subtraction/multiplication operations are demonstrated to achieve generally better performance on four different datasets.
While the weak point is that this is an incremental work and a bit lack of innovation. A qualitative evaluation about how subtraction, multiplication and other comparison functions perform on varied kinds of sentences would be more interesting.

### Polished review:



This paper introduces a compare-aggregate model for NLP tasks requiring semantic comparison of text sequences, such as question answering and textual entailment. The core framework processes text sequences through attentive LSTMs, followed by an element-wise comparison operation (e.g., subtraction or multiplication), and finally aggregates the results via a convolutional neural network. The primary contribution lies in systematically evaluating multiple comparison operations for sequence matching; the authors demonstrate that element-wise subtraction and multiplication consistently outperform alternatives across four distinct datasets. While the empirical results are solid, the work represents an incremental advancement rather than a novel conceptual leap. A more compelling qualitative analysis examining how subtraction, multiplication, and other comparison functions behave across diverse sentence structures would significantly strengthen the paper’s contribution.

## (54) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/iclr_2017/test/333/level4/gpt-5/level4@P2PURE:::2.txt
### Human review:

This paper provides an interesting analysis of the conditions which enable generation of natural looking textures. The results is quite surprising, and analysis is quite thorough. 
I do think the evaluation methods require more work, but as other reviewers mentioned this could be an interesting line of work moving forwards and does not take too much from this current paper which, I think, should be accepted.

### Polished review:

This paper offers an insightful analysis of the conditions that enable the generation of natural-looking textures. The results are quite surprising, and the analysis is thorough. I do think the evaluation methodology requires further work; however, as other reviewers have noted, this is a promising avenue for future research and does not substantially detract from the present paper, which I believe should be accepted.

## (55) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/iclr_2017/test/333/level4/meta-llama-Llama-3.1-70B-Instruct-AWQ-INT4/level4@P2PURE:::2.txt
### Human review:

This paper provides an interesting analysis of the conditions which enable generation of natural looking textures. The results is quite surprising, and analysis is quite thorough. 
I do think the evaluation methods require more work, but as other reviewers mentioned this could be an interesting line of work moving forwards and does not take too much from this current paper which, I think, should be accepted.

### Polished review:

This paper provides an interesting analysis of the conditions that enable the generation of natural-looking textures, yielding quite surprising results. The analysis is thorough and well-conducted. However, I believe the evaluation methods require further refinement. Nevertheless, as other reviewers have noted, this work presents an interesting direction for future research, and its limitations do not detract significantly from the contributions of this paper, which I think merits acceptance.

## (56) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/iclr_2017/test/333/level4/gemini-2.5-pro/level4@P2PURE:::2.txt
### Human review:

This paper provides an interesting analysis of the conditions which enable generation of natural looking textures. The results is quite surprising, and analysis is quite thorough. 
I do think the evaluation methods require more work, but as other reviewers mentioned this could be an interesting line of work moving forwards and does not take too much from this current paper which, I think, should be accepted.

### Polished review:

This paper presents a thorough analysis of the conditions that enable the generation of naturalistic textures. The results are surprising, and the analysis is compelling.

While the evaluation methods could be improved, this does not significantly detract from the paper's core contributions. As other reviewers have noted, this work opens up a promising line of inquiry for future research. Therefore, I believe the paper should be accepted.

## (57) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/iclr_2017/test/333/level4/gemini-2.5-pro/level4@P3PURE:::2.txt
### Human review:

This paper provides an interesting analysis of the conditions which enable generation of natural looking textures. The results is quite surprising, and analysis is quite thorough. 
I do think the evaluation methods require more work, but as other reviewers mentioned this could be an interesting line of work moving forwards and does not take too much from this current paper which, I think, should be accepted.

### Polished review:

This paper presents a thorough and interesting analysis of the conditions required for generating natural-looking textures. The results are surprising, and the analysis is comprehensive.

While I believe the evaluation methods could be strengthened, this point has been raised by other reviewers and represents a promising direction for future work. This limitation does not significantly detract from the core contributions of the current paper. Given its novel insights, I recommend that it be accepted.

## (58) /home/rounak/ai-involvement-in-peer-reviews/Data_Preprocessing/cleandata/hard-subset/iclr_2017/test/333/level4/Qwen3-30B-A3B-Thinking-2507-FP8/level4@P3PURE:::2.txt
### Human review:

This paper provides an interesting analysis of the conditions which enable generation of natural looking textures. The results is quite surprising, and analysis is quite thorough. 
I do think the evaluation methods require more work, but as other reviewers mentioned this could be an interesting line of work moving forwards and does not take too much from this current paper which, I think, should be accepted.

### Polished review:



This paper presents an interesting analysis of the conditions enabling the generation of natural-looking textures, with results that are particularly surprising and supported by a thorough analysis. While the evaluation methods require further refinement, as noted by other reviewers, this represents a promising direction for future work and does not undermine the paper's core contributions. The paper should be accepted.

