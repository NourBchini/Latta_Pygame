import random


class MemoryBook:
    """Latta HAS a memory book. One object living inside another is composition."""

    def __init__(self):
        self.memories = [
            "Remember the rainy afternoon we sat by the window? You wrapped me in your sleeve.",
            "You used to tuck my ear under the blanket so I wouldn't get cold.",
            "That time you whispered secrets and I kept every one.",
            "I still remember you carrying me down the hallway, one hop at a time.",
            "When you couldn't sleep, you counted my stitches instead of sheep.",
            "You once introduced me to the moon and said we were both good listeners.",
            "I kept you company through every scraped knee. I would do it again.",
            "You whispered 'good night, Latta' even on the nights you were sad.",
        ]

    def pick_one(self):
        return random.choice(self.memories)


class Bunny:
    # Class constants: the same rule for every bunny, not one copy per object.
    HUNGER_PER_SECOND = 100 / 300  # full -> super hungry in 5 minutes
    CLEAN_DECAY_PER_SECOND = 100 / 480
    HAIR_DECAY_PER_SECOND = 100 / 360
    HAPPY_DECAY_PER_SECOND = 100 / 600
    HEALTHY_FOODS = ["carrots", "lettuce", "hay", "apple", "orange"]

    def __init__(self, name):
        # Constructor: runs when we write latta = Bunny("Latta")
        self.name = name
        self.hunger = 0
        self.happiness = 70
        self.cleanliness = 70
        self.hair_neatness = 60
        self.age = 0
        self.memories = MemoryBook()
        self._hungry_nudge_timer = 0

    def update(self, seconds_passed):
        """The game hands us elapsed seconds. We change how Latta feels."""
        old_hunger = self.hunger
        self.hunger = min(100, self.hunger + seconds_passed * self.HUNGER_PER_SECOND)
        self.cleanliness = max(0, self.cleanliness - seconds_passed * self.CLEAN_DECAY_PER_SECOND)
        self.hair_neatness = max(0, self.hair_neatness - seconds_passed * self.HAIR_DECAY_PER_SECOND)
        self.happiness = max(0, self.happiness - seconds_passed * self.HAPPY_DECAY_PER_SECOND)

        if old_hunger < 100 <= self.hunger:
            return f"{self.name} is super hungry... she thumps a little paw."
        if old_hunger < 70 <= self.hunger:
            return f"{self.name} is getting hungry."

        if self.hunger >= 70:
            self._hungry_nudge_timer += seconds_passed
            if self._hungry_nudge_timer >= 30:
                self._hungry_nudge_timer = 0
                if self.hunger >= 100:
                    return f"{self.name} is super hungry... she thumps a little paw."
                return f"{self.name} is getting hungry."
        else:
            self._hungry_nudge_timer = 0
        return None

    def pick_food(self, food):
        if food not in self.HEALTHY_FOODS:
            self.happiness = max(0, self.happiness - 5)
            return f"{self.name} does not like this food! Pick a healthier choice."
        self.happiness = min(100, self.happiness + 5)
        return f"{self.name} loves {food}! Great job picking healthy food!"

    def feed(self, food):
        self.hunger = max(0, self.hunger - 35)
        self.happiness = min(100, self.happiness + 5)
        return f"{self.name} nibbles happily on the fresh {food}."

    def eat(self, food):
        """One player action: she judges the food, then eats it if she likes it."""
        message = self.pick_food(food)
        if food not in self.HEALTHY_FOODS:
            return message
        return self.feed(food)

    def brush(self):
        self.hair_neatness = min(100, self.hair_neatness + 25)
        self.happiness = min(100, self.happiness + 5)
        return f"{self.name} looks so cute with her shiny, clean fur!"

    def make_laugh(self):
        self.happiness = min(100, self.happiness + 15)
        return f"{self.name} is laughing and having fun!"

    def shower(self):
        self.cleanliness = 100
        self.hair_neatness = max(0, self.hair_neatness - 15)
        self.happiness = min(100, self.happiness + 5)
        return f"{self.name} is clean and fluffy! But you have to brush her fur again."

    def tell_memory(self):
        self.happiness = min(100, self.happiness + 8)
        return self.memories.pick_one()

    def mood(self):
        if self.hunger >= 100:
            return "starving"
        if self.hunger >= 70:
            return "hungry"
        if self.happiness >= 85 and self.hair_neatness >= 70:
            return "glowing"
        if self.happiness < 30:
            return "sad"
        if self.cleanliness < 30:
            return "grubby"
        return "content"
