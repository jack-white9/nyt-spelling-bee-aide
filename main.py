import os
from openai import OpenAI
from dotenv import load_dotenv


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


def generate_hints(word_list):
    load_dotenv()
    openai_client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )
    prompt = """
        You must take the following words and create crossword-style hints for each word.
        The list must be numbered.
        Append each hint with the length of the solution word.
    """

    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": ",".join(word_list)},
        ],
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    center_letter, letters = get_letters()
    valid_words = find_valid_words(center_letter, letters)
    hints = generate_hints(valid_words)
    print(hints)
