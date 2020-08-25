movie_name = input()
standard = 0
kid = 0
student = 0
total_ticket = 0

while movie_name != 'Finish':
    free_space = int(input())
    busy_seats = 0
    for i in range(free_space):
        ticket_type = input()
        if ticket_type == 'standard':
            standard += 1
        elif ticket_type == 'kid':
            kid += 1
        elif ticket_type == 'student':
            student += 1
        elif ticket_type == 'End':
            break
        total_ticket += 1
        busy_seats += 1

    percent_room = (busy_seats / free_space) * 100
    print(f'{movie_name} - {percent_room:.2f}% full.')
    movie_name = input()

total = standard + kid + student
print(f'Total tickets: {total}')
print(f'{100 * student / total:.2f}% student tickets.')
print(f'{100 * standard / total:.2f}% standard tickets.')
print(f'{100 * kid / total:.2f}% kids tickets.')
