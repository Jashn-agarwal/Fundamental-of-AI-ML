import csv
from datetime import datetime
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

FILE_NAME = "attendance.csv"

# Mark Attendance
def mark_attendance():
    name = input("Enter student name: ")
    status = input("Enter attendance (P/A): ").upper()

    if status not in ['P', 'A']:
        print("Invalid input!\n")
        return

    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, date, status])

    print("✅ Attendance marked!\n")


# View Attendance
def view_attendance():
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            print("\n--- Attendance Records ---")
            for row in reader:
                print(f"{row[0]} | {row[1]} | {row[2]}")
            print()
    except FileNotFoundError:
        print("No records found.\n")


# Attendance Percentage
def attendance_percentage():
    name = input("Enter student name: ")
    total = 0
    present = 0

    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0].lower() == name.lower():
                    total += 1
                    if row[2] == 'P':
                        present += 1

        if total == 0:
            print("No records found.\n")
        else:
            percent = (present / total) * 100
            print(f"{name}'s Attendance: {percent:.2f}%\n")

    except FileNotFoundError:
        print("No data found.\n")


# AI Prediction
def predict_attendance():
    try:
        df = pd.read_csv(FILE_NAME, header=None)
        df.columns = ["Name", "Date", "Status"]

        le_name = LabelEncoder()
        le_status = LabelEncoder()

        df["Name"] = le_name.fit_transform(df["Name"])
        df["Status"] = le_status.fit_transform(df["Status"])

        X = df[["Name"]]
        y = df["Status"]

        model = DecisionTreeClassifier()
        model.fit(X, y)

        student_name = input("Enter student name: ")

        try:
            name_encoded = le_name.transform([student_name])[0]
        except:
            print("Student not found.\n")
            return

        prediction = model.predict([[name_encoded]])
        result = le_status.inverse_transform(prediction)

        print(f"🤖 Predicted Attendance: {result[0]}\n")

    except FileNotFoundError:
        print("No data available.\n")


# Main Menu
def main():
    while True:
        print("===== Attendance System (AI) =====")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Attendance Percentage")
        print("4. Predict Attendance (AI)")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            mark_attendance()
        elif choice == '2':
            view_attendance()
        elif choice == '3':
            attendance_percentage()
        elif choice == '4':
            predict_attendance()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice!\n")


# Run program
main()