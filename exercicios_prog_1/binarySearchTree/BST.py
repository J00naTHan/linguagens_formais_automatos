from Node import Node

class BST:
  def __init__(self, root):
    self.root = Node(root) if type(root) == int else None
    self.min = self.root
    self.max = self.root
    self.size = 1 if type(root) == Node else 0
    self.depth = 0
    del self.root.parent

  def inorder(self):
    root = self.root
    if root is not None:
      inorder(root.left)
      inorder(root.right)

  def search(self, key):
    node = self.root
    while node is not None and node.key != key:
      if key < node.key:
        node = node.left
        continue
      elif key > node.key:
        node = node.right
        continue
    else:
      return node

  def insert(self, value):
    if type(value) == int:
      inserted = Node(value)
      node = self.root
      nodeParent = None
      while node is not None:
        nodeParent = node
        if value < node.key:
          node = node.left
          continue
        elif value > node.key:
          node = node.right
          continue
        else:
          return None
      else:
        inserted.parent = nodeParent
        if nodeParent > inserted and inserted < self.root:
          self.min = nodeParent.left = inserted
        elif nodeParent < inserted and inserted > self.root:
          self.max = nodeParent.right = inserted
        self.size += 1
        return inserted
    else:
      return None

  def delete(self, key):
    root = self.root

    if root is None:
      return root

    if root.key > key:
      root.left = delete(root.left, key)
      return root
    elif root.key < key:
      root.right = delete(root.right, key)
      return root

    if root.left is None:
      temp = root.right
      del root
      return temp
    elif root.right is None:
      temp = root.left
      del root
      return temp

    else:
      parent = root

      successor = root.right
      while successor.left is not None:
        parent = successor
        successor = successor.left

      if successor.parent != root:
        parent.left = successor.right
      else:
        parent.right = successor.right
  
      root.key = successor.key

      del successor
      return root
