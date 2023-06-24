class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        elif data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        elif data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
        else:
            return "not matching type"

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements

    def search(self, val):
        if self.data == val:
            return True
        elif self.data > val:
            if self.left:
                return self.left.search(val)
            else:
                return False
        else:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def delete_node(self, val):
        if self.data > val:
            if self.left:
                self.left = self.left.delete_node(val)
        elif self.data < val:
            if self.right:
                self.right = self.right.delete_node(val)

        else:
            if self.left is None and self.right is None:
                self.data = None
                return None
            elif self.right is None:
                max_val = self.left.find_max()
                self.data = max_val
                self.left = self.left.delete_node(max_val)
            else:
                min_val = self.right.find_min()
                self.data = min_val
                self.right = self.right.delete_node(min_val)

        return self

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()


if __name__ == '__main__':
    root = BinarySearchTreeNode(17)
    root.add_child(4)
    root.add_child(1)
    root.add_child(9)
    root.add_child(20)
    root.add_child(18)
    root.add_child(13)
    root.add_child(19)
    # root.add_child(23)
    # root.add_child(34)
    print('1', root.in_order_traversal())
    # print(root.search(12))
    root.delete_node(17)
    print('2', root.in_order_traversal())
