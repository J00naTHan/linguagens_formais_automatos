class Node:
  def __init__(self, value):
    self.key = value if type(value) == int else None
    self.parent = None
    self.left = None
    self.right = None

  def __str__(self):
    return str(self.key)

  def __bool__(self):
    return self.key

  def __eq__(self, other):
    return self.key == other.key

  def __ne__(self, other):
    return self.key != other.key

  def __lt__(self, other):
    return self.key < other.key

  def __le__(self, other):
    return self.key <= other.key

  def __gt__(self, other):
    return self.key > other.key

  def __ge__(self, other):
    return self.key >= other.key
