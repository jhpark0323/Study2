import java.util.Scanner;
 
public class Main {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		int N = in.nextInt();
		in.close();
        
		
        
		while(N > 0) {
			System.out.println(N);
			N--;
		}
	}
}