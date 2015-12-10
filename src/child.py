#coding:utf8

from father import father

class child(father):
    def run(self):
        print 'run'
        self.eat()
        self.walk()

        
if __name__ == '__main__':
    f = child()
    f.run()
