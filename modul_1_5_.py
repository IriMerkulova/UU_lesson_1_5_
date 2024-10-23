immutable_var = 1, 'Zoo', False, [2024, 'year'], 5.5
print('immutable_var:', immutable_var)
#immutable_var[1] = 'boo'           кортеж нельзя редактировать или как-либо изменять
mutable_list = [1, 2, 3, 4, 'z', 5, 6]
mutable_list[2] = mutable_list[-1]
print('mutable_list:', mutable_list)