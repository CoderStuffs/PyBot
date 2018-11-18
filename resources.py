from os import listdir

class Resources(object):
    __slots__ = ('dictionary')

    def __init__(self):
        self.dictionary = self.refresh()

    def refresh(self):
    #returns a dict containing current resource information
    #{'resource_title': [urls]}
        resources = {}
        filenames = listdir(path='Resources')
        for filename in filenames:
            #take first half of filename split at file descriptor
            resource_title = filename.split('.')[0]
            urls = []
            with open(f'Resources/{filename}', 'r') as file:
                for line in file:
                    urls.append(line.strip())
                resources[resource_title] = urls
        return(resources)

    def add_url(self, target, url):
        #add url to existing resource file
        #creates a backup of original in Backups directory
        #raises FileNotFoundError if target does not point to an existing file

        with open(f'Resources/{target}.txt', 'r+') as target_file:
            original_file = target_file.read() #read takes us to EOF
            target_file.write(f'{url}\n') #appends
        with open(f'Backups/{target}_backup.txt', 'w') as backup_file:
            backup_file.write(original_file)

    def create(self, resource_name):
        #create a new .txt file with given resource name
        #Raises "FileExists" error if file exists

        with open(f'Resources/{resource_name}.txt', 'x') as new_resource_file:
            pass

    def restore(self, target):
        #restore a backup
        with open(f'Backups/{target}_backup.txt') as backup_file:
            with open(f'Resources/{target}.txt', 'w') as target_file:
                target_file.write(backup_file.read())


