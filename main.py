import tkinter as tk
from tkinter import messagebox
import json
import os

class TrainingPlanner:
    def __init__(self, root):
        self.root = root
        self.root.title("Training Planner")

        self.date_label = tk.Label(root, text="Дата (YYYY-MM-DD):")
        self.date_label.pack()
        self.date_entry = tk.Entry(root)
        self.date_entry.pack()

        self.type_label = tk.Label(root, text="Тип тренировки:")
        self.type_label.pack()
        self.type_entry = tk.Entry(root)
        self.type_entry.pack()

        self.duration_label = tk.Label(root, text="Длительность (мин):")
        self.duration_label.pack()
        self.duration_entry = tk.Entry(root)
        self.duration_entry.pack()

        self.add_button = tk.Button(root, text="Добавить тренировку", command=self.add_training)
        self.add_button.pack()

        self.trainings = []
        self.load_data()

    def add_training(self):
        date = self.date_entry.get()
        workout_type = self.type_entry.get()
        duration = self.duration_entry.get()

        if not self.validate_input(date, workout_type, duration):
            return

        self.trainings.append({
            "date": date,
            "type": workout_type,
            "duration": int(duration)
        })
        self.save_data()
        self.clear_entries()

    def validate_input(self, date, workout_type, duration):
        if not self.is_valid_date(date):
            messagebox.showerror("Ошибка", "Некорректный формат даты. Используйте YYYY-MM-DD.")
            return False
        if not duration.isdigit() or int(duration) <= 0:
            messagebox.showerror("Ошибка", "Длительность должна быть положительным числом.")
            return False
        return True

    def is_valid_date(self, date):
        try:
            year, month, day = map(int, date.split('-'))
            return 1 <= month <= 12 and 1 <= day <= 31
        except ValueError:
            return False

    def save_data(self):
        with open('trainings.json', 'w') as f:
            json.dump(self.trainings, f)

    def load_data(self):
        if os.path.exists('trainings.json'):
            with open('trainings.json', 'r') as f:
                self.trainings = json.load(f)

    def clear_entries(self):
        self.date_entry.delete(0, tk.END)
        self.type_entry.delete(0, tk.END)
        self.duration_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TrainingPlanner(root)
    root.mainloop()
