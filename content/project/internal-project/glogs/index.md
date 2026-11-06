---
title: Interactive Graph Pattern Matching
summary: We develop GLogS system, allowing users to interactively submit queries using a declarative language, which will be compiled and automatically optimized, and eventually executed on the GAIA dataflow engine.
tags:
- Graph Database
- Distributed System
- Graph Pattern Matching
- Query Optimization
date: "2024-11-12T00:00:00Z"

# Optional external URL for project (replaces project detail page).
external_link: ""

image:
  caption: GLogS system
  focal_point: Smart

links: 
url_code: "https://github.com/MeloYang05/GLogS-Artifact"
url_pdf: "https://www.usenix.org/system/files/atc23-lai.pdf"

---

Interactive GPM (iGPM) is becoming increasingly important, where a series of graph pattern matching (GPM) queries are created and submitted in an interactive manner based on the insights provided by the prior queries. To solve the iGPM problem, three key considerations must be taken into account: performance, usability and scalability, namely if results can be returned in a timely manner, if queries can be written in a declarative way without the need of imperative fine-tune, and if it can work on large graphs. In this paper, we propose the GLogS system that allows users to interactively submit queries using a declarative language. The system will compile and automatically compute optimal execution plans for the queries, and execute them on an existing distributed dataflow engine. In the evaluation, we compare GLogS with the alternatives systems Neo4j and TigerGraph. GLogS outperforms Neo4j by 51 × on a single machine due to better execution plans. Additionally, GLogS can scale to processing large graphs with distributed capability. While compared to TigerGraph, GLogS is superior in usability, featuring an optimizer that can automatically compute optimal execution plans, eliminating the need of manual query tuning as required in TigerGraph.
