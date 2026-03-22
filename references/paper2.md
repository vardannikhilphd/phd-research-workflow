# Paper Note 2 citation

## Full Citation
Huang, L., Feng, X., Zhang, C., Qian, L., & Wu, Y. (2023). Deep reinforcement learning-based joint task offloading and bandwidth allocation for multi-user mobile edge computing. *IEEE Transactions on Wireless Communications*, 22(8), 5511–5524. https://doi.org/10.1109/TWC.2023.3240360

## Summary
Addresses multi-user MEC where simultaneous task offloading and bandwidth allocation decisions must be made in real time under dynamic channel conditions. Proposes a deep RL agent (DDPG-based) that treats both offloading decisions and bandwidth as continuous action spaces, achieving lower latency than fixed-allocation baselines.

## Key Points
- DDPG with continuous action space covers both offloading ratio and bandwidth allocation jointly
- Dynamic channel state fed as input to the actor network — adapts to fast-fading environments
- Multi-user interference modelled explicitly in the reward function
- Converges 30% faster than standard DQN due to continuous action formulation
- Tested under varying user density (5–50 users) — scales reasonably well

## Relevance to My Research
Useful as a latency-focused DRL baseline. The continuous action space formulation is applicable if your work involves fractional offloading. Compare bandwidth allocation strategy against your own resource management approach.
