class Jel:
    def __init__(self, ora, perc, mp, x, y):
        self.ora = ora
        self.perc = perc
        self.mp = mp
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"{self.ora} {self.perc}{self.mp}{self.x}{self.y}"
        
f = open("jel.txt", "rt", encoding="utf-8")

lista = []
db = 0

for sor in f:
    sor = sor.strip().split(" ")
    lista.append(Jel(sor[0],sor[1],sor[2],sor[3],sor[4]))
    
print('2.feladat')
sorszam = int(input("Adjon meg egy sorszámot: "))
print (f"x={lista[sorszam-1].x}  y={lista[sorszam-1].y}")

print('3.feladat')
def eltelt(elso,masodik):
    i1 = elso[0] + 3600 + elso[1] * 60 + masodik[2]
    i2 = elso[0] + 3600 + elso[1] * 60 + masodik[2]
    elt = i2-i1
    return elt
