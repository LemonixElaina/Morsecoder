# 导入

from morsecoder import Morsecoder

# 编码演示

my_code = Morsecoder(text='Hello World', sep='/')
for value in my_code.get_encode():
    print(value, end='')
print()
print(my_code.to_string('get_encode'))

# 译码演示

my_code.set_args(text='...././.-../.-../---/ /.--/---/.-./.-../-../',
                 sep=my_code.get_args()['sep']
                 )
for value in my_code.get_decode():
    print(value, end='')
print()

# __str__

print(my_code)

# Doc

print(help(Morsecoder))
