import re
import json
import shutil
import os # used for deleting json when restoring from backup

HELP_TEXT = 'I can give you some information depending on the topics available.\nHere are the available topics:\
            \nAsk for a topic by saying "!info [topic]"\n```{urls}```\n\
            \nTo add a URL resource to our topics, use the following command:\n\t"!info add [topic] [url]"'

INVALID_TOPIC_TEXT = 'That topic does not exist. If you wish to start the list of resources, use the following command:\
            \n\t"!info add [topic] [url]"'


class Resources(object):
    """Provides tools for using resources in Resources directory"""
    
    url_pattern = re.compile("^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$")

    def __init__(self):
        """Calls self.refresh to make self.dictionary available."""
        self.resources = {}
        self.load_file()

    def load_file(self):
        """Sets self.dictionary to current resource information
        {'resource_title': [urls]}.
        """
        with open("resources.json", "r") as resource_file:
            self.resources = json.loads(resource_file.read())
        
    def save_file(self):
        self.backup()
        with open('resources.json', 'w') as outfile:
            json.dump(self.resources, outfile)

    def add_url(self, target:str, url:str) -> bool:
        """Adds {url} to existing {target} file.
        Creates a backup of {target} in Backups directory.
        Raises FileNotFoundError if {target} does not point to an existing file.
        """
        target = target.lower()
        # does not add malformed URLs
        if not re.search(Resources.url_pattern, url):
            return False

        # trying to add a url for a target that does not exist - creates empty
        if target not in self.resources:
            self.resources[target] = []

        # does not add direct duplicates
        if url in self.resources[target]:
            return False


        self.resources[target].append(url)

        self.save_file()
        return True

    def backup(self) -> None:
        shutil.copyfile("resources.json", "resources_backup.json")

    def restore(self) -> None:
        """ Restore database with its backup """
        os.remove("resources.json")
        shutil.move("resources_backup.json", "resources.json")
        self.load_file()

    def get_urls(self, target: str) -> [str]:
        """ 
        Returns the list of urls associated with {target}
        May raise KeyError if target does not exist.
        """
        return self.resources[target.lower()]

    def get_keys(self) -> [str]:
        """ Returns a list of all the keys (representing topics) """
        return [k.capitalize() for k in self.resources.keys()]

    def get_help_text(self) -> str:
        return HELP_TEXT.format(urls='\n'.join(self.get_keys()))

    def get_invalid_text(self) -> str:
        return INVALID_TOPIC_TEXT