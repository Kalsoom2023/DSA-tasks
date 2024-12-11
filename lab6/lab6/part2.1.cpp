#include <iostream>
#include <stack>
using namespace std;

void reverseWords(const string& sentence) {
    stack<string> words;
    string currentWord;

    // Traverse the sentence character by character
    for (char ch : sentence) {
        if (ch != ' ') {
            currentWord += ch; // Build the current word
        } else {
            if (!currentWord.empty()) {
                words.push(currentWord); // Push the word onto the stack
                currentWord.clear(); // Clear the current word for the next one
            }
        }
    }

    // Push the last word if there is one
    if (!currentWord.empty()) {
        words.push(currentWord);
    }

    // Pop from the stack and print words in reverse order
    while (!words.empty()) {
        cout << words.top(); // Print the top word
        words.pop(); // Remove the word from the stack
        if (!words.empty()) {
            cout << " "; // Print space between words
        }
    }
    cout << endl; 
}

int main() {
    string sentence = "I am from University of Engineering and Technology Lahore";
    cout << "Input: " << sentence << endl;
    cout << "Output: ";
    reverseWords(sentence);
    return 0;
}
