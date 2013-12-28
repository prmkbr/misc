/**
 * Prints the numbers from 1 to 100. But for multiples of three print 'Fizz'
 * instead of the number and for the multiples of five print 'Buzz'.
 * For numbers which are multiples of both three and five print 'FizzBuzz'.
 */
public class FizzBuzz
{
    public static void main(String... args)
    {
        for (int i = 1; i <= 100; i++) {
            boolean factor3 = (i % 3 == 0), factor5 = (i % 5 == 0);
            if (factor3 && factor5) {
                System.out.println("FizzBuzz");
            }
            else if (factor3) {
                System.out.println("Fizz");
            }
            else if (factor5) {
                System.out.println("Buzz");
            }
            else {
                System.out.println(i);
            }
        }
    }
}
