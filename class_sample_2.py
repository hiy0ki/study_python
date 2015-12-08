'''
class を使ってみる

継承を使う
'''


class Hoge():

    def __init__(self, mes):
        self.hohoho = mes

    def fuga(self):
        print(self.hohoho)

    def fuga2(self):
        print(self.hohoho + ' world!')


class Aaa(Hoge):
    
    def fuga2(self):
        print(self.hohoho + ' woooooooooorld!')




hoge = Aaa('hello!')

hoge.fuga()
hoge.fuga2()

