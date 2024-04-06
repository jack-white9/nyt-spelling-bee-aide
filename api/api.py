from fastapi import FastAPI
from aide import SpellingBeeAide
import uvicorn


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Success"}


@app.get("/get_hints")
async def get_hints(center_letter, outside_letters):
    aide = SpellingBeeAide()
    letters = aide.get_letters(center_letter, outside_letters)
    valid_words = aide.find_valid_words(center_letter, letters)
    hints = aide.generate_hints(valid_words)
    return hints


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
