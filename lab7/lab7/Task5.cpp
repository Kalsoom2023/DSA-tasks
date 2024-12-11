#include <iostream>
#include <vector>
#include<conio.h>
using namespace std;

void displayMatrix(const vector<vector<int>>& matrix) {
    for (const auto& row : matrix) {
        for (int element : row) {
            cout << element << " ";
        }
        cout << endl;
    }
}

void addRow(vector<vector<int>>& matrix, const vector<int>& newRow) {
    matrix.push_back(newRow);
}


void addColumn(vector<vector<int>>& matrix, const vector<int>& newCol) {
    if (matrix.size() != newCol.size()) {
        cerr << "Error: The column size must match the number of rows in the matrix." << endl;
        return;
    }

    for (size_t i = 0; i < matrix.size(); ++i) {
        matrix[i].push_back(newCol[i]);
    }
}

vector<vector<int>> transpose(const vector<vector<int>>& matrix) {
    vector<vector<int>> transposed(matrix[0].size(), vector<int>(matrix.size()));

    for (size_t i = 0; i < matrix.size(); ++i) {
        for (size_t j = 0; j < matrix[i].size(); ++j) {
            transposed[j][i] = matrix[i][j];
        }
    }

    return transposed;
}

int main() {
    vector<vector<int>> matrix;

    addRow(matrix, {1, 2, 3});
    addRow(matrix, {0, 6, 4});
    addRow(matrix, {1, 2, 3});

    cout << "Original matrix:" << endl;
    displayMatrix(matrix);

    addRow(matrix, {1, 1, 2});
    cout << "\nAfter adding a row:" << endl;
    displayMatrix(matrix);

    addColumn(matrix, {3, 4, 5, 6});
    cout << "\nAfter adding a column:" << endl;
    displayMatrix(matrix);

    vector<vector<int>> transposedMatrix = transpose(matrix);
    cout << "\nTransposed matrix:" << endl;
    displayMatrix(transposedMatrix);

    return 0;
}
