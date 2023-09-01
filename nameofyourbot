import discord
import openai




intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return


# add the word to the exclamation point you want to use to make it talk
    if message.content.startswith('!'):
        user_input = message.content[len('! '):]  # Extract user input
       
        
        # Indicate that the bot is typing
        async with message.channel.typing():
            response = await generate_response(user_input)  # Await the response
            await message.channel.send(response)

async def generate_response(input_text):
    try:
        # Use the OpenAI API to generate a response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the chat model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": input_text}
            ]
        )
        return response.choices[0].message["content"]

    except Exception as e:
        print(f"Error generating response: {e}")
        return "An error occurred while generating the response."


# Set your OpenAI API key
openai.api_key = ''

# Run the bot with the token
client.run('');



