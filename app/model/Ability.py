import csv
import sys 

class Ability():
    def __init__(self, name, description, generation):
        self.name = name
        self.description = description
        self.generation = generation

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
        for ability in self.abilities:
            print(f"Name: {ability.name}, Description: {ability.description}, Generation: {ability.generation}")
            

if __name__ == "__main__":
    ability_repo = AbilityRepository()
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        print("No file path provided.")
        sys.exit(1)
    
    ability_repo.read_tsv(file_path)
    ability_repo.dump_records()