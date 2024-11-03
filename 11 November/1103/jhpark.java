import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());  
        int[] fruits = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            fruits[i] = Integer.parseInt(st.nextToken());
        }

        HashMap<Integer, Integer> fruitsCnt = new HashMap<>();
        int maxLength = 0; 
        int left = 0; 

        for (int right = 0; right < N; right++) {
            fruitsCnt.put(fruits[right], fruitsCnt.getOrDefault(fruits[right], 0) + 1);

            while (fruitsCnt.size() > 2) {
                fruitsCnt.put(fruits[left], fruitsCnt.get(fruits[left]) - 1);

                if (fruitsCnt.get(fruits[left]) == 0) {
                    fruitsCnt.remove(fruits[left]);
                }

                left++;
            }
            maxLength = Math.max(maxLength, right - left + 1);
        }
        System.out.println(maxLength);
    }
}