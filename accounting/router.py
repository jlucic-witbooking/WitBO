__author__ = 'mongoose'
class ManagementRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to auth_db.
        """
        if model._meta.app_label == 'management':
            return 'witmetadata'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to auth_db.
        """
        if model._meta.app_label == 'management':
            return 'witmetadata'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth app is involved.
        """
        if obj1._meta.app_label == 'management' or \
           obj2._meta.app_label == 'management':
           return True
        return None

    def allow_migrate(self, db, model):
        """
        Make sure the auth app only appears in the 'witmetadata'
        database.
        """
        if db == 'witmetadata':
            return model._meta.app_label == 'management'
        elif model._meta.app_label == 'management':
            return True
        return None