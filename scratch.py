import subprocess
import os
import time  # Add this import

def admin_panel():
    while True:
        print("=== ADMIN CONTROL PANEL ===")
        print("1. Shutdown computer")
        print("2. List files in directory")
        print("3. Open a file")
        print("4. Run terminal command")
        print("5. Exit")

        choice = input("Select option: ")

        if choice == "1":
            confirm = input("Are you sure you want to shutdown? (y/n): ")
            if confirm.lower() == "y":
                os.system("shutdown /s /t 1")  # Windows shutdown command
        elif choice == "2":
            path = input("Enter directory path: ")
            try:
                result = subprocess.run(f"dir {path}", shell=True, capture_output=True, text=True)
                print("Files:\n", result.stdout)
                if result.stderr:
                    print("Errors:\n", result.stderr)
            except FileNotFoundError:
                print("Directory not found.")
                time.sleep(1)
        elif choice == "3":
            filepath = input("Enter full path to file: ")
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    print(f.read())
            except Exception as e:
                print("Error opening file:", e)
                time.sleep(1)
        elif choice == "4":
           while True:
            command = input("Enter shell command to run: ")
            try:
                result = subprocess.run(command, shell=True, capture_output=True, text=True)
                print("Output:\n", result.stdout)
                if result.stderr:
                    print("Errors:\n", result.stderr)
            except Exception as e:
                print("Error running command:", e)
                time.sleep(1)
        elif choice == "5":
            print("Exiting admin panel...")
            time.sleep(3)
            exit()
        else:
            print("Invalid option")
            time.sleep(1)


def romdon():
    print("you have entered romdon area")
    confirm = input("Are you sure you want to shutdown? (y/n): ")
    if confirm.lower() == "y":
        os.system("shutdown /s /t 1")


x = input("What is your name: ")

while True:
    if x == "romdon":
        print(x, "it's you")
        romdon()
        break
    elif x == "tuwae":
        print("tuwae is a secret area ")
        password = input("Enter password: ")
        if password == "2599":
            print("password is correct")
            admin_panel()
            break
        else:
            print(x, "is not correct")
            exit()
    else:
        print("Who the heck are you?")
        exit()
