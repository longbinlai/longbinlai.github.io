---
title: Interactive Analysis on Distributed Graphs Using Gremlin Language
summary: GAIA (former name, Pegasus) is a distributed data-parallel compute engine based on the cyclic dataflow computation model. GAIA serves as the computation engine, lying at the core of the GraphScope system. Users can construct the computation via a directed acyclic graph (DAG), and easily run the job on their laptop or even a distributed environment across a cluster of computers.
tags:
- Distributed System
- Query Execution Engine
- Gremlin Query Execution
date: "2024-11-12T00:00:00Z"

# Optional external URL for project (replaces project detail page).
external_link: ""

image:
  caption: The GAIA System
  focal_point: Smart

links: 
url_code: "https://github.com/alibaba/GraphScope/tree/main/interactive_engine/executor/engine/pegasus"
url_pdf: "https://www.usenix.org/system/files/nsdi21-qian.pdf"

---

GAIA (GrAph Interactive Analysis) is a distributed system designed specifically to make it easy for a variety of users to interactively analyze big graph data on large clusters at low latency. It adopts a high-level language called Gremlin for graph traversal, and provides automatic parallel execution. In particular, we advocate a powerful new abstraction called Scope that caters to the specific needs in this new computation model to scale graph queries with complex dependencies and runtime dynamics, while at the same time maintaining the simple and concise programming model. GAIA has been deployed in production clusters at Alibaba to support a variety of business-critical scenarios. Extensive evaluations using both benchmarks and real-world applications have validated the effectiveness of the proposed techniques, which enables GAIA to execute complex Gremlin traversal with orders-of-magnitude better performance than existing high-performance engines, and at much larger scales than recent state-of-the-art Gremlin-enabled systems such as JanusGraph.
