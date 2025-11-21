import time
import random

class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5

    def status(self):
        print("\n╔══════════════════════╗")
        print(f"   Status of {self.name} 🐾")
        print("╚══════════════════════╝")
        print(f"Hunger:     {self.hunger}/10")
        print(f"Energy:     {self.energy}/10")
        print(f"Happiness:  {self.happiness}/10")

    def feed(self):
        print(f"\n🍎 You fed {self.name}!")
        self.hunger = min(10, self.hunger + 3)

    def play(self):
        print(f"\n🎾 You played with {self.name}!")
        self.happiness = min(10, self.happiness + 3)
        self.energy = max(0, self.energy - 2)

    def sleep(self):
        print(f"\n💤 {self.name} is sleeping...")
        time.sleep(1)
        self.energy = min(10, self.energy + 4)

    def random_event(self):
        events = [
            f"{self.name} chased a butterfly 🦋",
            f"{self.name} rolled on the floor 🐾",
            f"{self.name} found a shiny leaf 🍃",
        ]
        print("\n✨ Random Event:", random.choice(events))
        self.happiness = min(10, self.happiness + 1)

# -------------------------
# Game loop
# -------------------------
print("🐱 Welcome to your Virtual Pet!")
pet_name = input("Name your pet: ")

pet = VirtualPet(pet_name)

while True:
    pet.status()
    print("\nWhat would you like to do?")
    print("1. Feed 🍎")
    print("2. Play 🎾")
    print("3. Sleep 😴")
    print("4. Quit ❌")

    choice = input("Choose (1/2/3/4): ")

    if choice == "1":
        pet.feed()
    elif choice == "2":
        pet.play()
    elif choice == "3":
        pet.sleep()
    elif choice == "4":
        print("\n💖 Bye bye! Your pet will miss you!")
        break
    else:
        print("❗ Invalid choice!")

    pet.random_event()
    time.sleep(1)
