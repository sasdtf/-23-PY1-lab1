disk_capacity_bytes = 1.44 * 1024 * 1024

pages = 100
lines = 50
chars = 25
byte_char = 4

book_data_bytes = pages*lines*chars*byte_char

books_disk = disk_capacity_bytes // book_data_bytes
print("Количество книг, помещающихся на дискету:", int(books_disk))
