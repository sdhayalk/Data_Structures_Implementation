#include <iostream>
using namespace std;

struct node {
    int data;
    node* next;
};

node* createNode(int data)  {
    node* newNode = new node();
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

node* populate(node* head)    {
    head = createNode(1);
    head->next = createNode(2);
    head->next->next = createNode(3);
    head->next->next->next = createNode(4);
    head->next->next->next->next = createNode(5);
    return head;
}

void printAllData(node* head) {
    while(head != NULL)   {
        cout << head->data << " ";
        head = head->next;
    }
    cout << endl;
}

node* insertAtHead(int data, node* head) {
    node* newNode = createNode(data);
    newNode->next = head;
    head = newNode;
    return head;
}

node* insertAtTail(int data, node* head) {
    node* temp = head;
    while(temp->next != NULL)   {
        temp = temp->next;
    }
    temp->next = createNode(data);
    return head;
}

node* insertAtIndex(int data, int index, node* head)    {
    if(index < 0)   {
        cout << "Index must be greater than or equal to 0" << endl;
        return head;
    }
        
    if(index == 0)
        return insertAtHead(data, head);

    node* temp = head;
    try {
        for(int i=0 ; i<index-1 ; i++)
            temp = temp->next;
        
        node* newNode = createNode(data);
        newNode->next = temp->next;
        temp->next = newNode;
    } catch(...)   {
        cout << "Error, possibly index out of range" << endl;
    }
    return head;
}

node* deleteHead(node* head)  {
    node* temp = head->next;
    free(head);
    head = temp;
    return head;
}

node* deleteTail(node* head)    {
    struct node* temp = head;
    while(temp->next->next != NULL)
        temp = temp->next;
    free(temp->next);
    temp->next = NULL;
    return head;
}

node* deleteAtIndex(int index, node* head)  {
    if(index < 0)   {
        cout << "Index must be greater than or equal to 0" << endl;
        return head;
    }
        
    if(index == 0)
        return deleteHead(head);

    node* temp = head;
    try {
        for(int i=0 ; i<index-1 ; i++)
            temp = temp->next;
        
        if(temp->next == NULL)
            return head;
            
        struct node* toBeDeleted = temp->next;
        temp->next = temp->next->next;
        free(toBeDeleted);
    } catch(...)   {
        cout << "Error" << endl;
    }
    return head;
}

node* reverseList(node* head) {
        if(head == NULL || head->next == NULL)
            return head;
        
        node* p = head;
        node* q = p->next;
        node* r = q->next;
        p->next = NULL;
        
        while(q->next != NULL)  {
            q->next = p;
            p = q;
            q = r;
            r = r->next;
        }
        q->next = p;
        head = q;
        
        return head;
}

int main() {
    node* head;     // using node* head, emptyHead; gives error
    node* emptyHead;
    head = populate(head);
    printAllData(head);
    printAllData(emptyHead);
    
    head = insertAtHead(0, head);
    head = insertAtTail(6, head);
    printAllData(head);
    head = insertAtIndex(-1, 0, head);
    head = insertAtIndex(98, 2, head);
    head = insertAtIndex(99, 9, head);
    printAllData(head);
    
    head = deleteHead(head);
    head = deleteTail(head);
    head = deleteAtIndex(2, head);
    head = deleteDataEqualsTO(2, head);
    printAllData(head);
    
    return 0;
}



