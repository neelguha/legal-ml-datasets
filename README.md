# Datasets for Machine Learning in Law
This page contains my efforts to aggregate datasets/tasks/benchmarks pertaining to the intersection of machine learning and law. 

This page is continually being updated. If I missed something, please contact me at nguha@cs.stanford.edu and I'll add it! 

Neel Guha


## Task agnostic datasets 
These datasets can be used for pretraining larger models. Alternatively, you cause them to construct artificial tasks. 

- [Caselaw Access Project](https://case.law/): all official, book-published United States case law.
- [Legifrance](https://www.legifrance.gouv.fr/): a French legal publisher providing access to law codes and legal decisions. Requires scraping ([Paper](http://ceur-ws.org/Vol-2645/paper2.pdf)). 
- [US Supreme Court Database](http://scdb.wustl.edu/): information about every case decided by the US Supreme Court between 1791 and today.
- [European Parliment Proceedings](https://www.statmt.org/europarl/): Parallel text of the proceedings of the European Parliment, collected in 11 languages. 
- [US Code](https://uscode.house.gov/download/download.shtml): downloadable version of the US code in XML format
- [Patent Litigation Docket Reports](https://www.uspto.gov/learning-and-resources/electronic-data-products/patent-litigation-docket-reports-data): detailed patent litigation data on over 80k unique district court cases



## Judgement prediction
Training a model to predicti the outcome of a case from various case specific features. 
- [European Court of Human Rights](https://archive.org/details/ECHR-ACL2019): 11.5k cases from ECHR's public database. [Paper](https://www.aclweb.org/anthology/P19-1424/).

## Annotation
Training a model to annotate clauses in a contract (or other document) according to various criteria (e.g. unfairness)

- [Detecting unfair clauses from online terms-of-service](http://155.185.228.137/claudette/ToS.zip): ~12k sentences from 50 terms-of-service agreements. [Paper](https://arxiv.org/pdf/1805.01217.pdf).
- [Usable Privacy Project Data](https://usableprivacy.org/data): a collection of datasets for privacy policies, including OPP-115, APP-350, MAPS, and the ACL/COLING 2014 Dataset.
- [Contract extraction dataset](http://nlp.cs.aueb.gr/software_and_datasets/CONTRACTS_ICAIL2017/index.html): 3,500 English contracts manually annotated with 11 different contract elements. [Paper](http://nlp.cs.aueb.gr/pubs/icail2017.pdf).
- [EURLEX with EUROVOC annotations](http://nlp.cs.aueb.gr/software_and_datasets/EURLEX57K/index.html): 57k legilsative documents from the EU's public document database, annotated with concepts from EUROVOC. [Paper](https://www.aclweb.org/anthology/W19-2209/).



## Summarization 
Training a model to summarize complex contractual jargon or legal analysis 
- [Summarizing contracts into plain english](https://github.com/lauramanor/legal_summarization): 446 contracts with parallel plain-text section-level English summaries. [Paper](https://www.aclweb.org/anthology/W19-2201/).
- [Cookie policies from 151 companies](https://github.com/senjed/Summarization-of-Privacy-Policies): User agreements for 151 services with sections annotated by TOS;DR. [Paper](http://ceur-ws.org/Vol-2645/paper3.pdf).
- [Australian case citation summarization](https://archive.ics.uci.edu/ml/datasets/Legal+Case+Reports): 4000 cases from the Federal Court of Australia with citation-based summaries. 

##







## References





 
