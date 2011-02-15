from django.db import connections

class ModelSpecified(object):
    """
    A router to control all database operations on models by parameter
    Specify model.connection_name to refer to any db other than 'default'
    """

    def db_for_read(self, model, **hints):
        if hasattr(model,'connection_name'):
            return model.connection_name
        return None

    def db_for_write(self, model, **hints):
        if hasattr(model,'connection_name'):
            return model.connection_name
        return None

    def allow_syncdb(self, db, model):
        if hasattr(model,'connection_name'):
            return model.connection_name == db
        return db == 'default'
