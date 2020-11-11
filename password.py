
# so we have to create a password generator
#if it is weak it will be a mix of letters and letters capital or not
#for a medium password it will be a mix of nums letters
#for strong it will be the above but with some special symbols

#ask user to generate a weak, medium ro string password
#lets import the random module and use the random.randint(from,to)

#lets ask the user how long the password must be
#then ask which type of password to pick

#we can make three functions weak,medium,strong and have them return the password
#assign it to a value and display that value to screen
   
#as a challenge we can ask the user to tell us how long the password must be to have a range of different
#random size and random generated
import random
def dic():
	''' This function will create
	a list with all special characters, numbers, upper/lowercase letters
	Returns: list of characters
	args: none
	'''
    l = [ele for ele in "abcdefghijklmnopqrstuvwxyz"]
    l.extend([ele for ele in "abcdefghijklmnopqrstuvwxyz".upper()])
    l.extend("0123456789")
    l.extend("~!@#$%^&*?/")
    return l

def strong(start,end):
	'''
	This function will create a password with 
	random number of characters between 
	a start and end number of characters specified by the user
	The password is strong since it consists of upper/lowercase letters
	and special characters and numbers
	'''
    password = ""
    length = random.randint(start,end)
    listy = dic()
    for i in range(0,length):
        x = str(listy[random.randint(0,72)])
        if x in password:
            while True:
                y = str(listy[random.randint(0,72)])
                if y in password:
                    continue
                else:
                    password += y
                    break
        else:
            password+=x

    print(password)

def weak(start,end):
	'''
	This function will create a password with 
	random number of characters between 
	a start and end number of characters specified by the user
	The password is weak since it consists of upper/lowercase letters
	'''
    password = ""
    length = random.randint(start,end)
    listy = dic()
    for i in range(0,length):
    	#list indices from 0 - 41
        x = str(listy[random.randint(0,41)])
        if x in password:
            while True:
                y = str(listy[random.randint(0,41)])
                if y in password:
                    continue
                else:
                    password += y
                    break
        else:
            password+=x

    print(password)    

print("Hello welcome to my generator")
print("What type of password would you like: weak or strong?")
while(True):
	passtype = input("Enter weak or strong")
	if passtype == "weak" or passtype == "strong":
		break
	else:
		print("Try again, enter weak or strong")

start =int(input("what is the minimum number of digits for your password\n"))
end=int(input("what is the maximum number of digits in your password\n"))
if passtype == "weak":
	weak(start,end)
else:
	strong(start,end)
