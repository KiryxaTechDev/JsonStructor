class KeyDuplicateError(Exception):
    def __init__(self, key, message="The key '{}' already exists"):
        self.key = key
        self.message = message.format(key)
        super().__init__(self.message)