# Datasets for Machine Learning in Law
This is a collection of pointers to datasets/tasks/benchmarks pertaining to the intersection of machine learning and law. 

This page is continually being updated. If I missed something, please contact me at nguha@stanford.edu and I'll add it! 

Neel Guha


## Task agnostic datasets 
These datasets can be used for pretraining larger models. Alternatively, you cause them to construct artificial tasks. 

- [Caselaw Access Project](https://case.law/): all official, book-published United States case law.
- [Legifrance](https://www.legifrance.gouv.fr/): a French legal publisher providing access to law codes and legal decisions. Requires scraping ([Paper](http://ceur-ws.org/Vol-2645/paper2.pdf)). 
- [US Supreme Court Database](http://scdb.wustl.edu/): information about every case decided by the US Supreme Court between 1791 and today.
- [European Parliment Proceedings](https://www.statmt.org/europarl/): Parallel text of the proceedings of the European Parliment, collected in 11 languages. 
- [US Code](https://uscode.house.gov/download/download.shtml): downloadable version of the US Code in XML format
- [Patent Litigation Docket Reports](https://www.uspto.gov/learning-and-resources/electronic-data-products/patent-litigation-docket-reports-data): detailed patent litigation data on over 80k unique district court cases
- [Pile of Law](https://huggingface.co/datasets/pile-of-law/pile-of-law): a 256GB dataset of legal, administrative, and contractual texts.
- [Open Australian Legal Corpus](https://huggingface.co/datasets/umarbutler/open-australian-legal-corpus): The first and only multijurisdictional open corpus of Australian legislative and judicial documents.

## Benchmarks which combine multiple types of tasks
- [LexGlue](https://huggingface.co/datasets/lex_glue): a GLUE inspired set of legal tasks 
- [LegalBench](https://github.com/HazyResearch/legalbench): a large language model benchmark for legal reasoning


## Judgement prediction
Training a model to predict the outcome of a case from various case specific features. 
- [European Court of Human Rights](https://archive.org/details/ECHR-ACL2019): 11.5k cases from ECHR's public database. [Paper](https://www.aclweb.org/anthology/P19-1424/).


## Document/contract annotation
Training a model to annotate sentences/clauses/sections in a contract (or other document) according to various criteria (e.g. unfairness, argument structure, etc).

- [Detecting unfair clauses from online terms-of-service](http://155.185.228.137/claudette/ToS.zip): ~12k sentences from 50 terms-of-service agreements. [Paper](https://arxiv.org/pdf/1805.01217.pdf).
- [Usable Privacy Project Data](https://usableprivacy.org/data): a collection of datasets for privacy policies, including OPP-115, APP-350, MAPS, and the ACL/COLING 2014 Dataset.
- [Contract extraction dataset](http://nlp.cs.aueb.gr/software_and_datasets/CONTRACTS_ICAIL2017/index.html): 3,500 English contracts manually annotated with 11 different contract elements. [Paper](http://nlp.cs.aueb.gr/pubs/icail2017.pdf).
- [EURLEX with EUROVOC annotations](http://nlp.cs.aueb.gr/software_and_datasets/EURLEX57K/index.html): 57k legilsative documents from the EU's public document database, annotated with concepts from EUROVOC. [Paper](https://www.aclweb.org/anthology/W19-2209/).
- [Cornell eRulemaking Corpus](https://facultystaff.richmond.edu/~jpark/data/jpark_lrec18.zip): Collection of 731 user comments on the the Consumer Debt Collection Practices rule by the CFPB, with annotations containing information about argument structure. [Paper](https://facultystaff.richmond.edu/~jpark/papers/jpark_lrec18.pdf).
- [German rental agreements (in English)](https://github.com/sebischair/Legal-Sentence-Classification-Datasets-and-Models): ~913 sentences from German rental agreements annotated by semantic type. [Paper](https://www.researchgate.net/publication/332171940_Classifying_Semantic_Types_of_Legal_Sentences_Portability_of_Machine_Learning_Models).
- [Segmenting US court decision opinions into issue parts](https://github.com/jsavelka/us-dec-func-iss-sgm/blob/master/trade_secret_cases.json): 316 court decisions on cyber crime and trade secrets, manually segmented into 6 content based "types" (encompassing categories like "Introduction", "Dissent", or "Background"). [Paper](http://ebooks.iospress.nl/volumearticle/50840)
- [ContractNLI: A Dataset for Document-level Natural Language Inference for Contracts](https://arxiv.org/abs/2110.01799)
- 


## Summarization 
Training a model to summarize complex contractual jargon or legal analysis.
- [Summarizing contracts into plain english](https://github.com/lauramanor/legal_summarization): 446 contracts with parallel plain-text section-level English summaries. [Paper](https://www.aclweb.org/anthology/W19-2201/).
- [Cookie policies from 151 companies](https://github.com/senjed/Summarization-of-Privacy-Policies): User agreements for 151 services with sections annotated by TOS;DR. [Paper](http://ceur-ws.org/Vol-2645/paper3.pdf).
- [Australian case citation summarization](https://archive.ics.uci.edu/ml/datasets/Legal+Case+Reports): 4000 cases from the Federal Court of Australia with citation-based summaries. 
- [Board of Veterans' Appeals Case Summarization](https://github.com/luimagroup/bva-summarization): Summarizing BVA cases concerning PTSD. [Paper](https://dl.acm.org/doi/10.1145/3322640.3326728).
- [Multi-LexSum](https://openreview.net/forum?id=z1d8fUiS8Cr): Summarizing civil rights opinions at different granularities!
- [EUR-Lex-Sum](https://github.com/achouhan93/eur-lex-sum): Dataset for cross-lingual summarization based on manually curated document summaries of legal acts from the European Union law platform.

## Linking / question answering
Training a model to answer questions or to identify passages from a target document that are relevant to a specified query. 
- [Linking Supreme Court Opinions to the US Constitution](https://github.com/mayhewsw/legal-linking): 36k paragraphs from USC opinions with 41k links to the US Constitution. [Paper](https://www.aclweb.org/anthology/W19-2205.pdf).
- [StAtutory Reasoning Assessment (SARA)](https://nlp.jhu.edu/law/): Collection of rules extracted from US Internal Revenue Code and natural language questions requiring application of those rules. [Paper](http://ceur-ws.org/Vol-2645/paper5.pdf).
- [PrivacyQA](https://github.com/AbhilashaRavichander/PrivacyQA_EMNLP): 1750 questions on mobile application privacy policies and 3500 relevant expert annotations. [Paper](https://arxiv.org/abs/1911.00841)
- [CaseHOLD](https://github.com/reglab/casehold): 53,000+ MC questions that require identifying the correct holding for a case citation from the preceeding context. [Paper](https://arxiv.org/abs/2104.08671)
- [LegalSupport](https://crfm.stanford.edu/helm/v1.0/?group=legal_support): inferring BlueBook support signals from legal texts

## Document classification 
Training a model to classify a (typically lengthy) legal filing or document. 
- [EDGAR](https://www.sec.gov/edgar/searchedgar/accessing-edgar-data.htm): Online public database for US Securities and Exchange Commission. Filings can be classified by filing type. [Paper](https://arxiv.org/abs/1912.06905).


## Misc
Datasets which don't fit into the above categories:
- [Segmenting sentences in US cases](https://github.com/jsavelka/sbd_adjudicatory_dec): ~26k sentences from 80 cases. [Paper](https://www.atala.org/sites/default/files/2-%20TAL-58-2-sbd-adjudicatory-decisions.pdf).
- [Demosthenes](https://github.com/adele-project/demosthenes) Corpus for argument mining in legal documents.




 
