#include <fstream>
#include <iostream>

using namespace std;

int main(int argc, char* argv[])
{
    ifstream ifp(argv[1]);
    int num_tests;
    ifp >> num_tests;
    for (int i = 0; i < num_tests; i++) {
        long n_jars, k_coins, c_picks;
        ifp >> n_jars >> k_coins >> c_picks;

        long p_moves = c_picks;
        if ((k_coins / n_jars) * n_jars < c_picks) {
            p_moves += n_jars - (k_coins / (c_picks / n_jars + 1));
        }
        cout << "Case #" << (i + 1) << ": " << p_moves << endl;
    }

    return 1;
}
