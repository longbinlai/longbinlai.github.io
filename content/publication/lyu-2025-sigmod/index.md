---
title: "A Modular Graph-Native Query Optimization Framework"
date: 2025-04-01
publishDate: 2025-04-01T01:41:34.981585Z
authors: ["Bingqing Lyu", "Xiaoli Zhou", "Longbin Lai", "Yufan Yang", "Yunkai Lou", "Wenyuan Yu","Ying Zhang", "Jingren Zhou"]
publication_types: ["1"]
abstract: "Complex Graph Patterns (CGPs), which combine pattern matching with relational operations, are widely used in real-world applications. Existing systems rely on monolithic architectures for CGPs, which restrict their ability to integrate multiple query languages and lack certain advanced optimization techniques. Therefore, to address these issues, we introduce GOpt, a modular graph-native query optimization framework with the following features: (1) support for queries in multiple query languages, (2) decoupling execution from specific graph systems, and (3) integration of advanced optimization techniques. Specifically, GOpt offers a high-level interface, GraphIrBuilder, for converting queries from various graph query languages into a unified intermediate representation (GIR), thereby streamlining the optimization process. It also provides a low-level interface, PhysicalConverter, enabling backends integration by converting the optimized plan into a backend-compatible execution plan. Moreover, GOpt employs a graph-native optimizer that encompasses extensive heuristic rules, an automatic type inference approach, and cost-based optimization techniques tailored for CGPs. Comprehensive experiments show that integrating GOpt significantly boosts performance, with Neo4j achieving an average speedup of 9.2x (up to 48.6x), and GraphScope achieving an average speedup of 33.4x (up to 78.7x), on real-world datasets."
featured: true
url_pdf: files/gopt-cr.pdf
url_code: https://github.com/alibaba/GraphScope/tree/main/interactive_engine/compiler
url_slides: files/gopt-slides.pdf
publication: "ACM SIGMOD/PODS International Conference on Management of Data 2025 (to appear)"
doi: ""
tags: ["Graph database", "Graph pattern matching", "Query optimization", "Graph Intermediate Representation"]
---

