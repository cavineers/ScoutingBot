from boto3.session import Session
import configs
from constants import *


def setup():
    global session, client
    c = configs.read_configs()
    session = Session(aws_access_key_id=c[configs.AWS_ACCESS_KEY], aws_secret_access_key=c[configs.AWS_SECRET_KEY], region_name=c[configs.AWS_REGION])
    client = session.client("ec2")
    
session = None #Session(aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_ACCESS_KEY, region_name=REGION)
client = None #session.client("ec2")
