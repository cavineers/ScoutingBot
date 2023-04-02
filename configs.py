from constants import CONFIG_PATH
import json
import os

AWS_ACCESS_KEY = "AwsAccessKey"
AWS_SECRET_KEY = "AwsSecretKey"
AWS_REGION = "AwsRegion"
AWS_INSTANCE_IDS = "AwsInstanceIds"
DISCORD_TOKEN = "DiscordToken"
DISCORD_COMMAND_PREFIXES = "DiscordCommandPrefixes"
DISCORD_EC2_ROLES = "DiscordEc2Roles"


def read_configs()->"dict[str]":
    "Read values from the designated config file."
    if not os.path.isfile(CONFIG_PATH):
        return {}
    with open(CONFIG_PATH) as f:
        return json.load(f)
    
def write_config(__d:"dict[str]", **config):
    "Write values to the designated config file."
    new = dict(__d, **config)
    to_write = read_configs()
    to_write.update(new)
    with open(CONFIG_PATH, "w") as f:
        json.dump(to_write, f)
    


# TOKEN:str
# COMMAND_PREFIXES:"dict[str, str]"
# EC2_ROLES:"list[str|int]"

# def write_discord_configs(token=..., command_prefixes=..., ec2_roles=...):
#     global TOKEN, COMMAND_PREFIXES, EC2_ROLES
#     #update values
#     if token is not ...:
#         TOKEN = token
#     if command_prefixes is not ...:
#         COMMAND_PREFIXES = command_prefixes
#     if ec2_roles is not ...:
#         EC2_ROLES = ec2_roles

#     #write file
#     if not os.path.exists(DISCORD_CONFIG_PATH):
#         write_missing_config("discord_config.json")
#     with open(os.path.join(CONFIG_DIR, "discord_config.json"), "w") as f:
#         json.dump({
#             "TOKEN":TOKEN,
#             "COMMAND_PREFIXES":COMMAND_PREFIXES,
#             "EC2_ROLES":EC2_ROLES
#         }, f)


# ACCESS_KEY:str
# SECRET_ACCESS_KEY:str
# REGION:str
# INSTANCE_IDS:"dict[str, str]"

    
# def write_aws_configs(access_key=..., secret_access_key=..., region=..., instance_ids=...):
#     global ACCESS_KEY, SECRET_ACCESS_KEY, REGION, INSTANCE_IDS
#     #update values
#     if access_key is not ...:
#         ACCESS_KEY = access_key
#     if secret_access_key is not ...:
#         SECRET_ACCESS_KEY = secret_access_key
#     if region is not ...:
#         REGION = region
#     if instance_ids is not ...:
#         INSTANCE_IDS = instance_ids

#     #write file
#     if not os.path.exists(DISCORD_CONFIG_PATH):
#         write_missing_config("aws_config.json")
#     with open(os.path.join(CONFIG_DIR, "aws_config.json"), "w") as f:
#         json.dump({
#             "ACCESS_KEY":ACCESS_KEY,
#             "SECRET_ACCESS_KEY":SECRET_ACCESS_KEY,
#             "REGION":REGION,
#             "INSTANCE_IDS":INSTANCE_IDS
#         }, f)