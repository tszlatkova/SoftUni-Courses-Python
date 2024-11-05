# The Trainer class should receive a name (string). The Trainer should also have an
# attribute pokemons (list, empty by default). The Trainer has three methods:
# -	add_pokemon(pokemon: Pokemon)
# o	Adds the pokemon to the collection and returns
# "Caught {pokemon_name} with health {pokemon_health}".
# Hint: use the pokemon's details method.

# o	If the pokemon is already in the collection, return "This pokemon is already caught"
# Hint: to import the Pokemon class, you should add "from project.pokemon import Pokemon"
# -	release_pokemon(pokemon_name: string)
# o	Check if you have a pokemon with that name and remove it from the collection. In the
# end, returns "You have released {pokemon_name}"
# o	If there is no pokemon with that name in the collection, return
# "Pokemon is not caught"
# -	trainer_data()
# o	The method returns the information about the trainer and his pokemon's collection
# in the format:
# "Pokemon Trainer {trainer_name}
#  Pokemon count {the amount of pokemon caught}
#  - {pokemon_details1}
#  ...
#  - {pokemon_detailsN}"
from typing import List

from pokemon import Pokemon


class Trainer:

    def __init__(self, name: str):
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon in self.pokemons:
            return "This pokemon is already caught"
        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str) -> str:
        # for p in self.pokemons:
        #     if p.name == pokemon_name:
        #         self.pokemons.remove(p)
        #         return f"You have released {pokemon_name}"

        # pokemon_to_release = next(filter(lambda p: p.name == pokemon_name,
        # self.pokemons), None)

        pokemon_to_release = next((p for p in self.pokemons if p.name == pokemon_name),
                                  None)
        if pokemon_to_release:
            self.pokemons.remove(pokemon_to_release)
            return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self) -> str:
        result = f'Pokemon Trainer {self.name}\n' + \
                 f'Pokemon count {len(self.pokemons)}'

        for p in self.pokemons:
            result += f'\n- {p.pokemon_details()}'

        return result

        # info = [f'Pokemon Trainer {self.name}', f'Pokemon count {len(self.pokemons)}']
        # for p in self.pokemons:
        #     info.append(f'-{p.pokemon_details()}')
        # return'\n'.join(info)


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
