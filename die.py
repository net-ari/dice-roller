import random

class Die: 
    """Simulation of a randomly rollable die with a set number of sides.

    Attributes:
        sides (int): The number of sides of the die.
    """
    def __init__(self,dSides):
        self.sides = dSides
        self.name = f"d{dSides}"

    def roll(self) -> int:
        """Rolls the die based on its number of sides and returns the result.

        Returns:
            int: Result of the roll.
        """
        return random.randint(1,self.sides)

    def get_name(self) -> str:
        """Returns the name of the Die.

        Returns:
            str: _description_
        """
        return self.name