---
title: Distributed Pattern Matching System with Cypher
summary: To develop a graph pattern matching system in the distributed context, while gluing together the academic results of optimal join algorithms and industrial efforts of query language
tags:
- Graph Database
- Distributed System
- Graph Pattern Matching
- Query Optimization
- Cypher
date: "2018-05-01T00:00:00Z"

# Optional external URL for project (replaces project detail page).
external_link: ""

image:
  caption: The Patmat Architecture
  focal_point: Smart

links:
url_code: ""
url_pdf: ""
url_slides: ""
url_video: "https://youtu.be/df5bvs0AHHU"
---

Graph pattern matching is one of the most fundamental problems in graph database and is associated with a wide spectrum of applications. Due to its computational intensiveness, researchers have primarily devoted their efforts to improving the performance of the algorithm while constraining the graphs to have singular labels on vertices (edges) or no label. Whereas in practice graphs are typically associated with rich properties, thus the main focus in the industry is instead on powerful query languages that can express a sufficient number of pattern matching scenarios. We demo PatMat in this work to glue together the academic efforts on performance and the industrial efforts on expressiveness. To do so, we leverage the state-of-the-art join-based algorithms in the distributed contexts and Cypher query language - the most widely-adopted declarative language for graph pattern matching. The experiments demonstrate how we are capable of turning complex Cypher semantics into a distributed solution with high performance.
