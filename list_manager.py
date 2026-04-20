name = input("welcome to lists what is your name ")

name1 = input("welcome " + name + " to lists. What is the name of your current list ")

print("welcome to " + name1 + ". To add an item type <add \"insert item\">, to remove an item type <remove \"insert item\">, to view your list type <view>. ")
user_list = []
while True:
  comand = input("awating input:")
  if comand.startswith("add"):
    item = comand[4:].strip()
    user_list.append(item)
  elif comand.startswith("remove"):
    item2 = comand[7:].strip()
    user_list.remove(item2)
  elif comand == "view":
    print(user_list)
    break
