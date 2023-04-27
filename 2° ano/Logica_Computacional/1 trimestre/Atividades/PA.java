import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		
		int an;
		int a1;
		int r;
		int n;
		
		System.out.println(Deseja descobrir qual variavel?);
		System.out.println(1 = an);
		System.out.println(2 = a1);
		System.out.println(3 = r);
		System.out.println(4 = n);
		int question = s.nextInt();
		System.out.println();
		
		switch (question){
		    case 1:
		        System.out.print(a1 = );
		        a1 = s.nextInt();
		        System.out.print(r = );
		        r = s.nextInt();
		        System.out.print(n = );
		        n = s.nextInt();
		        System.out.println(=====);
		        an = a1 + (n-1) *r;
		        System.out.println(an =  + an);
		        break;
		        
		    case 2:
		        System.out.print(an = );
		        an = s.nextInt();
		        System.out.print(r = );
		        r = s.nextInt();
		        System.out.print(n = );
		        n = s.nextInt();
		        System.out.println(=====);
		        a1 = an - (n-1) *r;
		        System.out.println(a1 =  +a1);
		        break;
		        
		    case 3:
		        System.out.print(an = );
		        an = s.nextInt();
                System.out.print(a1 = );
		        a1 = s.nextInt();
		        System.out.print(n = );
		        n = s.nextInt();
		        System.out.println(=====);
		        r = (an - a1)/(n - 1);
		        System.out.println(r =  + r);
		        break;
		        
		    case 4:
		        System.out.print(an = );
		        an = s.nextInt();
                System.out.print(a1 = );
		        a1 = s.nextInt();
		        System.out.print(r = );
		        r = s.nextInt();
		        System.out.println(=====);
		        n = ((an - a1)/r)+1;
		        System.out.println(n =  + n);
		        break;
		  
		    default :
		        System.out.println(Ai tu que me ferrar, amigo.);
		}
		
	}
}

