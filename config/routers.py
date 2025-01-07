class PrimaryReplicaRouter:
    """
    A router to direct read and write operations:
    - Reads go to the replica database.
    - Writes go to the primary (default) database.
    """

    def db_for_read(self, model, **hints):
        """
        Direct reads to the replica database by default.
        """
        if model._meta.app_label in ['auth', 'sessions']:  # Redirect auth-related reads to primary
            return 'default'
        return 'replica'

    def db_for_write(self, model, **hints):
        """
        Direct all writes to the primary database.
        """
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations between objects in both databases.
        """
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Apply migrations only to the primary database.
        """
        return db == 'default'
