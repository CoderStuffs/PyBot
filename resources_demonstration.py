from resources import Resources
#great naming scheme...

#I thought that this might help you to quickly evaluate the code
#admins may find it convenient to use the bot to modify resources

resources = Resources()
#initializing the class will give you access to .dictionary

#here we create a new resource and view its contents (empty)
#note that these methods automatically update self.dictionary by calling self.refresh
resources.create('xtest')
print(resources.dictionary['xtest'])

#next we add our first url, note that this makes a backup as well
resources.add_url('xtest', 'https://google.com')
print(resources.dictionary['xtest'])

#make another backup, add a second url
resources.add_url('xtest', 'malformed_urlxxxxxxxxxxxxxxx')
print(resources.dictionary['xtest'])

#restore backup and show that the contents correctly display https://g...
resources.restore('xtest')
print(resources.dictionary['xtest'])

#Run me again and note that it excepts when trying to create 'xtest' due to exclusive write mode

