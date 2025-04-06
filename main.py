from node import Node
from linked_list import LinkedList

if __name__ == "__main__":
    
    list = LinkedList()
    print(list)
    print("Size: ", list.size)
    print("Empty? ", list.is_empty())
    print()
    
    list.push_back(5)
    print(list)
    print("Size: ", list.size)
    print("Empty? ", list.is_empty())
    print()

    list.push_back(6)
    print(list)
    print("Size: ", list.size)
    print("Empty? ", list.is_empty())
    print()

    list.push_back(7)
    list.push_back(8)
    print(list)
    print("Size: ", list.size)
    print("Empty? ", list.is_empty())
    print()

    print("Does the list contain 7?",list.contains(7))
    print("Does the list contain 4?",list.contains(4))
    print("Does the list contain 9?",list.contains(9))
    print("Does the list contain 5?",list.contains(5))

    list.insert_at(0, 4)
    print(list)

    list.insert_at(1, 9)
    print(list)
    list.insert_at(4, 11)
    print(list)
    print("Size: ", list.size)

    print("element at index 6 is ", list.get_at(6))
    print("element at index 4 is ", list.get_at(4))
    print("element at index 0 is ", list.get_at(0))

    list.set_at(0, 3)
    print(list)
    list.set_at(1, 4)
    print(list)
    list.set_at(4, 9)
    print(list)

    list.delete_at(0)
    print(list)
    print("Size: ", list.size)
    list.delete_at(3)
    print(list)
    print("Size: ", list.size)

    list.insert_at(5, 9)
    print(list)
    print("Size: ", list.size)

    list.delete(6)
    print(list)
    print("Size: ", list.size)