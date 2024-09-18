import java.io.*;
import java.util.*;

public class Main {
    static int k, size;
    static int[] arr;
    static int ans = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        k = Integer.parseInt(br.readLine());
        size = (int) Math.pow(2, k+1) - 1;
        arr = new int[size + 1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 2; i < size + 1; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
//        System.out.println(Arrays.toString(arr));
        func(1);
        System.out.println(ans);

    }

    public static int func(int node) {
        if (2 * node >= size) {
            ans += arr[node];
            return arr[node];
        }

        int left = func(2 * node);
        int right = func(2 * node + 1);

        ans += arr[node] + Math.abs(left - right);
        return arr[node] + Math.max(left, right);
    }
}