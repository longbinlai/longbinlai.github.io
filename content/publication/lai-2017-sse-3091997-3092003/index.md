---
title: "Scalable Subgraph Enumeration in MapReduce: A Cost-oriented Approach"
date: 2017-06-01
publishDate: 2017-06-01T01:46:20.547551Z
authors: ["Longbin Lai", "Lu Qin", "Xuemin Lin", "Lijun Chang"]
publication_types: ["2"]
abstract: Subgraph enumeration, which aims to find all the subgraphs of a large data graph that are isomorphic to a given pattern graph, is a fundamental graph problem with a wide range of applications. However, existing sequential algorithms for subgraph enumeration fall short in handling large graphs due to the involvement of computationally intensive subgraph isomorphism operations. Thus, some recent researches focus on solving the problem using MapReduce. Nevertheless, exiting MapReduce approaches are not scalable to handle very large graphs since they either produce a huge number of partial results or consume a large amount of memory. Motivated by this, in this paper, we propose a new algorithm TwinTwigJoin based on a left-deep-join framework in MapReduce, in which the basic join unit is a TwinTwig (an edge or two incident edges of a node). We show that in the Erdös-Rényi random-graph model, TwinTwigJoin is instance optimal in the left-deep-join framework under reasonable assumptions, and we devise an algorithm to compute the optimal join plan. Three optimization strategies are explored to improve our algorithm. Furthermore, we discuss how our approach can be adapted in the power-law random-graph model. We conduct extensive performance studies in several real graphs, one of which contains billions of edges. Our approach significantly outperforms existing solutions in all tests.
featured: false
url_pdf: files/subgraphj.pdf
publication: "*The VLDB Journal*"
tags: ["MapReduce", "Power-law graph", "Random graph", "Subgraph enumeration"]
doi: "10.1007/s00778-017-0459-4"
---

