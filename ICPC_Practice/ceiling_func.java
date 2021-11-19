import java.util.*;

public class ceiling_func
{
    public static int n; //n combinations
    public static int k; //k integers in each combination
    public static node[] trees;

    public static void main(String[] args)
    {
        Scanner stdin = new Scanner(System.in);
        n = stdin.nextInt();
        k = stdin.nextInt();
        trees = new node[n];

        for (int i=0; i<n; i++){
            int root = stdin.nextInt();
            trees[i] = new node(root);
            for (int j=1; j<k;j++){
                int item = stdin.nextInt();
                trees[i].insert(item);
            }
        }

        int res = 1;
        
        for (int i=1; i<n; i++){

            boolean countIt = true;
            
            for (int j = 0; j<i; j++){
                if (trees[i].sameStructure(trees[j])){
                    countIt = false;
                    break;
                }
            }

            if (countIt) {res++;}

        }

        System.out.println(res);
    }

}

class node
{
    public int theNode;
    public node left;
    public node right;

    public node(int val){
        theNode = val;
        left = null;
        right = null;
    }

    public int nullnum(){
        if (right == null && left == null){ return 2;}
        else if(right == null || left == null){ return 1;}
        else { return 0;}
    }

    public void insert(int val){
        if (val < theNode) {
            if (left == null){ left = new node (val);}
            else{ left.insert(val);}
        }
        else{
            if (right == null){right = new node (val);}
            else{ right.insert(val);}
        }
    }

    public boolean sameStructure (node other){
        if (other.nullnum() == nullnum()){
        if (nullnum() == 2){ return true;}
        if(nullnum() == 1){ 
                if (other.left != null && left != null){ return left.sameStructure(other.left);}
                if (other.right != null && right != null){ return right.sameStructure(other.right);}
        }
        if (nullnum() == 0){ 
            if (left.sameStructure(other.left) == true && right.sameStructure(other.right) == true){ return true;}
            else { return false;}
            }
        }
        return false;
    }

}