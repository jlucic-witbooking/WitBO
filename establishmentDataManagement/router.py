import threading
from WitbookingBackoffice import settings

__author__ = 'mongoose'

local_global = threading.local()

CURRENT_ESTABLISHMENT_PROPERTY = "selected_db"


class MultipleDbMiddleware(object):
    def process_request(self, request):
        attr = CURRENT_ESTABLISHMENT_PROPERTY
        value = None
        if CURRENT_ESTABLISHMENT_PROPERTY in request.session:
            value = request.session[CURRENT_ESTABLISHMENT_PROPERTY]
        elif request.user.is_authenticated():
            request.session[CURRENT_ESTABLISHMENT_PROPERTY] = request.user.default_db
            value = request.session[CURRENT_ESTABLISHMENT_PROPERTY]
        if value:
            setattr(local_global, attr, value)
            request.user.current_establishment = value


class MultiDBRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to auth_db.
        """
        # if 'witbookinguser' in model._meta.model_name:
        #     return 'default'

        if model._meta.app_label == 'establishmentDataManagement':
            if hasattr(local_global, CURRENT_ESTABLISHMENT_PROPERTY) and local_global.__getattribute__(CURRENT_ESTABLISHMENT_PROPERTY) in settings.DATABASES:
                return local_global.__getattribute__(CURRENT_ESTABLISHMENT_PROPERTY)

        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to auth_db.
        """
        # if 'witbookinguser' in model._meta.model_name:
        #     return 'default'

        if model._meta.app_label == 'establishmentDataManagement':
            return 'hoteldemo.com.v6'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth app is involved.
        """
        if obj1._meta.app_label == 'establishmentDataManagement' or \
                        obj2._meta.app_label == 'establishmentDataManagement':
            return True
        return None

    def allow_migrate(self, db, model):
        """
        Make sure the auth app only appears in the 'witmetadata'
        database.
        """
        if db == 'hoteldemo.com.v6':
            return model._meta.app_label == 'establishmentDataManagement'
        elif model._meta.app_label == 'establishmentDataManagement':
            return True
        return None