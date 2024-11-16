import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int Q = Integer.parseInt(st.nextToken());
		StringBuilder sb = new StringBuilder();
		List<Integer> list = new ArrayList<Integer>();
		
		//곡은 1번부터 N번까지 있기에 1부터 N까지 반복하는 반복문
		for(int i = 1; i <= N; i++) {
			int time = Integer.parseInt(br.readLine());
			//1번의 시간부터 순서대로 입력되기 때문에 시간만큼 반복하며 list에 순서대로 곡 번호를 저장한다.
			for(int j = 0; j < time; j++) {
				list.add(i);
			}
		}
		
		//입력된 질문에 해당하는 인덱스에 저장된 값을 sb에 저장
		for(int i = 0; i < Q; i++) {
			int num = Integer.parseInt(br.readLine());
			sb.append(list.get(num)).append("\n");
		}
		System.out.println(sb);
	}

}