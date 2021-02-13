#include <iostream>

using namespace std;

int main()
{
    int x = 0;
    int y = 0;
    int z = 0;
    cin >> x >> y >> z;
    if (y == max(max(x, y), z)) {
        swap(x, y);
    }
    if (z == max(max(x, y), z)) {
        swap(x, z);
    }
    if (x >= y + z) {
        cout << "impossible";
    }
    else if (x*x - y*y - z*z == 0) {
        cout << "right";
    }
    else if (x*x - y*y - z*z > 0) {
        cout << "butse";
    }
    else if (x*x - y*y - z*z < 0) {
        cout << "acute";
    }
    return 0;
}
