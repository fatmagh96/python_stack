from pet import Pet

from ninja import Ninja

rusty = Pet("cat","jump",100,110)

mio = Ninja("Mio","Chan",rusty,"kibble","fish")



mio.feed().walk().bathe()
print(f"health is : {rusty.health} energy is { rusty.energy}")