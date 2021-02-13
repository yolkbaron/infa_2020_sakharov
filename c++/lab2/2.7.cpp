#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int n;
    bool impossible = true;
    cin >> n;
    for (int i = 0; i*i*i <= n; i++) {
        for (int j = 0; j <= i; j++) {
            for (int k = 0; k <= j; k++) {
                if (k*k*k + j*j*j + i*i*i == n) {
                    cout << k << " " << j << " " << i;
                    impossible = false;
                }
            }
        }
    }
    if (impossible) {
        cout << "impossible";
    }
    return 0;
}
