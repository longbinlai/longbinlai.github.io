---
title: "GLogS: Interactive Graph Pattern Matching Query At Large Scale"
date: 2023-05-03
publishDate: 2023-05-03T01:41:34.981585Z
authors: ["Longbin Lai", "Yufan Yang", "Zhibin Wang", "Yuxuan Liu", "Haotian Ma", "Sijie Shen", "Bingqing Lyu", "Xiaoli Zhou", "Wenyuan Yu", "Zhengping Qian", "Chen Tian", "Shen Zhong", "Yeh-Ching Chung", "Jingren Zhou"]
publication_types: ["1"]
abstract: Interactive GPM (iGPM) is becoming increasingly important for data scientists to explore graphs in real life, where a series of graph pattern matching (GPM) queries are created and submitted in an interactive manner based on the insights provided by the prior queries. To solve the iGPM problem, three key considerations must be taken into account -- performance, usability and scalability -- namely if results can be returned in a timely manner, if queries can be written in a declarative way without the need of imperative fine-tune, and if it can work on large graphs. In this paper, we propose the GLogS system that allows users to interactively submit queries using a declarative language. The system will compile and automatically compute optimal execution plans for the queries, and execute them on an existing distributed dataflow engine. In the evaluation, we compare GLogS with the alternatives systems Neo4j and TigerGraph. GLogS outperforms Neo4j by $51\times$ on a single machine due to better execution plans. Additionally, GLogS can scale to handle large graphs with distributed capability. While compared to TigerGraph, GLogS is superior in usability, featuring an optimizer that can automatically compute optimal execution plans, eliminating the need of manual query tuning as required in TigerGraph.
featured: true
url_pdf: files/paper193_glogs_final.pdf
url_code: https://github.com/MeloYang05/GLogS-Artifact
url_slides: files/atc23_slides_lai_0.pdf
publication: "USENIX Annual Technical Conference (ATC) 2023"
tags: ["Graph database", "Graph pattern matching", "Distributed system", "Query optimization", "Graph sparsification"]
---

