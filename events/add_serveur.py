# Events de test c'est juste pour que vous avez la structure 
import discord
from discord.ext import commands
from discord.ui import Button, View

class Addserv(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        channel_id = TON_ID_SALON
        channel = self.bot.get_channel(channel_id)

        if channel:
            owner = guild.owner
            total_members = len(guild.members)
            total_bots = len([member for member in guild.members if member.bot])

            embed = discord.Embed(
                title="📡 Status Bot !",
                description=f"Merci au serveur **`{guild.name}`** de m'avoir ajouté !",
                color=discord.Color.from_rgb(250, 192, 103) 
            )

            embed.add_field(name="👤 Créateur :", value=f"> {owner.mention}", inline=False)
            embed.add_field(name="👥 Membres :", value=f"> ***`{total_members}`***", inline=True)
            embed.add_field(name="🤖 Bots :", value=f"> ***`{total_bots}`***", inline=True)

            buttons = View()

            buttons.add_item(Button(style=discord.ButtonStyle.secondary, label="Infos", disabled=True))
            buttons.add_item(Button(style=discord.ButtonStyle.green, label=f"{total_members}", disabled=True))
            buttons.add_item(Button(style=discord.ButtonStyle.blurple, label=f"{total_bots}", disabled=True))

            buttons.add_item(Button(style=discord.ButtonStyle.secondary, label="Liens", disabled=True))
            buttons.add_item(Button(style=discord.ButtonStyle.link, label="Site", url="https://botbump.sdev.online"))
            buttons.add_item(Button(style=discord.ButtonStyle.link, label="Ajoute-moi", url="https://discord.com/oauth2/authorize?client_id=1359242131520360709"))

            await channel.send(embed=embed, view=buttons)

async def setup(bot):
    await bot.add_cog(Addserv(bot))
