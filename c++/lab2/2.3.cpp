#include <iostream>

using namespace std;

int main()
{
    int x = 0;
    int n = 2;
    cin >> x;
    while (x != 1) {
        if (x%n == 0) {
        cout << n;
        x = x/n;
        if (x != 1) {
            cout << "*";
        }
        }
        else{
            n++;
        }
    }
    return 0;
}
