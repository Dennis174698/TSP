
## Applying Ant Colony Optimisation to the Travelling Salesman Problem

### problem discription 
Travelling salesman problem:if a travelling salesman wishes to visit exactly once each of a list of m cities (where the cost of travelling from city i to city j is cij) and then return to the home city, what is the least costly route a salesman can take?

### Algorithm
The ACO algorithm is based on the behaviour of ants, attempts to find the optimal path between two points.<br>
This is achieved by sending a number of waves of ants to traverse the graph. The first wave of ants traverse the graph either randomly or based on a simple heuristic approach (such as taking the shortest path from any node). Pheromone is then distributed along successful paths such that the paths determined to be better by a scoring function will receive a higher amount of pheromone. Further generations of ants are then sent to traverse the graph, taking into account pheromone levels and heuristic, and again laying pheromone on paths proportionally to the paths score. <br>
In this way, the most optimal paths will accumulate the highest amounts of pheromone and are more likely to be chosen by subsequent generations of ants. <br>

### Implementation
<div align="center">
<img src="https://github.com/Dennis174698/TSP/raw/master/workflow1.png" height="646px" >    
</div>
 
