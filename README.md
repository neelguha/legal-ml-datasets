# Datasets for Machine Learning in Law

This is a collection of pointers to datasets/tasks/benchmarks pertaining to the intersection of machine learning and law.

This page is continually being updated. If there's a dataset/resource you think should be included here, please make a pull request adding it, or contact me at nguha@stanford.edu and I'll add it!

A spreadsheet corresponding to the papers listed here can be found [here](https://docs.google.com/spreadsheets/d/11o7R3TRtREbDcxcbCMUERu5WRZsgLZtTaRFUhr4jLtk/edit?usp=sharing).

Neel Guha

 ---

### [A Corpus of eRulemaking User Comments for Measuring Evaluability of Arguments](https://facultystaff.richmond.edu/~jpark/papers/jpark_lrec18.pdf)

>eRulemaking is a means for government agencies to directly reach citizens to solicit their opinions and experiences regarding newly proposed rules. The effort, however, is partly hampered by citizens’ comments that lack reasoning and evidence, which are largely ignored since government agencies are unable to evaluate the validity and strength. We present Cornell eRulemaking Corpus – CDCP, an argument mining corpus annotated with argumentative structure information capturing the evaluability of arguments. The corpus consists of 731 user comments on Consumer Debt Collection Practices (CDCP) rule by the Consumer Financial Protection Bureau (CFPB); the resulting dataset contains 4931 elementary unit and 1221 support relation annotations. It is a resource for building argument mining systems that can not only extract arguments from unstructured text, but also identify what additional information is necessary for readers to understand and evaluate a given argument. Immediate applications include providing real-time feedback to commenters, specifying which types of support for which propositions can be added to construct better-formed arguments.


### [A Dataset for Statutory Reasoning in Tax Law Entailment and Question Answering](https://ceur-ws.org/Vol-2645/paper5.pdf)

>Legislation can be viewed as a body of prescriptive rules expressed in natural language. The application of legislation to facts of a case we refer to as statutory reasoning, where those facts are also expressed in natural language. Computational statutory reasoning is distinct from most existing work in machine reading, in that much of the information needed for deciding a case is declared exactly once (a law), while the information needed in much of machine reading tends to be learned through distributional language statistics. To investigate the performance of natural language understanding approaches on statutory reasoning, we introduce a dataset, together with a legal-domain text corpus. Straightforward application of machine reading models exhibits low out-of-the-box performance on our questions, whether or not they have been fine-tuned to the legal domain. We contrast this with a hand-constructed Prolog-based system, designed to fully solve the task. These experiments support a discussion of the challenges facing statutory reasoning moving forward, which we argue is an interesting real-world task that can motivate the development of models able to utilize prescriptive rules specified in natural language.


### [ACL/CoLing Dataset](https://usableprivacy.org/data)

>We created a corpus of 1,010 privacy policies from the top websites ranked on Alexa.com. The privacy policies in the dataset were retrieved in December 2013 and January 2014.


### [APP-350 Dataset](https://usableprivacy.org/data)

>The APP-350 Corpus consists of 350 Android app privacy policies annotated with privacy practices (i.e., behavior that can have privacy implications).


### [AsyLex: A Dataset for Legal Language Processing of Refugee Claims](https://aclanthology.org/2023.nllp-1.24/)

>Advancements in natural language processing (NLP) and language models have demonstrated immense potential in the legal domain, enabling automated analysis and comprehension of legal texts. However, developing robust models in Legal NLP is significantly challenged by the scarcity of resources. This paper presents AsyLex, the first dataset specifically designed for Refugee Law applications to address this gap. The dataset introduces 59,112 documents on refugee status determination in Canada from 1996 to 2022, providing researchers and practitioners with essential material for training and evaluating NLP models for legal research and case review. Case review is defined as entity extraction and outcome prediction tasks. The dataset includes 19,115 gold-standard human-labeled annotations for 20 legally relevant entity types curated with the help of legal experts and 1,682 gold-standard labeled documents for the case outcome. Furthermore, we supply the corresponding trained entity extraction models and the resulting labeled entities generated through the inference process on AsyLex. Four supplementary features are obtained through rule-based extraction. We demonstrate the usefulness of our dataset on the legal judgment prediction task to predict the binary outcome and test a set of baselines using the text of the documents and our annotations. We observe that models pretrained on similar legal documents reach better scores, suggesting that acquiring more datasets for specialized domains such as law is crucial.


### [Australian Legal Cases](https://archive.ics.uci.edu/dataset/239/legal+case+reports)

>A textual corpus of 4000 legal cases for automatic summarization and citation analysis. For each document we collect catchphrases, citations sentences, citation catchphrases and citation classes.


### [Board of Veterans Appeals Summarization](https://dl.acm.org/doi/10.1145/3322640.3326728)

>We report on a pilot experiment in automatic, extractive summarization of legal cases concerning Post-traumatic Stress Disorder from the US Board of Veterans' Appeals. We hypothesize that length-constrained extractive summaries benefit from choosing among sentences that are predictive for the case outcome. We develop a novel train-attribute-mask pipeline using a CNN classifier to iteratively select predictive sentences from the case, which measurably improves prediction accuracy on partially masked decisions. We then select a subset for the summary through type classification, maximum marginal relevance, and a summarization template. We use ROUGE metrics and a qualitative survey to evaluate generated summaries along with expert-extracted and expert-drafted summaries. We show that sentence predictiveness does not reliably cover all decision-relevant aspects of a case, illustrate that lexical overlap metrics are not well suited for evaluating legal summaries, and suggest that future work should focus on case-aspect coverage.


### [CLERC: A Dataset for Legal Case Retrieval and Retrieval-Augmented Analysis Generation](https://arxiv.org/pdf/2406.17186)

>Legal professionals need to write analyses that rely on citations to relevant precedents, i.e., previous case decisions. Intelligence systems assisting legal professionals in writing such documents provide great benefits but are challenging to design. Such systems need to help locate, summarize, and reason over salient precedents in order to be useful. To enable systems for such tasks, we work with legal professionals to transform a large open-source legal corpus into a dataset1 supporting two important backbone tasks: information retrieval (IR) and retrieval-augmented generation (RAG). This dataset CLERC (Case Law Evaluation and Retrieval Corpus), is constructed for training and evaluating models on their ability to (1) find corresponding citations for a given piece of legal analysis and to (2) compile the text of these citations (as well as previous context) into a cogent analysis that supports a reasoning goal. We benchmark state-of-the-art models on CLERC, showing that current approaches still struggle: GPT-4o generates analyses with the highest ROUGE F-scores but hallucinates the most, while zero-shot IR models only achieve 48.3% recall@1000.


### [CUAD: An Expert-Annotated NLP Dataset for Legal Contract Review](https://arxiv.org/abs/2103.06268)

>Many specialized domains remain untouched by deep learning, as large labeled datasets require expensive expert annotators. We address this bottleneck within the legal domain by introducing the Contract Understanding Atticus Dataset (CUAD), a new dataset for legal contract review. CUAD was created with dozens of legal experts from The Atticus Project and consists of over 13,000 annotations. The task is to highlight salient portions of a contract that are important for a human to review. We find that Transformer models have nascent performance, but that this performance is strongly influenced by model design and training dataset size. Despite these promising results, there is still substantial room for improvement. As one of the only large, specialized NLP benchmarks annotated by experts, CUAD can serve as a challenging research benchmark for the broader NLP community.


### [Cambridge Law Corpus](https://www.cst.cam.ac.uk/research/srg/projects/law)

>We introduce the Cambridge Law Corpus (CLC), a corpus for legal AI research. It consists of over 250 000 court cases from the UK. Most cases are from the 21st century, but the corpus includes cases as old as the 16th century. This paper presents the first release of the corpus, containing the raw text and meta-data. Together with the corpus, we provide annotations on case outcomes for 638 cases, done by legal experts. Using our annotated data, we have trained and evaluated case outcome extraction with GPT-3, GPT-4 and RoBERTa models to provide benchmarks. We include an extensive legal and ethical discussion to address the potentially sensitive nature of this material. As a consequence, the corpus will only be released for research purposes under certain restrictions.


### [CaseHOLD](https://arxiv.org/abs/2104.08671)

>While self-supervised learning has made rapid advances in natural language processing, it remains unclear when researchers should engage in resource-intensive domain-specific pretraining (domain pretraining). The law, puzzlingly, has yielded few documented instances of substantial gains to domain pretraining in spite of the fact that legal language is widely seen to be unique. We hypothesize that these existing results stem from the fact that existing legal NLP tasks are too easy and fail to meet conditions for when domain pretraining can help. To address this, we first present CaseHOLD (Case Holdings On Legal Decisions), a new dataset comprised of over 53,000+ multiple choice questions to identify the relevant holding of a cited case. This dataset presents a fundamental task to lawyers and is both legally meaningful and difficult from an NLP perspective (F1 of 0.4 with a BiLSTM baseline). Second, we assess performance gains on CaseHOLD and existing legal NLP datasets. While a Transformer architecture (BERT) pretrained on a general corpus (Google Books and Wikipedia) improves performance, domain pretraining (using corpus of approximately 3.5M decisions across all courts in the U.S. that is larger than BERT's) with a custom legal vocabulary exhibits the most substantial performance gains with CaseHOLD (gain of 7.2% on F1, representing a 12% improvement on BERT) and consistent performance gains across two other legal tasks. Third, we show that domain pretraining may be warranted when the task exhibits sufficient similarity to the pretraining corpus: the level of performance increase in three legal tasks was directly tied to the domain specificity of the task. Our findings inform when researchers should engage resource-intensive pretraining and show that Transformer-based architectures, too, learn embeddings suggestive of distinct legal language.


### [Caselaw Access Project](https://case.law/)

>CAP includes all official, book-published state and federal United States case law through 2020 — every volume or case designated as an official report of decisions by a court within the United States.


### [Classifying Semantic Types of Legal Sentences: Portability of Machine Learning Models](https://www.researchgate.net/publication/332171940_Classifying_Semantic_Types_of_Legal_Sentences_Portability_of_Machine_Learning_Models)

>Legal contract analysis is an important research area. The classification of clauses or sentences enables valuable insights such as the extraction of rights and obligations. However, datasets consisting of contracts are quite rare, particularly regarding German language. Therefore this paper experiments the portability of machine learning (ML) models with regard to different document types. We trained different ML classifiers on the tenancy law of the German Civil Code (BGB) to apply the resulting models on a set of rental agreements afterwards. The performance of our models varies on the contract set. Some models perform significantly worse, while certain settings reveal a portability. Additionally, we trained and evaluated the same classifiers on a dataset consisting solely of contracts, to be able to observe a reference performance. We could show that the performance of ML models may depend on the document type used for training, while certain setups result in portable models.


### [ContractNLI: A Dataset for Document-level Natural Language Inference for Contracts](https://arxiv.org/abs/2110.01799)

>Reviewing contracts is a time-consuming procedure that incurs large expenses to companies and social inequality to those who cannot afford it. In this work, we propose "document-level natural language inference (NLI) for contracts", a novel, real-world application of NLI that addresses such problems. In this task, a system is given a set of hypotheses (such as "Some obligations of Agreement may survive termination.") and a contract, and it is asked to classify whether each hypothesis is "entailed by", "contradicting to" or "not mentioned by" (neutral to) the contract as well as identifying "evidence" for the decision as spans in the contract. We annotated and release the largest corpus to date consisting of 607 annotated contracts. We then show that existing models fail badly on our task and introduce a strong baseline, which (1) models evidence identification as multi-label classification over spans instead of trying to predict start and end tokens, and (2) employs more sophisticated context segmentation for dealing with long documents. We also show that linguistic characteristics of contracts, such as negations by exceptions, are contributing to the difficulty of this task and that there is much room for improvement.


### [DOLOMITES: Domain-Specific Long-Form Methodical Tasks](https://arxiv.org/abs/2405.05938)

>Experts in various fields routinely perform methodical writing tasks to plan, organize, and report their work. From a clinician writing a differential diagnosis for a patient, to a teacher writing a lesson plan for students, these tasks are pervasive, requiring to methodically generate structured long-form output for a given input. We develop a typology of methodical tasks structured in the form of a task objective, procedure, input, and output, and introduce DoLoMiTes, a novel benchmark with specifications for 519 such tasks elicited from hundreds of experts from across 25 fields. Our benchmark further contains specific instantiations of methodical tasks with concrete input and output examples (1,857 in total) which we obtain by collecting expert revisions of up to 10 model-generated examples of each task. We use these examples to evaluate contemporary language models highlighting that automating methodical tasks is a challenging long-form generation problem, as it requires performing complex inferences, while drawing upon the given context as well as domain knowledge.


### [Demosthenes](https://github.com/adele-project/demosthenes)

>A novel corpus for argument mining in legal documents composed of 40 decisions of the Court of Justice of the European Union on matters of fiscal state aid. The corpus is annotated at three hierarchical levels: the argumentative elements, their types, and their argument schemes.


### [EUR-Lex-Sum: A Multi- and Cross-lingual Dataset for Long-form Summarization in the Legal Domain](https://github.com/achouhan93/eur-lex-sum)

>The EUR-Lex-Sum dataset is a multilingual resource intended for text summarization in the legal domain. It is based on human-written summaries of legal acts issued by the European Union. It distinguishes itself by introducing a smaller set of high-quality human-written samples, each of which have much longer references (and summaries!) than comparable datasets. Additionally, the underlying legal acts provide a challenging domain-specific application to legal texts, which are so far underrepresented in non-English languages. For each legal act, the sample can be available in up to 24 languages (the officially recognized languages in the European Union); the validation and test samples consist entirely of samples available in all languages, and are aligned across all languages at the paragraph level.


### [EURLex 57K](https://aclanthology.org/P19-1636/)

>We consider Large-Scale Multi-Label Text Classification (LMTC) in the legal domain. We release a new dataset of 57k legislative documents from EUR-LEX, annotated with ∼4.3k EUROVOC labels, which is suitable for LMTC, few- and zero-shot learning. Experimenting with several neural classifiers, we show that BIGRUs with label-wise attention perform better than other current state of the art methods. Domain-specific WORD2VEC and context-sensitive ELMO embeddings further improve performance. We also find that considering only particular zones of the documents is sufficient. This allows us to bypass BERT’s maximum text length limit and fine-tune BERT, obtaining the best results in all but zero-shot learning cases.


### [European Court of Human Rights Dataset](https://arxiv.org/abs/1906.02059)

>Legal judgment prediction is the task of automatically predicting the outcome of a court case, given a text describing the case's facts. Previous work on using neural models for this task has focused on Chinese; only feature-based models (e.g., using bags of words and topics) have been considered in English. We release a new English legal judgment prediction dataset, containing cases from the European Court of Human Rights. We evaluate a broad variety of neural models on the new dataset, establishing strong baselines that surpass previous feature-based models in three tasks: (1) binary violation classification; (2) multi-label classification; (3) case importance prediction. We also explore if models are biased towards demographic information via data anonymization. As a side-product, we propose a hierarchical version of BERT, which bypasses BERT's length limitation.


### [European Parliament Proceedings Parallel Corpus](https://www.statmt.org/europarl/)

>We collected a corpus of parallel text in 11 languages from the proceedings of the European Parliament, which are published on the web. This corpus has found widespread use in the NLP community. Here, we focus on its acquisition and its application as training data for statistical machine translation (SMT). We trained SMT systems for 110 language pairs, which reveal interesting clues into the challenges ahead.


### [ExpertQA: Expert-Curated Questions and Attributed Answers ](https://arxiv.org/abs/2309.07852)

>As language models are adopted by a more sophisticated and diverse set of users, the importance of guaranteeing that they provide factually correct information supported by verifiable sources is critical across fields of study. This is especially the case for high-stakes fields, such as medicine and law, where the risk of propagating false information is high and can lead to undesirable societal consequences. Previous work studying attribution and factuality has not focused on analyzing these characteristics of language model outputs in domain-specific scenarios. In this work, we conduct human evaluation of responses from a few representative systems along various axes of attribution and factuality, by bringing domain experts in the loop. Specifically, we collect expert-curated questions from 484 participants across 32 fields of study, and then ask the same experts to evaluate generated responses to their own questions. In addition, we ask experts to improve upon responses from language models. The output of our analysis is ExpertQA, a high-quality long-form QA dataset with 2177 questions spanning 32 fields, along with verified answers and attributions for claims in the answers.


### [Extracting Contract Elements Dataset](https://pages.aueb.gr/users/ion/docs/icail2017.pdf)

>We study how contract element extraction can be automated. We provide a labeled dataset with gold contract element annotations, along with an unlabeled dataset of contracts that can be used to pretrain word embeddings. Both datasets are provided in an encoded form to bypass privacy issues. We describe and experimentally compare several contract element extraction methods that use manually written rules and linear classifiers (logistic regression, SVMs) with hand-crafted features, word embeddings, and part-of-speech tag embeddings. The best results are obtained by a hybrid method that combines machine learning (with hand-crafted features and embeddings) and manually written post-processing rules.


### [Legal Linking: Citation Resolution and Suggestion in Constitutional Law](https://aclanthology.org/W19-2205.pdf)

>This paper describes a dataset and baseline systems for linking paragraphs from court cases to clauses or amendments in the US Constitution. We implement a rule-based system, a linear model, and a neural architecture for matching pairs of paragraphs, taking training data from online databases in a distantly-supervised fashion. In experiments on a manually-annotated evaluation set, we find that our proposed neural system outperforms a rules-driven baseline. Qualitatively, this performance gap seems largest for abstract or indirect links between documents, which suggests that our system might be useful for answering political science and legal research questions or discovering novel links. We release the dataset along with the manuallyannotated evaluation set to foster future work.


### [Legal-Sentence Classification Datasets](https://github.com/sebischair/Legal-Sentence-Classification-Datasets-and-Models)

>This project is a collection of two different datasets constituting legal sentences from the tenancy law of the German civil law as well as legal word2vec models.


### [LegalBench](https://hazyresearch.stanford.edu/legalbench/)

>The advent of large language models (LLMs) and their adoption by the legal community has given rise to the question: what types of legal reasoning can LLMs perform? To enable greater study of this question, we present LegalBench: a collaboratively constructed legal reasoning benchmark consisting of 162 tasks covering six different types of legal reasoning. LegalBench was built through an interdisciplinary process, in which we collected tasks designed and hand-crafted by legal professionals. Because these subject matter experts took a leading role in construction, tasks either measure legal reasoning capabilities that are practically useful, or measure reasoning skills that lawyers find interesting. To enable cross-disciplinary conversations about LLMs in the law, we additionally show how popular legal frameworks for describing legal reasoning -- which distinguish between its many forms -- correspond to LegalBench tasks, thus giving lawyers and LLM developers a common vocabulary. This paper describes LegalBench, presents an empirical evaluation of 20 open-source and commercial LLMs, and illustrates the types of research explorations LegalBench enables.


### [LegalDiscourse: Interpreting When Laws Apply and Who They Affect](https://aclanthology.org/2024.naacl-long.472.pdf)

>While legal AI has made strides in recent years, it still struggles with basic legal concepts: when does a law apply? Who does it applies to? What does it do? We take a discourse approach to addressing these problems and introduce a novel taxonomy for span-and-relation parsing of legal texts. We create a dataset, LegalDiscourse of 602 state-level law paragraphs consisting of 3, 715 discourse spans and 1, 671 relations. Our trained annotators have an agreement-rate κ > .8, yet few-shot GPT3.5 performs poorly at span identification and relation classification. Although fine-tuning improves performance, GPT3.5 still lags far below human level. We demonstrate the usefulness of our schema by creating a web application with journalists. We collect over 100, 000 laws for 52 U.S. states and territories using 20 scrapers we built, and apply our trained models to 6, 000 laws using U.S. Census population numbers. We describe two journalistic outputs stemming from this application: (1) an investigation into the increase in liquor licenses following population growth and (2) a decrease in applicable laws under different under-count projections.


### [LexGLUE](https://huggingface.co/datasets/coastalcph/lex_glue)

>Laws and their interpretations, legal arguments and agreements\ are typically expressed in writing, leading to the production of vast corpora of legal text. Their analysis, which is at the center of legal practice, becomes increasingly elaborate as these collections grow in size. Natural language understanding (NLU) technologies can be a valuable tool to support legal practitioners in these endeavors. Their usefulness, however, largely depends on whether current state-of-the-art models can generalize across various tasks in the legal domain. To answer this currently open question, we introduce the Legal General Language Understanding Evaluation (LexGLUE) benchmark, a collection of datasets for evaluating model performance across a diverse set of legal NLU tasks in a standardized way. We also provide an evaluation and analysis of several generic and legal-oriented models demonstrating that the latter consistently offer performance improvements across multiple tasks.


### [Long Context Retrieval (LoCo)](https://hazyresearch.stanford.edu/blog/2024-05-20-m2-bert-retrieval)

>A long-context benchmark consisting of 12 tasks drawn from law, medicine, science, finance, corporate governance, government reports, and more. LoCoV1 tasks use real-world datasets spanning diverse domains, including Tau Scrolls, QASPER, LongBench, the Legal Case Reports corpus, and more.


### [MAPP Corpus](https://usableprivacy.org/data)

>The MAPP Corpus (Mobile App Privacy Policies, set of 155) is the first bilingual corpus of mobile app privacy policies consisting of 64 privacy policies in English and 91 privacy policies in German with manual annotations that specify data practices in the text. Each privacy policy was read and annotated by three graduate students in law - native German speakers for the German version of the policy and native English speakers for the English version of the policies.


### [MAPS Policies Dataset](https://usableprivacy.org/data)

>The MAPS Policies Dataset consists of the URLs of 441,626 privacy policies. These privacy policies were discovered as part of the Google Play Store app analysis conducted by the Mobile App Privacy System (MAPS) from April to May, 2018.


### [MAUD: An Expert-Annotated Legal NLP Dataset for Merger Agreement Understanding](https://arxiv.org/abs/2301.00876)

>Reading comprehension of legal text can be a particularly challenging task due to the length and complexity of legal clauses and a shortage of expert-annotated datasets. To address this challenge, we introduce the Merger Agreement Understanding Dataset (MAUD), an expert-annotated reading comprehension dataset based on the American Bar Association's 2021 Public Target Deal Points Study, with over 39,000 examples and over 47,000 total annotations. Our fine-tuned Transformer baselines show promising results, with models performing well above random on most questions. However, on a large subset of questions, there is still room for significant improvement. As the only expert-annotated merger agreement dataset, MAUD is valuable as a benchmark for both the legal profession and the NLP community.


### [Multi-LexSum: Real-world Summaries of Civil Rights Lawsuits at Multiple Granularities](https://multilexsum.github.io/)

>The Multi-LexSum dataset is a collection of 9,280 such legal case summaries. Multi-LexSum is distinct from other datasets in its multiple target summaries, each at a different granularity (ranging from one-sentence “extreme” summaries to multi-paragraph narrations of over five hundred words). It presents a challenging multi-document summarization task given the long length of the source documents, often exceeding two hundred pages per case. Unlike other summarization datasets that are (semi-)automatically curated, Multi-LexSum consists of expert-authored summaries: the experts—lawyers and law students—are trained to follow carefully created guidelines, and their work is reviewed by an additional expert to ensure quality.


### [OPP-115 Corpus](https://usableprivacy.org/data)

>The OPP-115 Corpus (Online Privacy Policies, set of 115) is a collection of website privacy policies (i.e., in natural language) with annotations that specify data practices in the text. Each privacy policy was read and annotated by three graduate students in law.


### [Ontario Laws and Regs](https://huggingface.co/datasets/hordruma/ontario_laws_and_regs)

>The Ontario Laws & Regs dataset contains 5,096 Ontario laws and regulations.


### [Open Australian Legal Corpus](https://huggingface.co/datasets/umarbutler/open-australian-legal-corpus)

>The Open Australian Legal Corpus is the first and only multijurisdictional open corpus of Australian legislative and judicial documents. Comprised of 227,488 texts totalling over 70 million lines and 1.4 billion tokens, the Corpus includes every in force statute and regulation in the Commonwealth, New South Wales, Queensland, Western Australia, South Australia, Tasmania and Norfolk Island, in addition to thousands of bills and hundreds of thousands of court and tribunal decisions.


### [Opt-Out Choice Dataset](https://usableprivacy.org/data)

>We assembled a corpus of website privacy policies (i.e., in natural language) to train machine learning and natural language processing models to detect hyperlinks that offer opt-out choices, and determine the categories of data involved (e.g., behavioral advertising). This corpus is significantly larger than the corpus we describe in our EMNLP 2017 paper.


### [Patent Litigation Docket Reports Data](https://www.uspto.gov/ip-policy/economic-research/research-datasets/patent-litigation-docket-reports-data)

>The Patent Litigation Dataset has been updated as of March 2024 and now contains detailed patent litigation data on 96,966 unique district court cases filed during the period 1963-2020. OCE and partners at the University of San Diego Law School collected all of the data from the Public Access to Court Electronic Records (PACER) and RECAP, an independent project designed to serve as a repository for litigation data sourced from PACER. The final output datasets, provided in six different files, include information on the litigating parties involved and their attorneys; the cause of action; the court location; important dates in the litigation history; and descriptions of all documents submitted in a given case, which cover more than 5 million separate documents contained in the case docket reports. There is also a sixth file with hand-coded information on patent-in-suit and case type for most cases filed between 2003 and 2020. 


### [Pile of Law](https://huggingface.co/datasets/pile-of-law/pile-of-law)

>One concern with the rise of large language models lies with their potential for significant harm, particularly from pretraining on biased, obscene, copyrighted, and private information. Emerging ethical approaches have attempted to filter pretraining material, but such approaches have been ad hoc and failed to take context into account. We offer an approach to filtering grounded in law, which has directly addressed the tradeoffs in filtering material. First, we gather and make available the Pile of Law, a 256GB (and growing) dataset of open-source English-language legal and administrative data, covering court opinions, contracts, administrative rules, and legislative records. Pretraining on the Pile of Law may help with legal tasks that have the promise to improve access to justice. Second, we distill the legal norms that governments have developed to constrain the inclusion of toxic or private content into actionable lessons for researchers and discuss how our dataset reflects these norms. Third, we show how the Pile of Law offers researchers the opportunity to learn such filtering rules directly from the data, providing an exciting new research direction in model-based processing.


### [Plain English Summarization of Contracts](https://aclanthology.org/W19-2201/)

>Unilateral legal contracts, such as terms of service, play a substantial role in modern digital life. However, few read these documents before accepting the terms within, as they are too long and the language too complicated. We propose the task of summarizing such legal documents in plain English, which would enable users to have a better understanding of the terms they are accepting. We propose an initial dataset of legal text snippets paired with summaries written in plain English. We verify the quality of these summaries manually, and show that they involve heavy abstraction, compression, and simplification. Initial experiments show that unsupervised extractive summarization methods do not perform well on this task due to the level of abstraction and style differences. We conclude with a call for resource and technique development for simplification and style transfer for legal language.


### [Privacy Law Corpus](https://usableprivacy.org/data)

>The Privacy Law Corpus is a collection of 1,043 privacy laws, regulations, and guidelines covering 183 jurisdictions around the world. These documents are provided in two file formats (i.e., PDF showing the original formatting on the source website and TXT containing just the text of the privacy law) and, in some cases, in multiple languages (i.e., the original language(s) and an English translation).


### [PrivacyQA Dataset](https://usableprivacy.org/data)

>PrivacyQA is a corpus consisting of 1750 questions about the contents of privacy policies, paired with expert annotations. The goal of this effort is to kickstart the development of question-answering methods for this domain, to address the (unrealistic) expectation that a large population should be reading many policies per day.


### [SemEval-2024 Task 5: Argument Reasoning in Civil Procedure](https://aclanthology.org/2024.semeval-1.276/)

>This paper describes the results of SemEval-2024 Task 5: Argument Reasoning in Civil Procedure, consisting of a single task on judging and reasoning about the answers to questions in U.S. civil procedure. The dataset for this task contains question, answer and explanation pairs taken from The Glannon Guide To Civil Procedure (Glannon, 2018). The task was to classify in a binary manner if the answer is a correct choice for the question or not. Twenty participants submitted their solutions, with the best results achieving a remarkable 82.31% F1-score. We summarize and analyze the results from all participating systems and provide an overview over the systems of 14 participants.


### [Sentence Boundary Detection in Adjudicatory Decisions in the United States](https://www.atala.org/sites/default/files/2-%20TAL-58-2-sbd-adjudicatory-decisions.pdf)

>We report results of an effort to enable computers to segment US adjudicatory decisions into sentences. We created a data set of 80 court decisions from four different domains. We show that legal decisions are more challenging for existing sentence boundary detection systems than for non-legal texts. Existing sentence boundary detection systems are based on a number of assumptions that do not hold for legal texts, hence their performance is impaired. We show that a general statistical sequence labeling model is capable of learning the definition more efficiently. We have trained a number of conditional random fields models that outperform the traditional sentence boundary detection systems when applied to adjudicatory decisions.


### [The United States Code](https://uscode.house.gov/download/download.shtml)

>Each update of the United States Code is a release point. This page provides downloadable files for the current release point. All files are current through Public Law 118-65 (06/17/2024). Titles in bold have been changed since the last release point.


### [Toward Domain-Guided Controllable Summarization of Privacy Policies](https://ceur-ws.org/Vol-2645/paper3.pdf)

>Companies’ privacy policies are often skipped by the users as they are too long, verbose, and difficult to comprehend. Identifying the key privacy and security risk factors mentioned in these unilateral contracts and effectively incorporating them in a summary can assist users in making a more informed decision when asked to agree to the terms and conditions. However, existing summarization methods fail to integrate domain knowledge into their framework or rely on a large corpus of annotated training data. We propose a hybrid approach to identify sections of privacy policies with a high privacy risk factor. We incorporate these sections into summaries by selecting the riskiest content from different privacy topics. Our approach enables users to select the content to be summarized within a controllable length. Users can view a summary that captures different privacy factors or a summary that covers the riskiest content. Our approach outperforms the domain-agnostic baselines by up to 27% in ROUGE-1 score and 50% in METEOR score using plain English reference summaries while relying on significantly less training data in comparison to abstractive approaches.


### [US Supreme Court Segmentation Dataset](https://ebooks.iospress.nl/volumearticle/50840)

>In common law jurisdictions, legal research often involves an analysis of relevant case law. Court opinions comprise several high-level parts with different functions. A statement's membership in one of the parts is a key factor influencing how the statement should be understood. In this paper we present a number of experiments in automatically segmenting court opinions into the functional and the issue specific parts. We defined a set of seven types including Background, Analysis, and Conclusions. We used the types to annotate a sizable corpus of US trade secret and cyber crime decisions. We used the data set to investigate the feasibility of recognizing the parts automatically. The proposed framework based on conditional random fields proved to be very promising in this respect. To support research in automatic case law analysis we plan to release the data set to the public.


### [Unfair clause detection in terms of service across multiple languages](https://link.springer.com/article/10.1007/s10506-024-09398-7)

>Most of the existing natural language processing systems for legal texts are developed for the English language. Nevertheless, there are several application domains where multiple versions of the same documents are provided in different languages, especially inside the European Union. One notable example is given by Terms of Service (ToS). In this paper, we compare different approaches to the task of detecting potential unfair clauses in ToS across multiple languages. In particular, after developing an annotated corpus and a machine learning classifier for English, we consider and compare several strategies to extend the system to other languages: building a novel corpus and training a novel machine learning system for each language, from scratch; projecting annotations across documents in different languages, to avoid the creation of novel corpora; translating training documents while keeping the original annotations; translating queries at prediction time and relying on the English system only. An extended experimental evaluation conducted on a large, original dataset indicates that the time-consuming task of re-building a novel annotated corpus for each language can often be avoided with no significant degradation in terms of performance. Dataset is available at [https://github.com/nlp-unibo/Multilingual-Unfair-Clause-Detection]


### [Washington University Law Supreme Court Database](http://scdb.wustl.edu/)

>The Supreme Court Database is the definitive source for researchers, students, journalists, and citizens interested in the U.S. Supreme Court. The Database contains over two hundred pieces of information about each case decided by the Court between the 1791 and 2022 terms. Examples include the identity of the court whose decision the Supreme Court reviewed, the parties to the suit, the legal provisions considered in the case, and the votes of the Justices.


### [Competition on Legal Information Extraction and Entailment (COLIEE)](https://coliee.org/overview)

>The Competition on Legal Information Extraction and Entailment (COLIEE) is an annual event that promotes research in legal information processing. It features four main tasks: Legal Case Retrieval, Legal Case Entailment, Statute Law Retrieval, and Legal Textual Entailment. COLIEE provides datasets in multiple languages, including low-resource ones, to encourage the development of AI solutions across diverse legal systems.


### [Automated Legal Question Answering Competition (ALQAC)](https://alqac.github.io/)

>The Automated Legal Question Answering Competition (ALQAC) is an annual event designed to foster research on legal assistance systems, particularly in low-resource languages. The competition focuses on challenging tasks such as Legal Document Retrieval and Legal Question Answering, providing manually annotated datasets derived from well-known legal statutes. By addressing the limitations of low-resource languages in the legal domain, ALQAC aims to advance AI-driven solutions and build a strong research community for legal technology development.


### [LEXam: Benchmarking Legal Reasoning on 340 Law Exams](https://lexam-benchmark.github.io/)
> Long-form legal reasoning remains a key challenge for large language models (LLMs) in spite of recent advances in test-time scaling. To address this, we introduce \textsc{LEXam}, a novel benchmark derived from 340 law exams spanning 116 law school courses across a range of subjects and degree levels. The dataset comprises 4,886 law exam questions in English and German, including 2,841 long-form, open-ended questions and 2,045 multiple-choice questions. Besides reference answers, the open questions are also accompanied by explicit guidance outlining the expected legal reasoning approach such as issue spotting, rule recall, or rule application. Our evaluation on both open-ended and multiple-choice questions present significant challenges for current LLMs; in particular, they notably struggle with open questions that require structured, multi-step legal reasoning. Moreover, our results underscore the effectiveness of the dataset in differentiating between models with varying capabilities. Deploying an ensemble LLM-as-a-Judge paradigm with rigorous human expert validation, we demonstrate how model-generated reasoning steps can be evaluated consistently and accurately, closely aligning with human expert assessments. Our evaluation setup provides a scalable method to assess legal reasoning quality beyond simple accuracy metrics. We have open-sourced our code on this https URL and released our data on this https URL. Project page: this https URL.