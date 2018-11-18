from os import listdir

class Resources(object):
    """Provides tools for using resources in Resources directory"""
    
    __slots__ = ('dictionary')    

    def __init__(self):
        """Calls self.refresh to make self.dictionary available."""
        self.refresh()

    def refresh(self):
        """Sets self.dictionary to current resource information
        {'resource_title': [urls]}.
        """    
        resources = {}
        filenames = listdir(path='Resources')
        for filename in filenames:
            #take first half of filename split at file descriptor
            resource_title = filename.split('.')[0]
            urls = []
            with open(f'Resources/{filename}', 'r') as resource_file:
                for line in resource_file:
                    urls.append(line.strip())
                resources[resource_title] = urls
        self.dictionary = resources
        

    def add_url(self, target, url):
        """Adds {url} to existing {target} file.
        Creates a backup of {target} in Backups directory.
        Raises FileNotFoundError if {target} does not point to an existing file.
        """
        with open(f'Resources/{target}.txt', 'r+') as target_file:
            original_file = target_file.read() #read takes us to EOF
            target_file.write(f'{url}\n') #appends
        with open(f'Backups/{target}_backup.txt', 'w') as backup_file:
            backup_file.write(original_file)
            
        self.refresh()

    def create(self, resource_name):
        """Creates a new .txt file with {resource_name}.
        Raises "FileExists" error if file exists.
        """

        with open(f'Resources/{resource_name}.txt', 'x') as new_resource_file:
            pass
        
        self.refresh()        

    def restore(self, target):
        """Restores {target} with its backup."""
        with open(f'Backups/{target}_backup.txt') as backup_file:
            with open(f'Resources/{target}.txt', 'w') as target_file:
                target_file.write(backup_file.read())
                
        self.refresh()


