import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); //scanner 와 유사

        int[] alpha = new int[26]; //알파벳 개수 배열
        int max = 0;
        String input; //EOF 처리를 위해 받을 문자열;; 이거땜에 엄청 헤맴
        String str = "";


        //인텔리제이에서는 입력의 끝을 모르기 때문에 임의로 엔터 한 번 더 치면 프로그램 종료되게끔 while문에 조건 한 개를 더 넣었다 [&& !input.isEmpty()]
        //근데 백준에서는 또 이렇게 하면 인식 안돼서 빼야됨 아 ㅋㅋ
        //인텔리제이에서 실행되게 만드는 조건문은 while ((input = br.readLine()) != null && !input.isEmpty())
        while ((input = br.readLine()) != null) {
            str += input;
        }

        //알파벳 갯수 저장 및 가장 많이 나온 알파벳의 횟수 저장
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) != ' ') {
                alpha[str.charAt(i) - 'a']++;

                if (alpha[str.charAt(i) - 'a'] > max) {
                    max = alpha[str.charAt(i) - 'a'];
                }
            }
        }

        for (int i = 0; i < 26; i++) {
            if (max == alpha[i]) {
                System.out.print((char) (i + 'a'));
            }
        }


    }
}
출처: https://dawning-record.tistory.com/28 [새벽의 기록:티스토리]