import os
import yaml

ordered_folders = ["discovery", "execution", "collection", "command-and-control", "defense-evasion", "credential-access", "privilege-escalation", "persistence", "impact", "lateral-movement", "exfiltration"]

tactic_abilities = {tactic: [] for tactic in ordered_folders}

file = input("Insert .yaml file name")
abilities_dir = "/home/administrador/caldera/plugins/stockpile/data/abilities/"

with open(file, 'r') as file:
    abilities_data = yaml.safe_load(file)

for ability_id in abilities_data['atomic_ordering']:
    for folder in ordered_folders:
        ability_file = os.path.join(abilities_dir, folder, f"{ability_id}.yaml")
        if os.path.exists(ability_file):
            tactic_abilities[folder].append(ability_id)
            break

print(tactic_abilities)
