#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int a;
    int b;
    int m;
    bool has_sol = false;
    cin >> a >> b >> m;
    for (int x = 0; x < m; x++) {
        if ((a*x - b)%m == 0) {
            cout << x << " ";
            has_sol = true;
        }
    }
    if (not has_sol) {
        cout << "-1";
    }
    return 0;
}
