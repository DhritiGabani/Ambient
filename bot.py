import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import DiscordUtils
import urllib.request
import re

load_dotenv()
client = commands.AutoShardedBot(command_prefix="!")
music = DiscordUtils.Music()


def get_video_list(keywords):

    url = "https://www.youtube.com/results?search_query=" + \
        keywords.replace(" ", "+") + "&sp=CAASAhAB"

    response = urllib.request.urlopen(url)
    html = response.read()
    html = html.decode("utf=8")

    video_ids = re.findall(r"watch\?v=(\S{11})", html)

    if len(video_ids) > 0:
        return 'https://www.youtube.com/watch?v=' + video_ids[0]
    else:
        return None


@client.event
async def on_ready():
    print('Bot is online')


@client.command()
async def ping(ctx):
    await ctx.send('Pong!')


@client.command()
async def join(ctx):
    voicetrue = ctx.author.voice
    if voicetrue is None:
        return await ctx.send('You are not currently in a voice channel ')
    await ctx.author.voice.channel.connect()
    await ctx.send('Joined the voice channel')


@client.command(aliases=['dc'])
async def leave(ctx):
    voicetrue = ctx.author.voice
    mevoicetrue = ctx.guild.me.voice
    if voicetrue is None:
        return await ctx.send('You are not currently in a voice channel ')
    if mevoicetrue is None:
        return await ctx.send('The bot is not currently in a voice channel ')
    await ctx.voice_client.disconnect()
    await ctx.send('Left the voice channel')


@client.command(aliases=['p'])
async def play(ctx, *, url):
    voicetrue = ctx.author.voice
    if voicetrue is None:
        return await ctx.send('You are not currently in a voice channel ')
    await ctx.author.voice.channel.connect()

    player = music.get_player(guild_id=ctx.guild.id)
    if not player:
        player = music.create_player(ctx, ffmpeg_error_betterfix=True)

    if not url.startswith('http'):
        url = get_video_list(url)
        print(url)
        if url is None:
            return await ctx.send('Song not found!')

    if not ctx.voice_client.is_playing():
        await player.queue(url, search=True)
        song = await player.play()
        await ctx.send(f'Playing {song.name}')
    else:
        song = await player.queue(url, search=True)
        await ctx.send(f'{song.name} has been added to the queue')


@client.command(aliases=['ps'])
async def pause(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.pause()
    await ctx.send(f"Paused {song.name}")


@client.command(aliases=['q'])
async def queue(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    await ctx.send(f"{', '.join([song.name for song in player.current_queue()])}")


@client.command(aliases=['r'])
async def resume(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.resume()
    await ctx.send(f"Resumed {song.name}")


@client.command(aliases=['l'])
async def loop(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.toggle_song_loop()
    if song.is_looping:
        await ctx.send(f"{song.name} is on a loop")
    else:
        await ctx.send(f"{song.name} is not on a loop")


@client.command()
async def np(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = player.now_playing()
    await ctx.send(song.name)


@client.command()
async def remove(ctx, index):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.remove_from_queue(int(index))
    await ctx.send(f"Removed {song.name} from queue")


@client.command(aliases=['s'])
async def skip(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    data = await player.skip(force=True)
    if len(data) == 2:
        await ctx.send(f"Skipped from {data[0].name} to {data[1].name}")
    else:
        await ctx.send(f"Skipped {data[0].name}")

client.run(os.environ.get('BOT_TOKEN'))
