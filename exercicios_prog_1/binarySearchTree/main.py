from BST import BST

if __name__ == '__main__':
  bst = BST(5)
  print(bst.root)

  print(bst.insert(1))
  print(bst.insert(4))
  print(bst.insert(2))
  print(bst.insert(23))
  print(bst.insert(12))
  print(bst.insert(6))

  print(bst.search(5))
  print(bst.search(3))
  print(bst.search(2))
  print(bst.search(23))

  print(bst.min)
  print(bst.max)

  print(bst.delete(23))
  print(bst.delete(2))
  print(bst.delete(5))

  print(bst.search(23))
