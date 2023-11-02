import discord
from discord import app_commands

import config


# TODO: Create embeds for commands
# TODO: Only allow certain people to use these commands
# TODO: Only allow commands to work in 750R server
# TODO: Create modlog embeds for commands


class PingGroup(app_commands.Group):

    @app_commands.command(name="ping", description="displays the bot's latency")
    async def ping(self, interaction):
        embed = discord.Embed(title=f'{discord.utils.escape_markdown(interaction.user.display_name)} Used /ping',
                              color=discord.Color.gold())
        embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar.url)
        embed.add_field(name="Latency", value=f"{round(interaction.client.latency * 1000, 2)} ms", inline=False)

        await interaction.client.get_guild(config.SERVER_750R).get_channel(config.CHANNEL_MODLOGS_750R).send(
            embed=embed)
        await interaction.response.send_message(
            f"{interaction.user.mention} Latency is {round(interaction.client.latency * 1000, 2)} ms", ephemeral=True)


async def setup(client):
    client.tree.add_command(PingGroup(name="ping", description="bot ping commands"))
