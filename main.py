import discord
from discord.ext import commands
import os
import dotenv
from dotenv import load_dotenv

load_dotenv()

# === CONFIGURE THESE ===

WELCOME_CHANNEL_ID = 1497062210818801744  # welcome channel ID
GOODBYE_CHANNEL_ID = 1497062210818801744  # goodbye channel ID

GTE_EMOJI_ID = 1509279030715879576        # your logo emoji ID
# =======================

intents = discord.Intents.default()
intents.members = True  # needed for join/leave events

bot = commands.Bot(command_prefix="!", intents=intents)

def get_gte_emoji(guild: discord.Guild):
    return discord.utils.get(guild.emojis, id=GTE_EMOJI_ID)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

@bot.event
async def on_member_join(member: discord.Member):
    channel = member.guild.get_channel(WELCOME_CHANNEL_ID)
    if channel is None:
        return

    msg = await channel.send(
        f"Welcome {member.mention} to **CML**! *Please Read The Server Rules*"
    )

    emoji = get_gte_emoji(member.guild)
    if emoji:
        try:
            await msg.add_reaction(emoji)
        except discord.HTTPException as e:
            print(f"Failed to add welcome reaction: {e}")

@bot.event
async def on_member_remove(member: discord.Member):
    channel = member.guild.get_channel(GOODBYE_CHANNEL_ID)
    if channel is None:
        return

    msg = await channel.send(
        f"{member.mention} has left **CML**"
    )

    emoji = get_gte_emoji(member.guild)
    if emoji:
        try:
            await msg.add_reaction(emoji)
        except discord.HTTPException as e:
            print(f"Failed to add goodbye reaction: {e}")

bot.run(os.getenv("TOKEN"))
