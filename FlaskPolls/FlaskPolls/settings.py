"""
Settings for the polls application.

You can set values of REPOSITORY_NAME and REPOSITORY_SETTINGS in
environment variables, or set the default values in code here.
"""

from os import environ

REPOSITORY_NAME = environ.get('REPOSITORY_NAME', 'memory')
#If you want to use Azure table store or Mondo DB, you must first initialize those data stores elsewhere,
#then set the necessary environment variables that tell the app how to connect to the store.

#The implementations of the Repository class that are specific to each data store can be found in 
#models\azuretablestorage.py, models\mongodb.py, and models\memory.py. The Azure storage implementation uses the 
#azure-storage package; the Mongo DB implementation uses the pymongo package. Both packages are included in the 
#project template's requirements.txt file.


if REPOSITORY_NAME == 'azuretablestorage':
    REPOSITORY_SETTINGS = {
        'STORAGE_NAME': environ.get('STORAGE_NAME', ''),
        'STORAGE_KEY': environ.get('STORAGE_KEY', ''),
        'STORAGE_TABLE_POLL': environ.get('STORAGE_TABLE_POLL', 'polls'),
        'STORAGE_TABLE_CHOICE': environ.get('STORAGE_TABLE_CHOICE', 'choices'),
    }
elif REPOSITORY_NAME == 'mongodb':
    REPOSITORY_SETTINGS = {
        'MONGODB_HOST': environ.get('MONGODB_HOST', None),
        'MONGODB_DATABASE': environ.get('MONGODB_DATABASE', 'polls'),
        'MONGODB_COLLECTION': environ.get('MONGODB_COLLECTION', 'polls'),
    }
elif REPOSITORY_NAME == 'memory':
    REPOSITORY_SETTINGS = {}
else:
    raise ValueError('Unknown repository.')
