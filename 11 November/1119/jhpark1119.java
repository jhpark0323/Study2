import java.util.*;
import java.io.*;

// 매직 포션_12913
public class Main {
    static int n;
    static int k;
    static int[][] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        arr = new int[n][n];
        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < n; j++) {
                arr[i][j] = line.charAt(j) - '0';
            }
        }
//        System.out.println(Arrays.deepToString(arr));

        dijkstra();
//        System.out.println(Arrays.toString(path));
//        System.out.println(path[1]);

    }

    static class Node {
        int idx, magic;
        float weight;

        Node(int idx, float weight, int magic) {
            this.idx = idx;
            this.weight = weight;
            this.magic = magic;
        }
    }

    static void dijkstra() {
        // path 배열 초기화
        float[][] path = new float[n][k + 1];
        for (int i = 0; i < n; i++) {
            Arrays.fill(path[i], Float.MAX_VALUE);
        }
        path[0][k] = 0; // 시작 노드, 포션 사용 가능 횟수 k

        PriorityQueue<Node> pq = new PriorityQueue<>((o1, o2) -> Float.compare(o1.weight, o2.weight));
        pq.offer(new Node(0, 0, k)); // 시작 노드 삽입

        while (!pq.isEmpty()) {
            Node cur = pq.poll();
            int curIdx = cur.idx;
            float curWeight = cur.weight;
            int curMagic = cur.magic;

            // 현재 상태에서 최단 경로가 이미 갱신된 경우 무시
            if (curWeight > path[curIdx][curMagic]) {
                continue;
            }

            // 인접 노드 탐색
            for (int nextIdx = 0; nextIdx < n; nextIdx++) {
                if (curIdx == nextIdx) continue;

                // 포션 사용하지 않고 이동
                if (curWeight + arr[curIdx][nextIdx] < path[nextIdx][curMagic]) {
                    path[nextIdx][curMagic] = curWeight + arr[curIdx][nextIdx];
                    pq.offer(new Node(nextIdx, path[nextIdx][curMagic], curMagic));
                }

                // 포션 사용하고 이동
                if (curMagic > 0 && curWeight + (float) arr[curIdx][nextIdx] / 2 < path[nextIdx][curMagic - 1]) {
                    path[nextIdx][curMagic - 1] = curWeight + (float) arr[curIdx][nextIdx] / 2;
                    pq.offer(new Node(nextIdx, path[nextIdx][curMagic - 1], curMagic - 1));
                }
            }
        }

        // 결과 출력: 최종 목적지까지의 최소 비용
        float result = Float.MAX_VALUE;
        for (int i = 0; i <= k; i++) {
            result = Math.min(result, path[1][i]);
        }
        System.out.println(result);
    }

}
