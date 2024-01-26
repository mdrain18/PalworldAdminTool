# rcon_client.py
import time
from valve.rcon import RCON

class RCONClient:
    def __init__(self, address, password):
        self.address = address
        self.password = password

    def send_command(self, command):
        with RCON(self.address, self.password) as rcon:
            response = rcon.execute(command)
            return response

    def send_custom_message(self, message):
        return self.send_command(f"say {message}")
        
    def shutdown_message(self, message):
        return self.send_command(f"say {message}")

    def shutdown_procedure(self):
        # Send 5 minutes warning
        self.shutdown_message("Server will shutdown in 5 minutes.")
        time.sleep(300 - 120)  # Wait for 3 minutes

        # Send 2 minutes warning
        self.shutdown_message("Server will shutdown in 2 minutes.")
        time.sleep(120 - 30)   # Wait for 1 minute and 30 seconds

        # Send 30 seconds warning
        self.shutdown_message("Server will shutdown in 30 seconds.")
        time.sleep(30)         # Wait for 30 seconds

        # Execute shutdown
        self.send_command("stop")  # Replace 'stop' with the actual shutdown command
