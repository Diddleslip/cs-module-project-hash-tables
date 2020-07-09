def no_dups(s):
    # Your code here

    ### Cache is super helpful here, because we can make a dict storing the values that are unique, and removing repeating ones afterwards. 

    # Initialize cache
    cache = {}

    word = s.split()

    # Lets make a dictionary for the words in a loop
    for index in word:
        # Add index to cache
        if index not in cache:
            cache[index] = 1


    newWord = " "

    # Join the indexes in cache back together to form a string once again.
    newWord = newWord.join(cache) 

    return newWord

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))