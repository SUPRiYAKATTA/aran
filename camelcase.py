a=str(input())
def camel(word):
        import re
        return ''.join(x.capitalize() or ' ' for x in word.split(' '))
    print(camel(a))
