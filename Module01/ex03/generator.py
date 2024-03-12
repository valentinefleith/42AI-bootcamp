from random import shuffle

def generator(text, sep=" ", option=None):
    """
    Splits the text according to sep value and yields the substrings.
    Option precise if an action is performed to the substrings.
    """
    if not isinstance(text, str):
        print("ERROR")
        return "ERROR"
    words = text.split(sep)
    if option == "shuffle":
        shuffle(words)
    elif option == "unique":
        words = set(words)
    elif option == "ordered":
        words.sort()
    elif option is not None:
        print("ERROR")
        return "ERROR"
    for word in words:
        yield word
