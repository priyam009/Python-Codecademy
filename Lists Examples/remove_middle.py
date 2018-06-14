#Create a function named remove_middle which has three parameters named lst, start, and end. The function should return a sub-list of lst with all elements with index between start and end removed (inclusive).

def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]
  
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))