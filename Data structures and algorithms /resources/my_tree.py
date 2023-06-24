class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = '  ' * self.get_level()*2
        if self.get_level()>0:
            spaces += '|--'
        print(spaces + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_product_tree():
    root = TreeNode('Electronics')

    laptop = TreeNode('Laptop')
    laptop.add_child(TreeNode('Mac'))
    laptop.add_child(TreeNode('Thinkpad'))
    laptop.add_child(TreeNode('Surface'))

    cellphone = TreeNode('Cellphone')
    cellphone.add_child(TreeNode('Iphone'))
    cellphone.add_child(TreeNode('Sony'))
    cellphone.add_child(TreeNode('Samsung'))

    root.add_child(laptop)
    root.add_child(cellphone)

    return root


if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()