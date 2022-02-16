from random import randint
class Roper():
    def __init__(self):
        self.Roper = Roper
    def Bite(self):
        hitrolls = [randint(1,20) + 7 for i in range(2)]
        damage = sum(randint(1,8) for i in range(4)) + 4
        desc = "The roper rolls {} to bite a target dealing {} piercing damage".format(hitrolls, damage)
        return desc
    def Tendril(self):
        hitrolls = [randint(1,20) + 7 for i in range(2)]
        desc = "The roper rolls {} to grapple a target within 50ft with its tendril.".format(hitrolls)
        return desc
    def Reel(self):
        desc = 'The roper pulls each creature grappled by it 25 feet towards its mouth.'
        return desc
    def Attack(self, modifier = ""):
        for i in range(4):
            print (self.Tendril())
        print (self.Reel())
        print (self.Bite())
class YoungGoldDragon():
    def __init__(self):
        self.YoungGoldDragon = YoungGoldDragon
    def Bite(self):
        hitrolls = [randint(1,20) + 10 for i in range(2)]
        damage = sum(randint(1,10) for i in range(2)) + 6
        desc = "The dragon rolls {} to bite a target (10 ft) dealing {} piercing damage".format(hitrolls, damage)
        return desc
    def Claw(self):
        hitrolls = [randint(1,20) + 10 for i in range(2)]
        damage = sum(randint(1,6) for i in range(2)) + 6
        desc = "The dragon rolls {} to claw a target dealing {} slashing damage".format(hitrolls, damage)
        return desc
    def FireBreath(self):
        damage = sum(randint(1,10) for i in range(10))
        desc = "The dragon breaths fire dealing {}/{} fire damage against DC 17 Dex save.".format(damage, damage // 2)
        return desc
    def WeakeningBreath(self):
        desc = "The dragon breaths weakning poison to poison against DC 17 Str save."
        return desc        
    def Attack(self, modifier = ""):
        if modifier == "f" or randint(0,2) == 2:
            if randint(0,1) == 0:
                print (self.FireBreath())
            else:
                print (self.WeakeningBreath())
        else:
            for i in range(2):
                print (self.Claw())
            print (self.Bite())
class HornedDevil():
    def __init__(self):
        self.HornedDevil = HornedDevil
    def Fork(self):
        hitrolls = [randint(1,20) + 10 for i in range(2)]
        damage = sum(randint(1,8) for i in range(2)) + 6
        desc = "The devil rolls {} to stab a target (10 ft) with its fork dealing {} piercing damage".format(hitrolls, damage)
        return desc
    def Tail(self):
        hitrolls = [randint(1,20) + 10 for i in range(2)]
        damage = sum(randint(1,8) for i in range(1)) + 6
        damage2 = sum(randint(1,6) for i in range(3))
        desc = "The devil rolls {} to stab a target (10 ft) with its tail dealing {}" \
        " slashing damage. DC 17 Con to avoid taking {} damage at the start of each of its turns".format(hitrolls, damage, damage2)
        return desc
    def HurlFlame(self):
        hitrolls = [randint(1,20) + 7 for i in range(2)]        
        damage = sum(randint(1,6) for i in range(4))
        desc = "The devil rolls {} to hurl fire at a target (150 ft) dealing {} damage.".format(hitrolls, damage)
        return desc   
    def Attack(self, modifier=""):
        if modifier == "r":
            for i in range(3):
                print (self.HurlFlame())
        else:
            for i in range(2):
                if randint(0,1) == 1:
                    print (self.Fork())
                else:
                    print (self.HurlFlame())
            print (self.Tail())
class BlackPudding():
    def __init__(self):
        self.HornedDevil = HornedDevil
    def Pseudopod(self):
        hitrolls = [randint(1,20) + 5 for i in range(2)]
        damage = sum(randint(1,6) for i in range(1)) + 3
        damage2 = sum(randint(1,8) for i in range(4))
        desc = "The pudding rolls {} to ooze over a creature, dealing {} "\
               "bludgening damage and {} acid damage. Dissolves nonmagical "\
               "armor.".format(hitrolls, damage, damage2)
        return desc 
    def Attack(self, modifier=""):
        print (self.Pseudopod())
class IronGolem():
    def __Init__(self):
        self.IronGolem = IronGolem
    def Slam(self):
        hitrolls = [randint(1,20) + 13 for i in range(2)]        
        damage = sum(randint(1,8) for i in range(3))+7
        desc = "The iron golem rolls {} to crush a target with its fist "\
               "for {} bludgeoning damage".format(hitrolls, damage)
        return desc
    def Sword(self):
        hitrolls = [randint(1,20) + 13 for i in range(2)]        
        damage = sum(randint(1,10) for i in range(3))+7
        desc = "The iron golem rolls {} to hack a target with its sword "\
               "for {} slashing damage".format(hitrolls, damage)
        return desc  
    def PoisonBreath(self):      
        damage = sum(randint(1,8) for i in range(10))
        desc = "The iron golem exahles poison gas that deals {}/{} "\
               "poison damage against DC 19 Con save".format(damage, damage//2)
        return desc
    def Attack(self, modifier=""):
        if modifier=="f" or randint(0,2) == 2:
            print (self.PoisonBreath())
        else:
            for i in range(2):
                if randint(0,1) == 0:
                    print (self.Slam())
                else:
                    print (self.Sword())
monster1 = IronGolem()
while True:
    instructions = input()
    if instructions == "a":
        monster1.Attack()
    elif instructions == "f":
        monster1.Attack('f')
    if instructions == "r":
        monster1.Attack('r')
    elif instructions == "q":
        exit()
