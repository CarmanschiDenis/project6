#declararea variabilelor globale
players = [] #array
heal_power = 15
class characters():
    Name = ('')
    Hp = 0
    Armor = 0
    DamagePower = 0

    def __init__(self, name, hp, armor, damage):
        self.Name = name
        self.Hp = hp
        self.Armor = armor
        self.DamagePower = damage


class game(characters):
    def heal(self):
        global heal_power
        self.Hp = self.Hp + heal_power
        #sau self.Hp += heal.power
        print(self.Name , 'hp =', self.Hp, 'left')
    def attack(self, DamagePower):
        if self.Hp - DamagePower > 0:
            if self.Armor > 0: #Hp=100 si DamageP. = 20, Armor = 40
                self.Armor = self.Armor - DamagePower
                self.Hp = self.Hp - (DamagePower/2)

            else:
                self.Hp = self.Hp - DamagePower
            print(self.Name, 'have',
                  self.Hp, 'left',
                  self.Armor, 'armor left')
            return True
        else:
            print(self.Name, 'died')
            return False

while 1:
    try:
        confirmation = input('Enter any key to start')
        break
    except:
        print('Wrong Data input')
        continue

hp = int(input('Enter players hp'))
armor =int(input('Enter player armor'))
damage = int(input('Enter player damage power'))
for i in range(0, 2):
    name = input('Enter player name')
    #daca vrem ca playerii sa aiba diferit damage scriem codul cu int de mai sus
    players.append(game(name, hp, armor, damage))
alive = True #verificam daca toti sunt in viata
player1 = players[0]
player2 = players[1]

current_player = player1
next_player = player2

while alive: #cat timp viata = true jocul continua daca = False jocul se termina
    print('Turn to choose for', current_player.Name)
    print('Enter 1 to attack')
    print('Enter 2 to heal')
    print('Enter 3 to continue')
    move = int(input())
    if move == 1:
        alive = next_player.attack(current_player.DamagePower)
    elif move == 2:
        current_player.heal()
    elif move == 3:
        continue
    else:
        print('Wrong data')
        continue
    if current_player == player1:
        current_player = player2
        next_player = player1
    else:
        current_player = player1
        next_player = player2