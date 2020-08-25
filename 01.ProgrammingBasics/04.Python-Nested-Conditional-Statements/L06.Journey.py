budget = float(input())
seasons = input()
destination = ''
trip_type = ''

if budget <= 100:
    destination = 'Bulgaria'
    if seasons == 'summer':
        budget *= 0.3
        trip_type = 'Camp'
    else:
        budget *= 0.7
        trip_type = 'Hotel'
elif 100 < budget <= 1000:
    destination = 'Balkans'
    if seasons == 'summer':
        budget *= 0.4
        trip_type = 'Camp'
    else:
        budget *= 0.8
        trip_type = 'Hotel'
else:
    destination = 'Europe'
    budget *= 0.9
    trip_type = 'Hotel'

print(f'Somewhere in {destination}')
print(f'{trip_type} - {budget:.2f}')
