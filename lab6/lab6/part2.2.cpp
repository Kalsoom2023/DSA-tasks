#include <iostream>
#include <sstream>
#include <stack>
#include <string>
#include <cctype>

class Stack {
private:
    std::stack<int> s;

public:
    void push(int value) {
        s.push(value);
    }

    int pop() {
        if (s.empty()) {
            std::cerr << "Stack is empty. Cannot pop." << std::endl;
            return 0; // Returning 0 on error; could handle this better
        }
        int value = s.top();
        s.pop();
        return value;
    }

    bool isEmpty() const {
        return s.empty();
    }

    void printStack() const {
        std::stack<int> temp = s; // Make a copy to print
        std::cout << "[ ";
        while (!temp.empty()) {
            std::cout << temp.top() << " ";
            temp.pop();
        }
        std::cout << "]" << std::endl;
    }
};

class Calculator {
private:
    Stack stack;

public:
    void processInput(const std::string& input) {
        std::istringstream stream(input);
        std::string token;

        while (stream >> token) {
            if (std::isdigit(token[0]) || (token[0] == '-' && token.length() > 1)) {
                // If the token is a valid integer, push it onto the stack
                stack.push(std::stoi(token));
            } else if (token == "+" || token == "-" || token == "*" || token == "/" || token == "%") {
                // Perform arithmetic operations
                int b = stack.pop();
                int a = stack.pop();
                int result = 0;

                if (token == "+") {
                    result = a + b;
                } else if (token == "-") {
                    result = a - b;
                } else if (token == "*") {
                    result = a * b;
                } else if (token == "/") {
                    if (b == 0) {
                        std::cerr << "Error: Division by zero." << std::endl;
                        stack.push(a); // Push back the operand to maintain stack state
                        stack.push(b);
                        continue;
                    }
                    result = a / b;
                } else if (token == "%") {
                    if (b == 0) {
                        std::cerr << "Error: Division by zero." << std::endl;
                        stack.push(a); // Push back the operand to maintain stack state
                        stack.push(b);
                        continue;
                    }
                    result = a % b;
                }

                stack.push(result);
            } else if (token == "?") {
                // Print the current state of the stack
                stack.printStack();
            } else if (token == "^") {
                // Pop and print the top element
                if (!stack.isEmpty()) {
                    std::cout << stack.pop() << std::endl;
                } else {
                    std::cerr << "Stack is empty. Cannot pop." << std::endl;
                }
            } else if (token == "!") {
                // Exit the program
                std::cout << "Exiting calculator." << std::endl;
                exit(0);
            } else {
                std::cerr << "Unknown command: " << token << std::endl;
            }
        }
    }
};

int main() {
    Calculator calculator;
    std::string input;

    std::cout << "Enter postfix expressions (enter '!' to exit):" << std::endl;

    while (true) {
        std::getline(std::cin, input);
        calculator.processInput(input);
    }

    return 0;
}
