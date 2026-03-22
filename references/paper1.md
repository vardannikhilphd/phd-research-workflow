# Paper Note 1 Citation

## Full Citation
Chen, Z., Hu, J., Min, G., Zhou, A., & Georgalas, N. (2024). Joint computation offloading and resource allocation in multi-edge smart communities with personalized federated deep reinforcement learning. *IEEE Transactions on Mobile Computing*, 23(12), 11604–11619. https://doi.org/10.1109/TMC.2024.3396511

## Summary
Proposes PFR-OA, a personalized federated deep RL framework for joint task offloading and resource allocation in heterogeneous multi-edge smart communities. Solves the non-IID data problem in federated RL via a proximal term that aligns local and global Q-values, reducing latency and energy consumption without sharing raw data.

## Key Points
- Federated DRL with personalized local Q-network training — no raw data sharing (privacy-preserving)
- Proximal term modification reduces divergence between local and global models
- Partial-greedy participant selection reduces FL aggregation overhead
- Joint optimization of delay + energy across heterogeneous edge servers
- Outperforms DQN, DDPG, FedAvg baselines on task success rate and latency-energy trade-off

## Relevance to My Research
Strong baseline for federated RL-based offloading; directly comparable to any multi-edge latency optimization work. Gap to exploit: does not handle user mobility or DAG-structured tasks.
