text = input("Type sentence here:")
counter_txt = {word.lower(): text.lower().split().count(word.lower()) for word in text.split()}          

print(counter_txt)             
