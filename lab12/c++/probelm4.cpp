#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> vec = {10, 20, 10, 40, 30, 20, 40};

    // Reverse
    reverse(vec.begin(), vec.end());
    cout << "Reversed: ";
    for (int x : vec) cout << x << " ";
    cout << endl;

    // Sort
    sort(vec.begin(), vec.end());
    cout << "Sorted: ";
    for (int x : vec) cout << x << " ";
    cout << endl;

    // Remove duplicates
    vec.erase(unique(vec.begin(), vec.end()), vec.end());
    cout << "After removing duplicates: ";
    for (int x : vec) cout << x << " ";
    cout << endl;

    return 0;
}
