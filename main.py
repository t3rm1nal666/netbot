import random
import string

import discord

client = discord.Client()


@client.event
async def on_ready():
    print("bot ready")
    logfile = open("logs.txt", "a")
    logfile.write("bot ready \n")
    logfile.close()


@client.event
async def on_guild_join(guild):
    embed = discord.Embed(title='thankyou for adding netbot', description='do $help for help')
    await guild.send(embed=embed)
    print('new server added netbot ' + str(discord.Guild.name) + ' ' + str(discord.Guild.banner_url) + ' '
          + str(discord.Guild.owner))
    logfile = open("logs.txt", "a")
    logfile.write('new server added netbot ' + str(discord.Guild.name) + ' ' + str(discord.Guild.owner) + '\n')
    logfile.close()


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("$help"):
        embed = discord.Embed(title='help', description='commands: $help, $ipinfo, $invite, $randomip, $pfp, $beep, '
                                                        '$british, $servers, $cache, $8ball, $logs, $mineforeskin, '
                                                        '$info, $randomembed, $support, ')
        embed.set_footer(text='developed by s0ck3t')
        await message.channel.send(embed=embed)
        print('$help ' + message.author.name + ' ' + str(message.author.id))
        logfile = open("logs.txt", "a")
        logfile.write('$help ' + message.author.name + ' ' + str(message.author.id) + '\n')
        logfile.close()
    if message.content.startswith("$info "):
        content = message.content[7:]
        print('$info ' + content + " " + message.author.name + ' ' + str(message.author.id))
        logfile = open("logs.txt", "a")
        logfile.write('$info ' + content + " " + message.author.name + ' ' + str(message.author.id) + '\n')
        logfile.close()
        if message.content.startswith('$randomembed') or message.content.startswith("randomembed"):
            randomembedinfo = discord.Embed(title='info for $randomembed', description='generates a random embed')
            await message.channel.send(embed=randomembedinfo)

        if content == 'help' or content == '$help':
            helpinfo = discord.Embed(title='info for $help', description='are you fucking smoothbrained?')
            await message.channel.send(embed=helpinfo)
        if content == 'ipinfo' or content == '$ipinfo':
            ipinfoinfo = discord.Embed(title='info for $ipinfo', description='gives you information about a ip address')
            ipinfoinfo.set_footer(text='DO NOT PUT YOUR OWN IP IN IT WILL GO INTO THE BOTS LOGS')
            await message.channel.send(embed=ipinfoinfo)
        if content == 'invite' or content == '$invite':
            inviteinfo = discord.Embed(title='info for $invite',
                                       description='sends the link to add the bot to your server')
            await message.channel.send(embed=inviteinfo)
        if content == 'randomip' or content == '$randomip':
            randomipinfo = discord.Embed(title='info for $randomip', description='generates a random ip address')
            randomipinfo.set_footer(text='not gurenteed to be a live ip')
            await message.channel.send(embed=randomipinfo)
        if content == 'pfp' or content == '$pfp':
            pfpinfo = discord.Embed(title='info for $pfp', description='shows you the bots pfp')
            await message.channel.send(embed=pfpinfo)
        if content == '$beep' or content == 'beep':
            beepinfo = discord.Embed(title='info about $beep', description='beep boop beep bop boop beep')
            await message.channel.send(embed=beepinfo)
        if content == 'british' or content == '$british':
            britishinfo = discord.Embed(title='info bout $bri`ish ay', description='pos memes bout the bri`ish ay')
            await message.channel.send(embed=britishinfo)
        if content == 'servers' or content == '$servers':
            serversinfo = discord.Embed(title='posts raw data on the servers the bots in (just dont)')
            await message.channel.send(embed=serversinfo)
        if content == 'cache' or content == '$cache':
            cacheinfo = discord.Embed(title='info about $cache', description='i dont fucking know LOL')
            await message.channel.send(embed=cacheinfo)
        if content == '8ball' or content == '$8ball':
            ballinfo = discord.Embed(title='info about $8ball', description='a custom magic 8 ball')
            await message.channel.send(embed=ballinfo)
        if content == 'logs' or content == '$logs':
            logsinfo = discord.Embed(title='info about $logs',
                                     description=':wood::wood::wood::wood::wood::wood::wood::wood::wood::wood::wood'
                                                 '::wood::wood::wood::wood::wood::wood:')
            await message.channel.send(embed=logsinfo)
        if content == '$mineforeskin' or content == 'mineforeskin':
            foreskininfo = discord.Embed(title='info about $mineforeskin', description='mines foreskin')
            await message.channel.send(embed=foreskininfo)
        if content == '$support' or content == 'support':
            supportinfo = discord.Embed(title='info about $support', description="links you to the s0ck3t "
                                                                                 "developement discord")
            await message.channel.send(embed=supportinfo)
    if message.content.startswith('rat') or message.content.startswith('RAT'):
        ratlist = ['download phobos 1.5.4 for free popbob sex dupe punjabi movies no haram no virus 100% clean',
                   'https://bigrat.monster/']
        rat = random.choice(ratlist)
        await message.channel.send(rat)
    if message.content.startswith("$ipinfo "):
        ip = message.content[8:]
        await message.channel.send('https://myip.ms/info/whois/' + ip)
        print('$ipinfo ' + ip + " " + message.author.name + ' ' + str(message.author.id))
        logfile = open("logs.txt", "a")
        logfile.write('$ipinfo ' + ip + message.author.name + ' ' + str(message.author.id) + '\n')
        logfile.close()
    if message.content.startswith("$invite"):
        await message.channel.send(
            "https://discord.com/api/oauth2/authorize?client_id=863859504080093194&permissions=0&scope=bot")
        print('$invite ' + message.author.name + ' ' + str(message.author.id))
        logfile = open("logs.txt", "a")
        logfile.write('$invite ' + message.author.name + ' ' + str(message.author.id))
        logfile.close()
    if message.content.startswith('$randomip'):
        num1 = random.randint(0, 256)
        num2 = random.randint(0, 256)
        num3 = random.randint(0, 256)
        num4 = random.randint(0, 256)
        ranip = (str(num1) + '.' + str(num2) + '.' + str(num3) + '.' + str(num4))
        await message.channel.send(ranip)
        print('$randomip ' + message.author.name + ' ' + str(message.author.id))
        logfile = open("logs.txt", "a")
        logfile.write('$randomip ' + message.author.name + ' ' + str(message.author.id) + '\n')
        logfile.close()
    if message.content.startswith('sjnez') or message.content.startswith('Sjnez') or message.content.startswith(
            'SJNEZ'):
        await message.channel.send('gay hitler')
    if message.content.startswith('synz') or message.content.startswith('Synz'):
        await message.channel.send('moar uptime')
    if message.content.startswith('bluemonkey') or message.content.startswith('BlueMonkey'):
        await message.channel.send('crybaby')
    if message.content.startswith('best music'):
        await message.channel.send('https://www.reddit.com/r/sounding/')
    if message.content.startswith('discord') or message.content.startswith('deep web'):
        await message.channel.send(
            'discord servers arent indexed by google so discord is technically part of the deep web')
    if message.content.startswith('genderfluid') or message.content.startswith('gender fluid'):
        await message.channel.send('https://i.redd.it/yrq8xe85rqa71.gif')
    if message.content.startswith('foreskin') or message.content.startswith('innards'):
        await message.channel.send(file=discord.File('9d44f1d92f7118a3496056a3fe29ec551.mp4'))
    if message.content.startswith('twitter') or message.content.startswith('TWITTER'):
        await message.channel.send(file=discord.File('IHATETWITTER.png'))
    if message.content.startswith('$beep'):
        beepembed = discord.Embed(title='beep boop', description='geometric screeching of racial slurs')
        await message.channel.send(embed=beepembed)
        await message.channel.send(file=discord.File('beep.mp3'))
        print('$beep ' + message.author.name + ' ' + str(message.author.id))
        logfile = open("logs.txt", "a")
        logfile.write('$beep ' + message.author.name + ' ' + str(message.author.id) + '\n')
        logfile.close()
    if message.content.startswith('$pfp'):
        await message.channel.send(file=discord.File('pfp.jpg'))
        print('$pfp ' + message.author.name + ' ' + str(message.author.id))
        logfile = open("logs.txt", "a")
        logfile.write('$pfp ' + message.author.name + ' ' + str(message.author.id) + '\n')
        logfile.close()
    if message.content.startswith('yum') or message.content.startswith('YUM'):
        await message.channel.send(file=discord.File('t6yhjs0.gif'))
    if message.content.startswith('$british'):
        britishmemes = ['img.png', 'img_1.png', 'img_2.png', 'img_3.png', 'img_4.png', 'img_5.png', 'img_6.png',
                        'img_7.png']
        british = random.choice(britishmemes)
        await message.channel.send(file=discord.File(british))
        print('$british ' + message.author.name + ' ' + str(message.author.id))
        logfile = open("logs.txt", "a")
        logfile.write('$british ' + message.author.name + ' ' + str(message.author.id) + '\n')
        logfile.close()
    if message.content.startswith('linux') or message.content.startswith('LINUX'):
        if discord.channel.TextChannel.is_nsfw(self=message.channel):
            await message.channel.send(file=discord.File('linux.png'))
        else:
            linux = ['https://tenor.com/view/fortnite-banana-kali-kali-linux-linux-computer-gif-20207141',
                     'https://tenor.com/view/linux-trash-linuxbad-gif-18671901',
                     'https://tenor.com/view/sudo-rm-rf-linux-bruh-chungus-poggers-gif-19024993',
                     'https://tenor.com/view/installing-linux-linux-install-gentoo-linux-linux-memes-linux-meme-gif'
                     '-22136845']
            linuxnonnsfw = random.choice(linux)
            await message.channel.send(linuxnonnsfw)
    if message.content.startswith('software') or message.content.startswith('SOFTWARE'):
        redditid = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        await message.channel.send('https://www.reddit.com/r/softwaregore/comments/' + redditid)
    if message.content.startswith('$servers'):
        serversembed = discord.Embed(title='servers the bot is in', description=client.guilds)
        serversembed.set_footer(text='enjoy the horrific amalgamation of text')
        await message.channel.send(embed=serversembed)
        print('$servers ' + message.author.name + ' ' + str(message.author.id))
        logfile = open("logs.txt", "a")
        logfile.write('$servers ' + message.author.name + ' ' + str(message.author.id) + '\n')
        logfile.close()
    if message.content.startswith('bad bot') or message.content.startswith('cringe bot') or message.content.startswith(
            'shit bot'):
        await message.channel.send('https://tenor.com/view/cry-about-it-cat-hoverboard-cat-on-hoverboard-cry-gif'
                                   '-21748938')
    if message.content.startswith('what should i add to the bot') or message.content.startswith(
            'bot ideas') or message.content.startswith('ideas for the bot'):
        await message.channel.send('more ram')
    if message.content.startswith('$cache'):
        cacheembed = discord.Embed(title='cache', description=client.cached_messages)
        cacheembed.set_footer(text='why would you do this')
        await message.channel.send(embed=cacheembed)
        print('$cache ' + message.author.name + ' ' + str(message.author.id))
        logfile = open("logs.txt", "a")
        logfile.write('$cache ' + message.author.name + ' ' + str(message.author.id) + '\n')
        logfile.close()
    if message.content.startswith('death grips') or message.content.startswith('DEATH GRIPS'):
        await message.channel.send(file=discord.File('roa-7.jpg'))
    if message.content.startswith('george floyd') or message.content.startswith(
            'GEORGE FLOYD') or message.content.startswith('georgefloyd') or message.content.startswith('GEORGEFLOYD'):
        await message.channel.send(file=discord.File('georgefloyd.mp4'))
    if message.content.startswith('socialism') or message.content.startswith('SOCIALISM') or message.content.startswith(
            'communism') or message.content.startswith('COMMUNISM'):
        await message.channel.send(file=discord.File('socialismdoesntwork.mp4'))
    if message.content.startswith('cope') or message.content.startswith('COPE') or message.content.startswith('sus') \
            or message.content.startswith('SUS') or message.content.startswith('amogus') \
            or message.content.startswith('AMOGUS'):
        await message.channel.send('GET OUT OF MY HEAD \n GET OUT OF MY HEAD \n GET OUT OF MY HEAD \n GET OUT OF '
                                   'MY HEAD \n GET OUT OF MY HEAD')
    if message.content.startswith('$8ball'):
        ballanswers = ['yes', 'no', 'maybe', 'possible', 'unlikely', 'likely', 'dont count on it', 'maybe some day',
                       'ask again', 'go fuck yourself', 'no LOL', 'impossible']
        answer = random.choice(ballanswers)
        await message.channel.send(answer)
        print('$8ball' + message.author.name + ' ' + str(message.author.id))
        logfile = open("logs.txt", "a")
        logfile.write('$8ball ' + message.author.name + ' ' + str(message.author.id) + '\n')
        logfile.close()
    if message.content.startswith('$logs'):
        await message.channel.send(':wood: :wood: :wood:')
        print('$logs ' + message.author.name + ' ' + str(message.author.id))
        logfile = open("logs.txt", "a")
        logfile.write('$logs ' + message.author.name + ' ' + str(message.author.id) + '\n')
        logfile.close()
    if message.content.startswith('$logfile'):
        await message.channel.send(file=discord.File('logs.txt'))
        print('$logfile ' + message.author.name + ' ' + str(message.author.id))
        logfile = open("logs.txt", "a")
        logfile.write('$logfile ' + message.author.name + ' ' + str(message.author.id) + '\n')
        logfile.close()
    if message.content.startswith('$mineforeskin'):
        foreskinmined = random.randint(1, 100)
        await message.channel.send('you just mined ' + str(foreskinmined) + " foreskin!")
        print('$mineforeskin ' + message.author.name + ' ' + str(message.author.id))
        logfile = open("logs.txt", "a")
        logfile.write('$mineforeskin ' + message.author.name + ' ' + str(message.author.id) + '\n')
        logfile.close()
    if message.content.startswith('$randomembed'):
        textlengthrange1 = random.randint(1, 256)
        textlengthrange2 = random.randint(1, 1500)
        textlengthrange3 = random.randint(1, 250)
        randomtext1 = ''.join(random.choices(string.ascii_letters + string.digits, k=textlengthrange1))
        randomtext2 = ''.join(random.choices(string.ascii_letters + string.digits, k=textlengthrange2))
        randomtext3 = ''.join(random.choices(string.ascii_letters + string.digits, k=textlengthrange3))
        randomembed = discord.Embed(title=randomtext1, description=randomtext2)
        generateembedrandomizer = random.randint(1, 5)
        lines = open('urls.txt').read().splitlines()
        myline = random.choice(lines)
        lines2 = open('english3.txt').read().splitlines()
        myline2 = random.choice(lines2)
        lines3 = open('glitchedimages/images.txt').read().splitlines()
        myline3 = random.choice(lines3)
        randomimage = discord.File(myline3)
        if generateembedrandomizer == 1:
            await message.channel.send(file=randomimage)
        if generateembedrandomizer == 2:
            randomembed.set_footer(text=randomtext3)
        if generateembedrandomizer == 3:
            randomembed.set_author(name=myline, url=myline)
        if generateembedrandomizer == 4:
            randomembed.set_author(name='bot built by s0ck3t', url='https://discord.gg/eWmXRhVhck')
        if generateembedrandomizer == 5:
            randomembed.set_footer(text=myline2)
        await message.channel.send(embed=randomembed)

    if message.content.startswith("$support"):
        await message.channel.send("support at https://discord.gg/eWmXRhVhck")
client.run("ODYzODU5NTA0MDgwMDkzMTk0.YOtB2w.ADWcyIWzIFKcoC9QFLgGck46F3Y")
