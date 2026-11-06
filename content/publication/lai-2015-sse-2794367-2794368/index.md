---
title: "Scalable Subgraph Enumeration in MapReduce"
date: 2015-06-01
publishDate: 2015-06-01T01:41:34.981585Z
authors: ["Longbin Lai", "Lu Qin", "Xuemin Lin", "Lijun Chang"]
publication_types: ["2"]
abstract: Subgraph enumeration, which aims to find all the subgraphs of a large data graph that are isomorphic to a given pattern graph, is a fundamental graph problem with a wide range of applications. However, existing sequential algorithms for subgraph enumeration fall short in handling large graphs due to the involvement of computationally intensive subgraph isomorphism operations. Thus, some recent researches focus on solving the problem using MapReduce. Nevertheless, exiting MapReduce approaches are not scalable to handle very large graphs since they either produce a huge number of partial results or consume a large amount of memory. Motivated by this, in this paper, we propose a new algorithm $$\mathsf {Twin}$$Twin$$\mathsf {Twig}$$Twig$$\mathsf {Join}$$Join based on a left-deep-join framework in MapReduce, in which the basic join unit is a $$\mathsf {Twin}$$Twin$$\mathsf {Twig}$$Twig (an edge or two incident edges of a node). We show that in the Erdös---Rényi random graph model, $$\mathsf {Twin}$$Twin$$\mathsf {Twig}$$Twig$$\mathsf {Join}$$Join is instance optimal in the left-deep-join framework under reasonable assumptions, and we devise an algorithm to compute the optimal join plan. We further discuss how our approach can be adapted to handle the power-law random graph model. Three optimization strategies are explored to improve our algorithm. Ultimately, by aggregating equivalent nodes into a compressed node, we construct the compressed graph, upon which the subgraph enumeration is further improved. We conduct extensive performance studies in several real graphs, one of which contains billions of edges. Our approach significantly outperforms existing solutions in all tests.
featured: false
url_pdf: files/p974-lai.pdf
url_slides: files/vldb2015-slides.pdf
url_code: https://github.com/longbinlai/SubgEnumFramework
publication: "*Proc. VLDB Endow.*"
doi: "10.14778/2794367.2794368"
---

