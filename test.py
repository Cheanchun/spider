# coding:utf-8
class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class Stack(object):
    def __init__(self, node=None):
        self.head = node
        self.len = 0

    def add(self, node):
        if not self.head:
            self.head = node
        node.next = self.head
        self.head = node
        self.len += 1

    def pop(self):
        pop_item = self.head
        self.head = self.head.next
        self.len -= 1
        return pop_item


def match_symbol(expression):
    """
    匹配表达式括号是否使用正确
    :param expression: 算术表达式
    :return:
    """
    assert isinstance(expression, str)
    add_symbol = '([{'
    pop_symbol = ')]}'
    match_map = {')': '(', ']': '[', '}': '{'}
    stack = Stack()
    for string in expression:
        if string in add_symbol:
            stack.add(Node(string))
        elif string in pop_symbol:
            pop_str = stack.pop()
            if ord(pop_str.item) == ord(match_map.get(string)):
                continue
            else:
                return False
    return True


def calculate(expression):
    pass


# 用列表实现队列
class ListQueue(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return bool(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def size(self):
        return len(self.items)


# 用链表实现队列
class LinkQueue(object):
    def __init__(self, max_size=10):
        self.max_size = max_size
        self.current_size = 0
        self.head = None
        self.front = 0
        self.rear = 0

    def is_empty(self):
        if self.rear - self.front == 0:
            return False
        return True

    def enqueue(self, node):
        if not self.front:
            self.head = node
            self.rear += 1
        else:
            current_node = self.head
            for _ in range(self.rear):
                current_node = current_node.next
                if current_node.next is None:
                    current_node.next = node
            self.rear += 1

    def dequeue(self):
        if not self.is_empty():
            re_node = self.head
            self.head = self.head.next
            self.front += 1
            return re_node
        return None

    def size(self):
        pass


# 用链表实现环队列


if __name__ == '__main__':
    # t = ['a', 'b', 'c', 'd']
    # stack = Stack()
    # for i in t:
    #     stack.add(Node(i))
    # print(stack.len)
    print(match_symbol('a+b+[{(a-r)-(f-4)}]'))
