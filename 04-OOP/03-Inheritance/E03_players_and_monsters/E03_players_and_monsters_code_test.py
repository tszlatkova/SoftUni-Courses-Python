from project.hero import Hero
from project.elf import Elf
from project.blade_knight import BladeKnight


hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))

elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)

blade_knight = BladeKnight('BK', 5)
print(blade_knight.__class__.__bases__[0].__name__)
print(str(blade_knight))
