import pokebase as pb
import random
import requests

class PokemonFetcher:
    def __init__(self):
        self._id = None
        self._data = None
        self._name = None
        self._img = None
        self._type = None
        self._evolves_from = None
        self._evolves_to = None
    
    def set_id(self):
        self._id = random.randrange(1, 1025)
    
    def set_data(self):
        self._data = pb.pokemon(self._id)
        
    def set_name(self):
        name = str(self._data)
        self._name = self.format_name(name)

    def set_img(self):
        return f"https://img.pokemondb.net/artwork/large/{str(self._data)}.jpg"

    def set_type(self):
        types = [type_data.type.name.capitalize() for type_data in self._data.types]
        self._type = "/".join(types)

    def set_evolves_from(self):
        evolves_from = str(self._data.species.evolves_from_species).capitalize()
        self._evolves_from = self.format_name(evolves_from)
        
    def set_evolves_to(self):
        species_data = pb.pokemon_species(self._data.species.name)
        evolution_chain_url = species_data.evolution_chain.url
        data = requests.get(evolution_chain_url).json()
        chain = data["chain"]
        evolution_chain = chain.get('evolves_to')
        
        if not evolution_chain:
            self._evolves_to = "None"
            return
        
        next_evolution = evolution_chain[0]['species']['name']
        self._evolves_to = self.format_name(next_evolution)
        
    def format_name(self, name):
        names_with_capitalization_and_hypen = {'chi-yu', 'chien-pao', 'ho-oh', 'poryon-z', 'ting-lu', 'wo-chien'}
        names_without_capitalization_with_hypen = {'hakamo-o', 'jangmo-o', 'kommo-o'}
        
        if name in names_without_capitalization_with_hypen or '-' not in name:
            return name.capitalize()
        else:            
            if name in names_with_capitalization_and_hypen:
                return "-".join([word.capitalize() for word in name.split("-")])
            else:
                return " ".join([word.capitalize() for word in name.split("-")])                  
        
    def get_type_text(self):
        vowels = { "a", "e", "i" , "o", "u"}
        first_letter = self._type[0].lower()
        article = "an" if first_letter.lower() in vowels else "a"
        return f" is {article} {self._type}-type"
    
    def get_evolve_text(self):        
        if self._evolves_from != "None":
            return f" and it evolves from {self._evolves_from}"
        elif self._evolves_to != "None":
            return f" and it evolves into {self._evolves_to}"
        return " and has no evolutions"        

    def get_caption(self):
        type_text = self.get_type_text()
        evolve_text = self.get_evolve_text()
        return f"The Pokemon of the day is {self._name}! \n\n{self._name}{type_text}{evolve_text}."
             
    def generate_caption(self):
        self.set_id()
        self.set_data()
        self.set_name()
        self.set_type()
        self.set_evolves_from()
        self.set_evolves_to()
        return self.get_caption()
