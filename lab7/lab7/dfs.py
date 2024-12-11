#include <iostream>
#include <stdexcept>

using namespace std;

template <typename T>
class AutoGrowingArray {
private:
    T* data;          
    int size;        
    int capacity;     

public:
    AutoGrowingArray() : size(0), capacity(1) {
        data = new T[capacity];
    }

    ~AutoGrowingArray() {
        delete[] data; 
    }

    void PushBack(T value) {
        if (size >= capacity) {
            capacity *= 2;
            T* newData = new T[capacity];
            for (int i = 0; i < size; ++i) {
                newData[i] = data[i];
            }
            delete[] data;
            data = newData;
        }
        data[size++] = value;
    }

    T operator[](int index) const {
        if (index < 0 || index >= size) {
            throw out_of_range("Index out of range");
        }
        return data[index];
    }

    T& operator[](int index) {
        if (index < 0 || index >= size) {
            throw out_of_range("Index out of range");
        }
        return data[index];
    }

    friend ostream& operator<<(ostream& out, const AutoGrowingArray& arr) {
        for (int i = 0; i < arr.size; ++i) {
            out << arr.data[i] << " ";
        }
        return out;
    }
};

int main() {
    AutoGrowingArray<int> arr;

    for (int i = 1; i <= 10; ++i) {
        arr.PushBack(i);
        cout << "Array after inserting " << i << ": " << arr << endl;
    }

    try {
        cout << "Element at index 5: " << arr[5] << endl;
        cout << "Element at index 10: " << arr[10] << endl; 
    } catch (const out_of_range& e) {
        cerr << e.what() << endl;
    }

    return 0;
}
