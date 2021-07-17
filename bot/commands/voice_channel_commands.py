from discord import channel, guild
from .voiceChannelCommandsServices import getVoiceChannelInCategory
import discord

class VoiceChannelCommands():
    async def on_voice_state_update(self, member, before, after):
        channel = before.channel or after.channel
        if after.channel == None:
            membersInChannel = channel.members.__len__()
            voiceChannelsInCategory = getVoiceChannelInCategory(channel)
            voiceChannelsInCategory = [channel for channel in channel.category.channels if channel.type.name == "voice"].__len__()
            if membersInChannel == 0 and voiceChannelsInCategory > 1:
                await channel.delete()
        else:
            pass
        #guild = self.guilds[0]
        #guild.create_voice_channel('tttt')

    async def on_message(self, message):
        pass