print("~~~HERE IS YOUR  BASIC RULE BASED CHATBOT~~~")
c='y'
while c in 'yY':
    x=input("Enter: ")
    if x.lower()=="hello":
        print("Hi!")
    elif x.lower()=="hi":
        print("Hello!")
    elif x.lower()=="how are you":
        print("I'm fine, Thanks!")
    elif x.lower()=="what's your name":
        print("I'm your Chatbot!")
    elif x.lower()=="thank you":
        print("You're welcome!")
    elif x.lower()=="bye":
        print("Goodbye!")
        y=input("DO YOU WANNA CONTINUE (Y/N): ")
        if y in "nN":
            print("CHATBOT IS CLOSING....")
            break
        elif y in "yY":
            pass
        else:
            print("Invalid Input")
    else:
        print("Sorry, I haven't learned how to respond to that yet!")

        
    
