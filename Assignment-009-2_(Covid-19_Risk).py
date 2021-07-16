age = input("Are you a cigarette addict older than 75 years old? ('Yes' or 'No') : ").capitalize()
chronic = input("Do you have a severe chronic disease? ('Yes' or 'No') : ").capitalize()
immune = input("Is your immune system too weak? ('Yes' or 'No') : ").capitalize()
risk = (age == "Yes") or (immune == "Yes") or (chronic == "Yes")
if risk :
    print("You are in risky group")
else :
    print("You are not in risky group")
