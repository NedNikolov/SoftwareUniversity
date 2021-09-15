queries = int(input())
stack = []
for _ in range(queries):
    line_input = input().split()
    command = int(line_input[0])
    if command == 1:
        stack.append(int(line_input[1]))
    elif command == 2:
        if stack:
            stack.pop()
    elif command == 3:
        if stack:
            print(f"{max(stack)}")
    elif command == 4:
        if stack:
            print(f"{min(stack)}")

reversed_stack = []
while stack:
    reversed_stack.append(str(stack.pop()))
print(", ".join(reversed_stack))
