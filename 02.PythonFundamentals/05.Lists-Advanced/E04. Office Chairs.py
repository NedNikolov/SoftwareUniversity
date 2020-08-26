def room_chairs(rooms):
    boolean = True
    free_chairs = 0
    for i in range(1, rooms + 1):
        command = input().split(' ')
        chairs = len(command[0])
        taken = int(command[1])
        if chairs < taken:
            print(f"{taken - chairs} more chairs needed in room {i}")
            boolean = False
        else:
            free_chairs += (chairs - taken)
    if boolean:
        print(f"Game On, {free_chairs} free chairs left")


total_rooms = int(input())
room_chairs(total_rooms)
