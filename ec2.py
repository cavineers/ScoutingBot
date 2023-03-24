from boto3.session import Session
from configs import *
from constants import *

# def write_configs(access_key, secret_access_key, region):
#     homedir = os.path.expanduser("~")
#     awsdir = os.path.join(homedir, ".aws")
#     if not os.path.isdir(awsdir):
#         os.mkdir(awsdir)
#     with open(os.path.join(awsdir, "credentials"), "w") as f:
#         f.write(f"[profile {PROFILE_NAME}]\naws_access_key_id = {access_key}\naws_secret_access_key = {secret_access_key}\n")
#     with open(os.path.join(awsdir, "config"), "w") as f:
#         f.write(f"[profile {PROFILE_NAME}]\nregion = {region}\noutput = json")

read_aws_configs()
session = Session(aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_ACCESS_KEY, region_name=REGION)
client = session.client("ec2")