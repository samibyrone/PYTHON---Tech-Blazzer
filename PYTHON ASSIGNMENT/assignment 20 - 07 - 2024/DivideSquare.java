import java.util.Scanner;
import java.lang.Math; 

public class DivideSquare {

	public static void main(String... args) {

		Scanner input = new Scanner(System.in);

		System.out.println(" Enter your number: ");
		int number = input.nextInt();

		if (number % 5 == 0) {
			System.out.println(number);	
		} else
			if (number % 5 != 0) {
				System.out.println(Math.sqrt(number));
		}
 
	}

}