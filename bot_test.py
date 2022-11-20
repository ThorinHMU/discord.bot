from discord.ext import commands

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("pret")


@bot.command()
async def ip(ctx, *text):
    await ctx.send("l'ip du serveur est: **ThorinHMUh338.aternos.me**")


@bot.command()
async def clear(ctx, nbr: int):
    nbr += 1
    message = await ctx.channel.history(limit=nbr).flatten()
    for messages in message:
        await messages.delete()
        print(message)


bot.run("OTQ1MDI5NzkwNTI2NzYzMDA5.GYI52k.ae66lXgQxV70bAkEfPdZchW-AHTupiVMdXTIgg")
