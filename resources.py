from os import listdir

def get_dictionary():
#returns a dict containing resource information
#{'resource_title': [urls]}
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
    return(resources)           
