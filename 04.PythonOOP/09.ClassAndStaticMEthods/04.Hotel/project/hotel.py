class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, guests_count):
        possible_rooms = [x for x in self.rooms if x.number == room_number]
        room = possible_rooms[0]

        if room.take_room(guests_count):
            return

        self.guests += guests_count

    def free_room(self, room_number):
        possible_rooms = [x for x in self.rooms if x.number == room_number]
        room = possible_rooms[0]

        if room.free_room():
            return
        self.guests += room.guests

    def status(self):

        result = f"Hotel {self.name} has {self.guests} total guests" + '\n'
        result += f"Free rooms: {', '.join([str(x.number) for x in self.rooms if not x.is_taken])}" + '\n'
        result += f"Taken rooms: {', '.join([str(x.number) for x in self.rooms if x.is_taken])}"
        return result
