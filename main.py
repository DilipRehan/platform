import platform

print("Enter your name:", end= '')
name = input()
print("Hello "+name+" You are using "+platform.system()+"\n")
if platform.system() == "Windows":
    print("You are using windows OS")
else if :
    print("You are using Linux")
