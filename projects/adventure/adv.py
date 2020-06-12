from room import Room
from player import Player
from world import World
from util import Stack

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
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

directions = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}

s = Stack()

visited = set()

s.push(player.current_room)

# if length of visited is less than total # of rooms, there are still moves to make
while len(visited) < len(world.rooms):
    # directions to move out of the current room
    exits = player.current_room.get_exits()

    # for each exit available
    for exit in exits:
        # if there is an exit and that room has not been visited
        if exit and player.current_room.get_room_in_direction(exit) not in visited:
            # add that direction to the path
            traversal_path.append(exit)
    # add current room to visited
    visited.add(player.current_room)

    # if there is a path to traverse
    if len(traversal_path) > 0:
        room = s.pop()
        # move down available path
        player.travel(room)
        # mark as visited
        visited.add(room)
        # add to traversal path
        traversal_path.append(room)
    # can't move forward, move back in opposite direction
    else:
        player.travel(directions[room])
        traversal_path.append(directions[room])


# # add starting room to stack
# s.push(player.current_room)

# while s.size() > 0:
#     # remove last room
#     room = s.pop()
    
#     player.travel(room)

#     # if current room has not been visited
#     if player.current_room not in visited:
#         # add current room to visited
#         visited.add(player.current_room)
#         # add to path
#         traversal_path.append(directions[room])
#         # add to stack
#         s.push(directions[room])
        
#     # iterate through available moves
#     for option in player.current_room.get_exits(option):
#         # assign new room to direction chosen
#         new_room = player.current_room.get_room_in_direction(option)

#         # if can move in direction and that room has not been visited
#         if new_room and new_room not in visited:
#             # add to path
#             traversal_path.append(new_room)
#             # add to stack
#             s.push(new_room)




# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
