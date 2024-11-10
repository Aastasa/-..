# TODO Найдите количество книг, которое можно разместить на дискете
v_Mb = 1.44
len_page = 100
len_str = 50
len_sim = 25
v_1sim_b = 4
v_book = v_1sim_b * len_sim * len_str * len_page
len_book = (v_Mb*1024**2) // v_book
print("Количество книг, помещающихся на дискету:", int(len_book))
