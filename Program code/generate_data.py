import csv
import random
from datetime import datetime, timedelta

students = ["Rahul", "Ankit", "Priya", "Sneha", "Aman", "Riya", "Karan", "Neha", "Arjun", "Simran"]

start_date = datetime(2026, 3, 1)

with open("attendance.csv", "w", newline="") as file:
    writer = csv.writer(file)

    for i in range(10):  # 10 days
        date = (start_date + timedelta(days=i)).strftime("%Y-%m-%d")
        for student in students:
            # 70% present, 30% absent (realistic)
            status = "P" if random.random() > 0.3 else "A"
            writer.writerow([student, date, status])

print("✅ Dataset created successfully with 100 entries!")