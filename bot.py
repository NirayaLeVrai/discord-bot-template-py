import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import asyncio
from utils.logger import setup_logger

# Chargement des variables d'environnement
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Logger
logger = setup_logger("Bot")

# Intents
intents = discord.Intents.default()
intents.presences = True
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    logger.info(f"✅ Connecté en tant que {bot.user} (ID: {bot.user.id})")

# Chargement des extensions
async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py") and not filename.startswith("_"):
            extension = f"cogs.{filename[:-3]}"
            try:
                await bot.load_extension(extension)
                logger.info(f"📦 Extension chargée : {extension}")
            except Exception as e:
                logger.error(f"❌ Erreur de chargement {extension} : {e}")

async def load_events():
    for filename in os.listdir("./events"):
        if filename.endswith(".py") and not filename.startswith("_"):
            extension = f"events.{filename[:-3]}"
            try:
                await bot.load_extension(extension)
                logger.info(f"🎯 Event chargé : {extension}")
            except Exception as e:
                logger.error(f"❌ Erreur de chargement {extension} : {e}")

# Lancement complet du bot
async def start_all():
    await load_cogs()
    await load_events()
    await bot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(start_all())
