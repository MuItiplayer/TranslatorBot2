import discord
from discord.ext import commands
from azure.ai.translation.text import TranslatorClient
from azure.core.credentials import AzureKeyCredential


# Bot-Prefix (für Befehle wie /english)
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='/', intents=intents)

# Microsoft Translator API Details
TRANSLATOR_KEY = '2kyCUAbTh3dPDHXHMOPj6WNGCnDhte19xKilbZZwO0M6AckC5J9yJQQJ99ALAC5RqLJXJ3w3AAAbACOGKMaG'
TRANSLATOR_ENDPOINT = 'https://xevex.cognitiveservices.azure.com/'

translator_client = TranslatorClient(
    endpoint=TRANSLATOR_ENDPOINT,
    credential=AzureKeyCredential(TRANSLATOR_KEY)
)

@bot.command()
async def english(ctx, *, text: str):
    """Übersetzt Text ins Englische."""
    translation = translator_client.translate_text(text, target_language="en")
    await ctx.send(f"Englisch: {translation.translations[0].text}")

@bot.command()
async def deutsch(ctx, *, text: str):
    """Übersetzt Text ins Deutsche."""
    translation = translator_client.translate_text(text, target_language="de")
    await ctx.send(f"Deutsch: {translation.translations[0].text}")

# Bot starten
TOKEN = "MTMxOTIzOTE2MzU1OTY3Nzk2Mg.GDIE_j.jOsEEJq17ARWns9FrjmOSajSyB_T5Ghy0Bcqhc"
bot.run(TOKEN)
