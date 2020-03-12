from room import Room
from player import Player
import textwrap
import os
from item import Food, Weapon

# Declare all the rooms

room = {
    "outside": Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
    ),
}


# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

# Add items to rooms
sword = Weapon("Sword", "A rusty old sword for basic combat", 5)
bow = Weapon("Bow", "An old used bow for basic combat", 3)

tomato = Food("Tomato", "A red circular fruit", 3)
potato = Food("Potato", "A stud", 2)

room["foyer"].items.append(sword)
room["overlook"].items.extend([potato, tomato])
room["treasure"].items.append(bow)

#
# Main
#

wrapper = textwrap.TextWrapper(width=40)

# Make a new player object that is currently in the 'outside' room.
player = Player("Mark", room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
invalid_room_error = False
invalid_command_error = False
print_inventory = False
while True:
    # os.system("clear")

    if invalid_command_error == True:
        print("Invalid Command. Available commands: ")
        print("n: Go North \ns: Go South \nw: Go West \ne: Go East \nq: Quit")
        invalid_command_error = False

    if invalid_room_error == True:
        print("#### There is no room in that direction ####")
        invalid_room_error = False

    current_room = player.current_room

    # Print current room details
    print("-------Current Room: " + current_room.name + "---------")
    word_list = wrapper.wrap(current_room.description)
    for line in word_list:
        indented_words = textwrap.indent(text=line, prefix="* ")
        print(indented_words)

    current_room.print_items()

    if print_inventory:
        player.print_inventory()
        print_inventory = False

    # Wait for user input
    command = input("Please enter your command:   ")
    cmdList = command.split(" ")
    command = cmdList[0]
    if len(cmdList) == 1:
        if command == "n":
            if current_room.n_to is None:
                invalid_room_error = True
            else:
                player.current_room = current_room.n_to
        elif command == "s":
            if current_room.s_to is None:
                invalid_room_error = True
            else:
                player.current_room = current_room.s_to
        elif command == "w":
            if current_room.w_to is None:
                invalid_room_error = True
            else:
                player.current_room = current_room.w_to
        elif command == "e":
            if current_room.e_to is None:
                invalid_room_error = True
            else:
                player.current_room = current_room.e_to
        elif command == "i":
            print_inventory = True
        elif command == "q":
            print("Goodbye")
            break
        else:
            invalid_command_error = True
    elif len(cmdList) > 1:
        if cmdList[0] == "get":
            item_name = cmdList[1]
            found = False
            for item in current_room.items:
                if item_name == item.name:
                    player.add_item(item)
                    current_room.items.remove(item)
                    print(f"Picked up {item.name}")
                    found = True
                    break
            if not found:
                print("There was no item found")
        if cmdList[0] == "drop":
            item_name = cmdList[1]
            player.drop_item(item_name)

