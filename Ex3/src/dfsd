package api;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.*;

public class DirectedWeightedGraphAlgorithmsImpl implements DirectedWeightedGraphAlgorithms {
    public DirectedWeightedGraphImpl g;
    final double INF = 99999.0;

    public DirectedWeightedGraphAlgorithmsImpl() {
        g = new DirectedWeightedGraphImpl();
    }

    @Override
    public void init(DirectedWeightedGraph g) {
        this.g = (DirectedWeightedGraphImpl) g;
    }


    @Override
    public DirectedWeightedGraph getGraph() {
        return g;
    }

    @Override
    public DirectedWeightedGraph copy() {
        DirectedWeightedGraphImpl ans = new DirectedWeightedGraphImpl();
        Iterator<NodeData> nodeIterator = g.nodeIter();
        while (nodeIterator.hasNext()) {
            ans.addNode(nodeIterator.next());
        }
        for (int i : g.Edges.keySet()) {
            for (int k : g.Edges.get(i).keySet()) {
                int src = g.Edges.get(i).get(k).getSrc();
                int dest = g.Edges.get(i).get(k).getDest();
                double weight = g.Edges.get(i).get(k).getWeight();
                ans.connect(src, dest, weight);
            }
        }
        return ans;
    }

    @Override
    public boolean isConnected() {
        int n = g.Nodes.size();
        List<List<Integer>> adjList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adjList.add(new ArrayList<>());
        }
        Iterator<EdgeData> iter = g.edgeIter();
        while (iter.hasNext()) {
            EdgeData edge = iter.next();
            int src = edge.getSrc();
            int dest = edge.getDest();
            adjList.get(src).add(dest);
        }

        for (int i = 0; i < n; i++) {
            boolean[] visited = new boolean[n];
            DFS(adjList, i, visited);
            for (boolean b : visited) {
                if (!b) {
                    return false;
                }
            }
        }
        return true;
    }


    private void DFS(List<List<Integer>> adjList, int v, boolean[] visited) {
        visited[v] = true;
        for (int u : adjList.get(v)) {
            if (!visited[u]) {
                DFS(adjList, u, visited);
            }
        }
    }

    @Override
    public double shortestPathDist(int src, int dest) {
        double[][] mat = floydWarshallAlgorithm();
        if (mat[src][dest] != INF)
            return mat[src][dest];
        return -1;
    }

    @Override
    public List<NodeData> shortestPath(int src, int dest) {
        List<NodeData> ans = new LinkedList<>();
        int n = g.nodeSize();
        double[][] dis = new double[n][n];
        int[][] next = new int[n][n];
        double[][] mat = new double[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j)
                    mat[i][j] = 0;
                else
                    mat[i][j] = INF;
            }
        }
        Iterator<EdgeData> iter = g.edgeIter();
        while (iter.hasNext()) {
            EdgeData temp = iter.next();
            mat[temp.getSrc()][temp.getDest()] = temp.getWeight();
        }
//        initialize:
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dis[i][j] = mat[i][j];
                if (mat[i][j] == INF)
                    next[i][j] = -1;
                else
                    next[i][j] = j;
            }
        }

//        Floyd Warshall Algorithm:
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (dis[i][k] + dis[k][j] < dis[i][j]) {
                        dis[i][j] = dis[i][k] + dis[k][j];
                        next[i][j] = next[i][k];
                    }
                }
            }
        }

        if (next[src][dest] == -1)
            return null;
        ans.add(g.getNode(src));
        while (src != dest) {
            src = next[src][dest];
            ans.add(g.getNode(src));
        }
        return ans;
    }

    @Override
    public NodeData center() {
        int n = g.Nodes.size();
        double[][] D = floydWarshallAlgorithm();
        double[] temp = new double[n];
        for (int i = 0; i < n; i++) {
            temp[i] = 0;
            for (int j = 0; j < n; j++) {
                if (temp[i] < D[i][j]) {
                    temp[i] = D[i][j];
                }
            }
        }
        double max = INF;
        for (int i = 0; i < n; i++) {
            if (max > temp[i])
                max = temp[i];
        }
        for (int i = 0; i < n; i++) {
            if (temp[i] == max) {
                return g.getNode(i);
            }
        }
        return null;
    }

    private double[][] floydWarshallAlgorithm() {
        int n = g.nodeSize();
        double[][] ans = new double[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j)
                    ans[i][j] = 0;
                else
                    ans[i][j] = INF;
            }
        }
        Iterator<EdgeData> iter = g.edgeIter();
        while (iter.hasNext()) {
            EdgeData temp = iter.next();
            ans[temp.getSrc()][temp.getDest()] = temp.getWeight();
        }
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (ans[i][k] + ans[k][j] < ans[i][j]) {
                        ans[i][j] = ans[i][k] + ans[k][j];
                    }
                }
            }
        }
        return ans;
    }

    @Override
    public List<NodeData> tsp(List<NodeData> cities) {
        double[][] mat = floydWarshallAlgorithm();
        int counter = 0;
        int j = 0, i = 0;
        int n = cities.size();
        double min = Double.MAX_VALUE;
        List<NodeData> visited = new ArrayList<>();
        visited.add(cities.get(0));
        int[] route = new int[mat.length];
        while (i < n && j < n) {
            if (counter >= n - 1) {
                break;
            }
            if (j != i && !(visited.contains(cities.get(j)))) {
                if (mat[i][j] < min) {
                    min = mat[i][j];
                    route[counter] = j + 1;
                }
            }
            j++;
            if (j == n) {
                min = Integer.MAX_VALUE;
                visited.add(cities.get(route[counter] - 1));
                j = 0;
                i = route[counter] - 1;
                counter++;
            }
        }
        for (j = 0; j < n; j++) {
            if ((i != j) && mat[i][j] < min) {
                min = mat[i][j];
                route[counter] = j + 1;
            }
        }
        return visited;
    }


    public boolean save(String file) {
        JsonObject graph = new JsonObject();
        JsonArray Nodes = new JsonArray();
        Iterator<NodeData> nodeIter = g.nodeIter();
        while (nodeIter.hasNext()) {
            NodeData temp = nodeIter.next();
            JsonObject node = new JsonObject();
            node.addProperty("pos", temp.getLocation().toString());
            node.addProperty("id", temp.getKey());
            Nodes.add(node);
        }
        JsonArray Edges = new JsonArray();
        Iterator<EdgeData> edgeIter = g.edgeIter();
        while (edgeIter.hasNext()) {
            EdgeData temp = edgeIter.next();
            JsonObject edge = new JsonObject();
            edge.addProperty("src", temp.getSrc());
            edge.addProperty("w", temp.getWeight());
            edge.addProperty("dest", temp.getDest());
            Edges.add(edge);
        }
        graph.add("Edges", Edges);
        graph.add("Nodes", Nodes);
        try {
            Gson gson = new GsonBuilder().setPrettyPrinting().create();
            FileWriter w = new FileWriter(file);
            gson.toJson(graph, w);
            w.close();
            return true;
        } catch (IOException e) {
            e.printStackTrace();
            return false;
        }
    }


    @Override
    public boolean load(String file) {
        try {
            this.init(g);
            Gson gson = new Gson();
            FileReader r = new FileReader(file);
            JsonObject graph = gson.fromJson(r, JsonObject.class);
            JsonArray Nodes = graph.get("Nodes").getAsJsonArray();
            for (int i = 0; i < Nodes.size(); i++) {
                JsonObject node = Nodes.get(i).getAsJsonObject();
                String str = node.get("pos").getAsString();
                NodeData n = new NodeDataImpl(new GeoLocationImpl(str), node.get("id").getAsInt());
                this.g.addNode(n);
            }
            JsonArray Edges = graph.get("Edges").getAsJsonArray();
            for (int i = 0; i < Edges.size(); i++) {
                JsonObject edge = Edges.get(i).getAsJsonObject();
                int src = edge.get("src").getAsInt();
                double w = edge.get("w").getAsDouble();
                int dest = edge.get("dest").getAsInt();
                this.g.connect(src, dest, w);
            }
            r.close();
        } catch (IOException e) {
            e.printStackTrace();
            return false;
        }
        return false;
    }

}
