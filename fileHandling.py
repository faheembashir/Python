##################### Tradational way of file handling #####################

# f=open("logic.txt","w")
# f.write("Hello faheem")
# f.close()



# f=open("logic.txt","a")
# f.write(" and zaieem")
# f.close()


# f=open("logic.txt","r")
# print(f.read())
# f.close()

# f=open("logic.txt","x")
# f.write('hello')
# f.close()


################ Modern way of file handling ########################

with open("key.txt","w") as file:
    file.write("hello python")

with open("key.txt",'a') as file:
    file.write(" and java")
with open ("key.txt",'r') as file:
    print(file.read())
