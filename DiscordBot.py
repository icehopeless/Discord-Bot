import discord 
import asyncio

intents = discord.Intents.default()
intents.message_content = True  # Para ler o conteúdo das mensagens
intents.reactions = True  # Para adicionar reações às mensagens
client = discord.Client(intents=intents)


#funcao quando tiver online
@client.event
async def on_ready():
    print("_______Hello - Im Online_______")
    print('ID: ' + str(client.user.id))


#React Function
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(f"Received message: {message.content}")

    if message.content.lower().startswith('?check'):
        await message.channel.send('On\n ID: ' + str(client.user.id))

    if message.content.lower().startswith('?test'):
        await message.add_reaction('😴')
        print("Reaction added")

    if message.content.lower().startswith('?request'):
        messagecont = message.content
        command_requested = message.content[9:]
        await message.channel.send(command_requested)



client.run('') #token here