import discord
from discord.ext import commands

# === CONFIGURE THESE ===
TOKEN = "MTUwOTI3NzM1MTM0OTk4MTI0NA.GfXehI.G929TIoEwzgCLB7Wv8sAlZ6cKW3CZOZGytVets"

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
        f"Welcome {member.mention} to **GTE**! *Please Read The Server Rules*"
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
        f"{member.mention} has left **GTE**"
    )

    emoji = get_gte_emoji(member.guild)
    if emoji:
        try:
            await msg.add_reaction(emoji)
        except discord.HTTPException as e:
            print(f"Failed to add goodbye reaction: {e}")

bot.run(TOKEN)
