import java.util.*;
import java.io.*;

// 백준 1759 암호 만들기
// https://www.acmicpc.net/problem/1759
public class Main {
    static char[] vowels = {'a', 'e', 'i', 'o', 'u'};
    static int l;
    static int c;
    static char[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        l = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        arr = new char[c];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < arr.length; i++) {
            arr[i] = st.nextToken().charAt(0);
        }
        Arrays.sort(arr);

//         System.out.println(Arrays.toString(arr));

        StringBuilder sb = new StringBuilder();
        back(sb, 0, 0, 0, 0);
    }

    public static void back(StringBuilder ans,int vowel, int consonoant, int depth, int start) {
        if (depth == l) {
            if (vowel >= 1 && consonoant >= 2) {
                System.out.println(ans);
            }
            return;
        }

        for (int i = start; i < c; i++) {
            ans.append(arr[i]);
            // 모음 자음 확인
            boolean found = false;
            for (int j = 0; j < 5; j++) {
                if (arr[i] == vowels[j]) {
                    found = true;
                    break;
                }
            }
            // 백트
            if (found) {
                back(ans, vowel + 1, consonoant, depth + 1, i+1);
            } else {
                back(ans, vowel, consonoant+1, depth+1, i+1);
            }

            ans.deleteCharAt(ans.length() - 1);

        }

    }

}