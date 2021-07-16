name = "Faruk"
password = "W1q2a3@"

given_name = str(input("Please enter your name :"))

if given_name == name :
    print("Hello, {}! The password is : {}".format(given_name, password))
else:
    print("Hello, {}! See you later.".format(given_name))
