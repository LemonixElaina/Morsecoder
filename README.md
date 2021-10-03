# Morsecoder
> By Lemonix

![Python 图标](https://img.shields.io/badge/Python-3.6%2B-brightgreen?style=for-the-badge&logo=appveyor)
![Build 图标](https://img.shields.io/badge/Build-Passing-orange?style=for-the-badge&logo=appveyor)
![License 图标](https://img.shields.io/badge/License-Apache-brightgreen?style=for-the-badge&logo=appveyor)

***
## 介绍
一个关于摩斯密码编码与译码的库

 _Warning:_ 本项目基于 **Python3.6+** 开发，低版本会出现Bug

 **Latest version:** *v0.54*

 ***v1.0 Coming soon**

### v0.53更新内容
- 去除主文件内的测试
- 改用snake_case命名法
- 修复已知Bug
- 优化代码风格
- 使用反射优化性能
- 优化报错信息

### v0.54更新内容
- 将类变量author version改成系统内置变量
- 用[]代替list()提升性能
- 用类方法modify get_list代替普通方法modify get_list
- 优化try..except
- 修复已知Bug
- 添加is_morsecode方法

***
## 使用教程 (以下[ ]内的内容代表可选参数)
- 实例化与设置
```python
code = Morsecoder( [文本, 分隔符] )
```

- 编码与译码
```python
# 编码
for i in code.get_encode():
    print(i, end='')
print()

# 译码
for i in code.get_decode():
    print(i, end='')
print()
```

- 查看文本与分隔符
```python
# 文本
code.get_args()['text']

# 分隔符
code.get_args()['sep']
```

- 修改或添加摩斯密码对照表的内容
```python
# key是键，value是值
Morsecoder.modify(key, value)
```

- 初始化后设置参数
```python
code.set_args(文本, 分隔符)
```

- 查看对照表内容
```python
# encode_list为编码表，decode_list为解码表
Morsecoder.get_list(对照表类型)
```

- 将迭代器转为字符串或列表(此方法不改变迭代器本身，字符串和列表是返回值)
```python
# 方法同get_encode和get_decode
code.to_string(方法)
code.to_list(方法)
```
***

## 使用实例 (此导入方式仅针对同文件夹导入)

- 用分隔符"/"加密字符串"你好世界"
```python
from morsecoder import Morsecoder

my_code = Morsecoder(text='你好世界', sep='/')
for i in morse1.get_encode():
    print(i, end="")
print() # 输出空行
```

输出:
```
-..----.--...../-.--..-.-----.-/-..---....-.--./---.-.-.-..--../
```


- 解密摩斯密码".-.././--/---/-./../-..-/"

```python
from morsecoder import Morsecoder

my_code = Morsecoder(text='.-.././--/---/-./../-..-/', sep='/')
for i in morse1.get_decode():
    print(i, end="")
print() # 输出空行
```

输出:
```
LEMONIX
```


- 向摩斯密码对照表中添加"①"，对应摩斯密码为".-.-.-"
```python
from morsecoder import Morsecoder

Morsecoder.modify('①', '.-.-.-')
```

- 将迭代器转为字符串
```python
from morsecoder import Morsecoder

my_code = Morsecoder(text='...././.-../.-../---/ /.--/---/.-./.-../-../', sep='/')
print(my_code.to_string('get_decode'))
```

输出:
```
HELLO WORLD
```


- 部分功能测试
```python
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

```

输出:
```
...././.-../.-../---/ /.--/---/.-./.-../-../
...././.-../.-../---/ /.--/---/.-./.-../-../
HELLO WORLD

Instance -> 'Morsecoder'
Text(11) -> '......-...-..--- .-----.-..-..-..'
Sep(1) -> '/'
        
Help on class Morsecoder in module morsecoder:

class Morsecoder(builtins.object)
 |  Morsecoder(text=None, sep=None)
 |  
 |  基于Python3.6+的摩斯密码库,
 |  支持编码, 译码, 自定义密码
 |  
 |  Methods defined here:
 |  
 |  __init__(self, text=None, sep=None)
 |      初始化参数,
 |      设置文本, 分隔符以及自动分析空格,
 |      如果当前文本含有不在对照表不包含的字符时,
 |      会通过Unicode进行编码
 |  
 |  __repr__ = __str__(self)
 |  
 |  __str__(self)
 |      Return str(self).
 |  
 |  get_args(self)
 |      获取当前实例的text和sep
 |  
 |  get_decode(self)
 |      获取当前实例的译码
 |  
 |  get_encode(self)
 |      获取当前实例的编码
 |  
 |  set_args(self, text, sep)
 |      设置当前实例的text和sep
 |  
 |  to_list(self, func)
 |      将迭代器转化为字符串
 |  
 |  to_string(self, func)
 |      将迭代器转化为字符串
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  get_list(list_type) from builtins.type
 |      获取编码表或译码表
 |  
 |  modify(key, value) from builtins.type
 |      修改编码表或译码表

None
```

****
## 参与贡献
Lemonix(开发与测试), Sherlockcxk(优化与测试)

[Lemonix-Gitee](https://gitee.com/lemonix)

[Lemonix-Github](https://github.com/lemonix-xxx)

[Sherlockcxk-Gitee](https://gitee.com/cxk-53)

[Sherlockcxk-Github](https://github.com/sherlockcxk)

## 你知道吗
Morsecoder第一个版本:RtMorsecoder于2021/1/11 17:19发布

Morsecoder的灵感来源于本项目的共同开发者Sherlockcxk的C#项目Morsecoder
