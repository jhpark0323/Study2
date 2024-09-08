import java.io.*;
import java.util.*;

//TIP 코드를 <b>실행</b>하려면 <shortcut actionId="Run"/>을(를) 누르거나
// 에디터 여백에 있는 <icon src="AllIcons.Actions.Execute"/> 아이콘을 클릭하세요.
// 1941 소문난 칠공주
public class Main {
    static char arr[][] = new char[5][5];
    static int row[] = new int[25];
    static int col[] = new int[25];
    static int di[] = {1, -1, 0, 0};
    static int dj[] = {0, 0, 1, -1};
    static int ans = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int i = 0; i < 5; i++) {
            arr[i] = br.readLine().toCharArray();
        }
//        System.out.println(Arrays.deepToString(arr));

        // (0,0) 부터 (4, 4)까지를 0~24까지로 대입
        for (int i = 0; i < 25; i++) {
            row[i] = i / 5;
            col[i] = i % 5;
        }

        back(new int[7], 7, 0, 0, 0);
        System.out.println(ans);

    }
    static void back(int[] ls, int left, int depth, int idx, int dsCnt) {
        if (left == 0) {
            // 다솜파가 4명이상일시 bfs로 옆자리인지 확인
            if (dsCnt >= 4) {
                bfs(ls);
            }
            return;
        }

        if (depth == 25) {
            return;
        }

        // idx값을 선택 (조합)
        ls[idx] = depth;
        // 다솜파 확인 후 선택
        if (arr[row[depth]][col[depth]] == 'S') {
            back(ls, left - 1, depth + 1, idx + 1, dsCnt + 1);
        } else {
            back(ls, left - 1, depth + 1, idx + 1, dsCnt);
        }
        // 선택 X
        back(ls, left, depth + 1, idx, dsCnt);
    }
    public static void bfs(int[] ls) {
//        System.out.println(Arrays.toString(ls));
        Queue<Integer> q = new LinkedList<>();
        boolean[] visited = new boolean[7];
        visited[0] = true;
        q.add(ls[0]);
        int cnt = 0;
        while (!q.isEmpty()) {
            int now = q.poll();

            for (int dij = 0; dij < 4; dij++) {
                for (int next = 1; next < 7; next++) {
                    // 방문하지 않았고 행과 열이 같은게 있으면
                    if (!visited[next] && row[now] + di[dij] == row[ls[next]] && col[now] + dj[dij] == col[ls[next]]) {
                        visited[next] = true;
                        q.add(ls[next]);
                        cnt++;
                    }
                }
            }
        }

        if (cnt == 6) {
            ans++;
        }


    }
}