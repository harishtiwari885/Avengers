import java.util.*;
public class CountingWords{
    public static void main(String[] args){
        Scanner j = new Scanner(System.in);
        System.out.print("Enter the Sentence: ");
        String s = j.nextLine();
        //breaking sentence into words
        String[] w = s.split(" ");
        //creating the hashmap
        Map<String , Integer> m = new HashMap<>();
        for(String words : w){
            m.put(words , m.getOrDefault(words , 0) + 1);
        }
        System.out.println(m);
        j.close();
    }
}