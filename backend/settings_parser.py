# settings_parser.py
import json
import configparser

def load_config(config_file):
    with open(config_file, 'r') as file:
        return json.load(file)

def parse_settings(config):
    config_parser = configparser.ConfigParser()
    config_parser.read(config["PalGameWorldSettingsPath"])
    rcon_port = config_parser.get('OptionSettings', 'RCONPort')
    admin_password = config_parser.get('OptionSettings', 'AdminPassword').strip('"')
    return rcon_port, admin_password

# Example usage
if __name__ == "__main__":
    config = load_config('config.json')
    rcon_port, admin_password = parse_settings(config)
    print(f'RCON Port: {rcon_port}, Admin Password: {admin_password}')
