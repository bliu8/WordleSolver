wrongspot, correctspot, correctspot2, wrongspot2 = {}, {}, {}, {}

with open("words.txt", "r") as f:
    words = [word.strip() for word in f.readlines()]

words.remove('pupa')
words.append('pupal')

print("Suggested guesses: oater, crane")
print(len(words))

gameOver = False

while not gameOver:
    x = int(input("1: gray, 2: yellow, 3: green, 4: continue \n"))

    if x == 1:
        letter = input("What letter is it?")
        words = [word for word in words if letter not in word or (letter in correctspot2 and any(word[z-1] == letter for z in correctspot2[letter]))]
    
    elif x == 2:
        letter = input("What letter was it?")
        spot = int(input("What spot is it in? 1 for first letter, 5 for last"))
        wrongspot.setdefault(letter, []).append(spot)
        words = [word for word in words if any(word[z-1] != letter and letter in word for z in wrongspot[letter])]
        
        if wrongspot:
            wrongspot2.update(wrongspot)
            wrongspot.clear()
    
    elif x == 3:
        letter = input("What letter was it?")
        spot = int(input("What spot is it in? 1 for first letter, 5 for last"))
        
        if letter not in correctspot:
            correctspot[letter] = [spot]
            words = [word for word in words if any(word[z-1] == letter for z in correctspot[letter])]
            
            if correctspot:
                correctspot2.update(correctspot)
                correctspot.clear()
        else:
            print("I already know!")
    
    print(words)
    print(len(words))
