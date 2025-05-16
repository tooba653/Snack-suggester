import random

class SuggestionEngine:
    def __init__(self, snack_data):
        self.snack_data = snack_data

    def suggest_by_mood(self, mood):
        matches = [snack for snack in self.snack_data if mood in snack.mood_tags]
        return random.choice(matches) if matches else None

    def suggest_by_time(self, time_of_day):
        matches = [snack for snack in self.snack_data if time_of_day in snack.time_tags or 'any' in snack.time_tags]
        return random.choice(matches) if matches else None

    def suggest_random(self):
        return random.choice(self.snack_data)
