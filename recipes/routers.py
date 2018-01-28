class RecipeRouter:
    def db_for_read(self, model, **hints):
        """
        Recipes should read from both DBs but let's default to newsstand
        """
        if model._meta.app_label == 'recipes':
            return 'newsstand'
        return None

    def db_for_write(self, model, **hints):
        """
        Recipes should always be written to default DB
        """
        if model._meta.app_label == 'recipes':
            return 'default'
        return None
