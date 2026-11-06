---
title: A Graph-Native Query Optimization Framework
summary: GOpt is built on top of a unified intermediate representation (IR) that is capable of capturing both graph and relational operations, thereby streamlining the optimization of graph queries.
tags:
- Graph Database
- Query Language
- Graph Pattern Matching
- Query Optimization
date: "2024-11-12T00:00:00Z"

# Optional external URL for project (replaces project detail page).
external_link: ""

image:
  caption: The GOpt Framework
  focal_point: Smart

links: 
url_code: "https://github.com/alibaba/GraphScope/tree/main/interactive_engine/compiler"
url_pdf: "https://arxiv.org/pdf/2401.17786"
url_docs: "https://graphscope.io/docs/interactive_engine/optimizer"
url_blog: "https://graphscope.io/blog/tech/2024/02/22/GOpt-A-Unified-Graph-Query-Optimization-Framework-in-GraphScope"

---

Graph queries that combine pattern matching with relational operations, referred as PatRelQuery, are widely used in many real-world applications. It allows users to identify arbitrary patterns in a graph and further perform in-depth relational analysis on the results. To effectively support PatRelQuery, two key challenges need to be addressed: (1) how to optimize PatRelQuery in a unified framework, and (2) how to handle the arbitrary type constraints in patterns in PatRelQuery. In this paper, we present a graph-native query optimization framework named GOpt, to tackle these issues. GOpt is built on top of a unified intermediate representation (IR) that is capable of capturing both graph and relational operations, thereby streamlining the optimization of PatRelQuery. To handle the arbitrary type constraints, GOpt employs an automatic type inference approach to identify implicit type constraints. Additionally, GOpt introduces a graph-native optimizer, which encompasses an extensive collection of optimization rules along with cost-based techniques tailored for arbitrary patterns, to optimize PatRelQuery. Through comprehensive experiments, we demonstrate that GOpt can achieve significant query performance improvements, in both crafted benchmarks and real-world applications.
