"""
🌳 What is a Tree?

A tree is a collection of nodes connected by edges, with these properties:

One special node called the root
Every node can have zero or more children
No cycles (unlike graphs)
Exactly one path between any two nodes
🧩 Basic Terminology
Node: An element in the tree
Root: The topmost node
Parent / Child: Relationship between connected nodes
Leaf node: Node with no children
Subtree: A tree formed by a node and its descendants
Depth: Distance from root to a node
Height: Longest path from a node to a leaf
🌲 Types of Trees
1. Binary Tree

Each node has at most 2 children (left and right).

Variants:
Full Binary Tree: Every node has 0 or 2 children
Complete Binary Tree: All levels filled except possibly last, filled left to right
Perfect Binary Tree: All internal nodes have 2 children, all leaves at same level
2. Binary Search Tree (BST)

A special binary tree with ordering:

Left subtree values < node value
Right subtree values > node value

➡️ Enables efficient searching (average O(log n))

3. Balanced Trees

Trees that maintain height balance for efficiency.

Examples:

AVL Tree
Red-Black Tree

➡️ Keep operations like search/insert/delete in O(log n)

4. Heap (Binary Heap)

Used in priority queues.

Min Heap: Parent ≤ children
Max Heap: Parent ≥ children

➡️ Root always has min or max value

5. Trie (Prefix Tree)

Used for strings and fast prefix searching.

Example uses:

Autocomplete
Spell checking
6. N-ary Tree

Each node can have more than 2 children.

🔁 Tree Traversals

Ways to visit nodes:

Depth First Traversal (DFS):
Inorder (LNR) → Left, Node, Right
Preorder (NLR) → Node, Left, Right
Postorder (LRN) → Left, Right, Node
Breadth First Traversal (BFS):
Level order traversal (using queue)
⚙️ Common Operations
Insertion
Deletion
Searching
Traversal

Time complexity depends on tree type:

Balanced trees → O(log n)
Skewed trees → O(n)
💡 Why Trees Matter

Trees are everywhere in computer science:

File systems
Databases (indexing with B-trees)
Compilers (syntax trees)
Networking (routing trees)
AI (decision trees)

EXAMPLE

        10
       /  \
      5    20
     / \     \
    3   7     30

Root = 10
Leaf nodes = 3, 7, 30
Height = 2

🚀 When to Use Trees

Use trees when:

Data is hierarchical
You need fast search/insert/delete
You need sorted data (BST)
You need priority handling (Heap)

"""