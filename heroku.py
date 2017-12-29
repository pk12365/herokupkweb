import os

from discord.ext import commands as cmds

# Tuple of the path to the cog file, and the extra args it takes
cogs = [
    ("cogs.commands", {}),
    ("cogs.custom_commands", {"db_url": os.environ["DATABASE_URL"]}),
    ("cogs.greetings", {"db_url": os.environ["DATABASE_URL"]}),
    ("cogs.music", {}),
    ("cogs.notifications", {"db_url": os.environ["DATABASE_URL"]}),
    ("cogs.roles", {"db_url": os.environ["DATABASE_URL"]}),
    ("cogs.reminders", {"db_url": os.environ["DATABASE_URL"]}),
    ("cogs.spoiler", {}),
]

heroku.load_cogs(cogs)

heroku.run(os.environ["TOKEN"])
