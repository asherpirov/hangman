"https://github.com/asherpirov/hangman.git"
import random
WORDS = [
    "apple", "banana", "orange", "grape", "melon", "water", "house", "table", "chair", "window",
    "school", "teacher", "student", "pencil", "paper","computer", "keyboard", "mouse", "screen",
    "phone","music", "guitar", "piano", "drum", "song",
    "river", "ocean", "beach", "mountain", "forest", "animal", "tiger", "lion", "zebra", "monkey",
    "rabbit", "horse", "sheep", "goat", "camel", "bird", "eagle", "snake", "fish", "shark",
    "pizza", "bread", "cheese", "salad", "soup", "coffee", "sugar", "honey", "butter", "cookie",
    "happy", "angry", "funny", "quiet", "brave", "smart", "strong", "clean", "dirty", "small",
    "large", "short", "long", "early", "late", "green", "yellow", "purple", "black", "white",
    "silver", "gold", "brown", "pink", "blue", "summer", "winter", "spring", "autumn", "season",
    "morning", "night", "today", "tomorrow", "yesterday", "family", "father", "mother", "brother", "sister",
    "friend", "people", "child", "baby", "woman", "man", "doctor", "driver", "soldier", "police",
    "engineer", "artist", "farmer", "chef", "pilot", "city", "village", "street", "bridge", "garden",
    "market", "store", "hotel", "airport", "station", "travel", "ticket", "train", "plane", "bottle",
    "camera", "picture", "letter", "number", "answer", "question", "game", "winner", "player", "score",
    "level", "start", "finish", "secret", "danger", "dream", "story", "movie", "book", "lesson",
    "language", "english", "hebrew", "word", "sentence", "voice", "sound", "light", "shadow", "fire",
    "earth", "stone", "metal", "wood", "glass", "cloud", "rain", "storm", "snow", "wind",
    "heart", "brain", "hand", "finger", "shoulder",  "body", "face", "mouth", "tooth", "eye",
    "jump", "run", "walk", "swim", "drive", "write", "read", "speak", "listen", "learn",
    "build", "break", "open", "close", "catch", "throw", "bring", "carry", "choose", "change",
    "create", "delete", "search", "print", "input", "output", "random", "python", "function", "variable",
    "loop", "condition", "string", "list", "index", "error", "program", "project", "folder", "file"
]


# קודי צבעים להדפסה בטרמינל
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

# ציור פתיחה מרהיב למשחק
WELCOME_ART = CYAN + r"""
══════════════════════════════════════════════════════════════
""" + YELLOW + r"""
  _   _      _      _   _    ____   __  __      _      _   _ 
 | | | |    / \    | \ | |  / ___| |  \/  |    / \    | \ | |
 | |_| |   / _ \   |  \| | | |  _  | |\/| |   / _ \   |  \| |
 |  _  |  / ___ \  | |\  | | |_| | | |  | |  / ___ \  | |\  |
 |_| |_| /_/   \_\ |_| \_|  \____| |_|  |_| /_/   \_\ |_| \_|
""" + CYAN + r"""
══════════════════════════════════════════════════════════════
""" + RESET

# ציור צבעוני לניצחון בכתב בלוקים ברור
YOU_WON_ART = GREEN + r"""
★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★
""" + YELLOW + r"""
 __   __ ___  _   _   __      __ ___  _  _  __ 
 \ \ / // _ \| | | |  \ \    / // _ \| \| | | |
  \ V /| | | | | | |   \ \/\/ /| | | | .` | | |
   | | | |_| | |_| |    \    / | |_| | |\ | |_|
   |_|  \___/ \___/      \/\/   \___/|_| \_|(_)
""" + GREEN + r"""
★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★
""" + RESET

# ציור צבעוני להפסד בכתב בלוקים ברור
GAME_OVER_ART = RED + r"""
☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠

   ____   ___  __  __  ____    ___  _  _  ____  ____  
  / ___| / _ \|  \/  || ___|  / _ \| || || ___||  _ \ 
 | |  _ | |_| | |\/| || |__  | | | | || || |__ | |_) |
 | |_| ||  _  | |  | ||  __| | |_| | \/ ||  __||  _ < 
  \____||_| |_|_|  |_||____|  \___/ \__/ |____||_| \_\

☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠
""" + RESET

MAX_TRIES = 6

def random_word():
    return random.choice(WORDS)

def hidden_word(word) -> list:
    return list("_" * len(word))

def if_guess_word(word, guess):
    return guess in word

def print_the_hidden_word(hide_word):
    print("The guess word:", " ".join(hide_word))
    return None

def validate_input(user_input):
    if len(user_input) != 1:
        print("Please try again, write only one letter.")
        return False
    elif not user_input.isalpha():
        print("Please try again, write only letters.")
        return False
    return True

def get_letter_input():
    while True:
        user_input = input("Please enter a letter: ")
        if validate_input(user_input):
            return user_input

def reveal_the_letter(guess, secret_word, hide_word)-> list[str]:
    for index, letter in enumerate(secret_word):
        if letter == guess:
            hide_word[index] = letter
    return hide_word

def game_controller():
    # 1. הדפסת מסך הפתיחה
    print(WELCOME_ART)
    print(f"{GREEN}Welcome to the Hangman Game! Can you guess the secret word?{RESET}\n")
    secret_word = random_word()
    # print(secret_word) #test
    tries_left = MAX_TRIES
    guessed_letters = set()
    hide_word = hidden_word(secret_word)

    while tries_left > 0 and "_" in hide_word:
        print("Tries Left:", tries_left)
        print_the_hidden_word(hide_word)
        guess = get_letter_input()
        if guess in guessed_letters:
            print("You have already chosen this letter.")
        elif guess in secret_word:
            hide_word = reveal_the_letter(guess, secret_word, hide_word)

        else:
            tries_left -= 1
        guessed_letters.add(guess)
        print(guessed_letters)


    if tries_left == 0:
        print(GAME_OVER_ART)
        print(f"{YELLOW}The secret word was: {RESET}{GREEN}{secret_word}{RESET}")
    else:
        print(YOU_WON_ART)
        print(f"{CYAN}Amazing job! You guessed the secret word!{secret_word}{RESET}")

if __name__ =="__main__":
    game_controller()