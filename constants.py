import os

CONFIG_DIR = os.path.join(os.path.dirname(__file__), "config")
AWS_CONFIG_PATH = os.path.join(CONFIG_DIR, "aws_config.json")
DISCORD_CONFIG_PATH = os.path.join(CONFIG_DIR, "discord_config.json")
PROFILE_NAME = "scoutingawsbot"

AWS_DEFAULT_REGION = "eu-north-1"

DEFAULT_COMMAND_PREFIX = "s."
DEFAULT_INSTANCE_ID = "i-033f8a189e510d2a7"
DEFAULT_INSTANCE_NAME = "scouting23"
