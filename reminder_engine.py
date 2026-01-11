from datetime import datetime
from core.database import init, record, history 

init()

def log_dose():
    name = input("Enter patient name: ")
    supplement = input("Enter supplement/medication: ")
    now = datetime.now().strftime("%H:%M")
    record(name, supplement, now)
    print(f"[{now}] Logged: {name} took {supplement}")

def view_history():
    name = input("Enter patient name: ")
    rows = history(name, limit=10)
    if not rows:
        print("No records found.")
        return
    print("\nLast 10 logs:")
    for date, time, supplement in rows:
        print(f"{date} {time} → {supplement}")

def main():
    print("1) Log a dose")
    print("2) View history")
    choice = input("Choose (1/2): ").strip()

    if choice == "1":
        log_dose()
    elif choice == "2":
        view_history()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
