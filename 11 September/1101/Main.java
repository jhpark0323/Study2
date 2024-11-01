import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int[][] arr;
    static int[][] dp;
    static int[] di = {1, -1, 0, 0};
    static int[] dj = {0, 0, 1, -1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        arr = new int[n][n];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

//        System.out.println(Arrays.deepToString(arr));
        dp = new int[n][n];

        int answer = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                answer = Math.max(answer, dfs(i, j));
//                System.out.println(i + "," + j);
//                System.out.println(Arrays.deepToString(dp));
            }
        }

        System.out.println(answer);
//        System.out.println(Arrays.deepToString(dp));
    }
    static int dfs(int row, int col) {
        if (dp[row][col] != 0) return dp[row][col];

        dp[row][col] = 1;

        int next_row, next_col;
        for (int dij = 0; dij < 4; dij++) {
            next_row = row + di[dij];
            next_col = col + dj[dij];
            if (next_row < 0 || next_col < 0 || next_row >= n || next_col >= n) {
                continue;
            }
            if (arr[next_row][next_col] > arr[row][col]) {
                dp[row][col] = Math.max(dp[row][col], dfs(next_row, next_col) + 1);
            }
        }
        return dp[row][col];
    }
}