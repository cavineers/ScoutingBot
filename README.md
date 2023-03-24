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

2. ### Create `config` folder in repository root add `aws_config.json` and `discord_config.json` files.
    Diagram:
    ```
        ScoutingBot
        | ...
        |- config
        |  |- aws_config.json
        |  |- discord_config.json
        | ...
    ```
3. ### Fill `aws_config.json` file
    A somewhat outdated, yet still helpful tutorial on setting up AWS AMIs for programmatic use: https://www.youtube.com/watch?v=tW3HoYRnABs

    Diagram:
    ```
        {
            "ACCESS_KEY": "...",
            "SECRET_ACCESS_KEY": "...",
            "REGION": "...",
            "INSTANCE_IDS": {
                "instance_name":"instance_id"
            }
        }
    ```

    - ACCESS_KEY
       - The access key for your AMI provided to you by AWS after setting up the AMI.
       - type: `str`
    - SECRET_ACCESS_KEY
        - The access key for your AMI provided to you by AWS after setting up the AMI.
        - type: `str`
    - REGION
        - The region that your instances are in.
        - type: `str`
    - INSTANCE_IDS
        - A mapping of instance name to instance id for the bot to use when executing commands that require an instance id, allowing for instance names to be entered then converted to instance ids.
        - type: `dict[str, str]`

4. ### Fill `discord_config.json` file
    Diagram:
    ```
        {
            "TOKEN": "...",
            "COMMAND_PREFIXES":{
                "guild_or_channel_id":"prefix"
            },
            "EC2_ROLES": [
                ...
            ]

        }
    ```

    - TOKEN
       - The token for your discord bot.
       - type: `str`
    - COMMAND_PREFIXES
       - The local prefixes set in each guild/private channel, mapping the guild/channel id (as a string) to its prefix. This will be filled by the bot, but can also be set ahead of time.
       - type: `dict[str, str]`
    - EC2_ROLES
       - The role ids or names that are allowed to execute EC2 commands.
       - type: `list[int|str]`

## Run

Run with:
- Windows:  &emsp;`py main.py`
- Linux:    &emsp;`python3 main.py`