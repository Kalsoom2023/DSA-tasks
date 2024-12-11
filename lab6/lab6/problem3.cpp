#include <iostream>
using namespace std;
class DoublyNode {
public:
    int data;
    DoublyNode* next;
    DoublyNode* prev;

    DoublyNode(int x) : data(x), next(NULL), prev(NULL) {}
};


class DoublyLinkList {
public:
    DoublyLinkList() { head = NULL; }
    ~DoublyLinkList();
    bool isEmpty() { return head == NULL; }
    DoublyNode* insertNode(int index, int x);
    DoublyNode* insertAtHead(int x);
    DoublyNode* insertAtEnd(int x);
    bool findNode(int x);
    bool deleteNode(int x);
    bool deleteFromStart();
    bool deleteFromEnd();
    void displayList();
    DoublyNode* reverseList();
    DoublyNode* sortList(DoublyNode* list);
    DoublyNode* removeDuplicates(DoublyNode* list);
    DoublyNode* mergeLists(DoublyNode* list1, DoublyNode* list2);
    DoublyNode* interestLists(DoublyNode* list1, DoublyNode* list2);

private:
    DoublyNode* head;
};

// Destructor: Deletes all nodes in the list
DoublyLinkList::~DoublyLinkList() {
    DoublyNode* current = head;
    while (current != NULL) {
        DoublyNode* next = current->next;
        delete current;
        current = next;
    }
}

// Insert a node at a given index
DoublyNode* DoublyLinkList::insertNode(int index, int x) {
    if (index < 0) return NULL;

    DoublyNode* newNode = new DoublyNode(x);
    if (index == 0) {
        return insertAtHead(x);
    }

    DoublyNode* current = head;
    for (int i = 0; i < index - 1 && current != NULL; ++i) {
        current = current->next;
    }

    if (current == NULL) {
        delete newNode;
        return NULL; // Index is out of bounds
    }

    newNode->next = current->next;
    newNode->prev = current;

    if (current->next != NULL) {
        current->next->prev = newNode;
    }
    current->next = newNode;

    return newNode;
}

// Insert a node at the head
DoublyNode* DoublyLinkList::insertAtHead(int x) {
    DoublyNode* newNode = new DoublyNode(x);
    if (isEmpty()) {
        head = newNode;
    } else {
        newNode->next = head;
        head->prev = newNode;
        head = newNode;
    }
    return newNode;
}

// Insert a node at the end
DoublyNode* DoublyLinkList::insertAtEnd(int x) {
    DoublyNode* newNode = new DoublyNode(x);
    if (isEmpty()) {
        head = newNode;
    } else {
        DoublyNode* current = head;
        while (current->next != NULL) {
            current = current->next;
        }
        current->next = newNode;
        newNode->prev = current;
    }
    return newNode;
}

// Search for a node with a specific value
bool DoublyLinkList::findNode(int x) {
    DoublyNode* current = head;
    while (current != NULL) {
        if (current->data == x) return true;
        current = current->next;
    }
    return false;
}

// Delete all occurrences of a node with a specific value
bool DoublyLinkList::deleteNode(int x) {
    DoublyNode* current = head;
    bool found = false;

    while (current != NULL) {
        if (current->data == x) {
            found = true;
            if (current->prev != NULL) {
                current->prev->next = current->next;
            } else {
                head = current->next; // Deleting head
            }

            if (current->next != NULL) {
                current->next->prev = current->prev;
            }

            DoublyNode* temp = current;
            current = current->next;
            delete temp;
        } else {
            current = current->next;
        }
    }
    return found;
}

// Delete the node at the start
bool DoublyLinkList::deleteFromStart() {
    if (isEmpty()) return false;

    DoublyNode* temp = head;
    head = head->next;

    if (head != NULL) {
        head->prev = NULL;
    }
    delete temp;
    return true;
}

// Delete the node at the end
bool DoublyLinkList::deleteFromEnd() {
    if (isEmpty()) return false;

    DoublyNode* current = head;
    while (current->next != NULL) {
        current = current->next;
    }

    if (current->prev != NULL) {
        current->prev->next = NULL;
    } else {
        head = NULL; 
    }
    delete current;
    return true;
}

void DoublyLinkList::displayList() {
    DoublyNode* current = head;
    while (current != NULL) {
        cout << current->data << " ";
        current = current->next;
    }
    cout << endl;
}


