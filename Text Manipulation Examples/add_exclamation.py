#Create a function named add_exclamation that has one parameter named word. This function should add exclamation points to the end of word until word is 20 characters long. If word is already at least 20 characters long, just return word.

def add_exclamation(word):
  if len(word) >=20:
    return word
  else:
    sentence_with_exclamation = []
    sentence_with_exclamation.append(word)
    index = len(word)
    for index in range (len(word), 20):
      sentence_with_exclamation.append('!')
    sentence_with_exclamation = ''.join(sentence_with_exclamation)
    return sentence_with_exclamation
      

# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn