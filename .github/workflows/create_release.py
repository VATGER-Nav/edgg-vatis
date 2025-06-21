import json
from datetime import datetime
import sys

def main():
    dev_file_path = "vATIS Profile - EDGG D-ATIS.json"
    release_file_path = "vATIS Profile - EDGG D-ATIS Release.json"

    with open(dev_file_path, "r") as f:
        data = json.load(f)

    try:
        with open(release_file_path, "r") as f:
            release_data = json.load(f)
            current_serial = int(release_data.get("updateSerial", 0))
    except FileNotFoundError:
        current_serial = 0

    today = datetime.now().strftime("%Y%m%d")
    
    if current_serial == 0:
        new_serial = int(today) * 100 + 1
    else:
        current_date = int(str(current_serial)[:8])
        current_count = int(str(current_serial)[8:])

        if current_date == int(today):
            if current_count >= 99:
                print("Error: Daily counter has reached its maximum value of 99.")
                sys.exit(1)
            new_serial = current_serial + 1
        else:
            new_serial = int(today) * 100 + 1

    release_data = data.copy()
    release_data["updateUrl"] = "https://raw.githubusercontent.com/VATGER-Nav/edgg-vatis/refs/heads/main/vATIS%20Profile%20-%20EDGG%20D-ATIS%20Release.json"
    release_data["updateSerial"] = new_serial

    with open(release_file_path, "w") as f:
        json.dump(release_data, f, indent=4)

    if "updateUrl" in data:
        del data["updateUrl"]
    if "updateSerial" in data:
        del data["updateSerial"]
    
    with open(dev_file_path, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Created release version with serial {new_serial}")
    print("Development version cleaned (no updateUrl/updateSerial)")

if __name__ == "__main__":
    main()
