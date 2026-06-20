import random

# List of words
words = ["python", "computer", "student", "project", "hangman"]

# Select a random word
word = random.choice(words)

# Create hidden word display
display = ["_"] * len(word)

# Store guessed letters
guessed_letters = []

# Number of attempts
attempts = 6

print("🎮 Welcome to Hangman Game!")
print("Guess the word:", " ".join(display))

while attempts > 0 and "_" in display:

    guess = input("\nEnter a letter: ").lower()

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct Guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess

    else:
        attempts -= 1
        print("❌ Wrong Guess!")
        print("Attempts left:", attempts)

    print("Word:", " ".join(display))

# Game result
if "_" not in display:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over!")
    print("The correct word was:", word)