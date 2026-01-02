from google import genai
import time
import sys


class GeminiAPI:
    def __init__(self, api_key: str) -> None:
        self.client = genai.Client(api_key=api_key)

    def ask_question(self, question: str) -> None:
        response = self.client.models.generate_content(
            model="gemini-2.5-flash", contents=question
        )
        response = str(response.text)
        self._animate_text(response)

    def _animate_text(self, response: str) -> None:
        for char in response:
            print(char, end="", flush=True)
            time.sleep(0.02)


def load_api_key(filepath: str = "api_key.txt"):
    with open(filepath, "r") as file:
        return file.read().strip()


def main():
    API_KEY = load_api_key()
    gemini = GeminiAPI(API_KEY)

    if not sys.stdin.isatty():
        piped_input = sys.stdin.read().strip()
        gemini.ask_question(piped_input)


if __name__ == "__main__":
    main()
