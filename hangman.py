import random
l=['Umbrella', 'Parrot', 'Computer', 'Movie', 'Snacks']
print("-------------------------------------------------------")
print("        HANGMAN GAME BEGINS!!")
print("-------------------------------------------------------")
print("INSTRUCTIONS:\n1. You can only make 6 wrong guesses\n2. Once your 6 wrong guesses are over, the game would end ")
ch='y'
while ch not in 'nN':
    g=6
    gsd=[]
    word=random.choice(l)
    ln=len(word)
    print("So your word is", end=' ')
    w='-'*ln
    print(w)
    print("So the game starts now!!")
    while g!=0:
        inp = input("Enter letter: ").lower()
        if not inp.isalpha():
            print("Please enter a letter.")
            continue
        if len(inp)!=1:
            print("Please enter only one letter.")
            continue
        if inp in gsd:
            print("You already guessed that letter!")
            continue
        gsd.append(inp)
        if inp in word.lower():
            print("Your guess is Correct!!\nNow the word is,")
            wl = list(w)
            for i in range(len(word)):
                if word[i].lower() == inp:
                    wl[i] = inp
            w = ''.join(wl)
            print(w)
        else:
            g-=1
            print("Wrong Guess \nYou have ",g,"more guesses left")
        if '-' not in w:
            break
    if '-' not in w:
        print("GAME OVER!! YOUR GUESS IS CORRECT\nTHE WORD IS '",w,"'")
    elif g==0:
        print("YOU ARE OUT OF GUESSES, THE MAN IS HANGED :(\n THE CORRECT WORD IS '",word,"'")
    ch=input(" Do you wanna play again(Y/N): ")
            

            
            
            
                
            
        
        
