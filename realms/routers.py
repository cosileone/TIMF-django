class RealmRouter:
    def db_for_read(self, model, **hints):
        """
        Realms are read-only from TUJ 'newsstand'
        """
        if model._meta.app_label == 'realms':
            return 'newsstand'
        return None
