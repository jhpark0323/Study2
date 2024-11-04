import java.util.Scanner;

public class Main {
	
	private static int Rev(int num) {
       int result = 0;
            while (num > 0) {
            result = result * 10 + num % 10;
            num /= 10;
        }

       return result; 
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int x = sc.nextInt();
		int y = sc.nextInt();

        sc.close();
	
        int result = Rev(Rev(x) + Rev(y));
        System.out.println(result);
	}
}