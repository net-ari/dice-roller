from die import Die

class Roller:
    """Maintains a list of dice which it can roll at once or add to.

    Attributes:
        dice_list (list[Die]): List of current dice. Begins empty.
    """
    def __init__(self):
        self._dice_list: list[Die] = []

    def add(self,die: Die) -> None:
        """Adds a die to the internal list of dice.

        Args:
            die (Die): Die to be added.
        """
        self._dice_list.append(die)
    
    def rollAll(self) -> list[tuple[str,int]]:
        """Rolls all dice in the internal list of dice, returning a list of results.

        Returns:
            list[int]: List of dice roll results in order of dice rolled.
        """
        results: list[tuple[str,int]] = []

        for die in self._dice_list:
            results.append((die.get_name(),die.roll()))
        
        return results