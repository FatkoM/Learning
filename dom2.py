import random

while True:
    wrong_guesses=0
    words=["Apple", "Banana", "Umbrella", "Gay"]

    random_word = [*random.choice(words)]

    print(random_word)

    underscores=["_ "]*len(random_word)
    for i in underscores:
        print(i,end="")

    
    while "_ " in underscores:
        guess = input("Input a letter ")
        
        if guess in random_word:
            guess_index = random_word.index(guess)
            for i in random_word:
                if i == guess:
                    underscores1 = underscores.pop(guess_index)
                    print(underscores)
                
            #underscores= underscores.insert(guess_index, guess)
            print(underscores)
            
