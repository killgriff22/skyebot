import discord, os

token = input()
user = discord.Client()
FirstLogin = True
presence = None
active = False
print()
@user.event
async def on_ready():
  if FirstLogin:
    FirstLogin = False
    print(f'''Logged in as {user.user.name}
        (ID: {user.user.id})''')
  elif not FirstLogin:
      print(f'Welcome Back {user.user.name}!')
      await user.change_presence(activity=presence)

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
      elif command[1] == "random":
        import threading
        async def random_activity():
          import random
          global active
          active = True
          while active:
            choice = random.choice(["listen","watch","stream","game"])
            pres=""
            for _ in range(16):
              pres += random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"]) 
            if choice == 'listen':
              await user.change_presence(activity=discord.Activity(
                type=discord.ActivityType.listening, name=pres))
            elif choice == "game":
              await user.change_presence(activity=discord.Game(name=pres))
            elif choice == "stream":
              await user.change_presence(activity=discord.Streaming(name=pres, url="https://discord.gg/code"))
            elif choice == "watch":
              await user.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=pres))
        thread=threading.Thread(target=random_activity)
        thread.start()
      elif command == "randomstop":
        global active
        active = False
    elif message.content.startswith('!spam'):
      running = True
      while running:
        try:
          await message.channel.send(message.content.split(' ')[1:].join())
        except:
          running = False


user.run(token)
