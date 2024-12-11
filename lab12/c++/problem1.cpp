#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<string> vec;
    int choice;
    string input;

    while (true) {
        cout << "1. Add String\n2. Remove String\n3. Display Vector\n4. Exit\nEnter your choice: ";
        cin >> choice;

        if (choice == 1) {
            cout << "Enter string to add: ";
            cin >> input;
            vec.push_back(input);
        } else if (choice == 2) {
            if (!vec.empty()) {
                cout << "Enter string to remove: ";
                cin >> input;
                auto it = find(vec.begin(), vec.end(), input);
                if (it != vec.end()) vec.erase(it);
                else cout << "String not found.\n";
            } else {
                cout << "Vector is empty.\n";
            }
        } else if (choice == 3) {
            cout << "Vector elements: ";
            for (const auto& str : vec) cout << str << " ";
            cout << "\nSize: " << vec.size() << ", Capacity: " << vec.capacity() << "\n";
        } else if (choice == 4) {
            break;
        } else {
            cout << "Invalid choice.\n";
        }
    }
    return 0;
}
