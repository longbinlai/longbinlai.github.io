---
title: "MPMatch: A Multi-core Parallel Subgraph Matching Algorithm"
date: 2019-04-01
publishDate: 2019-04-01T03:35:52.300283Z
authors: ["Xin Jin", "Longbin Lai"]
publication_types: ["1"]
abstract: Subgraph Matching is a fundamental problem in graph analysis, and is widely used in many application scenarios in biology, chemistry and social network. Given a data graph and a query graph, subgraph matching aims to compute all subgraphs of the data graph that are isomorphic to the query graph. The problem is computationally expensive as the core operation it depends on, known as subgraph isomorphism, is NP-complete. In recent years, graph is increasing extensively and it is hard to compute subgraph matching on massive graph data using existing serial algorithm. Meanwhile, there exist distributed solutions, but they are mostly limited to the case where the graphs are unlabelled. In response to this gap, we study the subgraph matching problem in the multi-core environment. From the algorithm level, we propose a multi-core parallel subgraph matching algorithm called MPMatch. From the research level, we explore the concurrent allocation of subgraph matching search space to approach load balancing. We conduct extensive empirical studies on real and synthetic graphs to demonstrate that our techniques improve the performance of serial subgraph matching algorithm via parallelization and well-developed load balancing schema.
featured: false
url_pdf: files/08750958.pdf
publication: "*2019 IEEE 35th International Conference on Data Engineering Workshops (ICDEW)*"
tags: ["subgraph matching", "subgraph isomorphism", "parallelism of multicore", "load balance"]
doi: "10.1109/ICDEW.2019.000-6"
---

