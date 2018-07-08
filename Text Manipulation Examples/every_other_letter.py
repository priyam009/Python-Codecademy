#Create a function named every_other_letter that takes a string named word as a parameter. The function should return a string containing every other letter in word.

def every_other_letter(word):
  index = 0
  temp = []
  for index in range(0, len(word)-1):
    if index % 2 == 0:
      temp.append(word[index])
  temp = ''.join(temp)
  return temp