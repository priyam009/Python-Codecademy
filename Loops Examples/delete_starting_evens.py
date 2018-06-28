#Write a function called delete_starting_evens that has a parameter named lst. The function should remove element from the front of lst until the front of the list is not even. The function should then return lst.

def delete_starting_evens(lst):
  for i in lst:
    if i % 2 == 0:
      break
  return lst[i-1:]
  

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))