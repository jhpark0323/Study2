import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));


        int N=Integer.parseInt(br.readLine());

        int[] dp=new int[N+2];
        int[] trace=new int[N+2];

        dp[1]=0;
        trace[1]=-1;


        for(int x=2;x<=N;x++){
            dp[x]=dp[x-1]+1;
            trace[x]=x-1;

            if(x%2==0 && dp[x]>dp[x/2]+1){
                dp[x]=dp[x/2]+1;
                trace[x]=x/2;
            }

            if(x%3==0 && dp[x]>dp[x/3]+1){
                dp[x]=dp[x/3]+1;
                trace[x]=x/3;
            }

        }

        int num=dp[N];

        bw.write(String.valueOf(num)+"\n");

        int index=N;

        for(int x=0;x<=num;x++){
            bw.write(String.valueOf(index)+" ");
            index=trace[index];
        }

        bw.flush();
        bw.close();
        br.close();
    }


}