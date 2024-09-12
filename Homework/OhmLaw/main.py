
def calculate_ohms_law(voltage=None, current=None, resistance=None):

    if voltage is not None and current is not None and resistance is None:
        resistance = voltage / current
        print(f"Resistance: {resistance} Ω")


    elif voltage is not None and resistance is not None and current is None:
        raise NotImplementedError("Current calculation is not yet implemented.")


    elif current is not None and resistance is not None and voltage is None:
        raise NotImplementedError("Voltage calculation is not yet implemented.")


    else:
        print("You must provide two out of three quantities (voltage, current, resistance).")


while True:
    try:
        voltage = float(input("Enter voltage (V): ") or 0)
    except ValueError:
        print("Invalid input. Please enter valid input")
    else:
        break
while True:
    try:
        current = float(input("Enter current (A): ") or 0)
    except ValueError:
        print("Invalid input. Please enter valid input")
    else:
        break
while True:
    try:
        resistance = float(input("Enter resistance (Ω): ") or 0)
    except ValueError:
        print("Invalid input. Please enter valid input")
    else:
        break
calculate_ohms_law(
    voltage if voltage != 0 else None,
    current if current != 0 else None,
    resistance if resistance != 0 else None
)