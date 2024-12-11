#include <iostream>
#include <vector>
using namespace std;
int main() {
       vector<int> myVector = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    int integer;
       cout << "Enter the integer: ";
       cin >> integer;

    bool found = false;
    for (size_t i = 0; i < myVector.size(); ++i) {
        if (myVector[i] == integer) {
            cout << "Integer " << integer << " found at index: " << i << endl;
            found = true;
            break; // Exit the loop if found
        }
    }

    if (!found) {
           cout << "Integer " << integer << " is not present in the vector." << endl;
    }

    return 0;
}
