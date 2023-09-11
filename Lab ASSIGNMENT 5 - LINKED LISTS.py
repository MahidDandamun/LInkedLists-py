class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None

    def createlist(self, no_nodes):
        if self.head is None:
            for i in range(no_nodes):
                data = input("Enter the element: ")
                newNode = Node(data)
                current = self.head
                if current is None:
                    self.head = newNode
                else:
                    while current.next:
                        current = current.next
                    current.next = newNode
        else:
            current = self.head
            for i in range(no_nodes):
                data = input("Enter the element: ")
                newNode = Node(data)
                while current.next:
                    current = current.next
                current.next = newNode

    def addbeginning(self, data):
        if self.head is None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    def addafter(self, data, position):
        try:
            if self.head is not None:
                newNode = Node(data)
                current = self.head
                for i in range(0, position):
                    current = current.next
                newNode.next = current.next
                current.next = newNode
            else:
                return
        except AttributeError:
            print("Position is out of range")
            return

    def count(self):
        current = self.head
        pos = 0
        while current is not None:
            current = current.next
            pos += 1
        print("The number of elements are:", pos)

    def delete(self, data):
        if self.head is None:
            return
        if data == self.head.data:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if data == current.next.data:
                break
            current = current.next
        if current.next is None:
            print(data, "is not present")
        else:
            current.next = current.next.next

    def reverse(self):
        previous = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

    def search(self, data):
        current = self.head
        pos = 0
        while current is not None:
            if current.data == data:
                print(data, " is found at position", pos)
                return
            pos = pos + 1
            current = current.next

        print(data, "is not found")
        return

    def printList(self):
        current = self.head
        if current is not None:
            while current:
                print(current.data, "--> ", end='')
                current = current.next
        else:
            print("The list is empty")


def choices():
    print("""
Programmed by: Mahid L. Dandamun
BSCOE 2-5  

1.Create List
2.Add at beginning
3.Add after
4.Delete
5.Display
6.Count
7.Reverse
8.Search
9.Quit""")


def main_program():
    lst = linkedList()
    while True:
        choices()
        try:
            choice = int(input("Enter your choice: "))
            #  Create List
            if choice == 1:
                try:
                    while True:
                        no_nodes = int(input("How many nodes you want"))
                        if no_nodes != "":
                            lst.createlist(no_nodes)
                            lst.printList()
                            break
                        else:
                            continue
                except ValueError:
                    continue
            #  Add at the beginning
            elif choice == 2:
                try:
                    while True:
                        data = input("Enter the element: ")
                        if data != "":
                            lst.addbeginning(data)
                            lst.printList()
                            break
                        else:
                            continue
                except ValueError:
                    continue
            #  Add after a certain node
            elif choice == 3:
                try:
                    while True:
                        data = input("Enter the element: ")
                        position = int(input("Enter the position after which this element is inserted(the position starts from zero(0): "))
                        if (data and position) != "":
                            lst.addafter(data, position)
                            lst.printList()
                            break
                        else:
                            print("missing fields")
                            continue
                except ValueError:
                    continue
            #  Delete an element
            elif choice == 4:
                try:
                    while True:
                        data = input("Enter the element for deletion: ")
                        if data != "":
                            lst.delete(data)
                            lst.printList()
                            break
                        else:
                            print("missing fields")
                            break
                except ValueError:
                    continue
            #  print the linked list
            elif choice == 5:
                lst.printList()
            #  count the element inside the linked list
            elif choice == 6:
                lst.count()
            #  reverse the linked list
            elif choice == 7:
                lst.reverse()
                lst.printList()
            #  element search
            elif choice == 8:
                try:
                    elem = input("Enter the element to be searched:")
                    if elem != "":
                        lst.search(elem)
                    else:
                        print("missing fields")
                except ValueError:
                    continue
            #  exit
            elif choice == 9:
                break
            else:
                print("Invalid choice")
                print()
        except ValueError:
            print("Invalid input")
            print()
            continue


main_program()
