#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;
    
    Node(int x) : data(x), next(NULL) {}
};

class LinkList {
public:
    LinkList() { head = NULL; }
    ~LinkList();
    bool isEmpty() { return head == NULL; }

    Node* insertNode(int index, int x);
    Node* insertAtHead(int x);
    Node* insertAtEnd(int x);
    bool findNode(int x);
    bool deleteNode(int x);
    bool deleteFromStart();
    bool deleteFromEnd();
    void displayList();
    Node* reverseList();
    Node* sortList(Node* list);
    Node* removeDuplicates(Node* list);
    Node* mergeLists(Node* list1, Node* list2);
    Node* interestLists(Node* list1, Node* list2);

public:
    Node* head;
};

LinkList::~LinkList() {
    Node* current = head;
    Node* next;
    while (current != NULL) {
        next = current->next;
        delete current;
        current = next;
    }
}

Node* LinkList::insertNode(int index, int x) {
    Node* newNode = new Node(x);
    if (index == 0) {
        newNode->next = head;
        head = newNode;
        return head;
    }
    Node* temp = head;
    for (int i = 0; temp != NULL && i < index - 1; i++) {
        temp = temp->next;
    }
    if (temp == NULL) return NULL;
    newNode->next = temp->next;
    temp->next = newNode;
    return head;
}

Node* LinkList::insertAtHead(int x) {
    Node* newNode = new Node(x);
    newNode->next = head;
    head = newNode;
    return head;
}

Node* LinkList::insertAtEnd(int x) {
    Node* newNode = new Node(x);
    if (head == NULL) {
        head = newNode;
        return head;
    }
    Node* temp = head;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = newNode;
    return head;
}

bool LinkList::findNode(int x) {
    Node* temp = head;
    while (temp != NULL) {
        if (temp->data == x) return true;
        temp = temp->next;
    }
    return false;
}

bool LinkList::deleteNode(int x) {
    Node* temp = head;
    Node* prev = NULL;
    bool found = false;

    while (temp != NULL) {
        if (temp->data == x) {
            if (prev == NULL) {
                head = temp->next;
            } else {
                prev->next = temp->next;
            }
            Node* toDelete = temp;
            temp = temp->next;
            delete toDelete;
            found = true;
        } else {
            prev = temp;
            temp = temp->next;
        }
    }
    return found;
}

bool LinkList::deleteFromStart() {
    if (head == NULL) return false;
    Node* temp = head;
    head = head->next;
    delete temp;
    return true;
}

bool LinkList::deleteFromEnd() {
    if (head == NULL) return false;
    if (head->next == NULL) {
        delete head;
        head = NULL;
        return true;
    }
    Node* temp = head;
    while (temp->next->next != NULL) {
        temp = temp->next;
    }
    delete temp->next;
    temp->next = NULL;
    return true;
}

void LinkList::displayList() {
    Node* temp = head;
    while (temp != NULL) {
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << endl;
}

Node* LinkList::reverseList() {
    Node* prev = NULL;
    Node* current = head;
    Node* next = NULL;

    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    head = prev;
    return head;
}

Node* LinkList::sortList(Node* list) {
    if (!list) return NULL;
    Node* temp1 = list;
    while (temp1 != NULL) {
        Node* temp2 = temp1->next;
        while (temp2 != NULL) {
            if (temp1->data > temp2->data) {
                swap(temp1->data, temp2->data);
            }
            temp2 = temp2->next;
        }
        temp1 = temp1->next;
    }
    return list;
}

Node* LinkList::removeDuplicates(Node* list) {
    Node* temp = list;
    while (temp != NULL && temp->next != NULL) {
        if (temp->data == temp->next->data) {
            Node* toDelete = temp->next;
            temp->next = temp->next->next;
            delete toDelete;
        } else {
            temp = temp->next;
        }
    }
    return list;
}

Node* LinkList::mergeLists(Node* list1, Node* list2) {
    Node* mergedHead = NULL;
    if (list1 == NULL) return list2;
    if (list2 == NULL) return list1;

    if (list1->data <= list2->data) {
        mergedHead = list1;
        mergedHead->next = mergeLists(list1->next, list2);
    } else {
        mergedHead = list2;
        mergedHead->next = mergeLists(list1, list2->next);
    }
    return mergedHead;
}

Node* LinkList::interestLists(Node* list1, Node* list2) {
    Node* result = NULL;
    Node** lastPtrRef = &result;

    while (list1 != NULL && list2 != NULL) {
        if (list1->data == list2->data) {
            *lastPtrRef = new Node(list1->data);
            lastPtrRef = &((*lastPtrRef)->next);
            list1 = list1->next;
            list2 = list2->next;
        } else if (list1->data < list2->data) {
            list1 = list1->next;
        } else {
            list2 = list2->next;
        }
    }
    return result;
}

int main() {
    LinkList list;
    list.insertAtEnd(1);
    list.insertAtEnd(2);
    list.insertAtEnd(3);
    list.displayList();

    list.sortList(list.head);
    list.displayList();

    list.reverseList();
    list.displayList();

    return 0;
}
