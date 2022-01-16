import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Bot is currently ready')

@bot.command(pass_context=True)
async def help(ctx):
  author = ctx.message.author

  embed = discord.Embed(
      colour=discord.color.white()
  )

  embed.set_author(name='Help')
  embed.add_filed(name='.ping', value='Returns with a Pong!', inline=False)
  embed.add_filed(
      name='.Hello', value='Returns with a Hello there!', inline=False)
  embed.add_filed(name='.purge {number}',
                  value='purges messages', inline=False)
  embed.add_filed(name='.Ban @{user} {reason}',
                  value='Helps admins to ban someone bad', inline=False)
  embed.add_filed(name='.kick @{user} {reason}',
                  value='Helps admins to kick someone bad', inline=False)

  await client.send_message(author, embed=embed)
  
bot.run('your token here')
