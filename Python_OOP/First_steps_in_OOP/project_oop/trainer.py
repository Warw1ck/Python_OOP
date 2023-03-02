from pokemon import Pokemon


class Trainer:

    def __init__(self, name):
        self.name = name
        self.pokemons = {}

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon.name not in self.pokemons:
            self.pokemons[pokemon.name] = pokemon.pokemon_details()
            return f'Caught {pokemon.pokemon_details()}'
        else:
            return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        if pokemon_name in self.pokemons:
            del self.pokemons[pokemon_name]
            return f"You have released {pokemon_name}"
        else:
            return "Pokemon is not caught"

    def trainer_data(self):
        the_print = [f"Pokemon Trainer {self.name}", f'Pokemon count {len(self.pokemons)}']
        for value in self.pokemons.values():
            the_print.append(value)

        return '\n'.join(the_print)

