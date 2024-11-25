class PrimaryReplicaRouter:
    """
    A router to control all database operations:
    - Reads go to the replica database.
    - Writes go to the default (primary) database.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read data go to the replica database.
        """
        return 'replica'

    def db_for_write(self, model, **hints):
        """
        Attempts to write data go to the primary database.
        """
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow any relation between objects in both databases.
        """
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Ensure migrations only apply to the primary database.
        """
        return db == 'default'
