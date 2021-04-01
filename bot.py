import os # importing env vars
from twitchio.ext import commands

bot = commands.Bot(
	irc_token=os.environ['TMI_TOKEN'],
	client_id=os.environ['CLIENT_ID'],
	nick=os.environ['BOT_NICK'],
	prefix=os.environ['BOT_PREFIX'],
	initial_channels=[os.environ['CHANNEL']]
)

@bot.event
async def event_ready():
    print(f"{os.environ['BOT_NICK']} is online!")
    ws = bot._ws # needed to send messages within event_ready
    await ws.send_privmsg(os.environ['CHANNEL'], f"/me, nice to be here!")
    
@bot.event
async def event_message(ctx):
    if ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
        return
    await ctx.channel.send(ctx.content)

if __name__ == "__main__":
    bot.run()
