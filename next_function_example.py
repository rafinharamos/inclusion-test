list_of_dicts = [
    {'x': 1, 'y': 10},
    {'x': 2, 'y': 20},
    {'x': 3, 'y': 30},
    {'x': 5, 'y': 50},
    {'x': 6, 'y': 60}
]

result = next((item for item in list_of_dicts if item.get('x') == 5), {})

print(result)
