class TbldbcitemRouter:
    def db_for_read(self, model, **hints):
        """
        Items are read-only from TUJ 'newsstand'
        """
        if model._meta.app_label == 'newsstand':
            return 'newsstand'
        return None
