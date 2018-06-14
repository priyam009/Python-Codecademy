#Create a function called append_size that has one parameter named lst. The function should add all of the numbers between 1 and the size of lst (inclusive) to the end of lst. The function should then return this new list.

def append_size(lst):
  length = len(lst)
  lst1 = list(range(1, length + 1))
  new_lst = lst + lst1
  return new_lst


print(append_size([23, 42, 108]))