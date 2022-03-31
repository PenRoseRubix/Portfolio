import java.util.Scanner;
public class Main
{
    public static void main(String[] args) {
        Scanner Input = new Scanner(System.in);
        System.out.println(Quantos numeros primos você deseja?);
        int x = Input.nextInt();
        System.out.println(------------------------------------);
        int b = 1;
        int n = 0;
        while (b <= x) {
            int conta =1;
            int divi = 0;
            while(conta <= n){
              if(n % conta == 0) {
                  divi++;
              }
              conta++;
            }
            if (divi == 2) {
                System.out.println(n);
                b++;
            }
            n++;
        }

    }
}

