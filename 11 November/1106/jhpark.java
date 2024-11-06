import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

class Mirror implements Comparable<Mirror> {
    int x;
    int y;
    int dir; // 거울의 현재 방향
    int cnt; // 사용한 거울 개수

    public Mirror(int x, int y, int dir, int cnt) {
        this.x = x;
        this.y = y;
        this.dir = dir;
        this.cnt = cnt;
    }

    // 거울 개수를 기준으로 오름차순 정렬
    @Override
    public int compareTo(Mirror o) {
        return this.cnt - o.cnt;
    }
}

public class Main {

    static int[] dx = {-1, 0, 1, 0}; // 상좌 (북남)
    static int[] dy = {0, -1, 0, 1}; // 하우 (서동)

    static int N;
    static int sx, sy, ex, ey; // 문 좌표
    static char[][] map;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        map = new char[N][N];

        int idx = 0;
        for (int i = 0; i < N; i++) {
            String line = br.readLine();

            for (int j = 0; j < N; j++) {
                map[i][j] = line.charAt(j);

                // 문 좌표 저장
                if (map[i][j] == '#') {
                    if (idx == 0) {
                        sx = i;
                        sy = j;
                    } else {
                        ex = i;
                        ey = j;
                    }
                    idx++;
                }
            }
        }

        bfs();
    }

    public static void bfs() {
        // 거울의 최소 개수를 출력하는 것이므로 우선순위 큐를 사용
        PriorityQueue<Mirror> pq = new PriorityQueue<>();
        boolean[][][] visited = new boolean[N][N][4];

        // 처음 문 위치를 기준으로 4방향 모두 추가해줌
        for (int i = 0; i < 4; i++) {
            pq.add(new Mirror(sx, sy, i, 0));
        }

        while (!pq.isEmpty()) {
            Mirror cur = pq.poll();

            int x = cur.x;
            int y = cur.y;
            int dir = cur.dir;
            int cnt = cur.cnt;

            // 큐에서 꺼냈으니 방문처리 해줌
            visited[x][y][dir] = true;

            // 다른 쪽 문을 만난 경우 거울 개수 출력
            if (x == ex && y == ey) {
                System.out.println(cnt);
                return;
            }

            int nx = x + dx[dir];
            int ny = y + dy[dir];

            // 다음 좌표가 범위를 벗어나지 않음 && 방문하지 않은 곳 && 빛이 통과할 수 없는 곳이 아닌 경우
            if (nx >= 0 && nx < N && ny >= 0 && ny < N && !visited[nx][ny][dir] && map[nx][ny] != '*') {
                // 거울을 설치할 수 있는 곳인 경우
                if (map[nx][ny] == '!') {
                    // 거울이 특정 방향에서 45도 기울어진 대각선 방향으로 추가해야하므로
                    // '/'(시계 방향) 또는 '\'(반시계 방향) 모양으로 설치될 수 있음

                    // 시계 방향 (오른쪽)
                    int nDir = (dir + 3) % 4;
                    pq.add(new Mirror(nx, ny, nDir, cnt + 1));

                    // 반시계 방향 (왼쪽)
                    nDir = (dir + 1) % 4;
                    pq.add(new Mirror(nx, ny, nDir, cnt + 1));
                }

                // '!'인 곳에서 무조건 거울을 설치해야 하는 것은 아님
                // 거울을 설치 안 하는 경우도 추가해줌 -> 이전의 방향과 거울 개수를 그대로 추가
                pq.add(new Mirror(nx, ny, dir, cnt));
            }
        }

    }

}