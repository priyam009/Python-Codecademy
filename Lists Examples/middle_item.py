def middle_element(lst):
  if len(lst) % 2 == 0:
    length = int(len(lst) / 2)
    return (lst[length] + lst[length - 1]) / 2
  else:
    length = int(len(lst) / 2)
    return (lst[length])


print(middle_element([5, 2, -10, -4, 4, 5]))