import discord
from config import discToken


# intents = discord.Intents.default()
# intents.members = True
# intents.guilds = True
mattsID = 227628808394506243
earthafiresID = 113905827781410819
sanicEmoteID = 936003199234609172
class MyClient(discord.Client):
    
    async def on_ready(self):
        print('Logged on as {0}.'.format(self.user))
        
    async def on_member_join(self, member):
        await client.check_username(member)

    async def on_message(self, message):
        if message.author.id == mattsID:
            sanicEmoji = client.get_emoji(sanicEmoteID)
            if sanicEmoji != None:
                await message.add_reaction(sanicEmoji)
            else:
                print("matt typed but I can't find the right emoji :(")
            
        await client.check_username(message.author)

    async def on_voice_state_update(self, member, before, after):
        await client.check_username(member)

    #add to usernickname if it isnt already there
    async def check_username(self, member):
        if member.id == earthafiresID:
            return

        if member.nick is None:
            nickname = member.name.capitalize()
        else:
            nickname = member.nick.capitalize()

        print(nickname)
            
        #set nickname to hedgehog if no sonic related keywords found
        if "hedgehog" in nickname.lower():
             print('user {0.nick}\'s name already includes " the Hedgehog"'.format(member))
        elif "echidna" in nickname.lower():
            print('user {0.nick}\'s name already includes " the Echidna"'.format(member))
        elif "fox" in nickname.lower():
            print('user {0.nick}\'s name already includes " the Fox"'.format(member))
        elif "arms" in nickname.lower():
            print('user {0.nick}\'s name already includes " the Arms"'.format(member))
        elif "ex-wife" in nickname.lower():
            print('user {0.nick}\'s name already includes " the Ex-Wife"'.format(member))
        elif "edgehog" in nickname.lower():
            print('user {0.nick}\'s name already includes " the Edgehog"'.format(member))
        else:
            if len(nickname) > 19:
                nickname = nickname[0:18]
                
            print(nickname)
            await member.edit(nick=nickname)
            print('Changing user {0.name}\'s nickname to: '.format(member))
            print(nickname)
           
        

client = MyClient()
client.run(discToken)
#https://discord.com/api/oauth2/authorize?client_id=584839020966576196&permissions=1476405312&scope=bot