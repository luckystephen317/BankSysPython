# Bank System

def c_account():
    accno = input("Enter account number: ")
    name = input("Enter account name: ")
    balance = input("Enter initial balance: ")

    with open("accounts.txt", "a") as datafile:
        datafile.write(f"{accno},{name},{balance}\n")

    print("Account created successfully!")

def deposit():
    accno = input("Enter account number: ")
    amt = input("Enter amount to deposit: ")

    with open("accounts.txt", "r+") as datafile:
        data = datafile.readlines()
        datafile.seek(0)
        for line in data:
            info = line.strip().split(",")
            if info[0] == accno:
                info[2] = str(int(info[2]) + int(amt))
                datafile.write(",".join(info) + "\n")
            else:
                datafile.write(line)
        datafile.truncate()

    print("Deposit successful!")

def withdraw():
    accno = input("Enter account number: ")
    amt = input("Enter amount to withdraw: ")

    with open("accounts.txt", "r+") as datafile:
        data = datafile.readlines()
        datafile.seek(0)
        for line in data:
            info = line.strip().split(",")
            if info[0] == accno:
                if int(info[2]) >= int(amt):
                    info[2] = str(int(info[2]) - int(amt))
                    datafile.write(",".join(info) + "\n")
                else:
                    print("Insufficient balance!")
                    datafile.write(line)
            else:
                datafile.write(line)
        datafile.truncate()

    print("Withdrawal successful!")

def display_balance():
    accno = input("Enter account number: ")

    with open("accounts.txt", "r") as datafile:
        for line in datafile:
            info = line.strip().split(",")
            if info[0] == accno:
                print(f"Balance: {info[2]}")

while True:
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display Balance")
    print("5. Exit")

    xc = input("Enter your option: ")

    if xc == "1":
        c_account()
    elif xc == "2":
        deposit()
    elif xc == "3":
        withdraw()
    elif xc == "4":
        display_balance()
    elif xc == "5":
        break
    else:
        print("Invalid option!")
