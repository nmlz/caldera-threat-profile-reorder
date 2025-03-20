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
        ability_file = os.path.join(abilities_dir, folder, f"{ability_id}.yml")
        if os.path.exists(ability_file):
            tactic_abilities[folder].append(ability_id)
            break

with open(output_file, 'w') as newfile:
    newfile.writelines("---\n")
    newfile.writelines(f"id: {output_file}\n")
    newfile.writelines(f"description: Custom adversary threat profile created using AtomicThreatProfile and ordered with reorder.py\n")
    newfile.writelines("atomic_ordering:\n")
    for technique in tactic_abilities:
        for procedure in tactic_abilities[technique]: 
            newfile.writelines(f"- {procedure}\n")
newfile.close()
