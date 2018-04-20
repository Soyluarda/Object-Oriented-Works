import strategy2
class Fighter(object):
    def __init__(self,name=None,health=100):
        self.name = name
        self.health = health
        self.fighting_style = strategy2.Style()

    def attack(self,attacker,opponent):
        self.fighting_style.attack(attacker,opponent)

    def defend(self,defender,attacker):
        self.fighting_style.defend(defender,attacker)


class Asian(Fighter):
    def __init__(self,name=None,health=100,fighting_style = None):
        super(Asian,self).__init__(name,health)
        self.fighting_style = fighting_style
    def looks(self):
        print "{0.name} has Asian looks".format(self)

class Europen(Fighter):
    def __init__(self,name=None,health=100,fightin_style=None):
        super(Europen,self).__init__(name,health)
        self.fighting_style = fightin_style
    def looks(self):
        print "{0.name} has Europen looks.".format(self)


