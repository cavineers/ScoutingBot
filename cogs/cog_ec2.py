from configs import *
from constants import *
import discord
from discord.ext import commands
import ec2
from util import DiscordEmbed, handle_command_error

def map_iids(instance_identifiers:"tuple[str,...]"):
    mapped = {} if instance_identifiers else {DEFAULT_INSTANCE_ID:DEFAULT_INSTANCE_NAME}
    ids = [] if instance_identifiers else [DEFAULT_INSTANCE_ID]
    for identifier in instance_identifiers:
        if identifier in ec2.INSTANCE_IDS:
            iid = ec2.INSTANCE_IDS[identifier]
            mapped[iid] = identifier
            ids.append(iid)
        else:
            ids.append(identifier)
    return ids, mapped

ec2_permissions = commands.check_any(commands.has_any_role(*EC2_ROLES), commands.is_owner())


class EC2(commands.Cog):
    "All commands having to do with AWS EC2 instances."
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command(name="ec2.start")
    @ec2_permissions
    #https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/start_instances.html
    async def start(self, ctx:commands.Context, *instance_identifiers):
        "Start the instance(s) with the given instance identifier(s). If no instance identifier is specified, the default will be used."
        ids, mapped = map_iids(instance_identifiers)

        fields:"list[dict[str, str|bool]]" = []
        for iid in ids:
            #or inline could need to be True, False, but i think its right
            fields.extend(({"name":"Identifier", "value":iid, "inline":False}, {"name":"Mapped From", "value":str(mapped.get(iid)), "inline":False}))

        embed = DiscordEmbed("Starting Instances", f"Starting {len(ids)} instances.", discord.Color.blue(), *fields)
        await ctx.send(embed=embed)
        response:"dict[str, list[dict[str, dict[str, str|int]]]]" = ec2.client.start_instances(
            InstanceIds=ids,
            DryRun=False
        )
        print(response)
        started:"dict[str, tuple[str, str]]" = {}
        starting_instances = response["StartingInstances"]
        for instance in starting_instances:
            #im assuming non-existent instances will just no appear (but, it could just raise an error)
            started[instance["InstanceId"]] = instance["CurrentState"]["Name"], instance["PreviousState"]["Name"]

        after_fields:"list[dict[str, str|bool]]" = []
        for iid in ids:
            current_state, previous_state = started.get(iid, ("None", "None"))
            after_fields.extend((
                {"name":"Identifier", "value":iid, "inline":False},
                {"name":"Mapped From", "value":str(mapped.get(iid)), "inline":True},
                {"name":"Current State", "value":current_state, "inline":True},
                {"name":"Previous State", "value":previous_state, "inline":True}
            ))

        await ctx.reply(
            embed=DiscordEmbed("Started Instances", f"Started {len(started)} instances.", discord.Color.green() if started else discord.Color.red(), *after_fields),
            mention_author=False
        )

    @start.error
    async def start_error(self, ctx:commands.Context, e:Exception):
        await handle_command_error(ctx, e)

    @commands.command(name="ec2.stop")
    @ec2_permissions
    #https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/stop_instances.html
    async def stop(self, ctx:commands.Context, *instance_identifiers):
        "Stop the instance(s) with the given instance identifier(s). If no instance identifier is specified, the default will be used."
        ids, mapped = map_iids(instance_identifiers)

        fields:"list[dict[str, str|bool]]" = []
        for iid in ids:
            #or inline could need to be True, False, but i think its right
            fields.extend(({"name":"Identifier", "value":iid, "inline":False}, {"name":"Mapped From", "value":str(mapped.get(iid)), "inline":False}))

        embed = DiscordEmbed("Stopping Instances", f"Stopping {len(ids)} instances.", discord.Color.blue(), *fields)
        await ctx.send(embed=embed)
        response:"dict[str, list[dict[str, dict[str, str|int]]]]" = ec2.client.stop_instances(
            InstanceIds=ids,
            DryRun=False
        )
        print(response)
        stopped:"dict[str, tuple[str, str]]" = {}
        stopping_instances = response["StoppingInstances"]
        for instance in stopping_instances:
            #im assuming non-existent instances will just no appear (but, it could just raise an error)
            stopped[instance["InstanceId"]] = instance["CurrentState"]["Name"], instance["PreviousState"]["Name"]

        after_fields:"list[dict[str, str|bool]]" = []
        for iid in ids:
            current_state, previous_state = stopped.get(iid, ("None", "None"))
            after_fields.extend((
                {"name":"Identifier", "value":iid, "inline":False},
                {"name":"Mapped From", "value":str(mapped.get(iid)), "inline":True},
                {"name":"Current State", "value":current_state, "inline":True},
                {"name":"Previous State", "value":previous_state, "inline":True}
            ))

        await ctx.reply(
            embed=DiscordEmbed("Stopped Instances", f"Stopped {len(stopped)} instances.", discord.Color.green() if stopped else discord.Color.red(), *after_fields),
            mention_author=False
        )

    @stop.error
    async def stop_error(self, ctx:commands.Context, e:Exception):
        await handle_command_error(ctx, e)

    @commands.command(name="ec2.status")
    @ec2_permissions
    async def status(self, ctx:commands.Context, instance_identifier:str=DEFAULT_INSTANCE_NAME):
        "View status of instance with the given instance identifier. If no instance identifier is specified, the default will be used."
        mapped = INSTANCE_IDS.get(instance_identifier)
        iid = mapped or instance_identifier

        response:"list[dict[str, str|list[dict[str]]|dict[str]]]" = ec2.client.describe_instance_status(
            InstanceIds=[iid],
            DryRun=False,
            IncludeAllInstances=True
        )
        print(response)

        statuses = response.get("InstanceStatuses",[])

        irepr = iid
        if mapped:
            irepr += f" ({instance_identifier})"

        if not statuses or statuses[0]["InstanceId"] != iid:
            await ctx.reply(
                embed=DiscordEmbed("Failed to get Instance Status", f"Status for Instance {irepr} could not be retrieved.", discord.Color.red()),
                mention_author=False
            )
            return
        
        status = statuses[0]

        fields = (
            {"name":"Identifier", "value":iid, "inline":False},
            {"name":"Mapped From", "value":instance_identifier if mapped else "None", "inline":False},
            {"name":"Availability Zone", "value":status["AvailabilityZone"], "inline":False},
            {"name":"State", "value":status["InstanceState"]["Name"], "inline":False},
            {"name":"Status", "value":status["InstanceStatus"]["Status"], "inline":False},
            {"name":"System Status", "value":status["SystemStatus"]["Status"], "inline":False},
        )


        await ctx.reply(
            embed=DiscordEmbed("Instance Status", f"For Instance {irepr}", discord.Color.green(), *fields),
            mention_author=False
        )

    @status.error
    async def status_error(self, ctx:commands.Context, e:Exception):
        await handle_command_error(ctx, e)


