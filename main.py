import discord, os

token = input()
user = discord.Client()


@user.event
async def on_ready():
  print(f'''Logged in as {user.user.name}
        (ID: {user.user.id})''')


@user.event
async def on_message(message):
  if message.author.id == user.user.id:
    if message.content.startswith('!setpres'):
      command = message.content.split(' ')
      pres = ""
      for item in message.content.split(' ')[2:]:
        pres += item + " "
      if command[1] == 'listen':
        await user.change_presence(activity=discord.Activity(
          type=discord.ActivityType.listening, name=pres))
      elif command[1] == "game":
        await user.change_presence(activity=discord.Game(name=pres))
      elif command[1] == "stream":
        await user.change_presence(activity=discord.Streaming(name=pres, url="https://discord.gg/code"))
      elif command[1] == "watch":
        await user.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=pres))
    elif message.content.startswith('!spam'):
      running = True
      while running:
        try:
          await message.channel.send(message.content.split(' ')[1:].join())
        except:
          running = False


user.run(token)
