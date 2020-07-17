from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
traversal_graph = {}


def reverse_move(move):
    if move == "n":
        return "s"
    elif move == "s":
        return "n"
    elif move == "e":
        return "w"
    elif move == "w":
        return "e"
    else:
        return print("Invalid move")


def world_traversal():
    # Create a stack and visited rooms set for our DFT
    visited_rooms = set()
    s = Stack()
    # Declare variable for curr_room
    curr_room = player.current_room
    # Add our starting room to visited rooms
    visited_rooms.add(curr_room)
    # Get possible exits for said room
    current_exits = curr_room.get_exits()
    # Create a neighbors dictionary to keep track of which rooms have been explored
    neighbors = dict([(direction, '?') for direction in current_exits])
    # Add current room to the graph with its neighbors
    traversal_graph[curr_room.id] = neighbors
    # Our exit condition is that we have visited every room
    while len(visited_rooms) < len(world.rooms):
        # For all possible directions we can move
        for direction in dict.keys(traversal_graph[curr_room.id]):
            # If the room in the given direction is unexplored, set our move = to that direction
            if traversal_graph[curr_room.id][direction] == '?':
                move = direction
        # If no directions are available, pop one off of the stack
        if move is None:
            move = s.pop()
        # If we hit this else, we need to go back where we came from
        else:
            s.push(reverse_move(move))
        # Keep track of our previous room as we move to the next one
        prev_room = curr_room
        player.travel(move)
        traversal_path.append(move)
        # Update our current room
        curr_room = player.current_room
        # Update our traversal graph so that the direction we moved is now explored
        traversal_graph[prev_room.id][move] = curr_room.id
        # If the new current room has not been visited
        if curr_room not in visited_rooms:
            # Do the same as above
            current_exits = curr_room.get_exits()
            neighbors = dict([(direction, '?') for direction in current_exits])
            # However we do know one of the neighboring rooms
            neighbors[reverse_move(move)] = prev_room.id
            traversal_graph[curr_room.id] = neighbors
            visited_rooms.add(curr_room)
        # If it has been visited...
        else:
            # Get the neighbors from our graph
            neighbors = traversal_graph[curr_room.id]
            # Mark off the last room we were in as explored
            neighbors[reverse_move(move)] = prev_room.id
            # Update our graph
            traversal_graph[curr_room.id] = neighbors

        move = None


world_traversal()

# TRAVERSAL TEST
visited_rooms = set()

player.current_room = world.starting_room

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
