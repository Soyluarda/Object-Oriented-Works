import strategy
import strategy2

fighter1 = strategy.Asian(name="Rocky",health=100,fighting_style=strategy2.MuayThai())
fighter2 = strategy.Europen(name="Apollo",health=100,fightin_style=strategy2.JuiJutsu())

fighter1.attack(fighter1,fighter2)
fighter2.defend(fighter2,fighter1)
fighter2.attack(fighter2,fighter1)
fighter1.defend(fighter1,fighter2)

print("Rocky change his style")

fighter1.fighting_style=strategy2.KungFu()

fighter1.attack(fighter1,fighter2)
fighter1.defend(fighter1,fighter2)

print "Apollo changed his style"

fighter2.fighting_style=strategy2.MuayThai()
fighter2.attack(fighter2,fighter1)
fighter2.defend(fighter2,fighter1)


