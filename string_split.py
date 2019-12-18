# Input: "pelotoncycle"
# Output: "peloton cycle"

# Input: "abc"
# Output: ""

# Input: "apple"
# Output: "apple"

# Input: "apelotoncycle"
# Output: "a peloton cycle"

# Assumptions:
# - Return split string
# - You have is_word as a black box function
# - Assume that if there is no valid string split, return empty string
# - Assume that there are only 2 valid words in the string

def is_word(word):
    valid_words = set([
        'peloton', 
        'cycle', 
        'man', 
        'go', 
        'mango', 
        'the', 
        'a', 
        'app', 
        'lemon', 
        'apple', 
        'thesaurus', 
        'ape', 
        'lot', 
        'ton', 
        'lottery', 
        'to', 
        'on', 
        'orange', 
        'or', 
        'cat',
    ]) # assume it has all of the valid words in the english dictionary
    return word in valid_words

def find_split(word_str):
    if is_word(word_str):
        return word_str 
    word_len = len(word_str)
    for i in range(1, word_len-1):
        word1 = word_str[0:i]
        word2 = word_str[i:word_len]
        if is_word(word1) and is_word(word2):
            return word1 + " " + word2
    return "" 

# print( "%r" % find_split("apple"))
# print ("%r" % find_split("pelotoncycle"))
# print ("%r" % find_split("abc"))

def find_first_word(word_str):
    word_len = len(word_str)
    if is_word(word_str):
        return word_len
    for i in range(1, word_len-1):
        word1 = word_str[0:i]
        word2 = word_str[i:word_len]
        if is_word(word1):
            return i
    return -1


def find_words(word_str, words = []):
    if word_str == "":
        return ""
    
    if num_splits == len(word_str): 
        return ""
    
    if is_word(word_str):
        return word_str
    
    split_at = find_first_word(word_str)
    if split_at == -1:
        return ""
    words.append(word_str[0:split_at])
    return find_words(word_str[split_at:len(word_str)])
    
def find_splits(word_str):
    word_len = len(word_str)
    if is_word(word_str):
        # print ("returning word: " + word_str)
        return word_str
    for i in range(1, word_len):
        word1 = word_str[0:i]
        print ("word1: " + word1)
        if is_word(word1):
            print ("word1 is word: " + word1)
            rest_of_word = find_splits(word_str[i:word_len]) 
            if (rest_of_word  == ""):
                continue 
            return word1 + " " + rest_of_word
    return ""

#print find_splits("applecat")

print ("%r" % find_splits("acata"))



# "mango" -> "man go" (alternatively, you can return "mango". Either option is fine, you just need to return one valid string split)
# "mangox" -> ""
# "pelotoncycle" -> "peloton cycle"
# "aa" -> "a a"
# "thesaurus" -> "thesaurus" # not 'the'
# "applemon" -> "app lemon"      # note that if we take greedy approach, "a" will get taken as a word, but the rest cannot be parsed
# "toilet" -> should 
# "appleorange" -> "apple orange"
# "pelotoncyclez" -> ""
# "catcher" -> "catcher" (assuming 'cher' is not a valid word)