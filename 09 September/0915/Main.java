import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int l;
    static int r;
    static int[][] arr;
    static int[] di = {0, 0, -1, 1};
    static int[] dj = {1, -1, 0, 0};
    static boolean check = true;
    static boolean changeCheck = false;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        l = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());
        arr = new int[n][n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int ans = 0;

        while (check) {
            boolean[][] visited = new boolean[n][n];
            boolean[][] dayVisited = new boolean[n][n];
            check = false;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (!visited[i][j]) {
                        changeCheck = false;
                        int newNum = bfs(arr, visited, i, j, dayVisited);
                        if (changeCheck) {
                            change(visited, newNum, dayVisited);
                        }
//                        for (int k = 0; k < n; k++) {
//                            System.out.println(Arrays.toString(arr[k]));
//                        }
//                        for (int k = 0; k < n; k++) {
//                            System.out.println(Arrays.toString(visited[k]));
//                        }
                    }
                }
            }
            if (check) {
                ans++;
//                System.out.println("하루가 지남");
//                System.out.println();
            }
        }

        System.out.println(ans);
    }

    public static void change(boolean[][] visited, int num, boolean[][] dayVisited) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (visited[i][j] && dayVisited[i][j]) {
                    arr[i][j] = num;
                    dayVisited[i][j] = false;
                }
            }
        }
    }

    static class Country {
        int row, col;

        public Country(int row, int col) {
            this.row = row;
            this.col = col;
        }
    }

    public static int bfs(int[][] arr, boolean[][] visited, int row, int col, boolean[][] dayVisited) {
        visited[row][col] = true;
        dayVisited[row][col] = true;
        Queue<Country> q = new LinkedList<>();
        q.add(new Country(row, col));
        int num = arr[row][col];
        int count = 1;

        while (!q.isEmpty()) {
            Country new_l = q.poll();
            int cur_r = new_l.row;
            int cur_c = new_l.col;
            for (int dij = 0; dij < 4; dij++) {
                int next_r = cur_r + di[dij];
                int next_c = cur_c + dj[dij];

                if (0 <= next_r && next_r < n && 0 <= next_c && next_c < n && !visited[next_r][next_c] && l <= Math.abs(arr[next_r][next_c] - arr[cur_r][cur_c]) && Math.abs(arr[next_r][next_c] - arr[cur_r][cur_c]) <= r) {
                    visited[next_r][next_c] = true;
                    dayVisited[next_r][next_c] = true;
                    q.add(new Country(next_r, next_c));
                    num += arr[next_r][next_c];
                    check = true;
                    count++;
                    changeCheck = true;
                }

            }
        }
        if (count == 1) {
            visited[row][col] = false;
            dayVisited[row][col] = true;
        }
        return num / count;
    }
}