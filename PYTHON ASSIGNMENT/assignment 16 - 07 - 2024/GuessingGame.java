import java.util.Scanner;
import java.util.Random;

public class GuessingGame {

	public static void main(String... args) {
	
		Scanner input = new Scanner(System.in);
		Random rand = new Random();

		System.out.println("Welcome You Warmly To Your Guessing Game, All You Have To Do Is Guess The Number Right And You Become Our Champion!!!!");
		System.out.println();

		int computer = rand.nextInt(10);
		int gamer = 0;
		int flag = 1;
		int randomNumber = 0;
		int counter = 0;

		while (flag == 1) {	
			System.out.print("To continue, press 1 to continue or -1 to quit! ");
			gamer = input.nextInt();
			System.out.println();

			switch (gamer ) {
				case 1:
					System.out.println(" Guess a number between 1 and 10: ");
					computer = input.nextInt();
						counter = counter + computer;

					if (computer < randomNumber) System.out.println(" You Guess Too Low, Kindly Try Again!!! ");

					if (computer > randomNumber) System.out.println(" You Guessed Number is Too High, Kindly Try Again!!! ");

					if (computer == randomNumber) System.out.println(" Congratulations!!!, you guessed right..... ");
						break;
						
				case 2:
					System.out.println(" Invalid input, Please try again later !!!!! ");					
						break;

				default:
					System.out.println(" Thank you for Trying out This Game, Would Love To See You Again!!!!! ");
			}
		}

		System.out.print("To continue, press 1 to continue or -1 to quit! ");
		if (flag == -1) System.out.println(" You played the Game " + counter + " times. ");
			flag = input.nextInt();
	}

}