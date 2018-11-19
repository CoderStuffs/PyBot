"""Manipulate resources.json and its backups"""
import json

def load():
    """Returns resources as a dictionary
    {'resource_title': {'urls':[urls], 'attr':value},...}.
    """
    with open("Resources/resources.json") as f:            
        resources = json.load(f)
    return resources

def save(dictionary):
    """Dumps dictionary as json to resource.json.
    Call to backup currently just gives an undo option
    """            
    with open("Resources/resources.json", 'r+') as f:
        backup(f.read())
        f.seek(0)
        f.truncate()
        json.dump(dictionary, f, separators=(",\n",": "), sort_keys=True)
        #the separators try to maintain some human readability
        #if not desired, can easily remove the whitespace

def backup(original):
    """Not intended to be called directly yet, to be expanded upon."""
    with open("Backups/resources_backup.json", 'w') as f:
        f.write(original)
        
def restore():
    """Restores last backup."""
    with open(f'Backups/resources_backup.json') as backup_file:
        with open(f'Resources/resources.json', 'w') as target_file:
            target_file.write(backup_file.read())
