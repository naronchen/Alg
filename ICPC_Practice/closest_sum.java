import java.util.*;

public class closest_sum {
    public static void main(String[] args){
        Scanner sc = new Scanner (System.in);

        while (sc.hasNextLine()){
            int_num = sc.nextint();
            int [] ints = new int[int_num];
            for (int i = 0 ; i < int_num ; i++){
                ints[i] = sc.nextint();
            }

            query_num = sc.nextint();
            int [] queries = new int[query_num];
            for (int i = 0 ; i < query_num ; i++){
                queries[i] = sc.nextint();
            }

        }