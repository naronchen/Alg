//the question did not mention whether one issuer can have only one parent or multiple parents(if multiple parents I would use linkedlist list to implement a tree graph, then implement DFS)
//from my understanding of issuer parent, issuerparent should own 100% of the stock of the Issuer, mearning one child cannot have two parents

import java.util.*;
import java.io.*;

class ESG{

    public static void main(String[] args){
        // if we want to hold all the data, we can user two hash maps
        // HashMap<String, Integer> Rating =  new HashMap<String, Integer>(); // Issuer & Rating Map
        HashMap<String, String> childParent = new HashMap<String, String>();// Issuer & Parent Map
        // if we only want to get the answer,  we do the following
        List<String[]> cp = new ArrayList<String[]>();
        Scanner s = new Scanner(System.in);
        String line[] = s.nextLine().split(" \\| "); // RE, escape special character \ with "\\""
        
        //initializing variables

        String curParent = line[1];
        String curIssuer = line[0];
        String Ratingstr = line[2];
        int curRating = mapToValue(line[2]);
        int MaxRating = curRating;
        int count = 0;

        childParent.put(line[0], line[1]);
        while (s.hasNextLine()){
            line = s.nextLine().split(" \\| ");
            if (curParent.equals(line[0])){
                curRating = mapToValue(line[2]);
                if (curRating > MaxRating){ 
                    curIssuer = curParent;
                    MaxRating = curRating;
                    Ratingstr = line[2];}
            }
            childParent.put(line[0], line[1]);
        }

        String detect = "noncyclic";
        for (String c : childParent.keySet()){
            //Floyds Tortoise and Hare/two pointer alg to detect cycle
            String tortoise = c;
            String hare = c;
            System.out.println("c: " + c);
            if (detectCycle(tortoise, hare, childParent) == true)
            { 
                detect = "cyclic";
                break;
            }
        }

        System.out.println(detect);
        // System.out.println(curIssuer);
        // System.out.println(Ratingstr);
    }

    // converts String rating to Integers so its easier to compare later
    // each C  will be 1, each B will be 10, each C wil be 100
    public static int mapToValue(String r){
        int val = 0;
        char[] rChar = r.toCharArray();

        if (rChar[0] == 'A'){ val = 100;}
        if (rChar[0] == 'B'){ val = 10;}
        if (rChar[0] == 'C'){ val = 1;}

        val = val * rChar.length;
        return val;
        }

    public static String Move(String curpos, HashMap<String, String> map){
        return map.get(curpos);
    }

    public static boolean detectCycle(String t, String h, HashMap<String, String> map)
    {
        if (t == null | Move(t, map) == null){
            return false;
        }
        while(h != null && Move(h, map) != null){
            // System.out.println("h: " + h);
            // System.out.println("t: " + t);
            t = Move(t, map);
            h = Move(h, map);
            h = Move(h, map);
            if (t == h){
                return true;
            }
        }
        return false;
    }

}
