import java.util.*;
import java.io.*;

// 백준 3055 탈출
public class Main {
    static int r, c;
    static char[][] arr;
    static int[] di = {1, -1, 0, 0};
    static int[] dj = {0, 0, 1, -1};
    static List<RowCol> list = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        arr = new char[r][c];
        for (int i = 0; i < r; i++) {
            st = new StringTokenizer(br.readLine());
            arr[i] = st.nextToken().toCharArray();
        }
//        System.out.println(Arrays.deepToString(arr));

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (arr[i][j] == 'S') {
                    list.add(new RowCol(i, j, 'S', 0));
                } else if (arr[i][j] == '*') {
                    list.add(new RowCol(i, j, '*', 0));
                }
            }
        }

//        System.out.println(list);

        int ans = bfs();
        if (ans == -1) {
            System.out.println("KAKTUS");
        } else {
            System.out.println(ans);
        }

    }

    public static class RowCol {
        int row, col, ans;
        char type;
        RowCol(int row, int col, char type, int ans) {
            this.row = row;
            this.col = col;
            this.type = type;
            this.ans = ans;
        }
        public String toString() {
            return row + "," + col + "," + type;
        }
    }

    public static int bfs() {
        boolean[][] visited = new boolean[r][c];
        Queue<RowCol> q = new LinkedList<>();
        // *부터 Queue에 넣음
        for (int i = 0; i < list.size(); i++) {
            if (list.get(i).type == '*') {
                q.add(list.get(i));
                visited[list.get(i).row][list.get(i).col] = true;
            }
        }
        // 시작위치 담기
        for (int i = 0; i < list.size(); i++) {
            if (list.get(i).type == 'S') {
                q.add(list.get(i));
                visited[list.get(i).row][list.get(i).col] = true;
            }
        }

        while (!q.isEmpty()) {
            RowCol cur = q.poll();
            int row = cur.row;
            int col = cur.col;
            char type = cur.type;
            int ans = cur.ans;

            for (int dij = 0; dij < 4; dij++) {
                int next_r = row + di[dij];
                int next_c = col + dj[dij];
                if (next_r >= 0 && next_r < r && next_c >= 0 && next_c < c && !visited[next_r][next_c]) {
                    // *이 갈 수 있는 곳이면
                    if (type == '*' && arr[next_r][next_c] == '.') {
                        visited[next_r][next_c] = true;
                        q.add(new RowCol(next_r, next_c, type, ans));
                        arr[next_r][next_c] = type;
                    } else if (type == 'S' && arr[next_r][next_c] == 'D') {
                        return ans+1;

                    } else if (type == 'S' && arr[next_r][next_c] == '.') { // D가 갈 수 있는 곳이면
                        visited[next_r][next_c] = true;
                        q.add(new RowCol(next_r, next_c, type, ans+1));
                    }
                }
            }
        }
        return -1;
    }
}