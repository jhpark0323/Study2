import java.util.*;
import java.io.*;

// 주난의 난_14497
public class Main {
    static int n, m, x1, y1, x2, y2;
    static char[][] arr;
    static int[] di = {1, -1, 0, 0};
    static int[] dj = {0, 0, 1, -1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        x1 = Integer.parseInt(st.nextToken());
        y1 = Integer.parseInt(st.nextToken());
        x2 = Integer.parseInt(st.nextToken());
        y2 = Integer.parseInt(st.nextToken());
        arr = new char[n][m];
        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < m; j++) {
                arr[i][j] = line.charAt(j);
            }
        }
//        System.out.println(Arrays.deepToString(arr));

        int ans = bfs();
        System.out.println(ans);
    }

    static class Node {
        int row, col, cnt;

        Node(int row, int col, int cnt) {
            this.row = row;
            this.col = col;
            this.cnt = cnt;
        }
    }

    static int bfs() {
        boolean[][] visited = new boolean[n][m];
        visited[x1-1][y1-1] = true;
        ArrayDeque<Node> q = new ArrayDeque<>();
        q.offer(new Node(x1-1, y1-1, 0));
        while (!q.isEmpty()) {
            Node cur = q.poll();
            int curRow = cur.row;
            int curCol = cur.col;
            int curCnt = cur.cnt;

            if (arr[curRow][curCol] == '#') {
                return curCnt;
            }

            for (int dij = 0; dij < 4; dij++) {
                int nextRow = curRow + di[dij];
                int nextCol = curCol + dj[dij];

                if (nextRow < 0 || nextRow >= n || nextCol < 0 || nextCol >= m) {
                    continue;
                }

                if (visited[nextRow][nextCol]) {
                    continue;
                }

                if (arr[nextRow][nextCol] == '0') {
                    q.offerFirst(new Node(nextRow, nextCol, curCnt));
                } else {
                    q.offerLast(new Node(nextRow, nextCol, curCnt+1));
                }

                visited[nextRow][nextCol] = true;
            }

        }
        return -1;
    }
}