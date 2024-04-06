import os
from openai import OpenAI
from dotenv import load_dotenv


class SpellingBeeAide:
    def __init__(self):
        load_dotenv()
        self.openai_client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),
        )

    def get_letters(self, center_letter, outside_letters):
        letters = set(outside_letters).union(set(center_letter))
        return letters

    def find_valid_words(self, center_letter, letters):
        with open("english_words.txt") as f:
            words = [line.rstrip("\n") for line in f]
            valid_words = [
                word
                for word in words
                if letters.issuperset(word) and center_letter in word and len(word) >= 4
            ]
            return valid_words

    def generate_hints(self, word_list):
        prompt = """
            You must take the following words and create crossword-style hints for each word.
            The list must be numbered.
            Append each hint with the length of the solution word.
            Categorise the hints by the first two letters of the solution word.
        """

        response = self.openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": ",".join(word_list)},
            ],
        )
        return response.choices[0].message.content
