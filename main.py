import random
import time


# Klasse für den Spieler
class Player:
    def __init__(self, name):
        self.name = name
        self.stamina = 100
        self.skill = 0
        self.current_sport = None

    def train(self, hours):
        print(f"\n{self.name} trainiert für {hours} Stunden!")
        self.stamina -= hours * 10
        self.skill += hours * 5
        if self.stamina < 0:
            self.stamina = 0
        print(f"Stamina: {self.stamina}, Skill: {self.skill}")

    def rest(self, hours):
        print(f"\n{self.name} ruht sich {hours} Stunden aus.")
        self.stamina += hours * 15
        if self.stamina > 100:
            self.stamina = 100
        print(f"Stamina: {self.stamina}")


# Basisklasse für Sportarten
class Sport:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty

    def play(self, player):
        print(f"\n{player.name} spielt {self.name}!")
        success_chance = player.skill - self.difficulty + random.randint(0, 20)
        if success_chance > 10:
            print(f"{player.name} hat {self.name} erfolgreich gespielt!")
            player.skill += 10
        else:
            print(f"{player.name} hatte Schwierigkeiten mit {self.name}.")
            player.stamina -= 20


# Verschiedene Sportarten
class Soccer(Sport):
    def __init__(self):
        super().__init__("Fußball", 50)


class Basketball(Sport):
    def __init__(self):
        super().__init__("Basketball", 40)


class Tennis(Sport):
    def __init__(self):
        super().__init__("Tennis", 60)


class Boxing(Sport):
    def __init__(self):
        super().__init__("Boxen", 70)


# Der Ablauf des Abenteuers
def intro():
    print("Willkommen in der Welt der Sportarten!")
    print("Hier entscheidest du, welcher Sport der richtige für dich ist.")
    time.sleep(1)


def choose_sport():
    print("\nWelche Sportart möchtest du ausprobieren?")
    print("1. Fußball")
    print("2. Basketball")
    print("3. Tennis")
    print("4. Boxen")
    choice = input("Gib die Zahl deiner Wahl ein: ")
    if choice == '1':
        return Soccer()
    elif choice == '2':
        return Basketball()
    elif choice == '3':
        return Tennis()
    elif choice == '4':
        return Boxing()
    else:
        print("Ungültige Auswahl. Versuche es erneut.")
        return choose_sport()


def main():
    intro()
    name = input("\nWie lautet dein Name? ")
    player = Player(name)

    while True:
        if player.stamina <= 0:
            print("\nDu bist völlig erschöpft und kannst nicht weitermachen.")
            print("Spiel vorbei!")
            break

        print("\nWas möchtest du als nächstes tun?")
        print("1. Eine neue Sportart ausprobieren")
        print("2. Trainieren")
        print("3. Ausruhen")
        print("4. Aufhören")
        action = input("Gib die Zahl deiner Wahl ein: ")

        if action == '1':
            sport = choose_sport()
            player.current_sport = sport
            sport.play(player)
        elif action == '2':
            hours = int(input("\nWie viele Stunden möchtest du trainieren? "))
            player.train(hours)
        elif action == '3':
            hours = int(input("\nWie viele Stunden möchtest du dich ausruhen? "))
            player.rest(hours)
        elif action == '4':
            print("\nDanke fürs Spielen! Bis zum nächsten Mal.")
            break
        else:
            print("Ungültige Auswahl, versuche es erneut.")


if __name__ == "__main__":
    main()
