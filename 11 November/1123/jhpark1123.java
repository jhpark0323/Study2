import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		
		for(int i = 0; i < T; i++) {
			//테스트 케이스마다 한 줄을 비워서 입력받기 때문에 빈 줄을 받을 변수 L
			String L = br.readLine();
			StringTokenizer st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			//세준 세비의 제일 강한 병사의 힘을 저장할 변수
			int Smax = 0;
			int Bmax = 0;
			
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j < N; j++) {
				int S = Integer.parseInt(st.nextToken());
				
				if(Smax < S) Smax = S;
			}
			
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j < M; j++) {
				int B = Integer.parseInt(st.nextToken());
				
				if(Bmax < B) Bmax = B;
			}
			
			//힘이 더 쌘쪽이 이기고, 같으면 세준이가 이긴다.
			if(Smax > Bmax) System.out.println("S");
			else if(Bmax > Smax) System.out.println("B");
			else System.out.println("S");
		}
	}

}