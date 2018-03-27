_TYPE_OF_ENCODING = 4 #using byte coding
_CORRECTION_LEVEL = 'L'
_MEMORY_NEED = 0
_VERSION = 0
_SPACE_LENGTH = 0

_BYTEARRAY_LEVEL_L = [152 ,272 ,440 ,640 ,864 ,1088 ,1248 ,1552 ,
                      1856, 2192, 2592 ,2960 ,3424 ,3688 ,4184 ,
                      4712 ,5176 ,5768 ,6360 ,6888]

_BINARY_MESSAGE = ""
_ASCII_MESSAGE = ""

def make_more_zero(count, string):
    if len(string) > count:
        return string
    else:
        substring = ""
        for i in range(0, count-len(string)):
            substring += "0"
        return substring + string

def itob(int_t):
    if int_t is not None:
        return "{0:b}".format(int(int_t))

def ctob(char):
    if char is not None:
        return "{0:b}".format(ord(char))

def string_to_bin(string, spaces=False):
    st = ""
    if spaces:
        for i in string:
            st+=ctob(i)
            st+=" "
    else:
        for i in string:
            st+=ctob(i)
    return st

def _SET_MEMORY_NEED(binary):
    global _MEMORY_NEED
    _MEMORY_NEED = len(binary)

def _SET_VERSION():
    global _MEMORY_NEED, _CORRECTION_LEVEL, _VERSION
    if _CORRECTION_LEVEL == "L":
        index = 0
        for i in _BYTEARRAY_LEVEL_L:
            index+=1
            if _MEMORY_NEED <= i:
                _VERSION = index
                break

def _SET_SPACE_LENGTH():
    global _SPACE_LENGTH
    if _VERSION < 10:
        _SPACE_LENGTH = 8
    elif _VERSION < 27:
        _SPACE_LENGTH = 16
    else:
        _SPACE_LENGTH = 16

def _GET_ARRAY_OF_BYTES():
    global _TYPE_OF_ENCODING,_MEMORY_NEED, _BINARY_MESSAGE
    return make_more_zero(4,itob(_TYPE_OF_ENCODING)) + \
           make_more_zero(8,itob(_MEMORY_NEED/8)) + \
           _BINARY_MESSAGE

def _CONVERT_MESSAGE():
    global _BINARY_MESSAGE
    _BINARY_MESSAGE = string_to_bin(_ASCII_MESSAGE)

def main():
    global _ASCII_MESSAGE, _BINARY_MESSAGE
    message = str(input())
    _ASCII_MESSAGE = message
    _CONVERT_MESSAGE()
    _SET_MEMORY_NEED(_BINARY_MESSAGE)
    _SET_VERSION()
    _SET_SPACE_LENGTH()
    print(_GET_ARRAY_OF_BYTES())

main()

