import time
import random
import datetime

class DailyRiddleApp:
    def __init__(self):
        self.riddles = [
            {"question": "What has keys but can't open locks?", "answer": "A piano"},
            {"question": "What has to be broken before you can use it?", "answer": "An egg"},
            {"question": "I’m tall when I’m young, and I’m short when I’m old. What am I?", "answer": "A candle"},
            {"question": "What month of the year has 28 days?", "answer": "All of them"},
            {"question": "What is full of holes but still holds water?", "answer": "A sponge"}
        ]
        self.last_riddle_time = None
        self.current_riddle = None
    
    def get_riddle(self):
        if self.is_new_riddle_needed():
            self.current_riddle = random.choice(self.riddles)
            self.last_riddle_time = datetime.datetime.now()
        return self.current_riddle

    def is_new_riddle_needed(self):
        if self.last_riddle_time is None:
            return True
        return datetime.datetime.now() - self.last_riddle_time >= datetime.timedelta(hours=24)
    
    def show_riddle(self):
        riddle = self.get_riddle()
        print(f"Riddle of the Day: {riddle['question']}")

if __name__ == "__main__":
    app = DailyRiddleApp()
    
    # Simulate checking the riddle periodically
    while True:
        app.show_riddle()
        print("Check back tomorrow for a new riddle!\n")