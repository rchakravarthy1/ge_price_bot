import discord
from discord import Intents, Client, Message
import ge_prices
from config import DISCORD_TOKEN

# Load Token
TOKEN = DISCORD_TOKEN

# Bot setup
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents = intents)

# Message Functionality
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print("(Message was empty because intents were not enabled probably)")
        return

    if user_message[0:3] == ';ge':
        user_message = user_message[4:]
        if is_private := user_message[0:3] == '?ge':
            user_message = user_message[4:]
        try: 
            response: str = ge_prices.get_response(user_message)
            await message.author.send(response) if is_private else await message.channel.send(response)
        except Exception as e:
            print(e)

# Handling Startup for Bot
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

# Handling Incoming Messages
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: {user_message}')
    await send_message(message, user_message)

def main() -> None:
    client.run(token= TOKEN)


if __name__ == '__main__':
    main()