# -*- coding: utf-8 -*-


__author__ = 'Lemonix'
__version__ = 0.54


class MorsecoderError(Exception):
    """

    自定义异常

    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Morsecoder:
    """

    基于Python3.6+的摩斯密码库,

    支持编码, 译码, 自定义密码

    """

    __slots__ = ('__text', '__sep')
    # 限制实例的属性(不限制继承后的子类)

    __encode_list = {'A': '.-',
                     'B': '-...',
                     'C': '-.-.',
                     'D': '-..',
                     'E': '.',
                     'F': '..-.',
                     'G': '--.',
                     'H': '....',
                     'I': '..',
                     'J': '.---',
                     'K': '-.-',
                     'L': '.-..',
                     'M': '--',
                     'N': '-.',
                     'O': '---',
                     'P': '.--.',
                     'Q': '--.-',
                     'R': '.-.',
                     'S': '...',
                     'T': '-',
                     'U': '..-',
                     'V': '...-',
                     'W': '.--',
                     'X': '-..-',
                     'Y': '-.--',
                     'Z': '--.',
                     '1': '.----',
                     '2': '..---',
                     '3': '...--',
                     '4': '....-',
                     '5': '.....',
                     '6': '-....',
                     '7': '--...',
                     '8': '---..',
                     '9': '----.',
                     '0': '-----',
                     '.': '.-.-.-',
                     '/': '-..-.',
                     '-': '-....-',
                     '(': '-.--.',
                     ')': '-.--.-', }
    __decode_list = {value: key for key, value in __encode_list.items()}
    # encode_list: 编码表, decode_list: 译码表


    def __init__(self, text=None, sep=None):
        """

        初始化参数,

        设置文本, 分隔符以及自动分析空格,

        如果当前文本含有不在对照表不包含的字符时,

        会通过Unicode进行编码

        """

        if None in (text, sep):
            self.__text = self.__sep = ''

        else:
            self.set_args(text=text.upper(), sep=sep)

        if self.__sep == ' ':
            Morsecoder.__encode_list.update({' ': '/'})
            Morsecoder.__decode_list.update({'/': ' '})

        else:
            Morsecoder.__encode_list.update({' ': ' '})
            Morsecoder.__decode_list.update({' ': ' '})
        # 避免重复, 更改空格的样式


        for value in self.__text:
            if value not in Morsecoder.__encode_list:
                uni_char = bin(ord(value))[2:] \
                    .replace('1', '-') \
                    .replace('0', '.')
                Morsecoder.__encode_list.update({value: uni_char})
                Morsecoder.__decode_list.update({uni_char: value})
                # 用二进制的Unicode进行编码


    def __str__(self):
        return f'''

Instance -> '{type(self).__name__}'

Text({len(self.__text)}) -> '{''.join(self.__text)}'

Sep({len(self.__sep)}) -> '{self.__sep}'

        '''

    __repr__ = __str__

    def set_args(self, text, sep):
        """

        设置当前实例的text和sep

        """

        if isinstance(text, str) and isinstance(sep, str):
            self.__text, self.__sep = text.upper(), sep

        else:
            raise MorsecoderError('文本与分隔符类型必须为字符串')

    def get_args(self):
        """

        获取当前实例的text和sep

        """

        return {
            'text': self.__text,
            'sep': self.__sep
        }

    def get_encode(self):
        # En - 摩斯密码编码

        """

        获取当前实例的编码

        """

        try:
            for value in self.__text:
                yield f'{Morsecoder.__encode_list[value]}{self.__sep}'

        except KeyError:
            raise MorsecoderError('含有特殊字符')

    def get_decode(self):
        # De - 摩斯密码译码

        """

        获取当前实例的译码

        """

        try:
            self.__text = self.__text \
                .split(self.__sep)
            # 用sep把code分割为列表


            if self.__text[-1] == '':
                # 去除尾部的空元素

                self.__text.pop()

            for value in self.__text:
                yield Morsecoder.__decode_list[value]

        except KeyError:
            raise MorsecoderError('非法摩斯密码')

    def to_string(self, func):
        """

        将迭代器转化为字符串

        """

        res = []

        if hasattr(self, func):
            for i in getattr(self, func)():
                res.append(i)

        else:
            raise MorsecoderError('不存在此方法')

        return ''.join(res)

    def to_list(self, func):
        """

        将迭代器转化为字符串

        """

        return self.to_string(func) \
            .split(f'{self.__sep}')

    def is_morsecode(self):
        try:
            self.__text.to_list()

        except MorsecoderError:
            return False

        else:
            return True

    @classmethod
    def modify(cls, key, value):
        """

        修改编码表或译码表

        """

        if len(key) == 1:
            cls.__encode_list.update({key: value})
            cls.__decode_list.update({value: key})
            # 更新编码表和译码表


        else:
            raise MorsecoderError('键的长度必须为1')

    @classmethod
    def get_list(cls, list_type):
        """

        获取编码表或译码表

        """

        if hasattr(cls, list_type):
            return getattr(cls, f"__{list_type}")

        else:
            raise MorsecoderError('不存在此对照表')


'''

My Bilibili channel: https://b23.tv/wxyFrS

Thank u 4 using my program

'''
