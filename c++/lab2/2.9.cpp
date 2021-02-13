#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int maxn;
    int premaxn;
    int minn;
    int preminn;
    int n;
    int first;
    int second;
    int number;
    cin >> n >> first >> second;
    maxn = max(first, second);
    premaxn = min(first, second);
    minn = min(first, second);
    preminn = max(first, second);
    for (int i = 2; i < n; i++) {
        cin >> number;
        if (number >= maxn) {
            premaxn = maxn;
            maxn = number;
        }
        if (number < maxn and number > premaxn) {
            premaxn = number;
        }
        if (number > minn and number < preminn) {
            preminn = number;
        }
        if (number < minn) {
            preminn = minn;
            minn = number;
        }
    }
    cout << minn << " " << preminn << " " << premaxn << " " << maxn;
    return 0;
}
