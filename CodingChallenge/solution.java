//The initial attempt is to use DFS/Dijkstra algorithm
//Each vertex represents a kind of currency, each edge between vertex a&b should be the currency rate from a to b 
import java.util.*;


class solution{
    private HashMap<String, int> dist; //distance to each other vertex
    private Set<String> visited; //visited vertices
    private PriorityQueue<Node> pq; 
    private int N; //total number of vertices
    List<List<Node> > adj;//neighbor vertices

    public solution(int N){
        this.N = N;
        dist = new HashMap<String, int>();
        visited = new HashSet<String>();
        pq = new PriorityQueue<Node>(N, new Node());
    }
    public void dijkstra(List<List<Node>> adj, String from, String[][] Rate){
        this.adj = adj;

        for (int i = 0; i < N; i++){
            dist.put(Rate[i][0], Integer.MAX_VALUE);
        }

        pq.add(new Node(from, 0));
        dist.replace(from, 0);
        while (visited.size() != N){
            if (pq.isEmpty())
            return;
        
            String u = pq.remove().node; //remove min distance
            if (visited.contains(u))
                continue;
        
            visited.add(u);
            proceed_past(u);
        }
    }
    
    void proceed_past(String u)
    {
        int edgeDis = -1;
        int addDis = -1;

        for (int i = 0; i < adj.get(u).size(); i++){
            Node v = adj.get(u).get(i);
            if(!visited.contains(v.node)){
                edgeDis = v.val;
                addDis = dist.get(u) + edgeDis;
            }
            if(addDis < dist.get(v.node)){
                dist.get(v.node) = addDis;
            }
            pq.add(new Node(v.node, dist.get(v.node)));
        }
    }

    public static void main(String arg[]){
        Scanner s = new Scanner(System.in);
        String line[] = s.nextLine().split(";");
        // System.out.println(line[0].split(",")[0]);
        String[][] Rate = new String[line.length][3];
        for (int i = 0; i < line.length; i++){
            String temp[] = line[0].split(",");
            Rate[i][0] = temp[0];
            Rate[i][1] = temp[1];
            Rate[i][2] = temp[2];
        }
        int N = line.length;
        String from = s.nextLine();
        String to = s.nextLine();
        

        List<List<Node>> adj = new ArrayList<List<Node>>();
        for (int i = 0; i < N; i++){
            List<Node> item = new ArrayList<Node> ();
            adj.add(item);
        }

    }
}

class Node implements Comparator<Node> {
  
    public int node;
    public int val;
  
    public Node() {}
    public Node(String node, int val)
    {
        this.node = node;
        this.val = val;
    }
  
    @Override public int compare(Node node1, Node node2)
    {
  
        if (node1.val < node2.val)
            return -1;
  
        if (node1.val > node2.val)
            return 1;
  
        return 0;
    }

}
