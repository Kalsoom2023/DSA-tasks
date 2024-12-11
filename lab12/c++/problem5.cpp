#include <iostream>
#include <vector>
using namespace std;

void displayMatrix(const vector<vector<int>>& matrix) {
    for (const auto& row : matrix) {
        for (int val : row) cout << val << " ";
        cout << endl;
    }
}

int main() {
    vector<vector<int>> matrix = {{1, 2}, {3, 4}};
    cout << "Initial Matrix:\n";
    displayMatrix(matrix);

    // Add a row
    matrix.push_back({5, 6});
    cout << "After adding a row:\n";
    displayMatrix(matrix);

    // Add a column
    for (auto& row : matrix) row.push_back(0);
    cout << "After adding a column:\n";
    displayMatrix(matrix);

    return 0;
}
