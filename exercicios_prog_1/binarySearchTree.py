from Node import Node

class BST:
  def __init__(self, root):
    self.root = Node(root) if type(root) == int else None
    self.min = self.root
    self.max = self.root
    self.size = 1 if type(root) == Node else 0
    self.depth = 0
    del self.root.parent

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
    pass
