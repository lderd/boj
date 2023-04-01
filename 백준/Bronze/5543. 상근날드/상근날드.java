import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[]args) throws java.io.IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int burger = 2001;
        for (int i = 0; i < 3; i++) {
            int tmp = Integer.parseInt(br.readLine());
            if (tmp < burger) {
                burger = tmp;
            }
        }
        int drink = 2001;
        for (int i = 0; i < 2; i++) {
            int tmp = Integer.parseInt(br.readLine());
            if (tmp < drink) {
                drink = tmp;
            }
        }
        int answer = burger + drink - 50;
        System.out.println(answer);
    }
}