---
title: "GAIA: A System for Interactive Analysis on Distributed Graphs Using a High-Level Language"
date: 2021-03-04
publishDate: 2021-03-04T00:43:27.786038Z
authors: ["Zhengping Qian", "Chenqiang Min", "Longbin Lai", "Yong Fang", "Gaofeng Li", "Youyang Yao", "Bingqing Lyu", "Zhimin Chen", "Jingren Zhou" ]
publication_types: ["1"]
abstract: GAIA is a distributed system designed specifically to make it easy for a variety of users to interactively analyze big graph data on large clusters at low latency. It adopts a high-level language called Gremlin for graph traversal, and provides automatic parallel execution. In particular, we advocate a powerful new abstraction called Scope that caters to the specific needs in this new computation model to scale graph queries with complex dependencies and runtime dynamics, while at the same time maintaining the simple and concise programming model. GAIA has been deployed in production clusters at Alibaba to support a variety of business-critical scenarios. Extensive evaluations using both benchmarks and real-world applications have validated the effectiveness of the proposed techniques, which enables GAIA to execute complex Gremlin traversal with orders-of-magnitude better performance than existing high-performance engines, and at much larger scales than recent state-of-the-art Gremlin-enabled systems such as JanusGraph.
featured: true
url_pdf: files/NSDI21_GAIA_final.pdf
url_code: https://github.com/alibaba/GraphScope/tree/main/interactive_engine/executor/engine/pegasus
publication: "*18th USENIX Symposium on Networked Systems Design and Implementation*"
tags: ["Gremlin", "Distributed Graph Processing", "Interactive Graph Query", "Dynamic Scheduling"]
---

