immutable_var = [1, 2, 3, 4]
immutable_var[2] = 'a'
immutable_var[3] = 'b'
print(immutable_var)
mutable_list = [1, 2, 3, 4]
mutable_list[2] = 'a'
mutable_list[3] = 'b'
mutable_list.append('string')
print(mutable_list)