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

MAX_TRIES = 6

def random_word():
    return random.choice(WORDS)


def hidden_word(word) -> list:
    return list("_" * len(word))

def init():
    return {"word": random_word(),
            "tries" : MAX_TRIES,
            }

def if_guess_word(word, guess):
    return guess in word

def print_the_hidden_word(hide_word):
    print("the guess word:", "".join(hide_word))
    return None

def validate_input(user_input):
    return len(user_input) == 1 and user_input.isalpha()

def get_letter_input():
    while True:
        user_input = input("please enter a letter: ")
        if validate_input(user_input):
            return user_input
        print("please try again")

def game_controller():
    secret_word = random_word()
    print(secret_word) #test
    tries_left = MAX_TRIES
    guessed_letters = set()
    hide_word = hidden_word(secret_word)

    while tries_left > 0 or not "_" in hide_word:
        print("tries left:", tries_left)
        print_the_hidden_word(hide_word)
        guess = get_letter_input()

        if guess in secret_word:
            guessed_letters.add(guess)

        else:
            tries_left -= 1


if __name__ =="__main__":
    game_controller()
    # word = random_word()
    # print(word)
    # print(hidden_word(word))
    # get_letter_input()