---
title: "Bridging the Gap between Relational OLTP and Graph-based OLAP"
date: 2023-05-03
publishDate: 2023-05-03T01:41:34.981585Z
authors: ["Sijie Shen", "Zihang Yao", "Lin Shi", "Lei Wang", "Longbin Lai", "Qian Tao", "Li Su", "Rong Chen", "Wenyuan Yu", "Haibo Chen", "Bingyu Zang", "Jingren Zhou"]
publication_types: ["1"]
abstract: This paper presents GART, an in-memory system extended from hybrid transactional/analytical processing (HTAP) systems for hybrid transactional and graph analytical processing (HTGAP). GART should fulfill two unique goals not encountered by HTAP systems. First, to adapt to rich workloads flexibility, GART proposes transparent data model conversion by graph extraction interfaces, which define rules of relational-graph mapping. Second, to ensure the performance of graph analytical processing (GAP), GART proposes an efficient dynamic graph storage with good locality that stems from key insights into HTGAP workloads, including (1) an efficient and mutable CSR to guarantee the locality of scanning edges, (2) a coarse-grained MVCC to reduce the temporal and spatial overhead of versioning, and (3) a flexible property storage to efficiently run various GAP workloads. Evaluations show that GART is several orders of magnitude better than existing solutions in terms of freshness or performance. Meanwhile, for GAP workloads on the LDBC SNB dataset, GART outperforms the state-of-the-art general-purpose dynamic graph storage (i.e., LiveGraph) by up to $4.4\times$.
featured: false
url_pdf: files/atc23-final517.pdf 
url_code: https://github.com/SJTU-IPADS/vegito/tree/gart
publication: "USENIX Annual Technical Conference (ATC) 2023"
tags: ["Graph Database", "Relational Database", "HTAP", "HTGAP"]
---
