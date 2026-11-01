
def concat_with_space(*strings: str) -> str:
    new = ""
    for s in strings:
        new += ' ' + s
    return new


print(concat_with_space(
  "The",
  "baby",
  "laughed",
  "when",
  "the",
  "dog",
  "licked",
  "her",
  "toes."
))

