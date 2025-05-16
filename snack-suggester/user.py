class User:
    def __init__(self, name):
        self.name = name
        self.favorites = []

    def add_favorite(self, snack):
        if snack not in self.favorites:
            self.favorites.append(snack)

    def get_favorites(self):
        return self.favorites
