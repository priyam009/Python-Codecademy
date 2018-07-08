#Create a function called x_length_words that takes a string named sentence and an integer named x as parameters. This function should return True if every word in sentence has a length greater than or equal to x.

def x_length_words(sentence, x):
  sentence = sentence.split()
  count = 0
  for word in sentence:
    for letter in word:
      count += 1
    if count < x:
      return False
      break
    count = 0
  return True


print(x_length_words("i like apples", 2))

print(x_length_words("he likes apples", 2))
