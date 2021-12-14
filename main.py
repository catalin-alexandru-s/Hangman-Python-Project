import random
import string
import json

SAVE_PATH = "Result\\results.json"


def get_categories():
    try:
        with open("Categories\\categories.txt", 'r') as f:
            return [i[:-1] for i in f.readlines()]
    except FileNotFoundError as fnf_error:
        print(fnf_error)


def user_chose(options, str):
    while True:
        choose = input(str)
        if choose.isnumeric():
            choose = int(choose)
            if choose <= len(options):
                return options[choose]
        elif choose in options:
            return choose
        else:
            print(f"Type something valid, either a number between 0 and {len(options) - 1}")


def get_word_list(cat):
    try:
        with open(f"Categories\\{cat}.txt") as f:
            return [i[:-1] for i in f.readlines()]
    except FileNotFoundError as fnf_error:
        print(fnf_error)


def hangman(game_rounds):
    categories = get_categories()
    category = user_chose(categories, "Choose a category: ")
    words = get_word_list(category)
    word = random.choice(words).upper()
    letters_set = set(word)
    alphabet = set(string.ascii_uppercase)
    lettersUsed = set()
    errors = 0
    tries = len(word)

    while len(letters_set) > 0 and tries > 0:

        print('You have', tries, 'tries left and you have used these letters: ', ' '.join(lettersUsed))

        word_list = [letter if letter in lettersUsed else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))

        input_letter = input('Guess a letter: ').upper()
        if input_letter in alphabet - lettersUsed:
            lettersUsed.add(input_letter)
            if input_letter in letters_set:
                letters_set.remove(input_letter)
                print('')

            else:
                tries = tries - 1
                errors = errors + 1
                print('\nYour letter,', input_letter, 'is not in the word.')

        elif input_letter in lettersUsed:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    if tries == 0:
        print(f"You didn't guess, the word was: {word.upper()}")
    else:
        print(
            f"{word.upper()}, {errors}, (The user tried {errors} letters that do not exist in the word from a total of",
            len(word), "letters)")
    return {
        "round": game_rounds,
        "category": category,
        "word": word,
        "attempts": len(word),
        "wrong-attempts": errors
    }


def game():
    try:
        with open(SAVE_PATH, 'r') as json_read:
            game_results = json.load(json_read)
    except Exception:
        game_results = []

    game_rounds = len(game_results)
    while True:
        game_rounds += 1
        result = hangman(game_rounds)
        game_results.append(result)
        with open(SAVE_PATH, 'w') as json_file:
            json.dump(game_results, json_file, indent=2)
        new_game = user_chose(['yes', 'no', 'n', 'y'], "\nWanna play again? (y/n): ")
        if new_game == 'y' or new_game == 'yes':
            print("Continuing...")
        elif new_game.lower() == 'n' or new_game.lower() == 'no':
            print("Game ended.")
            break


if __name__ == "__main__":
    game()
