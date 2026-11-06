---
title:  A High-Throughput Transactional Graph Database
summary: GraphScope Interactive is a specialized construction of GraphScope Flex, designed to handle concurrent graph queries at an impressive speed. Its primary goal is to process as many queries as possible within a given timeframe, emphasizing a high query throughput rate.
tags:
- Graph Database
- Graph Pattern Matching
- LDBC Benchmark
date: "2024-11-12T00:00:00Z"

# Optional external URL for project (replaces project detail page).
external_link: ""

image:
  caption: GraphScope Interactive
  focal_point: Smart

links: 
url_code: "https://github.com/alibaba/GraphScope/tree/main/flex/interactive"
url_docs: "https://graphscope.io/docs/flex/interactive/overview"

---

GraphScope Interactive is a specialized construction of GraphScope Flex, designed to handle concurrent graph queries at an impressive speed. Its primary goal is to process as many queries as possible within a given timeframe, emphasizing a high query throughput rate. GraphScope Interactive stands on the shoulders of two pivotal pillars:

- GraphScope Flex: GraphScope Flex is a new architecture of GraphScope that provides a solid foundation for GraphScope Interactive. It is designed to handle high-QPS (Queries Per Second) scenarios, making it an ideal base for the high-throughput demands of GraphScope Interactive.

- Record-Breaking Benchmarking Results: GraphScope Interactive is built upon the [record-breaking LDBC SNB Interactive benchmarking results](https://ldbcouncil.org/benchmarks/snb-interactive/), which has achieved a throughput of 33,180.87 ops/s for the benchmarking, making it one of the most efficient systems for graph query processing.
