#include <iostream>

using std::cout;
using std::endl;

/**
 * Prints the numbers from 1 to 100. But for multiples of three print 'Fizz'
 * instead of the number and for the multiples of five print 'Buzz'.
 * For numbers which are multiples of both three and five print 'FizzBuzz'.
 */
int main()
{
    for (int i = 1; i <= 100; i++) {
        if (i % 3 == 0) {
            cout << ((i % 5 == 0) ? "FizzBuzz" : "Fizz") << endl;
        }
        else if (i % 5 == 0) {
            cout << "Buzz" << endl;
        }
        else {
            cout << i << endl;
        }
    }
}
