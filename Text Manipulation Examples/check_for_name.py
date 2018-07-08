#Write a function called check_for_name that takes two strings as parameters named sentence and name. The function should return True if name appears in sentence in all lower case letters, all uppercase letters, or with only the first letter capitalized. The function should return False otherwise

def check_for_name(sentence, name):
  if sentence.lower().find(name.lower()) == -1:
    return False
  else:
    return True