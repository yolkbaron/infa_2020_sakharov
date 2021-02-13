#include <iostream>
#include <cmath>

using namespace std;

int prime(int n)
{
    for (int i = 2; i > 0; i++) {
        bool isprime = true;
        for (int j = 2; j <= sqrt(i); j++) {
            if (i%j == 0){
                isprime = false;
            }
        }
        if (isprime){
            n = n-1;
            if (n == 0){
                return i;
            }
        }
    }
}

int main()
{
    int n = 0;
    cin >> n;
    cout << prime(n);
    return 0;
}
