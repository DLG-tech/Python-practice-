import requests

skip = {"of", "and", "the"}

first_letter_text = input("enter acronym phrase eg F.B.I Federal Bureau of Investigation: ")

first_letter = ".".join(word[0].upper() for word in first_letter_text.split() if word.lower() not in skip)
print("Acronym:", first_letter)

words = [word for word in first_letter_text.split() if word.lower() not in skip]

def get_same_pos_same_letter(word):

    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    data = requests.get(url).json()

    try:
        pos = data[0]["meanings"][0]["partOfSpeech"]
    except:
        return word

    pos_map = {
        "noun": ["n", "prop", "pn"],
        "verb": ["v", "aux"],
        "adjective": ["adj", "sat"],
        "adverb": ["adv"]
    }

    if pos not in pos_map:
        return word

    tag_list = pos_map[pos]

    first = word[0].lower()
    dm_url = f"https://api.datamuse.com/words?sp={first}*&md=p"
    results = requests.get(dm_url).json()

    for item in results:
        candidate = item["word"]

        if candidate.lower() == word.lower():
            continue

        if "tags" in item:
            if any(t in item["tags"] for t in tag_list):
                return candidate

        try:
            c_data = requests.get(
                f"https://api.dictionaryapi.dev/api/v2/entries/en/{candidate}"
            ).json()
            c_pos = c_data[0]["meanings"][0]["partOfSpeech"]

            if c_pos == pos:
                return candidate
        except:
            continue

    return word

new_phrase = ". ".join(get_same_pos_same_letter(w) for w in words)

print("Original phrase:", " ".join(words))
print("New phrase:", new_phrase)
