# Task 1: Write a function that takes the string word as a parameter.
# The function should return the total number of unique letters in the string. 
# Uppercase and lowercase letters should be counted as different letters.

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def uniqueEnglishLetters(word):
  count = 0
  for letter in letters:
    if letter in word:
      count +=1
  return count

# Test - Should return 4
print(uniqueEnglishLetters("Mississippi"))

# Test - Should return 4 again
print(uniqueEnglishLetters("Apple"))
print("-----------------")
# Task 2: Write a function that takes a string named 
# word and a single character named x as parameters. 
# The function should return the number of times x appears in word.

def characterCount(word,character):
  count = 0
  for letter in word:
    if character == letter:
      count +=1
  return count
# Test 1: Should print 4
print(characterCount("mississippi", "s"))
# Test 2: Should print 1
print(characterCount("mississippi", "m"))
print("-----------------")
# Task 3: Write a function named count_multi_char_x that takes a string named word and a string named x. 
# This function should return the number of times x appears in word. 
# However, this time, make sure your function works when x is multiple characters long.
def count_multi_char_x(word, x):
  splits = word.split(x)
  return(len(splits)-1)

# Test 1 should print 2
print(count_multi_char_x("mississippi", "iss"))
# Test 2: should print 1
print(count_multi_char_x("apple", "pp"))
print("-----------------")
# Task 4: Write a function that takes a string named word, 
# a single character named start, and another character named end. 
# This function should return the substring between the first occurrence of start and end in word.
# If start or end are not in word, the function should return word. 

def substringWithinAWord(word, start, end):
  # get index of start to be used in slice
  startIndex = word.find(start)
  endIndex = word.find(end)
  if start and end in word:
    return word[startIndex+1:endIndex]
  return word
# Test 1 - Should print 'pl'
print(substringWithinAWord("apple", "p", "e"))
# Test 2 - Should print the word
print(substringWithinAWord("apple", "p", "c"))
print("-----------------")
# Task 5: Create a function that takes a string and an int as an argument
# The function should return true if every word in the sentence has a length greater than x

def wordLengthCounter(sentence, minimumLength):
  words = sentence.split(" ")
  for word in words:
    if len(word) < minimumLength:
      return False
  return True

# Test 1 - Should return False
print(wordLengthCounter("I like apples", 2))
#Test 2 - Should return True
print(wordLengthCounter("He likes apples", 2))
print("-----------------")

# Create a function that takes in a string as a parameter and returns that string in reverse
def reverseString(word):
  stringReversed = ""
  for i in range(len(word) -1, -1, -1):
    stringReversed += word[i]
  return stringReversed

# Test 1 - "Timothy"
print(reverseString("Timothy"))
#Test 2 - ""
print(reverseString(" "))
print("-----------------")