from . import cog_ec2
from discord.ext.commands import Cog

all_cogs:"tuple[Cog|type[Cog], ...]" = (cog_ec2.EC2,)
