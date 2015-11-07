from django.conf import settings
from db_file_storage.storage import DatabaseFileStorage

# Necessary for Windows support
def normpath(path):
    return path.replace('\\', '/')

class DbStorage(DatabaseFileStorage):
    def _get_unique_filename(self, model_cls, filename_field, filename):
        return DatabaseFileStorage._get_unique_filename(self, model_cls,
                                                        filename_field,
                                                        normpath(filename))
    def _get_storage_attributes(self, name):
        return DatabaseFileStorage._get_storage_attributes(self,
                                                           normpath(name))
