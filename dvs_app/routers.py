# routers.py

class DatabaseRouter:
    """
    A router to control all database operations on models in the
    dvs_app application.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read dvs_app models go to backup database.
        """
        if model._meta.app_label == 'dvs_app':
            return 'backup'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write dvs_app models go to backup database.
        """
        if model._meta.app_label == 'dvs_app':
            return 'backup'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the dvs_app app is involved.
        """
        if obj1._meta.app_label == 'dvs_app' or obj2._meta.app_label == 'dvs_app':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the dvs_app app only appears in the 'backup'
        database.
        """
        if app_label == 'dvs_app':
            return db == 'backup'
        return None
