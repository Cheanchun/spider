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


if __name__ == '__main__':
    # t = ['a', 'b', 'c', 'd']
    # stack = Stack()
    # for i in t:
    #     stack.add(Node(i))
    # print(stack.len)
    print(match_symbol('a+b+[{(a-r)-(f-4)}]'))
