import java.util.Scanner;

public class Discount {

	public static void main(String... args) {

		Scanner input = new Scanner(System.in);

		int product = 0;
		double discount = 15 / 100;

		System.out.print(" Enter your Price: ");
		int price = input.nextInt();

		product = price *= discount;
		
		System.out.printf(" Your total price with discount is: %d", product);
	}

}