#include <iostream>
#include <fstream>
#include <stdexcept>
#include <vector>
#include <ctime>
#include <cstdlib>

using namespace std;

void CreateRandomFile(string fn, int Size, int RN = 100) {
    srand(time(0));
    ofstream Writer(fn);
    for (int i = 0; i < Size * 1024 * 1024; i++) {
        Writer << rand() % RN << " ";
    }
}

template <typename T>
class AutoGrowingArray {
private:
    T* data;
    int size;
    int capacity;

public:
    AutoGrowingArray() : size(0), capacity(2) {
        data = new T[capacity];
    }

    ~AutoGrowingArray() {
        delete[] data;
    }

    void PushBack(T value) {
        if (size == capacity) {
            capacity = static_cast<int>(capacity * 1.5);
            T* newData = new T[capacity];
            for (int i = 0; i < size; ++i) {
                newData[i] = data[i];
            }
            delete[] data;
            data = newData;
        }
        data[size++] = value;
    }

    void LoadFromFile(const string& filename) {
        ifstream file(filename);
        T value;
        while (file >> value) {
            PushBack(value);
        }
    }

    void WriteToFile(const string& filename) const {
        ofstream file(filename);
        for (int i = 0; i < size; ++i) {
            file << data[i] << " ";
        }
    }
};

template <typename T>
class ArrayList {
private:
    T* data;
    int size;
    int capacity;

public:
    ArrayList() : size(0), capacity(2) {
        data = new T[capacity];
    }

    ~ArrayList() {
        delete[] data;
    }

    void PushBack(T value) {
        if (size == capacity) {
            capacity = static_cast<int>(capacity * 1.5);
            T* newData = new T[capacity];
            for (int i = 0; i < size; ++i) {
                newData[i] = data[i];
            }
            delete[] data;
            data = newData;
        }
        data[size++] = value;
    }

    void LoadFromFile(const string& filename) {
        ifstream file(filename);
        T value;
        while (file >> value) {
            PushBack(value);
        }
    }

    void WriteToFile(const string& filename) const {
        ofstream file(filename);
        for (int i = 0; i < size; ++i) {
            file << data[i] << " ";
        }
    }
};

int main() {
    string filename = "random_numbers.txt";
    CreateRandomFile(filename, 2);

    AutoGrowingArray<int> autoGrowArray;
    clock_t start = clock();
    autoGrowArray.LoadFromFile(filename);
    clock_t end = clock();
    double autoGrowTime = double(end - start) / CLOCKS_PER_SEC;
    autoGrowArray.WriteToFile("OutputGA.txt");
    cout << "Time taken for AutoGrowingArray: " << autoGrowTime << " seconds." << endl;

    // Measure time for                                                              vector
    vector<int> stdVector;
    start = clock();
    ifstream file(filename);
    int value;
    while (file >> value) {
        stdVector.push_back(value);
    }
    end = clock();
    double vectorTime = double(end - start) / CLOCKS_PER_SEC;
    ofstream vectorOutput("OutputVector.txt");
    for (const auto& v : stdVector) {
        vectorOutput << v << " ";
    }
    cout << "Time taken for vector: " << vectorTime << " seconds." << endl;

    
    ArrayList<int> arrayList;
    start = clock();
    arrayList.LoadFromFile(filename);
    end = clock();
    double arrayListTime = double(end - start) / CLOCKS_PER_SEC;
    arrayList.WriteToFile("OutputArraylist.txt");
    cout << "Time taken for ArrayList: " << arrayListTime << " seconds." << endl;

    return 0;
}
