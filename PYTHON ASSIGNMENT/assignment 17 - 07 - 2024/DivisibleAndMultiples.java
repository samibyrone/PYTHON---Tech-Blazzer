public class DivisibleAndMultiples {

	public static void main(String... args){
		
		int counter = 0;
		for(int number = 4200; number >= 770; number --) {
			if(number % 7 == 0 && number % 5 != 0) System.out.println(number + "");
			counter ++;
		}
		System.out.printf("\n The total number of counts in-between is: " + counter );
	}

}