def my_function():
    print("Hello from a function")


my_function()


def call_matrix(name):
    print(name + ' is in Queue')


call_matrix('Neo')
call_matrix('Morpheus')


def queue_matrix(*names):
    print(names[0] + " are waiting in Queue")


queue_matrix('Trinity', 'Switch', 'Kail')


def inside_queue(one, two, three):
    print(one + ' ' + two + ' ' + three + ' are waiting')


inside_queue(two='Neo', one='Morpheus', three='Trinity')


def double_picker(**kid):
    print("His last name is " + kid["lname"])


double_picker(fname="Tobias", lname="Refsnes")


def ship_name(name = 'Nebuchadnezzar'):
    print("The real name is " + name)


ship_name("Nautilius")
ship_name()


def agent_list(names):
    for x in names:
        print(x)


names = ["Smith", "Smith", "Smith", "Smith"]
agent_list(names)


def smith_strength(strength):
    return 7 * strength


print(smith_strength(5))


def room_recursion(a):
    if a > 0:
        result = a + room_recursion(a - 1)
        print(result)
    else:
        result = 0
    return result


print("Resursion result")
room_recursion(6)


