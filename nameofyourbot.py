import discord
import openai

# Create a dictionary to store user-specific information
user_memory = {}

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

    if message.content.startswith('!'):
        user_input = message.content[len('! '):]  # Extract user input

        # Check if the user has interacted with the bot before
        if message.author.id not in user_memory:
            user_memory[message.author.id] = []

        # Store the user's message in memory
        user_memory[message.author.id].append(user_input)

        # Join the user's previous messages to provide context
        conversation_history = "\n".join(user_memory[message.author.id])

        # Indicate that the bot is typing
        async with message.channel.typing():
            response = await generate_response(conversation_history)  # Await the response
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
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Run the bot with the token
client.run('YOUR_BOT_TOKEN')
