#Password Validator
password = (input ("Type a password: "))
validity = 0
special_characters = ["@","#","₱","&","%","-","+","=","/",";",":",",", "$","¥","_","^","[","~","!","?"]
numbers = ["1","2","3","4","5","6","7","8","9","0"]
capital_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
if (len(password)) >= 15:
    validity += 1
if any (char in special_characters for char in password):
    validity += 1
if any (char in numbers for char in password):
    validity += 1
if any (char in capital_letters for char in password):
    validity += 1
if validity == 4:
    print (" The password is valid")
else:
    print ("The password is invalid")