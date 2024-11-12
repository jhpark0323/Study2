import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[] A = new int[n];
        int[] B = new int[n];
        int[] C = new int[n];
        int[] D = new int[n];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            A[i] = Integer.parseInt(st.nextToken());
            B[i] = Integer.parseInt(st.nextToken());
            C[i] = Integer.parseInt(st.nextToken());
            D[i] = Integer.parseInt(st.nextToken());
        }

        // AB와 CD 배열 생성 (크기는 n * n)
        int[] AB = new int[n * n];
        int[] CD = new int[n * n];

        // A와 B의 모든 합을 AB 배열에 저장
        int idx = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                AB[idx++] = A[i] + B[j];
            }
        }

        // C와 D의 모든 합을 CD 배열에 저장
        idx = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                CD[idx++] = C[i] + D[j];
            }
        }

        // AB와 CD를 정렬
        Arrays.sort(AB);
        Arrays.sort(CD);

        long ans = 0;
        int left = 0, right = CD.length - 1;

        // AB[left] + CD[right] == 0인 경우를 찾음
        while (left < AB.length && right >= 0) {
            int sum = AB[left] + CD[right];
            if (sum == 0) {
                long leftCount = 0, rightCount = 0;

                // 중복된 값의 개수 셈 (AB 배열)
                int leftVal = AB[left];
                while (left < AB.length && AB[left] == leftVal) {
                    leftCount++;
                    left++;
                }

                // 중복된 값의 개수 셈 (CD 배열)
                int rightVal = CD[right];
                while (right >= 0 && CD[right] == rightVal) {
                    rightCount++;
                    right--;
                }

                ans += leftCount * rightCount; // 경우의 수 추가
            } else if (sum < 0) {
                left++;
            } else {
                right--;
            }
        }

        System.out.println(ans);
    }
}
