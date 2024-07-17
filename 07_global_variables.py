print("\n--------- Way one global variables")
word = "awesome"
def myFunc():
    print("python is " + word)

myFunc()


print("\n--------- Way two global variables")
text = "awesome"
def myFunc():
    text = "fantastic"
    print("python is " + text)
 
myFunc()
print("python is {}".format(text))


print("\n--------- Way three global variables")
def myFunc():
    global msg
    msg = "fantastic"

myFunc()
print("python is " + msg)













