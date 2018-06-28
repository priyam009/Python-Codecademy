#Create a function named larger_sum that takes two lists of numbers as parameters named lst1 and lst2. The function return the list whose elements sum to the greater number. If the sum of the elements of each list are equal, return lst1.

def larger_sum(lst1, lst2):
  sum_lst1 = 0
  sum_lst2 = 0
  
  for i in lst1:
    sum_lst1 += i
  for j in lst2:
    sum_lst2 += j
    
  if sum_lst1 >= sum_lst2:
    return lst1
  else:
    return lst2


print(larger_sum([1, 9, 5], [2, 3, 7]))