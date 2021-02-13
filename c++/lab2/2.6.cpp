#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int maxel;
    int current;
    int amount;
    cin >> maxel;
    current = maxel;
    while (current != 0) {
        cin >> current;
        if (current == maxel){
            amount++;
        }
        if (current > maxel) {
            amount = 1;
            maxel = current;
        }
    }
    cout << maxel << " " << amount;
    return 0;
}
