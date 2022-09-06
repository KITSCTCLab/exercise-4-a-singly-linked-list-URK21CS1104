from typing import Optional
class Node:
    """
    Creating a node
    """

    def __init__(self, data=None, next=None):
        """
        declare the instance variable in the Node.
        """
        self.data = data
        self.next = next


class LinkedList:
    """
    Provide necessary documentation
    """

    def __init__(self):
        """
        Initialize the head
        """
        self.head = None

    def insert_at_end(self, data):
        node = Node(data, None)
        ptr = self.head
        if ptr is None:
            self.head = node

        else:
            while(ptr.next is not None):
                ptr = ptr.next
            ptr.next = node

    def status(self):
        """
        It prints all the elements of list.
        """
        data = []
        ptr = self.head
        while(ptr is not None):
            data.append(ptr.data)
            ptr = ptr.next

        print(data)



class Solution:
    """
    Provide necessary documentation
    """

    def addTwoNumbers(self, first_list: Optional[LinkedList], second_list: Optional[LinkedList]) -> Optional[LinkedList]:
        """
        :param first_list: Linkedlist with non-negative integers
        :param second_list: Linkedlist with non-negative integers
        :return: returns the sum as a linked list
        """
        result = self.Get_value(first_list) + self.Get_value(second_list)
        result = str(result)
        result = result[::-1]
        total_list = LinkedList()
        for i in result:
            total_list.insert_at_end(int(i))
        return total_list

    def Get_value(self,link : Optional[LinkedList]) -> int:
        ptr = link.head
        num = ""

        if(ptr is None):
            return 0

        while(ptr is not None):
            num += str(ptr.data)
            ptr = ptr.next

        return int(num)




# Do not edit the following code
# Create an instance for LinkedList
first_list = LinkedList()
# Create an another instance for LinkedList
second_list = LinkedList()
# Read data for first list
data_for_first_list = list(map(int, input().strip().split(" ")))
# Add data at the end of first_list
for data in data_for_first_list:
    first_list.insert_at_end(data)
# Read data for second list
data_for_second_list = list(map(int, input().strip().split(" ")))
# Add data at the end of second_list
for data in data_for_second_list:
    second_list.insert_at_end(data)
# Create an instance for Solution
solution = Solution()
# Pass first_list and second_list to addTwoNumbers, which returns a new linked list
new_list = solution.addTwoNumbers(first_list, second_list)
# Display the status of new_list
new_list.status()
