import discord
import requests
from time import sleep
from discord.ext import commands
import redis

REDIS_PORT = 6379
REDIS_HOST = '127.0.0.1'

r = redis.Redis(host = REDIS_HOST, port = REDIS_PORT)

#Initialization
client = discord.Client()
bot = commands.Bot(command_prefix = '!')
channel = client.get_channel(748823351321165845)

@bot.command(pass_context = True)
async def get_tasks(ctx):
    try:
        tasks = ''
        for date in r.keys():
            tasks += str(date) + '   :  ' + str(r.get(date)) + '\n'
            await ctx.send(tasks.replace(r"b'", ""))
    except HTTPException as ex:
        await ctx.send('no tasks in the list')


@bot.event
async def on_message(message):
    if message.content.lower().startswith('hello') or message.content.lower().startswith('hi'):
        await message.channel.send('(: hi')
    elif message.content.lower().startswith('how are u'):
        await message.channel.send(r"I'm good, u?")
    elif message.content.lower().startswith('i love u') or message.content.lower().startswith('i love you'):
        await message.channel.send('love you more, {} <3'.format('Nia'))
    elif message.content.lower().startswith('noel, add a task to the schedule:'):
        add_task, task, date = message.content.split('>')
        r.set(task, date)
        await message.channel.send('Okay\nDone, my love <3')
    elif message.content.lower().startswith('thanks') or message.content.lower().startswith('thank you') or message.content.lower().startswith('thank u'):
        await message.channel.send(r"you're welcome (;")
    elif message.content == '.<3':
        await message.channel.send('<3')
    await bot.process_commands(message)
    


data = requests.get('https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UC4xKdmAXFh4ACyhpiQ_3qBw&maxResults=1&order=date&type=video&key=AIzaSyDKO2fxOTZAFyxfcNhsOSbbTmksffd1u84').json()

#def show_new_youtube_vid():
#    vid_id = 'B-emtL137z4'
#    while True:
#        time.sleep(3.0)
#        new_vid_id = data['items'][0]['id']['videoId']
#        if vid_id != new_vid_id:
#            vid_id = new_vid_id





bot.run('NzQ4ODI0NDMyMDc1NzM1MDQw.X0jDGQ.NM6cjRKcIzf7gVfHnXgGQlvZPOE')
#client.run('NzQ4ODI0NDMyMDc1NzM1MDQw.X0jDGQ.NM6cjRKcIzf7gVfHnXgGQlvZPOE')
