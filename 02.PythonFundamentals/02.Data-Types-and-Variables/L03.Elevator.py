people = int(input())
capacity = int(input())

if people < capacity:
    print('All the persons fit inside in the elevator. Only one course is needed.')
elif people % capacity == 0:
    print(f'{people / capacity:.0f} courses * {capacity} people')
else:
    full = people / capacity
    half = people % capacity
    print(f'{full:.0f} courses * {capacity} people + 1 courses * {half} people')
