from constants import *
import json
import os
from util import write_missing_config

TOKEN:str
COMMAND_PREFIXES:"dict[str, str]"
EC2_ROLES:"list[str|int]"

#read discord configs
def read_discord_configs():
    global TOKEN, COMMAND_PREFIXES, EC2_ROLES
    if os.path.exists(DISCORD_CONFIG_PATH):
        with open(DISCORD_CONFIG_PATH) as f:
            config_data:"dict[str]" = json.load(f)
            TOKEN = config_data["TOKEN"]
            COMMAND_PREFIXES = config_data.get("COMMAND_PREFIXES", {}) #{str(guild_or_channel_id):command_prefix}
            EC2_ROLES = config_data.get("EC2_ROLES", [])
            return config_data
    else:
        write_missing_config("discord_config.json")
        raise RuntimeError("Discord config has not been set. Set under config/discord_config.json")

def write_discord_configs(token=..., command_prefixes=..., ec2_roles=...):
    global TOKEN, COMMAND_PREFIXES, EC2_ROLES
    #update values
    if token is not ...:
        TOKEN = token
    if command_prefixes is not ...:
        COMMAND_PREFIXES = command_prefixes
    if ec2_roles is not ...:
        EC2_ROLES = ec2_roles

    #write file
    if not os.path.exists(DISCORD_CONFIG_PATH):
        write_missing_config("discord_config.json")
    with open(os.path.join(CONFIG_DIR, "discord_config.json"), "w") as f:
        json.dump({
            "TOKEN":TOKEN,
            "COMMAND_PREFIXES":COMMAND_PREFIXES,
            "EC2_ROLES":EC2_ROLES
        }, f)


ACCESS_KEY:str
SECRET_ACCESS_KEY:str
REGION:str
INSTANCE_IDS:"dict[str, str]"

#read aws configs
def read_aws_configs():
    global ACCESS_KEY, SECRET_ACCESS_KEY, REGION, INSTANCE_IDS
    if os.path.isfile(AWS_CONFIG_PATH):
        with open(AWS_CONFIG_PATH) as f:
            config_data:"dict[str]" = json.load(f)
            ACCESS_KEY = config_data["ACCESS_KEY"]
            SECRET_ACCESS_KEY = config_data["SECRET_ACCESS_KEY"]
            REGION = config_data.get("REGION", AWS_DEFAULT_REGION)
            if "REGION" not in config_data:
                print(f"[WARNING] No AWS region specified in config, using default region '{AWS_DEFAULT_REGION}'.")
            INSTANCE_IDS = config_data.get("INSTANCE_IDS", {})
            return config_data
    else:
        write_missing_config("aws_config.json")
        raise RuntimeError("AWS config has not been set. Set under config/aws_config.json")
    
def write_aws_configs(access_key=..., secret_access_key=..., region=..., instance_ids=...):
    global ACCESS_KEY, SECRET_ACCESS_KEY, REGION, INSTANCE_IDS
    #update values
    if access_key is not ...:
        ACCESS_KEY = access_key
    if secret_access_key is not ...:
        SECRET_ACCESS_KEY = secret_access_key
    if region is not ...:
        REGION = region
    if instance_ids is not ...:
        INSTANCE_IDS = instance_ids

    #write file
    if not os.path.exists(DISCORD_CONFIG_PATH):
        write_missing_config("aws_config.json")
    with open(os.path.join(CONFIG_DIR, "aws_config.json"), "w") as f:
        json.dump({
            "ACCESS_KEY":ACCESS_KEY,
            "SECRET_ACCESS_KEY":SECRET_ACCESS_KEY,
            "REGION":REGION,
            "INSTANCE_IDS":INSTANCE_IDS
        }, f)


read_aws_configs()
read_discord_configs()