from datetime import datetime
from core.database import init, record

init()

def send_reminder(name, supplement):
    now = datetime.now().strftime("%H:%M")
    record(name, supplement, now)
    print(f"[{now}] Logged: {name} took {supplement}")

def main():
    name = input("Enter patient name: ")
    supplement = input("Enter supplement/medication: ")
    send_reminder(name, supplement)

if __name__ == "__main__":
    main()
