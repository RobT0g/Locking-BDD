class Node:
    item:any
    children:list['Node']

    def __init__(self, item:any):
        self.item = item
        self.children = []

    def add_children(self, child:'Node'):
        self.children.append(child)
    
    def __str__(self):
        return self.item


class ItemTree:
    root:Node
    number_of_items:int
    list_of_items:list[any]
    list_of_nodes:list[Node]

    # def __int__(self, root:any):
    #     self.root = Node(root)
    #     self.list_of_items = [root]
    #     self.list_of_nodes = [self.root]
    #     self.number_of_items = 1
    
    def set_root(self, root:any):
        self.root = Node(root)
        self.list_of_items = [root]
        self.list_of_nodes = [self.root]
        self.number_of_items = 1
    
    def add_new_node(self, child:Node, parent:Node):
        added = False

        for ind, val in enumerate(self.list_of_nodes):
            if not val == parent:
                continue

            added = True
            val.add_children(child)
        
        if not added:
            raise Exception(f'FAILED TO ADD NODE {child} IN THE TREE')

        self.list_of_nodes.append(child)
        self.list_of_items.append(child.item)
        self.number_of_items += 1

    def add_new_item(self, child_item:Node, parent_item:any):
        child = Node(child_item)
        added = False

        for ind, val in enumerate(self.list_of_items):
            if not val == parent_item:
                continue

            added = True
            self.list_of_nodes[ind].add_children(child)
        
        if not added:
            raise Exception(f'FAILED TO ADD ITEM {child_item} AND NODE {child} IN THE TREE')
        
        self.list_of_nodes.append(child)
        self.list_of_items.append(child.item)
        self.number_of_items += 1

    def navigate_step(self, current_node:Node, path:list[Node], depth:int):
        print(f'Current depth: {depth}\n Item: {current_node.item}')
        yield {'current_node': current_node, 'path': path, 'depth': depth}
        
        for child in current_node.children:    
            temp_path = path.copy()
            temp_path.append(current_node)

            yield from self.navigate_step(child, temp_path, depth+1)

    def navigate_depth_first(self):
        return self.navigate_step(self.root, [self.root], 0)


if __name__ == '__main__':
    root = 'a'
    items = [
        ('b', 'a'),
        ('c', 'b'),
        ('d', 'b'),
        ('e', 'd'),
        ('f', 'a'),
        ('g', 'a'),
        ('h', 'g')
    ]

    sample_node = Node('a')
    sample_tree = ItemTree()
    sample_tree.set_root(root)
    for i in items:
        sample_tree.add_new_item(i[0], i[1])
    
    for i in sample_tree.navigate_depth_first():
        print(i)

