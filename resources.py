from os import listdir


def get_dictionary():
    """ Returns a dict containing resource information
        {'resource_title': [urls]}
    """
    resources = {}
    file_names = listdir(path='Resources')
    for file_name in file_names:
        # Take first half of filename split at file descriptor
        resource_title = file_name.split('.')[0]
        urls = []
        with open(f'Resources/{file_name}', 'r') as resource_file:
            for line in resource_file:
                urls.append(line.strip())
            resources[resource_title] = urls
    return resources
