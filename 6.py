"""
旱獭原文件
现作参考
"""


import random


class Data():
    def __init__(self):
        self.income = {"E":5040, "C": 0, "U": 0, "X": 0, "F": 10,
                       "R": 10, "M": 80, "L": 400, "H": 400, "T": 750}
        self.tInc = {"E": 24, "C": 5, "U": 16, "X": 0, "F": 1,
                     "R": 1, "M": 1, "L": 3, "H": 2, "T": 12}
        self.price = {"E": 10**90, "C": 6300, "U": 6000, "X": 450, "F": 40,
                      "R": 40, "M": 525, "L": 3000, "H": 3150, "T": 7500}
        self.workers = {"E": 1200, "C": 10000, "U": 500, "X": 0, "F": 1000,
                        "R": 800, "M": 2500, "L": 8000, "H": 8000, "T": 2000}


data = Data()


class Land():
    def __init__(self, al, bd=0):
        self.al = al  # Altitude.
        self.bd = bd  # Buildings.
        self.ad = {"E": 1, "C": 1, "U": 1, "X": 0, "F": 1,  # Addition.
                   "R": 1, "M": 1, "L": 1, "H": 1, "T": 1}
        self.sl = 4  # Slots.
        self.wa = 0  # Water.
        self.cz = 0  # Citizens.
        self.sc = 1  # Satisfaction(citizens).
        self.sv = 0  # Slaves.
        self.ss = 1  # Satisfaction(slaves).
        self.ar = {"in": 0, "cv": 0, "cn": 0}  # Army.


class Nation():
    def __init__(self, wo, ix, na, ca, mn=300):
        self.wo = wo  # World.
        self.ix = ix
        self.na = na  # Name.
        self.ca = ca  # Capital.
        self.la = [ca]  # Land.
        cap = self.wo.world[ca[1]][ca[0]]  # Capital.
        spc = "F" if cap.al <= 3600 else "R"
        cap.bd = ["C", "R", spc]
        cap.ar["in"] = 500
        self.wo.world[ca[1]][ca[0]] = cap
        self.lv = 5  # Level(war).
        self.lt = 2  # Level(tech).
        self.mn = mn  # Money.
        self.ic = 0  # Income.

    def income(self):
        self.ic = 0
        for i in self.la:
            icm = 0  # Income of this land.
            cad = 1  # City addition.
            lnd = self.wo.world[i[1]][i[0]]
            bds = lnd.bd
            if bds == 0:
                continue
            for b in bds:
                if len(b) == 1:
                    b = b + "1"
                icm += data.income[b[0]]*int(b[1:])*lnd.ad[b[0]]
                if b[0] == "C":
                    cad *= 1 + int(b[1:]) * 0.2
                self.ic += icm * cad
        self.mn += self.ic
        print(f"Income of {self.na}: {self.ic}")


class Eutopia(Nation):
    def __init__(self, wo, ix, na, ca, mn=0):
        super().__init__(wo, ix, na, ca, 0)
        self.eu = 5354228880
        self.wo = wo  # World.
        self.ix = ix
        self.na = na  # Name.
        self.ca = ca  # Capital.
        self.la = [ca]  # Land.
        cap = self.wo.world[ca[1]][ca[0]]  # Capital.
        cap.bd = [f"C{self.eu}", f"E{self.eu}"]
        cap.ar["in"] = 500
        self.wo.world[ca[1]][ca[0]] = cap
        self.lv = 232792560  # Level(war).
        self.lt = 232792560  # Level(tech).
        self.mn = mn  # Money.
        self.ic = 0  # Income.


class World():
    def __init__(self, wd, ht, ls):
        self.world = []
        for i in range(ht):
            self.world.append([])
            for j in range(wd):
                self.world[i].append(Land(ls[i][j]))
                print(i, j, self.world[i][j])
        self.wl = []  # War list.
        self.at = []  # Attacked places(without any soldiers).


wd = ht = 8
world = World(wd, ht, [[random.random()]*wd]*ht)
nations = []
nations.append(Eutopia(world, 19, "Eutopia", (6, 6)))
nations.append(Nation(world, 7, "###", (4, 3)))


def move(pos, mov):
    x, y = se
    for i in mov:
        if i == "a":
            x -= 1
            if x < 0:
                x += 1
        if i == "d":
            x += 1
            if x >= wd:
                x -= 1
        if i == "s":
            y -= 1
            if y < 0:
                y += 1
        if i == "w":
            y += 1
            if y >= ht:
                y -= 1
    return (x, y)


for i in range(len(nations)):
    command = ""
    print(nations[i].na)
    se = nations[i].ca  # Selected.
    parts = []
    while command != "pass":
        print("parts:", parts)
        sl = world.world[se[1]][se[0]]  # Selected land.
        command = input("Command: ")
        parts = command.split("; ")
        if parts[0] == "select":
            if eval(parts[1]) in nations[i].la:
                se = eval(parts[1])
            else:
                print("Not your land!")
        if parts[0] == "check":
            print(se, sl.bd)
        if parts[0] == "add":
            nbd = parts[1]  # New building.
            if sl.bd == 0:
                print("You may not build anything here. This area is not exploited.")
            elif len(sl.bd) >= sl.sl:
                print("You may not build anything here. The slots are full.")
            elif nations[i].mn < data.price[nbd]:
                print("You do not have enough money.")
            else:
                nations[i].mn -= data.price[nbd]
                sl.bd.append(nbd)
                print("Money left: ", nations[i].mn)
            print("Buildings: ", sl.bd)
        if parts[0] == "move":
            typ, num, mov = parts[1:]
            if typ in world.world[se[1]][se[0]].ar.keys():
                if int(num) > world.world[se[1]][se[0]].ar[typ]:
                    print("You do not have so many soldiers here.")
                else:
                    to = move(se, mov)
                    nations[i].la.append(to)
                    print(int(num), to)
                    world.world[se[1]][se[0]].ar[typ] -= int(num)
                    world.world[to[1]][to[0]].ar[typ] += int(num)
                    print(f"Moved {num} {typ} to {to}. Land: {nations[i].la}.")
                    print("Left soldiers: ", world.world[se[1]][se[0]].ar[typ])


for i in range(len(nations)):
    nations[i].income()

_ = input()
