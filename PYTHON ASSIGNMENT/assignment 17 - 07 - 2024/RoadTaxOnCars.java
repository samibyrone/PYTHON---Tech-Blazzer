import java.util.Scanner;

public class RoadTaxOnCars {

	public static void main(String... args) {

		Scanner input = new Scanner(System.in);
		
		//System.out.println("");

		int taxRange = 0;

		System.out.println(" Enter the total cost for the car: ");
		int costOfCar = input.nextInt();

		if(costOfCar <= 1000000) {
			taxRange = (int)(costOfCar * (10/100));
			System.out.print(taxRange);
		}
		else if(costOfCar >= 100000 && costOfCar <= 3000000) {
			taxRange = (costOfCar * (15/100));
		}
		else if(costOfCar >= 300000 && costOfCar <= 5000000) {
			taxRange = (costOfCar * (20/100));
		}
		else if(costOfCar >= 5000000) {
			taxRange = (costOfCar * (25/100));
		}

		System.out.println(" Total cost of car is: %d including tax together is: %d%n ", costOfCar,taxRange );
		
		else if(costOfCar != costOfCar) { 
			System.out.println(" Invalid, Please Try Again... ");
		}

	}

}