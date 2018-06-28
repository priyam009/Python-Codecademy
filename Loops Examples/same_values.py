#Write a function named same_values that takes two lists of numbers of equal size as parameters. The function should return a list of the indices where the values were equal in lst1 and lst2.

def same_values(lst1, lst2):
  new_lst = []
  for i in range(len(lst1)):
    if lst1[i] == lst2[i]:
      new_lst.append(i)
  return new_lst

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))