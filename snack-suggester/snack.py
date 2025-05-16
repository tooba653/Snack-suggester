class Snack:
    def __init__(self, name, category, mood_tags, time_tags):
        self.name = name
        self.category = category
        self.mood_tags = mood_tags
        self.time_tags = time_tags

    def __str__(self):
        return f"{self.name} ({self.category})"
