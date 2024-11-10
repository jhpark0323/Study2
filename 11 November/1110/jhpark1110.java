import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

// 벽 부수고 이동하기 3, 16933
public class Main {
    static int n;
    static int m;
    static int k;
    static int[][] arr;
    static int[] di = {1, -1, 0, 0};
    static int[] dj = {0, 0, 1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        arr = new int[n][m];

        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < m; j++) {
                arr[i][j] = Character.getNumericValue(line.charAt(j));
            }
        }

        bfs();

    }

    static class Node {
        int row, col, cnt, wall;
        boolean afternoon;
        Node(int row, int col, int cnt, int wall, boolean afternoon) {
            this.row = row;
            this.col = col;
            this.cnt = cnt;
            this.wall = wall;
            this.afternoon = afternoon;
        }
    }

    static void bfs() {
        boolean[][][] visited = new boolean[n][m][k+1];
        Queue<Node> q = new LinkedList<>();
        q.offer(new Node(0, 0, 1, k, true));
        visited[0][0][k] = true;
        while (!q.isEmpty()) {
            Node cur = q.poll();

            if (cur.row == n-1 && cur.col == m-1) {
                System.out.println(cur.cnt);
                return;
            }

            for (int dij = 0; dij < 4; dij++) {
                int newRow = cur.row + di[dij];
                int newCol = cur.col + dj[dij];

                if (newRow < 0 || newRow >= n || newCol < 0 || newCol >= m) {
                    continue;
                }

                boolean reverse = !cur.afternoon;

                // 갈 수 있으면
                if (arr[newRow][newCol] == 0) {
                    if (!visited[newRow][newCol][cur.wall]) {
                        visited[newRow][newCol][cur.wall] = true;
                        q.offer(new Node(newRow, newCol, cur.cnt+1, cur.wall, reverse));
                    }
                }
                // 벽이면
                else {
                    // 벽 부술 수 있고 낮이면
                    if (cur.wall > 0 && cur.afternoon) {
                        if (!visited[newRow][newCol][cur.wall-1]) {
                            visited[newRow][newCol][cur.wall-1] = true;
                            q.offer(new Node(newRow, newCol, cur.cnt+1, cur.wall-1, reverse));
                        }
                    }
                    // 벽 부술 수 있는데 밤이면
                    else if (cur.wall > 0 && !cur.afternoon) {
                        q.offer(new Node(cur.row, cur.col, cur.cnt+1, cur.wall, reverse));
                    }
                }

            }

        }
        System.out.println(-1);
    }


}
