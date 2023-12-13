class BST_Node():
    def __init__(self, data):
        self.node_data = data
        self.left = None
        self.right = None



class BST():
    def __init__(self):
        self.root = None
        self.my_list = []
        self.duplicates_list = []

    # def insert_node(self):
    #     info = int(input("Enter root Node : "))

    # find algorithm finds and return the location and parent of a new value
    def find(self, value):
        if self.root is None:
            parent = None
            location = None
            return parent, location
        if value == self.root.node_data:
            parent = None
            location = self.root
            return parent, location
        current = self.root
        while current is not None:
            save = current
            if value == current.node_data:
                parent = save
                location = current
                return parent, location

            if value < current.node_data:
                current = current.left
            elif value > current.node_data:
                current = current.right

        parent = save
        location = None
        return parent, location

    def insert_node(self, value):
        parent, location = self.find(value)
        if location is not None:
            print("Node already exists!")
            self.duplicates_list.append(value)
            print("Added as a duplicate")

        # creating the node
        new_node = BST_Node(value)
        if parent is None:
            self.root = new_node
            print(self.root.node_data)
        else:
            if value < parent.node_data:
                parent.left = new_node
            else:
                parent.right = new_node

    def arrange_lvl_wise(self, total_levels):
        total_nodes = (2 ** total_levels) - 1
        print(f"Total Nodes : {total_nodes}")
        if not self.root:
            print("Tree is empty.")
            return
        my_queue = []
        my_queue.insert(0, self.root)
        self.my_list.append(self.root)
        nodes_processed = 0
        while nodes_processed != total_nodes:
            poped_ele = my_queue.pop(0)
            current = poped_ele
            if current:
                my_queue.append(current.left)
                self.my_list.append(current.left)
                my_queue.append(current.right)
                self.my_list.append(current.right)
            nodes_processed += 1
    def print_lvl_wise(self):
        for address in self.my_list:
            if address is not None:
                print(address.node_data)
            else:
                print("None")

    # def find_duplicates(self, total_levels):
    #     if not self.root:
    #         print("Input the tree first")
    #         return
    #     for address in self.my_list:
    #         parent, location = self.find(address.node_data)
    #         if location:
    #             print(f"NOde with value {address.node_data} has a duplicate")

    def find_duplicates(self, total_levels):
        if not self.root:
            print("Input the tree first")
            return
        print("The list of duplicates are : ")
        print(self.duplicates_list)

if __name__ == "__main__":
    my_bst = BST()
    size = int(input("How many elements you want to insert into BST : "))
    for i in range(size):
        my_bst.insert_node(int(input("Insert an element : ")))
    print(f"{size} elements inserted successfully!")

    my_bst.arrange_lvl_wise(3)
    my_bst.print_lvl_wise()
    my_bst.find_duplicates(3)