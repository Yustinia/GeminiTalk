# GeminiTalk

A small project that interacts with Gemini using your API key.

## Installation

1. Ensure that you have `git` and `python` installed on your system.

2. `git clone https://github.com/Yustinia/GeminiTalk.git` to your preferred directory.

3. `cd` into the folder and do `pip install -r requirements.txt`.

4. Create a file named `api_key.txt` and paste the API key that is generated.

## Usage

You can pipe certain commands into the `main.py`, an example of how it can be used below:

- Asking Gemini using `echo` and piping it to the script.

```python
echo "What are the common ice cream flavors" | python3 main.py
```

- Sending the contents of a file followed by your question.

```python
{ cat file.txt; echo "What does this do?" } | python3 main.py
```
