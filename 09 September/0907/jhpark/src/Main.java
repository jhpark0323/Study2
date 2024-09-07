import java.io.*;
import java.util.*;

//TIP 코드를 <b>실행</b>하려면 <shortcut actionId="Run"/>을(를) 누르거나
// 에디터 여백에 있는 <icon src="AllIcons.Actions.Execute"/> 아이콘을 클릭하세요.
// 1941 소문난 칠공주
public class Main {
    static char arr[][] = new char[5][5];
    static int row[] = new int[25];
    static int col[] = new int[25];
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

    }
    static void back(int[] ls, int left, int depth) {
        if (left == 0) {
            return;
        }

        if (depth == 25) {
            return;
        }



    }
}