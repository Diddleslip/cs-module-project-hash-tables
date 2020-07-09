
def word_count(s):
    # Your code here

    # Initialize cache
    cache = {}

    # Add filterable words
    bad_words = ['"', ":", ",", ";", ".", "-", "+", "=", "/", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&", '\\']

    word = s.lower()

    for i in bad_words:
        # I is every index in bad_words
        word = word.replace(str(i), "")

    # We have the string filtered, lets make a list with each word seperated.
    word = word.split()

    # A for loop to check each index
    for index in word:
        # If index is not in cache, add it
        if index not in cache:
            cache[index] = 1
        # Else it's already there, add one to the counter
        else:
            cache[index] += 1

    return cache

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))