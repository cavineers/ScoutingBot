# ScoutingBot
Discord bot for [Scouting App](https://github.com/cavineers/ScoutingApp2023) utility.

## Prerequisites
### Pypi packages
- [`boto3`](https://pypi.org/project/boto3/)
- [`discord.py`](https://pypi.org/project/discord.py/)

Install with
- Windows:  &emsp;`py -m pip install boto3 discord.py`
- Linux:    &emsp;`python3 -m pip install boto3 discord.py`

## Setup
1. ### Pull repository 
    `git pull https://github.com/cavineers/ScoutingBot`

2. ### Create `configs.json` file in repository root.
    Diagram:
    ```
        {
            "AwsAccessKey": "...",
            "AwsSecretKey": "...",
            "AwsRegion": "...",
            "AwsInstanceIds": {
                "instance_name":"instance_id"
            },
            "DiscordToken": "...",
            "DiscordCommandPrefixes":{
                "guild_or_channel_id":"prefix"
            },
            "DiscordEc2Roles": [
                ...
            ]
        }
    ```

    - AwsAccessKey
       - The access key for your AMI provided to you by AWS after setting up the AMI.
       - type: `str`
    - AwsSecretKey
        - The access key for your AMI provided to you by AWS after setting up the AMI.
        - type: `str`
    - AwsRegion
        - The region that your instances are in.
        - type: `str`
    - AwsInstanceIds
        - A mapping of instance name to instance id for the bot to use when executing commands that require an instance id, allowing for instance names to be entered then converted to instance ids.
        - type: `dict[str, str]`
    - DiscordToken
       - The token for your discord bot.
       - type: `str`
    - DiscordCommandPrefixes
       - The local prefixes set in each guild/private channel, mapping the guild/channel id (as a string) to its prefix. This will be filled by the bot, but can also be set ahead of time.
       - type: `dict[str, str]`
    - DiscordEc2Roles
       - The role ids or names that are allowed to execute EC2 commands.
       - type: `list[int|str]`

## Run

Run with:
- Windows:  &emsp;`py main.py`
- Linux:    &emsp;`python3 main.py`