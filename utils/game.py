import random

class Hangman:
    def __init__(self):
        # Word dictionary to choose random words from
        self.wordDictionary = ["python", "beefeater", "seaturtle", "oxygen", "eazy", "wow", "sacha"]
        
        # Randomly choose a word from the dictionary
        self.randomWord = random.choice(self.wordDictionary)
        
        # Length of the word to guess
        self.length_of_word_to_guess = len(self.randomWord)
        
        # Number of incorrect guesses
        self.amount_of_times_wrong = 0
        
        # Index to keep track of the current letter being guessed
        self.current_guess_index = 0
        
        # List to store the letters guessed so far
        self.current_letters_guessed = []
        
        # Number of correctly guessed letters
        self.current_letters_right = 0

    def print_hangman(self, wrong):
        # Print the hangman drawing per wrong guesses
        if wrong == 0:
            print("\n +---+")
            print("     |")
            print("     |")
            print("     |")
            print("    ===")
        elif wrong == 1:
            print("\n +---+")
            print(" O   |")
            print("     |")
            print("     |")
            print("    ===")
        elif wrong == 2:
            print("\n +---+")
            print(" O   |")
            print(" |   |")
            print("     |")
            print("    ===")
        elif wrong == 3:
            print("\n +---+")
            print(" O   |")
            print("/|   |")
            print("     |")
            print("    ===")
        elif wrong == 4:
            print("\n +---+")
            print(" O   |")
            print("/|\  |")
            print("     |")
            print("    ===")
        elif wrong == 5:
            print("\n +---+")
            print(" O   |")
            print("/|\  |")
            print("/    |")
            print("    ===")
        elif wrong == 6:
            print("\n +---+")
            print(" O   |")
            print("/|\  |")
            print("/ \  |")
            print("    ===")

    def printWord(self, guessedLetters):
        counter = 0
        rightLetters = 0
        for char in self.randomWord:
            if char in guessedLetters:
                # Print the correctly guessed letters
                print(self.randomWord[counter], end=" ")
                rightLetters += 1
            else:
                # Print spaces for letters not yet guessed
                print(" ", end=" ")
            counter += 1
        return rightLetters

    def printLines(self):
        # Print a line of underscores to represent the word to be guessed
        print("\r")
        for char in self.randomWord:
            print("_", end=" ")

    def input(self, prompt):
        # Wrapper for the input function to use within the class
        return input(prompt)

    def start_game(self):
        print("Welcome to Hangman!")
        print("-------------------")

        # Print initial underscores representing the word to be guessed
        for _ in self.randomWord:
            print("_", end=" ")

        while self.amount_of_times_wrong != 6 and self.current_letters_right != self.length_of_word_to_guess:
            print("\nLetters guessed so far: ")
            for letter in self.current_letters_guessed:
                print(letter, end=" ")

            # Prompt the user to guess a letter
            letterGuessed = self.input("\nGuess a letter: ")

            if self.randomWord[self.current_guess_index] == letterGuessed:
                # User guessed the correct letter
                self.print_hangman(self.amount_of_times_wrong)
                self.current_guess_index += 1
                self.current_letters_guessed.append(letterGuessed)
                self.current_letters_right = self.printWord(self.current_letters_guessed)
                self.printLines()
            else:
                # User guessed the wrong letter
                self.amount_of_times_wrong += 1
                self.current_letters_guessed.append(letterGuessed)
                self.print_hangman(self.amount_of_times_wrong)
                self.current_letters_right = self.printWord(self.current_letters_guessed)
                self.printLines()

        print("GAME OVER")
