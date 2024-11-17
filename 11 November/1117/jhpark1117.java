import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		//현재시간과 시작시간을 저장 할 변수
		int now = 0;
		int start = 0;
		
		StringTokenizer st = new StringTokenizer(br.readLine(), ":");
		int h = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int s = Integer.parseInt(st.nextToken());
		
		now = (h * 3600) + (m * 60) + s;
		
		st = new StringTokenizer(br.readLine(), ":");
		h = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		s = Integer.parseInt(st.nextToken());
		
		start = (h * 3600) + (m * 60) + s;
		
		//앞으로 남은 시간을 저장 할 변수
		int time = 0;
		
		if(start > now) {
			time = start - now;
		}else {
			time = (24 * 3600) - (now - start);
		}
		
		System.out.format("%02d:%02d:%02d", (time / 3600), ((time / 60) % 60), (time % 60));
	}

}