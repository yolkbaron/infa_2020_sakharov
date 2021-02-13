#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int n = 0;
    cin >> n;
    for (int a = 0; a <= sqrt(n); a++) {
        for (int b = a; b <= sqrt(n); b++) {
            for (int c = b; c <= sqrt(n); c++) {
                for (int d = b; d <= sqrt(n); d++) {
                    if (n == a*a + b*b + c*c + d*d){
                        cout << a << " " << b << " " << c << " " << d ;
                        a = n;
                        b = n;
                        c = n;
                        d = n;
                    }
                }
            }
        }
    }
    return 0;
}
