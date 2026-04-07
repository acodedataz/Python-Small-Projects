import time
import os
from plyer import notification

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=5
    )

def main():
    clear()
    print("====== 🔔 SMART NOTIFIER APP ======\n")

    title = input("Enter Notification Title: ")
    message = input("Enter Message: ")

    try:
        delay = int(input("After how many seconds? (e.g. 10): "))
        repeat = int(input("How many times to notify? "))
    except ValueError:
        print("❌ Please enter valid numbers!")
        return

    print("\n⏳ Waiting...")
    time.sleep(delay)

    for i in range(repeat):
        show_notification(title, message)
        print(f"✅ Notification {i+1} sent!")
        time.sleep(2)  # gap between notifications

    print("\n🎉 All notifications sent successfully!")

# Run App
while True:
    main()
    again = input("\nDo you want to run again? (y/n): ").lower()
    if again != "y":
        print("👋 Exiting App. Goodbye!")
        break