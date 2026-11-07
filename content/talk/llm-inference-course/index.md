---
title: How Large Language Models Run on GPUs
summary: "From a question to an answer: how LLM inference works, and how to make it more efficient."
date: "2026-11-05"
location: Zhejiang Gongshang University
url_course: /courses/llm-inference.html
featured: true
---

Follow the lifecycle of a single answer: from model parameters and text encoding, through attention and context, to loading weights into GPU memory, matrix computation, and next-token generation. The talk then explains inference bottlenecks and optimizations such as KV caching, batching, and quantization, showing how they improve response speed, reduce GPU memory usage, and support more concurrent users. The interactive course is in Chinese.
