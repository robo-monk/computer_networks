# Routing

## Key points of routing (properties)

1. Correctness 
2. Simplicity
3. Robustness
4. Stability
5. Fairness
6. Efficiency


## Optimality Principle
> If the best route C->A is through B, then B->A follows the same path
The collection of all best paths to a given destination forms a **tree**

# Algos to route packets
1. Distance vector routing
2. Link state routing
3. Hierarchical routing


## Routing tables
For every address, which link should you forward the packet to. 

> Routing table for C.
<img src="routing_table_eg.png">

---
## Distance vector routing

1. Send your distance vector to your neighbors.
2. You use incoming distance vectors from your neighbour to construct a routing table

> Updating routing table
<img src="routing_table_dvr1.png">
<img src="routing_table_dvr2.png">

### Problem - Count to infinity

Happends when a node goes offline.
<img src="count_to_infinity_problem.png">


