def str_upper():
    """все заглавные"""
    user_input = str(input())
    return user_input.upper()

def capitalize_words(string):
    """загланые каждая первая"""
    words = string.split()
    sentence = []
    for word in words:
        sentence.append(word.capitalize())
    return " ".join(sentence)
