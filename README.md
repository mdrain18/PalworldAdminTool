# Palworld Admin Tool

## Overview

The Palworld Admin Tool is a backend application designed to facilitate server administration for the game Palworld. It provides an interface for executing various administrative commands like sending server messages, performing server shutdowns with warnings, and more. The tool uses Python and Flask for backend operations and communicates with the game server using RCON (Remote Console).

## Features

- Send customizable messages to the game server.
- Schedule server shutdowns with warnings at 5 minutes, 2 minutes, and 30 seconds.
- Automatically handle the shutdown sequence, including sending warning messages and executing the shutdown.

## Setup and Installation

1. **Clone the Repository:**
	git clone https://github.com/mdrain18/PalworldAdminTool.git

2. **Install Dependencies:**
Navigate to the project directory and set up a virtual environment:
	python -m venv venv
	venv\Scripts\activate # On Windows
	source venv/bin/activate # On Unix or MacOS
	pip install -r requirements.txt

3. **Configuration:**
- Before running the application, you need to configure your server settings.
- Open the `config.json` file located in the root directory.
- Modify the `PalGameWorldSettingsPath` value to point to your `PalGameWorldSettings.ini` file.
  ```json
  {
      "PalGameWorldSettingsPath": "path/to/your/PalGameWorldSettings.ini"
  }
  ```
- Ensure that `PalGameWorldSettings.ini` contains the correct RCON port and admin password for your Palworld server.

4. **Running the Application:**
Execute the `run_backend.bat` script to start the backend server:
	run_backend.bat

## Contributing

We welcome contributions to the Palworld Admin Tool. If you're interested in contributing, please feel free to fork the repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

For any queries or contributions, please contact [Me on Github](https://github.com/mdrain18).

## Usage

Once the server is running, you can interact with the Palworld server via the provided API endpoints. For example, to send a custom message or initiate the shutdown sequence, use the respective API routes.

## License

This project is licensed under the GPL-3.0 - see the `LICENSE` file for details.
