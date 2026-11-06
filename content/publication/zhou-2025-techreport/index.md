---
title: "A Graph-native Optimization Framework for Complex Graph Queries"
date: 2025-04-01
publishDate: 2025-04-01T01:41:34.981585Z
authors: ["Bingqing Lyu", "Xiaoli Zhou", "Longbin Lai", "Yufan Yang", "Yunkai Lou", "Wenyuan Yu","Ying Zhang", "Jingren Zhou"]
publication_types: ["1"]
abstract: "This technical report extends the SIGMOD 2025 paper -- A Modular Graph-Native Query Optimization Framework -- by providing a comprehensive exposition of GOpt’s advanced technical mechanisms, implementation strategies, and extended evaluations. While the original paper introduced GOpt’s unified intermediate representation (GIR) and demonstrated its performance benefits, this report delves into the framework’s implementation depth: (1) the full specification of GOpt’s optimization rules; (2) a systematic treatment of semantic variations (e.g., homomorphism vs. edge-distinct matching) across query languages and their implications for optimization; (3) the design of GOpt’s Physical integration interface, enabling seamless integration with transactional (Neo4j) and distributed (GraphScope) backends via engine-specific operator customization; and (4) a detailed analysis of plan transformations for LDBC benchmark queries."
featured: true
url_pdf: files/gopt-tech-report.pdf
url_code: https://github.com/alibaba/GraphScope/tree/main/interactive_engine/compiler
publication: "arXiv:2503.22091"
tags: ["Graph database", "Graph pattern matching", "Query optimization", "Graph Intermediate Representation"]
---

