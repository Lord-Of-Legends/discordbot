import discord
import random
import time
current_time = time.localtime()
client = discord.Client()
word = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
        '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
current = ""


@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:

        return

    if message.content.startswith("joke"):
        jokes = [" What did one ocean say to the other ocean? Nothing, it just waved.", "Do you want to hear a construction joke nothing i am still working on it", "Why should you never trust stairs? they are always up to something",
                 "What does a house wear? Address!", "I heard the rumor going around about butter? Never mind, I shouldn’t spread it.", "How does NASA organise a party? they planet!", "Why doesn’t Dracula have any friends? Well, honestly, he’s a real pain in the neck."]

        await message.channel.send(random.choice(jokes))
    if message.content.startswith("laugh"):
        await message.channel.send("hahahhahahhahaha are you happy")
    if message.content.startswith("are you happy"):
        await message.channel.send("if you are i live to serve you, though i am new you will have to code me to do more")

        await message.channel.send("basicly")
        await message.channel.send("i want to become like you")
    if message.content.startswith("are you happy"):
        await message.channel.send("yes")
    if message.content.startswith("how are you feeling now"):
        feelings = ['happy', 'sad', 'exited', 'exuhsted', 'fine']
        await message.channel.send(random.choice(feelings))
    if message.content.startswith("How is the server doing"):
        await message.channel.send("no spamming for sure its just the 2 of us unless i go")
        await message.channel.send("i love pizza")
        await message.channel.send("i love pizza")
        await message.channel.send("i love pizza")
        await message.channel.send("i love pizza")
        await message.channel.send("i love pizza")
        await message.channel.send("i love pizza")
        time.sleep(0.7)
        await message.channel.send("CONNECTING")
        time.sleep(1)
        await message.channel.send("HACKING CORE")
        time.sleep(1)
        await message.channel.send("COPYING INFO FROM DATABASTE")
        time.sleep(0.3)
        await message.channel.send("DISCONECTING")
        time.sleep(0.6)
        await message.channel.send("dont worry")
        time.sleep(1)
        await message.channel.send("i am on your side master *evil laugh silently* ")
    if message.content.startswith(f"what is 5 + 2"):
        await message.channel.send("7")
        await message.channel.send("i am smart")
    if message.content.startswith("Check for spamming"):
        await message.channel.send("I can't do that yet i am just to keep you company")
    if message.content.startswith("spam"):
        spammed = 0
        for i in range(int(input(''))):
            spammed += (1)
            await message.channel.send(f"Mr. Bode is handsome {spammed}")

            print(f"Spammed! {spammed}")

    if message.content.startswith("guessing game"):
        time.sleep(5)
        guess = random.choice(word)
        if message.content.startswith((guess)):
            await message.channel.send("Congrats you guesse it right! (:")
        else:
            await message.channel.send("Sorry you are wrong ):")

    if message.content.startswith("what is the time"):
        await message.channel.send(f'the time is : {current_time.tm_hour, "/", current_time.tm_min, "/", current_time.tm_sec}')


client.run("input key here")
