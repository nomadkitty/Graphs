Solving Graph Problems!!

1. Describe the problem using graph terminology
   What are your nodes?
   When are nodes connected?
   What are your connected components?

2. Build your graph, or write your getNeighbors()
   Figure out how to get the node's edges

3. Choose your algorithm, and apply it

EXAMPLE
Given two words (begin_word and end_word), and a dictionary's word list,
return the shortest transformation sequence from begin_word to end_word, such that:
Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
begin_word = "hit"
end_word = "cog"
return: ['hit', 'hot', 'cot', 'cog']
begin_word = "sail"
end_word = "boat"
['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']

1. Translate into graphs terminology
   Node: words
   Edges: There's an edge if words are different by one letter and both are in the word list

2. getNeighbors

3. choose our algorithm: BFS
