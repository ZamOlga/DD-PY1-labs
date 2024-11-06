# TODO Найдите количество книг, которое можно разместить на дискете
disk_memory = 1.44 * (1024 ** 2)
pages = 100
strings = 50
symbols = 25
weight_of_symbol = 4
book_weight = strings * pages * symbols * weight_of_symbol
number_of_books = int(disk_memory//book_weight)

print("Количество книг, помещающихся на дискету:", number_of_books)
