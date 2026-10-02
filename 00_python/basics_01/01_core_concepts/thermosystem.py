device_status="active"
temperature=35

if device_status=="active":
    if temperature > 35:
        print(f"Warn: high temperature")
    else:
        print("Temperature Normal")
else:
    print("Device is offline")
