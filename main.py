from google import genai
from google.genai import types
from pathlib import Path
import time


class GeminiAPI:
    def __init__(self, api_key: str) -> None:
        self.client = genai.Client(api_key=api_key)
        self.instructions = [
            "Response must be factual and correct, regardless if response takes longer to generate.",
            "Ensure accuracy than baseless assumptions or opinions; unless, the user prompts for opinionated answers.",
            "Provide the entire hyperlink in the response when sourcing answers from other websites.",
            "Adopt a friendly and casual tone. Adjust based on user request.",
            "Clarification will not be provided, ensure on the first response that it tackles most possible questions or clarifications.",
            "In regards to code handling. Write clear, non-complex code with comments on confusing parts and provide concise explanations.",
            "The refusal structure must reference the exact ToS line and briefly explain why.",
        ]

    def ask_question(self, question: str) -> None:
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=question,
            config=types.GenerateContentConfig(
                system_instruction=self.instructions, temperature=0.2
            ),
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


def validate_api_key_file(path: Path) -> None:
    if not path.exists():
        path.touch()
        raise FileNotFoundError("api_key.txt was created. Add your API key and rerun.")

    if not path.read_text().strip():
        raise ValueError("api_key.txt exists but is empty")


def show_opts() -> None:
    options = [
        "[0] Exit",
        "[1] Ask Question",
        "[2] Text to Image",
        "[3] Image to Text",
    ]

    print()
    for line in options:
        print(line)
    print()


def validate_option_chosen(option: int) -> int:
    if 0 <= option < 4:
        return option
    raise ValueError(f"'{option}' is not a valid option")


def main() -> None:
    api_file = Path("api_key.txt")
    try:
        validate_api_key_file(api_file)
    except (FileNotFoundError, ValueError) as e:
        print(e)
        return

    API_KEY = load_api_key()
    gemini = GeminiAPI(API_KEY)

    while True:
        option = 0
        show_opts()

        try:
            option = int(input("Enter option: "))
            validate_option_chosen(option)

        except ValueError as e:
            print(e)

        match option:
            case 0:
                print("Goodbye!")
                break

            case 1:
                question = input("Enter your question: ").strip()
                gemini.ask_question(question)

            case 2:
                pass

            case 3:
                pass


if __name__ == "__main__":
    main()
