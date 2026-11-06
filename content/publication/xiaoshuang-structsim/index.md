---
title: "StructSim: Querying Structural Node Similarity at Billion Scale"
date: 2019-11-01
publishDate: 2019-11-01T00:43:27.786038Z
authors: ["Xiaoshuang Chen", "Longbin Lai", "Lu Qin", "Xuemin Lin"]
publication_types: ["1"]
abstract: Structural node similarity is widely used in analyzing complex networks. As one of the structural node similarity metrics, role similarity has the good merit of indicating automorphism (isomorphism). Existing algorithms to compute role similarity (e.g., RoleSim and NED) suffer from severe performance bottlenecks, and thus cannot handle large real-world graphs. In this paper, we propose a new framework StructSim to compute nodes' role similarity. Under this framework, we prove that StructSim is guaranteed to be an admissible role similarity metric based on the maximum matching. While maximum matching is too costly to scale, we then devise the BinCount matching to speed up the computation. BinCount-based StructSim admits a precomputed index to query one single pair in $O(k\log D)$ time, where $k$ is a small user-defined parameter and $D$ is the maximum node degree. Extensive empirical studies show that StructSim is significantly faster than existing works for computing structural node similarities on the real-world graphs, with comparable effectiveness.
featured: false
url_pdf: files/structsim_short.pdf
publication: "*36th IEEE International Conference on Data Engineering (short)*"
doi: "10.1109/ICDE48307.2020.00211"
tags: ["Node Similarity", "Role Similarity", "Efficiency", "Scalability"]
---

