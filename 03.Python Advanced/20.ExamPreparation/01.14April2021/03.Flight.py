def flights(*args):
    travel_dict = {}
    i, j = 0, 1
    while True:
        destination = args[i]
        if destination == 'Finish':
            return travel_dict

        passengers = args[j]

        if destination in travel_dict:
            travel_dict[destination] += passengers
        else:
            travel_dict[destination] = passengers
        i += 2
        j += 2


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))

# def flights(*n):  # 3. Problem
#     my_dict = {}
#     for i in range(0, len(n), 2):
#         if n[i] == 'Finish':
#             break
#         if not n[i] in my_dict.keys():
#             my_dict[n[i]] = 0
#         my_dict[n[i]] += n[i + 1]
#     return my_dict
