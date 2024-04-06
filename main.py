def get_letters():
    center_letter = input("Enter the center letter: ")
    outside_letters = input("Enter the outside letters (excluding the center letter): ")
    letters = set(outside_letters).union(set(center_letter))
    return center_letter, letters


def find_valid_words(center_letter, letters):
    with open("english_words.txt") as f:
        words = [line.rstrip("\n") for line in f]
        valid_words = [
            word
            for word in words
            if letters.issuperset(word) and center_letter in word and len(word) >= 4
        ]
        return valid_words


if __name__ == "__main__":
    center_letter, letters = get_letters()
    valid_words = find_valid_words(center_letter, letters)
    print(valid_words)
