import random
import string

print(
    "Welcome to hangman, please choose the number of the available categories:\n1-sport\n2-computer science\n3-europe\n")

done = False
while not done:
    category = input()
    if category == "1":
        with open('sport.txt', 'r') as file:
            words = file.readlines()
            print('Total Words:', len(words))
            break
    elif category == "2":
        with open('cs.txt', 'r') as file:
            words = file.readlines()
            print('Total Words:', len(words))
            break
    elif category == "3":
        with open('europe.txt', 'r') as file:
            words = file.readlines()
            print('Total Words:', len(words))
            break
    else:
        print("Please select one of the available categories")


def get_valid_word(words):
    word = random.choice(words)  # Se extrage un cuvant random din fisierul dat ca input
    while '-' in word or ' ' in word:  # cat timp avem una din cele doua semne, continua sa alegi
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)[:-1]
    lettersWord = set(word)  # literele in cuvant
    alphabet = set(string.ascii_uppercase)
    lettersUsed = set()  # ce a ghicit jucatorul pana acum
    errors = 0
    tries = len(word)  # incercari determinate de catre lungimea cuvantului

    while len(lettersWord) > 0 and tries > 0:

        print('You have', tries, 'tries left and you have used these letters: ', ' '.join(lettersUsed))
        # urmareste progresul jucatorului la cuvantul repsectiv
        word_list = [letter if letter in lettersUsed else '_' for letter in word]
        print('Current word: ', ' '.join(word_list)) # lista pentru a urmari cate litere a folosit jucatorul

        letterUser = input('Guess a letter: ').upper()
        if letterUser in alphabet - lettersUsed: # daca e caracter valid din alfabet, adauga in lista de litere folosite
            lettersUsed.add(letterUser)
            if letterUser in lettersWord: # daca jucatorul a ghicit un cuvant, acel cuvant va fi eliminat din lista pentru a nu se repeta litera respectiva
                lettersWord.remove(letterUser)
                print('')

            else:
                tries = tries - 1  # scade din incercari daca gresim
                errors = errors + 1  # crestem nr de litere gresite pentru a afisa pt scorul final
                print('\nYour letter,', letterUser, 'is not in the word.')

        elif letterUser in lettersUsed:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    if tries == 0:  # daca am irosit numarul de vieti atunci am pierdut
        print(f"You didn't guess, the word was: {word.upper()}")
    # with open('GeneralEvidence.txt', 'a+') as file:
    #    counter = int(file.readline()) + 1
    #   file.write(str(counter))
    #  file.close()
    else:
        if category == "2":
            with open('CsScoreEvidence.txt', 'a+') as file:
                file.write(f'{word}\n')
                file.close()
        elif category == "1":
            with open('SportScoreEvidence.txt', 'a+') as file:
                file.write(f'{word}\n')
                file.close()
        elif category == "3":
            with open('EuropeScoreEvidence.txt', 'a+') as file:
                file.write(f'{word}\n')
                file.close()
        print(
            f"{word.upper()}, {errors}, (The user tried {errors} letters that do not exist in the word from a total of",
            len(word), "letters)")


if __name__ == '__main__':
    hangman()
