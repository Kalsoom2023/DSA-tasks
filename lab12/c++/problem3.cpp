#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> vec = {10, 20, 30, 40, 50};
    int target;
    cout << "Enter integer to search: ";
    cin >> target;

    auto it = find(vec.begin(), vec.end(), target);
    if (it != vec.end()) {
        cout << "Found at index: " << distance(vec.begin(), it) << endl;
    } else {
        cout << "Integer not found.\n";
    }
    return 0;
}
