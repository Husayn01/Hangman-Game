import random
from hangManPics import pics, hangManArt

print(hangManArt)
wordList = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
secretWord = random.choice(wordList)
attemptLeft = len(secretWord)

progress = []
for letter in secretWord:
    progress.append("_")
print("Player's progress: ",  ' '.join( progress))
print("Attempt left: ", attemptLeft)

while attemptLeft > 0 and "_" in progress:
    guess = input("Guess a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid guess, please enter a single letter")
        continue
    if guess in secretWord:
        for n in range(len(secretWord)):
            if secretWord[n] == guess:
                progress[n] = guess
    else:
        attemptLeft -= 1
        print(pics[attemptLeft])
        print(f"Incorrect guess, you've lost a life")
        print(attemptLeft,"attempt left")
    if "_" not in progress:
        print("Congratulations! You guessed the word correctly!")
    if attemptLeft == 0:
        print("Game over! The word was: ",''.join(secretWord))
    print("Player's progress:", ' '.join( progress))
    print("\n")