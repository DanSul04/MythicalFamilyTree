class CreatureNode:
    # Creature class
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class MythicalFamilyTree:
    # Tree class
    def __init__(self):
        self.root = None

    def add_root(self, name):
        if not self.root:
            self.root = CreatureNode(name)
            print(f"Root '{name}' added.")
        else:
            print("Root already exists.")

    # Add child method
    def add_child(self, parent_name, child_name, position):
        parent = self.search(self.root, parent_name)
        if not parent:
            # alert user if not parent
            print(f"Parent '{parent_name}' not found.")
            return
        '''user can add child to position left/right
            and will be alerted if position is occupied'''
        if position == "left" and not parent.left:
            parent.left = CreatureNode(child_name)
            print(f"Added '{child_name}' as the left child of '{parent_name}'.")
        elif position == "right" and not parent.right:
            parent.right = CreatureNode(child_name)
            print(f"Added '{child_name}' as the right child of '{parent_name}'.")
        else:
            print(f"{position.capitalize()} child already exists for '{parent_name}' or invalid position.")

    def search(self, node, name):
        # Pre-Order Traversal, node/left/right
        if not node:
            return None
        if node.name == name:
            return node
        return self.search(node.left, name) or self.search(node.right, name)

    def print_tree(self, node, level=0):
        # In-Order Traversal, Reversed- right/node/left
        if node:
            self.print_tree(node.right, level + 1)
            print(" " * 5 * level + "--> " + node.name)
            self.print_tree(node.left, level + 1)

    def find_ancestors(self, node, target_name, ancestors):
        '''Post-Order Traversal, left/right/node'''
        if not node:
            return False
        if node.name == target_name:
            return True
        if (self.find_ancestors(node.left, target_name, ancestors) or
            self.find_ancestors(node.right, target_name, ancestors)):
            ancestors.append(node.name)
            return True
        return False

    def get_ancestors(self, name):
        ancestors = []
    # find_ancestors defined in get_ancestors to use its variables
        def find_ancestors(node, target_name):
            if not node:
                return False
            if node.name == target_name:
                return True
        
            if (find_ancestors(node.left, target_name) or
                find_ancestors(node.right, target_name)):
                ancestors.append(node.name)
                return True
            return False

    
        if find_ancestors(self.root, name):
            print(f"Ancestors of '{name}': {', '.join(ancestors)}")
        else:
            print(f"'{name}' not found in the tree.")



def menu():
    tree = MythicalFamilyTree()
    # check if root has been added
    root_added = False

    while True:
        print("\nMenu:")
        
        # Add Root option only appears if there is no root
        if not root_added:
            print("0. Add Root")
        else:
            print("1. Add Creature")
            print("2. Print Ancestors")
            print("3. Print Tree")
            print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "0" and not root_added:
            name = input("Enter the name of the root creature: ")
            tree.add_root(name)
            root_added = True  #True once root is added
            
        elif choice == "1":
            parent_name = input("Enter the creature's parent's name: ")
            child_name = input("Enter the creatures's name: ")
            position = input("Enter the position (left/right): ").lower()
            tree.add_child(parent_name, child_name, position)
        
        elif choice == "2":
            name = input("Enter the name of the creature to search: ")
            tree.get_ancestors(name)
        
        elif choice == "3":
            if tree.root:
                print("The Mythical Family Tree:")
                tree.print_tree(tree.root)
            else:
                print("The tree is empty.")
        
        elif choice == "4":
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    menu()

