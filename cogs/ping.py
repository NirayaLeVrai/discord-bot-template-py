from discord.ext import commands
from discord import app_commands, Interaction, Embed
import discord

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Affiche la latence du bot.")
    async def ping(self, interaction: Interaction):
        latency = round(self.bot.latency * 1000)
        embed = Embed(
            title="🏓 Pong !",
            description=f"Latence : `{latency} ms`",
            color=discord.Color.orange()
        )
        await interaction.response.send_message(embed=embed)

    @commands.Cog.listener()
    async def on_ready(self):
        try:
            synced = await self.bot.tree.sync()
            print(f"✅ Slash command synchronisée : {[cmd.name for cmd in synced]}")
        except Exception as e:
            print(f"❌ Erreur de sync : {e}")

async def setup(bot):
    await bot.add_cog(Ping(bot))
