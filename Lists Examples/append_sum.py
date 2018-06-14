#Write a function named append_sum that has one parameter named lst. The function should add the last two elements of lst together and append the result to lst. It should do this process three times and then return lst.

def append_sum(lst):
  last_two_add = lst[-1] + lst[-2]
  lst.append(last_two_add)
  
  last_two_add = lst[-1] + lst[-2]
  lst.append(last_two_add)
  
  last_two_add = lst[-1] + lst[-2]
  lst.append(last_two_add)
  return lst


print(append_sum([1, 1, 2]))