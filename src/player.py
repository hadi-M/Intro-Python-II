# Write a class to hold player information, e.g. what room they are in
# currently.
from collections import defaultdict
from room import Room
from pudb import set_trace as st


class Player():
    def __init__(self, name: str, current_room: "Room") -> None:
        self.name = name
        self.current_room = current_room
        self.available_directions =\
            self.get_available_directions(current_room)

    def get_available_directions(self, next_map):
        # st()
        return defaultdict(
            lambda: None,
            {
                "n": next_map.n_to,
                "e": next_map.e_to,
                "s": next_map.s_to,
                "w": next_map.w_to
            }
        )

    def move(self, direction: str) -> bool:
        # st()
        next_room = self.available_directions[direction]
        if next_room:
            self.current_room = next_room
            self.available_directions =\
                self.get_available_directions(next_room)
            return True
        else:
            return False
    
    def report_position(self):
        print(f"I am at \"{self.current_room.name}\"\n")

    