class Style(object):

    def attack(self,opponent):
        pass

    def defend(self,attacker):
        pass


class MuayThai(Style):
    def __init__(self):
        super(MuayThai,self).__init__()

    def attack(self,attacker,opponent):
        message = '{0.name} attacking {1.name} in Muay Thai style'.format(attacker,opponent)
        print message

    def defend(self,attacker,defender):
        message = '{0.name} defending {1.name} in Muay Thai Style'.format(defender,attacker)
        print message

class KungFu(Style):

    def __init__(self):
        super(KungFu,self).__init__()

    def attack(self,attacker,opponent):
        message = "{0.name} attacking {1.name} in Kung Fu style".format(attacker,opponent)
        print message
    def defend(self,attacker,defender):
        message = "{0.name} defending {1.name} in Kung Fu style".format(defender,attacker)
        print(message)


class JuiJutsu(Style):
    def __init__(self):
        super(JuiJutsu,self).__init__()

    def attack(self,attacker,opponent):
        message = "{0.name} attacking {1.name} in JuiJutsu style".format(attacker,opponent)
        print(message)

    def defend(self,defender,attacker):
        message = "{0.name} defending {1.name} in Juijutsu style".format(defender,attacker)
        print(message)

