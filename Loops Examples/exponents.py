#Create a function named exponents that takes two lists as parameters named bases and powers. Return a new list containing every number in bases raised to every number in powers.

def exponents(base, powers):
  new_lst= []
  for i in base:
    for j in powers:
      new_lst.append(i ** j)
  return new_lst


print(exponents([2, 3, 4], [1, 2, 3]))