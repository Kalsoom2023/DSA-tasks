#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
using namespace std;
void printVector(vector<int> Vec) {
    for (int num : Vec) {
         cout << num << " ";
    }
     cout <<  endl;
}

int main() {
    
     vector<int> Vec = {3, 5, 8, 1, 0, 3, 6, 4, 7};
    printVector(Vec);
    int n = Vec.size();
    for (int i = 0; i < n / 2; ++i) {
        swap(Vec[i], Vec[n - 1 - i]); 
    }     cout << "Reversed vector: ";
    printVector(Vec);

    
    for (int i = 0; i < n - 1; ++i) {
        for (size_t j = 0; j < n - 1 - i; ++j) {
            if (Vec[j] > Vec[j + 1]) {
                swap(Vec[j], Vec[j + 1]); 
            }
        }
    }     cout << "Sorted vector: ";
    printVector(Vec);

    if (!Vec.empty()) 
    {

    vector<int> uniqueVec;
    uniqueVec.push_back(Vec[0]); 

    for (int i = 1; i < Vec.size(); ++i) {
        // Only add if it's not a duplicate
        if (Vec[i] != Vec[i - 1]) {
            uniqueVec.push_back(Vec[i]);
        }
    }

    // Clear the original vector and copy unique elements back
    Vec.clear();
    Vec = uniqueVec;
    printVector(Vec);
    }
    return 0;
}
