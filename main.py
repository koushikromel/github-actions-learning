import json
from datetime import datetime
import socket


def add_entry():
  # Load existing data from the JSON file if it exists
  try:
    with open('database.json', 'r') as file:
      data = json.load(file)
  except FileNotFoundError:
    # If the file doesn't exist, initialize an empty list
    data = []

  # Get the current IP address and hostname
  current_ip = socket.gethostbyname(socket.gethostname())
  hostname = socket.gethostname()
  # Add a new entry with the current datetime
  new_entry = {
      'status': 'Alive',
      'current_ip': current_ip,
      'hostname': hostname,
      'timestamp': datetime.utcnow().strftime('%d-%m-%Y %I:%M:%S %p')
  }
  data.append(new_entry)

  # Save the updated data back to the JSON file
  with open('database.json', 'w') as file:
    json.dump(data, file, indent=2)


if __name__ == "__main__":
  add_entry()
