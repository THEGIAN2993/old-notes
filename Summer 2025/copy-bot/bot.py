import discord
from discord import app_commands
from discord.ext import commands

TOKEN = "MTQwNjQ2NzcyNTI3NDEyMDMwMg.GgHaZG.74YeMwqmFyVCg1KF7nbbH1qMZXpwPzQKFfJ3WM"

intents = discord.Intents.default()
intents.members = True  # Needed to fetch member info
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Bot is online as {bot.user}")

@bot.tree.command(
    name="copy",
    description="Send a message through memehook"
)
@app_commands.describe(member="Specified user", message="Message to send via webhook")
async def make_webhook(interaction: discord.Interaction, member: discord.Member, message: str):
    try:
        channel: discord.TextChannel = interaction.channel
        webhooks = await channel.webhooks()
        webhook = discord.utils.get(webhooks, name="memehook")

        if webhook is None:
            webhook = await channel.create_webhook(name="memehook")

        # Use member directly
        username = member.display_name
        avatar_url = member.display_avatar.url if member.display_avatar else member.default_avatar.url

        # Send the message via the webhook as that user
        await webhook.send(
            content=message,
            username=username,
            avatar_url=avatar_url
        )

        # Respond ephemerally to stop "thinking..."
        await interaction.response.send_message("Message sent via webhook.", ephemeral=True)

    except Exception as e:
        print(f"Error sending webhook message: {e}")
        if not interaction.response.is_done():
            await interaction.response.send_message(f"Error: {e}", ephemeral=True)

bot.run(TOKEN)

#test change for github

