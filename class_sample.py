'''
class を使ってみる

'''


class Hoge():

    def __init__(self, mes):
        self.hohoho = mes

    def fuga(self):
        print(self.hohoho)

    def fuga2(self):
        print(self.hohoho + ' world!')

hoge = Hoge('hello!')

hoge.fuga()
hoge.fuga2()

