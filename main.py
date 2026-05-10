from die import Die
from roller import Roller

r: Roller = Roller()

for i in range(5,21):
    r.add(Die(i))

results = r.rollAll()

for result in results:
    print(f"{result[0]} : {result[1]}")