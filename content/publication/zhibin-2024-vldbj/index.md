---
title: "Parallelization of Butterfly Counting on Hierarchical Memory"
date: 2024-04-24
publishDate: 2024-04-24T01:41:34.981585Z
authors: ["Zhibin Wang", "Longbin Lai", "Yixue Liu", "Bing Shui", "Chen Tian", "Sheng Zhong"]
publication_types: ["2"]
abstract: Butterfly (a cyclic graph motif) counting is a fundamental task with many applications in graph analysis, which aims at computing the number of butterflies in a large graph. With the rapid growth of graph data, it is more and more challenging to do butterfly counting due to the super-linear time complexity and large memory consumption. In this paper, we study I/O-efficient algorithms for doing butterfly counting on hierarchical memory. Existing algorithms of this kind cannot guarantee I/O optimality. Observing that in order to count butterflies, it suffices to ``witness'' a subgraph instead of the whole structure, a new class of algorithms called Semi-Witnessing algorithm is proposed. We prove that a Semi-Witnessing  algorithm is not restricted by the lower bound $\Omega(\frac{|E|^2}{MB})$ of a witnessing algorithm, and give a new bound of $\Omega(\min(\frac{|E|^2}{MB}, \frac{|E||V|}{\sqrt{M}B}))$. Subsequently, we develop the IOBufs algorithm that manages to approach the I/O lower bound, and thus claim its optimality. Finally, we investigate the parallelization of IOBufs to improve its performance and scalability. To support various hardware configurations, we introduce a general parallel framework, PIOBufs. Our analysis indicates that the key to implementing PIOBufs on multi-core CPUs lies in the fine-grained task division. Furthermore, we extend the CPU-tailored PIOBufs to harness the extensive parallelism that GPUs provide. Our experimental results show that IOBufs performs better than established algorithms such as EMRC, BFC-EM and G-BFC. Thanks to its I/O-efficient design, IOBufs can handle large graphs that exceed the main memory capacity on both CPUs and GPUs. A significant result is that IOBufs can manage butterfly counting on the Clueweb graph, which has 37 billion edges and quintillions ($10^{18}$) of butterflies.
url_pdf: files/iobufs-vldbj.pdf
doi: "10.1007/s00778-024-00856-x"
featured: false
publication: "VLDB Journal (Extended from Sigmod 2023 paper)"
tags: ["Graph", "Butterfly counting", "I/O-efficient algorithm", "Semi-witnessing", "Parallel algorithm", "GPU"]
---

