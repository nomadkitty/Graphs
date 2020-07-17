'''
Question: why can't we just use a traversal?
-Traversal will just visit all the nodes
- We want a list of directions to guide us step-by-step

- Also, we will want to minimize the number of steps

Translate into Graph Terminology
Nodes: rooms
Edges: Exits
find the closest known node with unexplored exits
'''

from room import Room
from player import Player
from world import World
from util import Stack, Queue
# from graph import Graph

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

# start from room 0
player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# print(player.current_room)
'''
Understand
# Build a graph {}
## check current room exits, {current_room.id: {}}
## loop through exits to build graph {current_room.id: {exit: "?"}}
## Randomly pick one of the exits 
## player travel to that exit
## check the current room again, add new key of current room and add current room to previous room
# recursively dft: 
# check exits
# loop: travel to all exits, record room id     
'''
graph = {}
starting_room = player.current_room
inverse_direction = {"n": "s", "s": "n", "w": "e", "e": "w"}

# add rooms to the graph
for room_id in range(len(room_graph)):
    graph[room_id] = {}


def get_neighbors(room):
    neighbors = {}
    room_id = room.id
    # add directions of each room to the graph
    exits = room.get_exits()  # return a list of exits
    # loop through exits
    for exit in exits:
        # travel to new room
        player.travel(exit)
        # get the new room id
        new_room = player.current_room
        # append the room id to neighbors
        neighbors[new_room] = new_room.id
        # add room to the exit in the graph
        graph[room_id][exit] = new_room.id
        # travel back to the original room
        player.travel(inverse_direction[exit])
    return neighbors


def dft_recursive(room, visited=set()):
    if room.id not in visited:
        visited.add(room.id)
        neighbors = get_neighbors(room)
        for neighbor, id in neighbors:
            dft_recursive(neighbor, visited)


dft_recursive(starting_room)


print(graph)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
