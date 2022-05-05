import random
a=["Welcome","random" ,"words" ,"generator" , "English", "python" ,"programming" ,"atitsharma" ,"family" ,"school", "secret", "coding"]
word=random.choice(a)
attempt_guess=5
guesses=[]
done=False
while not done :
    for letters in word:
        if letters.lower() in guesses:
            print(letters,end=" ")
        else:
            print("_",end=" ")
    print(" ")


    guess=input("Guess a Word")
    guesses.append(guess.lower())
    if guess.lower() not in word:
        attempt_guess-=1
    if guess.lower() in word:
        attempt_guess+=0



    if attempt_guess<0:
        print(f"You ran out of attempt!.Game over!!")
        break


    done=True
    for letters in word:
        if letters.lower() not in guesses:
            done=False

if done:
    print(f"You made it the word in {attempt_guess} guess .The correct word is  {word}")
else:
    print(f"Game over! The word was {word}")


