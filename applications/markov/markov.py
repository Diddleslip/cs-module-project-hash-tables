import random

# Read in all the words in one go
with open("./applications/markov/input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words

# Initialize cache
cache = {}

ends = [".", "!", "?", '"']
### Words will now be a list with each word made into an index.
words = words.split()

for i, word in enumerate(words):
    # Add words to cache if it's first time
    if word not in cache:
        try:
            cache[word] = [words[i+1]]
        ##### This neat piece of code below gives us the error in print, really cool!
        except Exception as e:
            # print(e)
            pass
    # Else word is already there, let's add another value to it
    else:
        cache[word].append(words[i+1])

def create_random_sentence():
    checker = True

    ### This gives us our starting word pair
    while checker:
        start = random.choice(list(cache.items()))

        try:
            if (start[0][0].isupper()) or (start[0][1].isupper() and start[0][0] == '"'):
                checker = False
                return start
        except:
            create_random_sentence()

# TODO: construct 5 random sentences
# Your code here

for i in range(5):
    checker = True
    sentence = ""
    start = create_random_sentence()
    sentence += start[0] + " "
    end = random.choice(start[1])
    # print("HEY!", cache[end])
    while end[-1] not in ends:
        sentence += end + " "
        end = random.choice(cache[end])
    
    sentence += end

    print(f"{sentence}\n")
