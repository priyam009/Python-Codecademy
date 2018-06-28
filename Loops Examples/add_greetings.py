#Create a function named add_greetings which takes a list of strings named names as a parameter. In the function, use list comprehension to add the string "Hello, " in front of each name in names. Return the new list containing the greetings.

def add_greetings(names):
  new_name = ["Hello, " + name for name in names]
  return new_name

print(add_greetings(["Owen", "Max", "Sophie"]))