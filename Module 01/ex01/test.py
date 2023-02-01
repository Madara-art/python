from game import Stark
arya = Stark("Arya")
print(arya.__dict__)
print(arya.is_alive)
arya.die()
print(arya.is_alive)
print(arya.doc())
