pali = input("palindrome detector type one word:")

pali2 = pali[::-1]

if pali.lower() == pali2.lower() :
  print("True")
  
else:
  print("false")
  
