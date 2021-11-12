//Naron - BlackRock OA Q1
import java.util.*;

class Cartesian{
   
    public static void main(String[] args){
    //input formatting
        Scanner s = new Scanner(System.in);
        String lineA[] = s.nextLine().split(",");
        String lineB[] = s.nextLine().split(",");
        String lineC = s.nextLine();
        // int[] C = new int[] { Integer.parseInt(String.valueOf(lineC.charAt(1))), Integer.parseInt(String.valueOf(lineC.charAt(3))) };
        int C_1 = Integer.parseInt(String.valueOf(lineC.charAt(1)));
        int C_2 = Integer.parseInt(String.valueOf(lineC.charAt(3)));

        lineA[0] = lineA[0].replace("[","");
        lineA[lineA.length - 1] = lineA[lineA.length - 1].replace("]","");
        lineB[0] = lineB[0].replace("[","");
        lineB[lineB.length - 1] = lineB[lineB.length - 1].replace("]","");
        double[] A; 
        double[] B;

        //exception handling for incorrect format of input
        try{
        A = Arrays.stream(lineA)
                        .mapToDouble(Double::parseDouble)
                        .toArray();
        B = Arrays.stream(lineB)
                .mapToDouble(Double::parseDouble)
                .toArray();
        }
        catch(NumberFormatException ex){
            System.out.println("-1");
            return;
        }
        

    //only information needed are the length of A, B and two number in tuple C.
    //solution part
        int Ans = C_1 * B.length + C_2;
        System.out.println(Ans); 

    // it was asking for index of one member in Cartesian product
    // if it was asking first member of matching set(which is what I originally thought), it will be a little more complex dealing with duplicates

    }
}
