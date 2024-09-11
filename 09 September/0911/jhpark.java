import java.util.*;
import java.io.*;

// 백준 15655 N과 M(6)
public class Main {
    static int n;
    static int m;
    static int[] ls;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        ls = new int[n];
        for (int i = 0; i < n; i++) {
            ls[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(ls);
//        System.out.println(Arrays.toString(ls));
        List<Integer> new_ls = new ArrayList<>();
        back(new_ls, 0);

    }

    public static void back(List<Integer> new_ls, int depth) {
        if (depth == m) {
            for (int i = 0; i < depth; i++) {
                System.out.print(new_ls.get(i) + " ");
            }
            System.out.println();
            return;
        }

        for (int i = 0; i < n; i++) {
            if (new_ls.isEmpty()) {
                new_ls.add(ls[i]);
                back(new_ls, depth + 1);
                new_ls.remove(new_ls.size() - 1);
            } else if (ls[i] > new_ls.get(depth-1)) {
                new_ls.add(ls[i]);
                back(new_ls, depth + 1);
                new_ls.remove(new_ls.size() - 1);
            }
        }

    }

}