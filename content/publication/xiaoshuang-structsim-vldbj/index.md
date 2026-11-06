---
title: "Efficient structural node similarity computation on billion-scale graphs (ICDE20 extended to VLDBJ)"
date: 2020-12-28
publishDate: 2021-2-23T00:43:27.786038Z
authors: ["Xiaoshuang Chen", "Longbin Lai", "Lu Qin", "Xuemin Lin"]
publication_types: ["2"]
abstract: Structural node similarity is widely used in analyzing complex networks. As one of the structural node similarity metrics, role similarity has the good merit of indicating automorphism (isomorphism). Existing algorithms to compute role similarity (e.g., \rolesim and \ned) suffer from severe performance bottlenecks, and thus cannot handle large real-world graphs. In this paper, we propose a new framework, namely \structsim, to compute nodes' role similarity. Under this framework, we first prove that \structsim is an admissible role similarity metric based on the maximum matching. While the maximum matching is still too costly to scale, we then devise the \bincount matching that not only is efficient to compute but also guarantees the admissibility of \structsim. \bincount-based \structsim admits a precomputed index to query a single pair of node in $O(k\log D)$ time, where $k$ is a small user-defined parameter and $D$ is the maximum node degree. To build the index, we further devise an FM-sketch-based technique that can handle graphs with billions of edges. Extensive empirical studies show that \structsim performs much better than the existing works regarding both effectiveness and efficiency when applied to compute structural node similarities on the real-world graphs. 
featured: false
url_pdf: files/StructSim_VLDBJ.pdf
publication: "VLDB Journal 2021"
doi: "https://doi.org/10.1007/s00778-021-00654-9"
tags: ["Node Similarity", "Role Similarity", "Efficiency", "Link Analysis"]
---
