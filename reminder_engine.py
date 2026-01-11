from datetime import datetime

def send_reminder(name, supplement):
    now = datetime.now().strftime("%H:%M")
    print(f"[{now}] Reminder: {name}, please take your {supplement}.")

def main():
    name = input("Enter patient name: ")
    supplement = input("Enter supplement/medication: ")
    send_reminder(name, supplement)

if __name__ == "__main__":
    main()