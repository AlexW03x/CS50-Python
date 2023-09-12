class entity(object):
    #initalising the entity's main class attributes for stats
    def __init__(self, name, health, mana, description, power, ability1, ability2, ability3, ability4, speed):
        self.name = name
        self.health = health
        self.max_health = health
        self.power = power
        self.mana = mana
        self.max_mana = mana
        self.description = description
        self.ability1 = ability1
        self.ability2 = ability2
        self.ability3 = ability3
        self.ability4 = ability4
        self.speed = speed

    #setters set information with the self <class>
    def setname(self, n):
        self.name = n

    def sethealth(self, n):
        self.health = n
        if self.health > self.max_health:
            self.health = self.max_health
        if self.health < 0:
            self.health = 0

    def setmaxhealth(self, n):
        self.max_health = n

    def setmana(self, n):
        self.mana = n
        if self.mana > self.max_mana:
            self.mana = self.max_mana
        if self.mana < 0:
            self.mana = 0

    def setmaxmana(self, n):
        self.max_mana = n

    def setdesc(self, n):
        self.description = n

    def setpower(self, n):
        self.power = n

    def setab1(self, n):
        self.ability1 = n

    def setab2(self, n):
        self.ability2 = n

    def setab3(self, n):
        self.ability3 = n

    def setab4(self, n):
        self.ability4 = n

    def setspeed(self, n):
        self.speed = n

    #getters - retrieve information from self <class>
    def gethealth(self):
        return self.health

    def getmaxhealth(self):
        return self.max_health

    def getname(self):
        return self.name

    def getdesc(self):
        return self.description

    def getpower(self):
        return self.power

    def getab1(self):
        return self.ability1

    def getab2(self):
        return self.ability2

    def getab3(self):
        return self.ability3

    def getab4(self):
        return self.ability4

    def getmana(self):
        return self.mana

    def getmaxmana(self):
        return self.max_mana

    def getspeed(self):
        return self.speed



