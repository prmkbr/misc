#include <iostream>
#include <cstdlib>
#include <ctime>

using std::cout;
using std::endl;

unsigned long recursion(int n)
{
    switch(n) {
        case 0: return 0;
        case 1: return 1;
        default: return recursion(n - 1) + recursion(n - 2);
    }
}

unsigned long tail_recursion(int n, unsigned long x = 0, unsigned long y = 1)
{
    if (n == 0) {
        return x;
    }
    return tail_recursion(n - 1, y, x + y);
}

unsigned long iteration(int n)
{
    if (n == 0) {
        return 0;
    }
    if (n == 1) {
        return 1;
    }
    unsigned long x = 0, y = 1;
    while (n-- > 1) {
        y = y + x;
        x = y - x;
    }
    return y;
}

int main(int argc, char *argv[])
{
    int n = -1;
    if (argc == 2) {
        n = atoi(argv[1]);
    }
    if (n < 0) {
        srand(time(NULL));
        n = rand() % 50;
    }

    cout << n << endl;
    cout << "recursion:      " << recursion(n) << endl;
    cout << "tail-recursion: " << tail_recursion(n) << endl;
    cout << "iteration:      " << iteration(n) << endl;
}
