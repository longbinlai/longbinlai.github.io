---
title: "HUGE: An Efficient and Scalable Subgraph Enumeration System"
date: 2021-03-11
publishDate: 2021-06-09T00:43:27.786038Z
authors: ["Zhengyi Yang", "Longbin Lai", "Xuemin Lin", "Kongzhang Hao", "Wenjie Zhang"]
publication_types: ["1"]
abstract: Subgraph enumeration is a fundamental problem in graph analytics, which aims to find all instances of a given query graph on a large data graph. In this paper, we propose a system called HUGE to efficiently process subgraph enumeration at scale in the distributed context. HUGE features 1) an optimiser to compute the generic optimal execution plan without the constraints of existing works; 2) a hybrid communication layer that supports both pushing and pulling communication; 3) a novel two-stage execution mode with a lock-free and zero-copy cache design, 4) a BFS/DFS-adaptive scheduler to bound memory consumption, and 5) two-layer intra- and inter-machine load balancing. HUGE is generic such that all existing distributed subgraph enumeration algorithms can be plugged into the system to enjoy automatic speed up and bounded-memory execution.
featured: true
url_pdf: files/huge-sigmod21.pdf
publication: "ACM SIGMOD/PODS International Conference on Management of Data 2021"
doi: "10.1145/3448016.3457237"
tags: ["subgraph enumeration", "distributed graph processing", "join processing", "dynamic scheduling", "load balancing"]
---

