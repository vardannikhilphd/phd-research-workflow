# Paper Note 3 Citation

## Full Citation
Wang, X., Han, Y., Wang, C., Zhao, Q., Chen, X., & Chen, M. (2023). In-edge AI: Intelligentizing mobile edge computing, caching and communication with heterogeneous model compression. *IEEE Journal on Selected Areas in Communications*, 41(3), 603–619. https://doi.org/10.1109/JSAC.2023.3240701

## Summary
Proposes In-Edge AI, a framework that co-optimizes model compression, edge caching, and computation offloading for AI inference tasks at the edge. Heterogeneous devices receive compressed model variants sized to their compute capacity, reducing inference latency while maintaining acceptable accuracy under constrained edge resources.

## Key Points
- Heterogeneous model compression: different compression ratios assigned per device based on available compute and channel quality
- Joint optimization of caching policy + offloading decision + compression ratio — three-way co-design
- Lyapunov-based online algorithm — no future system state knowledge required
- Reduces inference latency by up to 40% vs. full-model offloading baselines
- Handles time-varying task arrival rates and channel fluctuations stably

## Relevance to My Research
Directly relevant if your work involves Edge AI inference offloading. The Lyapunov online optimization technique is worth adopting for its stability guarantees. Gap: does not consider federated training — only inference. Combining this with FL training (as in Paper 1) is a potential novel direction.
