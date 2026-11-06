---
title: "ShmStreaming: A Shared Memory Approach for Improving Hadoop Streaming Performance"
date: 2013-03-01
publishDate: 2013-03-01T02:33:12.141757Z
authors: ["Longbin Lai", "Jingyu Zhou", "Long Zheng", "Huakang Li", "Yanchao Lu", "Feilong Tang", "Minyi Guo"]
publication_types: ["1"]
abstract: The Map-Reduce programming model is now drawing both academic and industrial attentions for processing large data. Hadoop, one of the most popular implementations of the model, has been widely adopted. To support application programs written in languages other than Java, Hadoop introduces a streaming mechanism that allows it to communicate with external programs through pipes. Because of the added overhead associated with pipes and context switches, the performance of Hadoop streaming is significantly worse than native Hadoop jobs. We propose ShmStreaming, a mechanism that takes advantages of shared memory to realize Hadoop streaming for better performance. Specifically, ShmStreaming uses shared memory to implement a lockless FIFO queue that connects Hadoop and external programs. To further reduce the number of context switches, the FIFO queue adopts a batching technique to allow multiple key-value pairs to be processed together. For typical benchmarks of word count, grep and inverted index, experimental results show 20-30% performance improvement comparing to the native Hadoop streaming implementation.
featured: false
url_pdf: files/06531748.pdf
url_code: https://github.com/longbinlai/ShmStreaming
publication: "*2013 IEEE 27th International Conference on Advanced Information Networking and Applications (AINA)*"
tags: 
- MapReduce
- Shared Memory
- Hadoop
- Synchronization
doi: "10.1109/AINA.2013.90"
---

