import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		//공의 위치
		int num = 1;
		
		for(int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int X =Integer.parseInt(st.nextToken());
			int Y =Integer.parseInt(st.nextToken());
			//공의 위치가 바뀔 경우 공의 위치를 재 저장
			if(X == num) {
				num = Y;
			}else if(Y == num){
				num = X;
			}
		}
		
		System.out.println(num);
	}

}