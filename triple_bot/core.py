import os

import interactions

from triple_bot.botutils import load_extensions

DOUBLE_SCORE_GUILD=1050992474283319366

def run_bot():
    client = interactions.Client(token=os.environ['BOT_TOKEN'], default_scope=DOUBLE_SCORE_GUILD)
    load_extensions(client, "triple_bot.cogs")
    client.start()
