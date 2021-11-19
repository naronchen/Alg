import java.util.*;

public class DifPro
{
    public static void main(String[] args)
    {  
        Scanner stdin = new Scanner(System.in);
        while (stdin.hasNextLine()){
            String str = stdin.nextLine();
            String[] splited = str.split("\\s");
            


            if (n > m){ System.out.println(n-m); }
            else{ System.out.println(m-n);}
        }
        stdin.close();
    }
}