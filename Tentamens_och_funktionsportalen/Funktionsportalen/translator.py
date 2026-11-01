def translate(sentence: str, glossary: dict[str, str]) -> str:
    new = ' '
    current_word = ''
    for word in sentence + ' ':
        if word != ' ':
            current_word += word
        else: 
            for gloss in glossary:
                print(current_word)
                if gloss == current_word:
                    new += ' ' + glossary[gloss]
            current_word = ''
    return new

print(translate(
  "en katt smög tyst genom rummet",
  {
    "genom": "through",
    "tyst": "quietly",
    "en": "a",
    "smög": "snuck",
    "rummet": "the room",
    "katt": "cat"
  }
))