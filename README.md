# OOP_Ex3

This project is about directed weighted graph.

Classes:
GeoLocation: represents a point in a plane <x,y,z>

NodeData: represents a vertex in a graph and contains its GeoLocation, key and weight.

EdgeData: represents an edge in a graph and contains source, destination, and the weight of the edge.

DirectedWeightedGraph: represents the whole graph. we implemented it using a HashMap<Integer,NodeData> of nodes and a HashMap<Integer, HashMap<Integer, EdgeData>> of edges. The keys of the nodes HashMap are the id's nodes, and the values are the nodes according to their id. The keys of the edges HashMap are the sources (on which vertex the edge starts) and the values contains HashMaps in which the keys are the destinations (on which vertex the edge ends) and the values are the Edges.

DirectedWeightedGraphAlgorithms: Functions explanation:

copy: gets a graph and make a deep copy of it.

isConnected: in this function we represented our graph as List<List> which is an adjacency list, then we iterated through the list and used DFS by recursion to check whether we were able to visit each vertex of the graph.
  
shortestPathDist: in this function we used Floyd Warshall Algorithm which gives us an adjacency matrix, then the answer is matrix[src][dest].
  
shortestPath: in this function we used Dijkstra's Algorithm with the help of another matrix so we can use her to save our path in the list and then return it.
  
centerPoint: in this function we also used Floyd Warshall Algorithm to get our matrix of shortest paths from each vertex to each vertex, then we saved the shortest distance of each vertex in a temp array and returned the max value in this array.
  
TSP: in this function we also used Floyd Warshall Algorithm.
  
save: saves our graph object into a JSON file.
  
load: reads a JSON file and loads it as graph.
  
plot_graph:in this function we used matplotlib to be able to present the graph. 
 
On the wiki link below, you will find our difference report between the plot and functions we used now to Ex2.  

https://github.com/tamar-revazishvili/OOP_Ex3.wiki

Running the program will be via Psycharm software or via CMD.
