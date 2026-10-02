seat_type = input("Enter the Preference (sleeper/AC/General/Luxury)").lower()

match seat_type:
    case "sleeper":
        print("Sleeper confirm")
    case "AC":
        print("AC confirm")
    case "General":
        print("General Confirm")
    case "Luxury":
        print("Luxury Confirm")
    case _:
        print("Invalid")