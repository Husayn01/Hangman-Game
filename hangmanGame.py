import random
print('''                                           
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
         ''')
wordList = ('ant badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         ' hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark  skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
secretWord = random.choice(wordList)
attemptLeft = len(secretWord)

progress = []
for letter in secretWord:
    progress.append("_")
print("Player's progress: ", progress)
print("Attempt left: ", attemptLeft)

while attemptLeft > 0 and "_" in progress:
    guess = input("Guess a letter: ").lower()
    if len(guess) != 1:
        print("Invalid guess, please enter a single letter")
        continue
    if guess in secretWord:
        for letter in secretWord:
            if guess == letter:
                n = secretWord.index(letter)
                progress[n] = letter
    else:
        attemptLeft -= 1
        print("Incorrect guess")
        print(attemptLeft,"attempt left")
    if "_" not in progress:
        print("Congratulations! You guessed the word correctly!")
    if attemptLeft == 0:
        print("Game over! The word was: ", secretWord)
    print("Player's progress: ", progress)