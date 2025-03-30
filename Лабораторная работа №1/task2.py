numbers_pages = 100
numbers_lines = 50
numbers_characters = 25
volume_char = 4
information_volume = 1.44*(1024**2)
volume_one_book = numbers_characters*numbers_lines*numbers_pages*volume_char
result = int(information_volume//volume_one_book)
print("Количество книг, помещающихся на дискету:", result)
