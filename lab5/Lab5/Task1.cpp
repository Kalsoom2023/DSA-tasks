#include <iostream>
#include <vector>
#include <string>
using namespace std;

void displayVectorInfo(vector<string> vec) {
    cout << "Current size: " << vec.size() << endl;
    cout << "Current capacity: " << vec.capacity() <<endl;
}

int main() {
     vector<string> Vec;
    int choice;
     string input;

    do {
   
         cout << "1. Add a string\n";
         cout << "2. Remove a string\n";
         cout << "3. Display vector info\n";
         cout << "4. Exit\n";
         cout << "Enter your choice: ";
         cin >> choice;

        switch (choice) {
            case 1:
                 cout << "Enter a string to add: ";
                 cin.ignore(); 
                 getline( cin, input);
                Vec.push_back(input);
                displayVectorInfo(Vec);
                break;

            case 2:
                if (!Vec.empty()) {
                    cout << "Enter the index ";
                    int index;
                    cin >> index;
                    if (index >= 0 && index < Vec.size()) {
                         cout << "\"" << Vec[index] << "\" removed.\n";
                        Vec.erase(Vec.begin() + index);
                    } else {
                         cout << "Invalid index!\n";
                    }
                } else {
                     cout << "The vector is empty!\n";
                }
                displayVectorInfo(Vec);
                break;

            case 3:
                displayVectorInfo(Vec);
                break;

            case 4:
                 cout << "Exiting the program.\n";
                break;

            default:
                 cout << "Invalid.\n";
        }
    } while (choice != 4);

    return 0;
}
