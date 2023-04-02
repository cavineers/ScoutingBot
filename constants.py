import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "configs.json")
AWS_CONFIG_PATH = os.path.join(CONFIG_PATH, "aws_config.json")
DISCORD_CONFIG_PATH = os.path.join(CONFIG_PATH, "discord_config.json")
PROFILE_NAME = "scoutingawsbot"

AWS_DEFAULT_REGION = "eu-north-1"

DEFAULT_COMMAND_PREFIX = "s."
DEFAULT_INSTANCE_ID = "i-033f8a189e510d2a7"
DEFAULT_INSTANCE_NAME = "scouting23"
