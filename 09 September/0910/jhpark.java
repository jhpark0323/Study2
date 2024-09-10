import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int dp[] = new int[n];

        for (int i = 0; i < n; i++) {
            dp[i] = 1;
        }

        int ans = 1;
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                // 앞의 상자가 현재보다 작으면
                if (arr[j] < arr[i]) {
                    dp[i] = Math.max(dp[i], dp[j]+1);
                }
                ans = Math.max(ans, dp[i]);
            }
        }

//        System.out.println(Arrays.toString(dp));
        System.out.println(ans);
    }
}