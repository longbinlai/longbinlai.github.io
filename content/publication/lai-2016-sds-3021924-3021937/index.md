---
title: "Scalable Distributed Subgraph Enumeration"
date: 2016-11-01
publishDate: 2016-11-01T01:43:10.687184Z
authors: ["Longbin Lai", "Lu Qin", "Xuemin Lin", "Ying Zhang", "Lijun Chang", "Shiyu Yang"]
publication_types: ["2"]
abstract: Subgraph enumeration aims to find all the subgraphs of a large data graph that are isomorphic to a given pattern graph. As the subgraph isomorphism operation is computationally intensive, researchers have recently focused on solving this problem in distributed environments, such as MapReduce and Pregel. Among them, the state-of-the-art algorithm, Twin TwigJoin, is proven to be instance optimal based on a left-deep join framework. However, it is still not scalable to large graphs because of the constraints in the left-deep join framework and that each decomposed component (join unit) must be a star. In this paper, we propose SEED - a scalable sub-graph enumeration approach in the distributed environment. Compared to Twin TwigJoin, SEED returns optimal solution in a generalized join framework without the constraints in Twin TwigJoin. We use both star and clique as the join units, and design an effective distributed graph storage mechanism to support such an extension. We develop a comprehensive cost model, that estimates the number of matches of any given pattern graph by considering power-law degree distribution in the data graph. We then generalize the left-deep join framework and develop a dynamic-programming algorithm to compute an optimal bushy join plan. We also consider overlaps among the join units. Finally, we propose clique compression to further improve the algorithm by reducing the number of the intermediate results. Extensive performance studies are conducted on several real graphs, one containing billions of edges. The results demonstrate that our algorithm outperforms all other state-of-the-art algorithms by more than one order of magnitude.
featured: false
url_pdf: files/p217-lai.pdf
url_slides: files/vldb2017-slides.pdf
url_code: https://github.com/longbinlai/SubgEnumFramework
publication: "*Proc. VLDB Endow.*"
doi: "10.14778/3021924.3021937"
---

