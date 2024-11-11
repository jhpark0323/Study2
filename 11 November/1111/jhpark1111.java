import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.stream.Stream;
class Main
{
	public static void main (String[] args) throws IOException
	{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    int idx = 0;
	    while(true){
	        int[] num = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
	        if(num[0] == 0 && num[1] == 0){
	            break;
	        }
            boolean chk = false;
	        while(true){
    	        String str = br.readLine();
    	        if(str.equals("# 0")){
    	            break;
    	        }
    	        if(!chk){
                    String[] str2 = str.split(" ");
    	            if(str2[0].equals("E")){
    	                num[1] -= Integer.parseInt(str2[1]);
    	            }else if(str2[0].equals("F")){
    	                num[1] += Integer.parseInt(str2[1]);   
    	            }    
                }
    	        if(num[1] <= 0){
    	            chk = true;
    	        }
	        }
	        idx++;
	        if(num[1] <= 0){
	            System.out.println(idx + " RIP");
			    continue;
	        }
	        if ((num[0] / 2) < num[1] && num[0] * 2 > num[1]) {
				System.out.println(idx + " :-)");
				continue;
			}
			System.out.println(idx + " :-(");
	    }
	}
}