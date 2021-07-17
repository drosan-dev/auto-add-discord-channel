def getVoiceChannelInCategory(channel):
    isInCategory = channel.category is not None
    if isInCategory:
        voiceChannelsInCategory = [channel for channel in channel.category.channels if channel.type.name == "voice"].__len__()
        return voiceChannelsInCategory
    else:
        voiceChannelsInCategory = [channel for channel in channel.category.channels if channel.type.name == "voice"].__len__()