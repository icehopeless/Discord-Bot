import discord 
import asyncio
import google.generativeai as genai
genai.configure(api_key='AIzaSyAmIDXpyneAYEi53bt46yLngzvzg6glcvU')

intents = discord.Intents.default()
intents.message_content = True  # Para ler o conteúdo das mensagens
intents.reactions = True  # Para adicionar reações às mensagens
client = discord.Client(intents=intents)

def format_response(response):
    embed = discord.Embed(
        description=response.text,  # Resposta da API  # Cor do embed
    )
    embed.set_footer(text="Gerado por Google Gemini API")
    return embed

#funcao quando tiver online
@client.event
async def on_ready():
    print("_______Hello - Im Online_______")
    print('ID: ' + str(client.user.id))
    await client.change_presence(activity=discord.Game(name="?help - https://github.com/icehopeless/Discord-Bot"))


#React Function
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(f"Received message: {message.content}")

    if message.content.lower().startswith('?help'):
        await message.channel.send("?ping -> Retorna o Ping do Bot\n?reaction -> Adiciona uma reação a sua mensagem\n?request (pergunta) -> retorna o Response da IA")

    if message.content.lower().startswith('?ping'):
        ping = round(client.latency * 1000) #converte o ping para milissegunds
        await message.channel.send('On ✅\n Ping: ' + str(ping) + ' Milisegundos')

    if message.content.lower().startswith('?reaction'):
        await message.add_reaction('😴')
        print("Reaction added")

    if message.content.lower().startswith('?request'):
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        messagecont = message.content
        command_requested = message.content[9:]
        response = model.generate_content(command_requested)
        
        embed = format_response(response)
        await message.channel.send(embed=embed)
        
        
        


client.run('MTI4MzQ3OTQyNDY4NzI3NjA3Mw.GGTJXZ.8bU8OWpODjyeGSwU9sBGKvWGzft0FaSMaR_a60') #token here