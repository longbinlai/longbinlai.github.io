---
title: "Improving Distribued Subgraph Matching Algorithm on Timely Dataflow"
date: 2019-04-01
publishDate: 2019-04-01T03:38:56.548246Z
authors: ["Zhengmin Lai", "Zhengyi Yang", "Longbin Lai"]
publication_types: ["1"]
abstract: The subgraph matching problem is defined to find all subgraphs of a data graph that are isomorphic to a given query graph. Subgraph matching plays a vital role in the fields of e-commerce, social media and biological science. CliqueJoin is a distributed subgraph matching algorithm that is designed to be efficient and scalable. However, CliqueJoin is originally developed on MapReduce, thus the performance of the algorithm can be affected by the notorious I/O issue of MapReduce while processing multi-round join tasks. Meanwhile, CliqueJoin does not propose a cost evaluation strategy for labelled graphs, which limits its application in practice where most real-world graphs are labelled. Targeting the limitations of CliqueJoin, we propose CliqueJoin++ to improve CliqueJoin in two aspects. Firstly, we implement CliqueJoin++ on the Timely dataflow system instead of MapReduce to avoid considerable I/O cost. Secondly, we extend the cost evaluation function in CliqueJoin to compute optimal join plans for labelled graphs in the distributed context. Extensive experiments have been conducted to show that the proposed method is up to 10 times faster than the MapReduce version for unlabelled matching, and it achieves good performance and scalability for labelled matching.
featured: false
publication: "*2019 IEEE 35th International Conference on Data Engineering Workshops (ICDEW)*"
tags: ["distribued subgraph matching", "dataflow system", "cost evaluation", "distributed algorithm"]
url_pdf: files/08750928.pdf
doi: "10.1109/ICDEW.2019.000-2"
---

