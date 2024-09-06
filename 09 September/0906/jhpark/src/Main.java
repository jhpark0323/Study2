import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int testCase = 1; testCase <= T; testCase++) {
            int n = Integer.parseInt(br.readLine());
            int[][] arr = new int[2][n];
            for (int i = 0; i < 2; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    arr[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            int[][] dp = new int[2][n];
            dp[0][0] = arr[0][0];
            dp[1][0] = arr[1][0];

            if (n >= 2) {
                dp[0][1] = arr[1][0] + arr[0][1];
                dp[1][1] = arr[1][1] + arr[0][0];
            }


            for (int j = 2; j < n; j++) {
                for (int i = 0; i < 2; i++) {
                    if (i == 0) {
                        dp[i][j] = Math.max(dp[1][j - 2], dp[1][j - 1]) + arr[i][j];
                    } else {
                        dp[i][j] = Math.max(dp[0][j-2], dp[0][j - 1]) + arr[i][j];
                    }
                }
            }

//            System.out.println(Arrays.deepToString(dp));

            System.out.println(Math.max(dp[0][n-1], dp[1][n-1]));


        }
    }
}