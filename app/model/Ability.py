import csv
import sys 
import json

class Ability():
    def __init__(self, name, description, generation):
        self.name = name
        self.description = description
        self.generation = generation
    
    def to_dict(self):
        # Convert the Ability object to a dictionary
        return {
            'name': self.name,
            'description': self.description,
            'generation': self.generation
        }

class AbilityRepository():
    def __init__(self):
        self.abilities = []

    def read_tsv(self, path):
        # read a TSV file with a header row and return a list of Ability objects, one for each row, where the columns are name (str), description (str), and generation (int)
        
        with open(path, 'r') as file:
            reader = csv.DictReader(file, delimiter='\t')
            # skip first row
            for row in reader:
                self.abilities.append(Ability(row['Name'], row['Description'], int(row['Gen']))) 
                
    def dump_records(self):
        print(type(self.abilities[0]))
        for ability in self.abilities:
            print(f"Name: {ability.name}, Description: {ability.description}, Generation: {ability.generation}")
    
    def get_records(self):
        return self.abilities
    
    def jsonify_abilities(self):
        # Convert the list of Ability objects to a list of dictionaries
        abilities_dict_list = [ability.to_dict() for ability in self.abilities]
        # Convert the list of dictionaries to a JSON string
        return json.dumps(abilities_dict_list, indent=4)
            

if __name__ == "__main__":
    ability_repo = AbilityRepository()
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        print("No file path provided.")
        sys.exit(1)
    
    ability_repo.read_tsv(file_path)
    ability_repo.dump_records()