book_name = input()
total_books = int(input())
counter = 1
search = input()

while total_books != counter and search != book_name:
    search = input()
    counter += 1
if total_books >= counter and search != book_name:
    print(f'The book you search is not here!')
    print(f'You checked {total_books} books.')
else:
    print(f'You checked {counter - 1} books and found it.')
