# app.py
from flask import Flask, jsonify, request
from rcon_client import RCONClient
from settings_parser import parse_settings

app = Flask(__name__)

# Load RCON settings from the config file
rcon_port, admin_password = parse_settings('path/to/PalGameWorldSetting.ini')
rcon_client = RCONClient(('localhost', int(rcon_port)), admin_password)

@app.route('/send_command', methods=['POST'])
def send_command():
    command = request.json.get('command')
    response = rcon_client.send_command(command)
    return jsonify({'response': response})

@app.route('/app/admin/send_message', methods=['POST'])
def send_message():
    message = request.json.get('message')
    if not message:
        return jsonify({'error': 'No message provided'}), 400

    response = rcon_client.send_custom_message(message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
