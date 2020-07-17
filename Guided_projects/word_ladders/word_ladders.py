# EXAMPLE
# Given two words (begin_word and end_word), and a dictionary's word list,
# return the shortest transformation sequence from begin_word to end_word, such that:
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
# begin_word = "hit"
# end_word = "cog"
# return: ['hit', 'hot', 'cot', 'cog']
# begin_word = "sail"
# end_word = "boat"
# ['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']

# 1. Translate into graphs terminology
#     Node: words
#     Edges exists when: words are 1 letter different, and in our giant list of words
# 2. Build graph or define getNeighbors
# 3. choose our algorithm: BFS

# Build our graph
# Could filter our word list by length
# remember to lower case stuff

# for every letter in the word,
# swap out a letter in the alphabet
# if the result is in our words list, it's a neighbor!
# time complexity len(word) * 26 => O(n*26) => O(n)

from util import Queue
import string

my_file = open('words.txt', 'r')
words = my_file.read().split("\n")
my_file.close()

word_set = set()
for word in words:
    word_set.add(word.lower())


def get_neighbors(start_word):
    neighbors = []
    # for every letter in the word,
    for letter_index in range(len(start_word)):
        # for every letter in the alphabet
        for letter in string.ascii_lowercase:
            # turn our start word into a list, then back again
            word_list = list(start_word)
            # swap out a letter in the alphabet
            word_list[letter_index] = letter

            word = "".join(word_list)
            # if the result is in our words list, it's a neighbor!
            if word in word_set and word != start_word:
                neighbors.append(word)
    return neighbors

# BFS


def word_ladders(start_word, end_word):
    q = Queue()
    visited = set()
    q.enqueue([start_word])

    while q.size() > 0:
        current_path = q.dequeue()
        current_word = current_path[-1]

        if current_word == end_word:
            return current_path

        if current_word not in visited:
            visited.add(current_word)
            neighbors = get_neighbors(current_word)

            for neighbor in neighbors:
                new_path = current_path + [neighbor]
                q.enqueue(new_path)


print(word_ladders('sail', 'boat'))
