def sort_fn(element):
    return element[0]


tasks_with_priority = []
while True:
    command = input()
    if command == 'End':
        break
    tokens = command.split('-', maxsplit=1)
    priority = int(tokens[0])
    note = tokens[1]
    tasks_with_priority.append((priority, note))


sorted_tasks = sorted(tasks_with_priority, key=sort_fn)
print([task[1] for task in sorted_tasks])



note = input()
notes_list = [None] * 10
while note != "End":
    note = note.split("-")
    idx = int(note[0])
    text = note[1]
    notes_list.insert(idx, text)
    note = input()
print(list(filter(lambda x: x != None, notes_list)))
