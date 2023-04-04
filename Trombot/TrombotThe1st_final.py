from dis import dis
import re
from turtle import title
from unicodedata import name
import discord
from discord.errors import Forbidden
from discord.ext import commands, tasks
import random
import asyncio


trombot = commands.Bot(command_prefix="$", description="Trombot The 1st est dans la place.")
trombot.remove_command("help")


cookies=["https://cdn.discordapp.com/attachments/900869947050295336/902324971248951316/nom-anime.gif","https://cdn.discordapp.com/attachments/900869947050295336/902333470813085786/cute-eating.gif" ,"https://cdn.discordapp.com/attachments/900869947050295336/902333737260437554/anime-food.gif","https://cdn.discordapp.com/attachments/900869947050295336/902334893000896532/anime-cookie.gif","https://cdn.discordapp.com/attachments/900869947050295336/902335141882494977/one-piece-carrot.gif","https://cdn.discordapp.com/attachments/900869947050295336/902335885058666526/cookie-mashiro.gif","https://cdn.discordapp.com/attachments/900869947050295336/902336193235136532/anime-animegirl.gif","https://cdn.discordapp.com/attachments/900869947050295336/902336498244931614/anime-eating.gif"]
selfmort=["https://cdn.discordapp.com/attachments/900869947050295336/902337068355698688/noragomi.gif","https://cdn.discordapp.com/attachments/900869947050295336/902337460422471710/anime-vegetables.gif","https://cdn.discordapp.com/attachments/900869947050295336/902337715062845440/ruru-suicide-show.gif"]
mort=["https://cdn.discordapp.com/attachments/900869947050295336/902338192198475876/91days-angelo-lagusa.gif","https://cdn.discordapp.com/attachments/900869947050295336/902338394145837066/fate-grand-order-babylonia.gif","https://cdn.discordapp.com/attachments/900869947050295336/902338667115323472/astolfo-trap-of-argalia.gif","https://cdn.discordapp.com/attachments/900869947050295336/902339124109910046/death-note-light-yagami.gif","https://cdn.discordapp.com/attachments/900869947050295336/902340200737411072/tensei-shitara-slime-datta-ken-that-time-i-got-reincarnated-as-a-slime.gif","https://cdn.discordapp.com/attachments/900869947050295336/902340558935179274/akudama-drive.gif","https://cdn.discordapp.com/attachments/900869947050295336/902340851110412298/megumin-kono-suba-gods-blessing-on-this-wonderful-world.gif","https://cdn.discordapp.com/attachments/900869947050295336/902341096980492288/killing-anime-girl.gif"]
jinglesncf=["https://cdn.discordapp.com/attachments/900869947050295336/913223786353008650/yahoo.mp4","https://cdn.discordapp.com/attachments/900869947050295336/909485468360531968/osmanthus.mp4","https://cdn.discordapp.com/attachments/900869947050295336/901805345742155776/tartine.mp4","https://cdn.discordapp.com/attachments/900869947050295336/901624309200588810/pates.mp4","https://cdn.discordapp.com/attachments/900869947050295336/901253663178244146/oubli.mp4","https://cdn.discordapp.com/attachments/900869947050295336/901246881177419776/daronnage.mp4","https://cdn.discordapp.com/attachments/900869947050295336/900878676520996904/debat.mp4"]
jingleratp=["https://cdn.discordapp.com/attachments/900869947050295336/901771950249099345/ligne_16.mp4","https://cdn.discordapp.com/attachments/900869947050295336/901771778152603668/GAS.mp4","https://cdn.discordapp.com/attachments/900869947050295336/901635865955143690/promotion.mp4","https://cdn.discordapp.com/attachments/900869947050295336/901635871030259752/traps.mp4"]
reponses=["Ça me parait évident en fait","J'en sais rien moi, je connais que Limule et Vivi dans la vie","Est-ce que j'ai fini de build ma Hu Tao décemment ? Tu as ta réponse.","Demande plutôt à BarnaB, c'est pas mon problème ça.","Tu veux pas aller boire de la potion de Konoha au lieu de me poser des questions ?","Alors par contre déso, mais je te réponds plus tard, là j'ai la crémaillère de mon meilleur pote et j'avais oublié *ahah*.","Essaye de trouver la puissance de Teppei pour voir si ça t'aide.","Je sais pas, mais **ACHÈTE UNE FIGURINE DE LIMULE** !","J'te répondrais plus tard, là j'suis ban twitch à cause des bangalas ...","Attend, je fini de regarder le tutoOôriel avant de te dire non."]
tanjikuimg=["https://media.discordapp.net/attachments/779498004880162836/901549689764196422/tobecontinued.png","https://media.discordapp.net/attachments/779498004880162836/901549997995196436/tobecontinued.png"]
hellogif=["https://cdn.discordapp.com/attachments/900869947050295336/902350498710032394/anime-girl.gif","https://cdn.discordapp.com/attachments/900869947050295336/902341761551171604/gerger.gif","https://cdn.discordapp.com/attachments/900869947050295336/902342017131090010/demon-slayer-anime.gif","https://cdn.discordapp.com/attachments/900869947050295336/902342341027827722/hi-wave.gif","https://cdn.discordapp.com/attachments/900869947050295336/902342529565995068/kisumi-wave.gif","https://cdn.discordapp.com/attachments/900869947050295336/902342712899026944/killua-zoldyck-anime.gif","https://cdn.discordapp.com/attachments/900869947050295336/902342994810798120/hey-hello.gif"]
hugging=["https://cdn.discordapp.com/attachments/900869947050295336/902343369567637534/crying-anime-kyoukai-no-kanata-hug.gif","https://cdn.discordapp.com/attachments/900869947050295336/902343628553338900/hug-anime-hug.gif","https://cdn.discordapp.com/attachments/900869947050295336/902343819939426355/toilet-bound-hanakokun.gif","https://cdn.discordapp.com/attachments/900869947050295336/902344124005515264/hug-anime.gif","https://cdn.discordapp.com/attachments/900869947050295336/902344428239339520/hug-anime.gif","https://cdn.discordapp.com/attachments/900869947050295336/902344704421675018/anime-cute.gif","https://cdn.discordapp.com/attachments/900869947050295336/902344984458571887/anime-hug.gif","https://cdn.discordapp.com/attachments/900869947050295336/902345243821764688/teria-wang-kishuku-gakkou-no-juliet.gif"]
limuletempest=["https://cdn.discordapp.com/attachments/900869947050295336/903046141241876510/tensei-shitara-slime-datta-ken-slime-question-mark.gif","https://cdn.discordapp.com/attachments/900869947050295336/902346084351885342/rimuru-slime-anime.gif","https://cdn.discordapp.com/attachments/900869947050295336/903046274008367134/tensei-shitara-slime-datta-ken-rimuru.gif","https://cdn.discordapp.com/attachments/900869947050295336/902346807114358830/qxwaii-kawaii.gif","https://cdn.discordapp.com/attachments/900869947050295336/902347376667291688/goodbye-bye.gif","https://cdn.discordapp.com/attachments/900869947050295336/902347628686241852/rimuru-tempest-rimuru.gif","https://cdn.discordapp.com/attachments/900869947050295336/902347856998989915/rimuru-rimuru-tempest.gif","https://cdn.discordapp.com/attachments/900869947050295336/902348124834644038/tensei-shitara-slime-datta-ken-huh.gif","https://cdn.discordapp.com/attachments/900869947050295336/902348748187914260/rimuru-rimuru-tempest.gif","https://cdn.discordapp.com/attachments/900869947050295336/902348973128425512/anime-black-lightning.gif"]
eviltrombone=[""]
evilazoth=["https://cdn.discordapp.com/attachments/900459561666904075/941631380071284777/u.png","https://cdn.discordapp.com/attachments/900459561666904075/941632264054390784/u2.png","https://cdn.discordapp.com/attachments/900459561666904075/941632272694665246/u3.png","https://cdn.discordapp.com/attachments/900459561666904075/941632821057949716/u4.png"]
evilyaourt=["https://cdn.discordapp.com/attachments/900459561666904075/941637355981381632/y.png"]
evilaka=[""]
evilkrea=[""]
evilasto=[]
evilelia=[""]
evilclary=[""]
evilrick=[""]
evilrock=[""]
evilbruno=[""]
devil=[eviltrombone,evilazoth,evilyaourt,evilaka,evilkrea,evilasto,evilelia,evilclary,evilrick,evilrock,evilbruno]

def convert(time):
    pos=["s","m","h","d",]
    time_dict={"s":1,"m":60,"h":3600,"d":3600*24}
    time=str(time)
    unit=time[-1]
    if unit not in pos:
        return -1
    try:
        val=int(time[:-1])
    except:
        return -2
    return val*time_dict[unit]

@trombot.event
async def on_ready():
    print("Limule on the road.")
    try:
        cpstatus.start()
    except RuntimeError:
        pass
status=["Être the First","Choisir entre Vivi et Limule","Farm les artéfacts de Hu Tao sur Genshin","Se réincarner en Slime","Se faire démarrer par Renjiro","Shiny hunt Ouisticram","Regarder le tutoOôriel !","Créé des démons"]
@tasks.loop(seconds=30)
async def cpstatus():
    game=discord.Game(random.choice(status))
    await trombot.change_presence(status=discord.Status.online, activity=game)

@trombot.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.CommandNotFound):
        await ctx.send("C'EST QUOI CETTE COMMANDE LÀ ! FAIT UN EFFORT ET REGARDE L'AIDE !",delete_after=5)
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("Il manque un truc, mais je sais pas quoi ...",delete_after=5)
    if isinstance(error,discord.Forbidden):
        await ctx.send("J'ai des problèmes de permissions pour cette commande, mais c'est rien, c'est la rue ...",delete_after=10)

@trombot.command()
async def help(ctx,mode="normal"):
    if mode=="normal":
        em=discord.Embed(title="Liste des commandes",description=f"Pour connaître toutes les commandes sur le bout des doigts. Le préfix du bot est {trombot.command_prefix}.",color=7394047)
        em.add_field(name="Aide",value="``help``",inline=False)
        em.add_field(name="Suggestions",value="``suggest``",inline=False)
        em.add_field(name="Interactions",value="``cookie``, ``hi``, ``kill``, ``hug``",inline=False)
        em.add_field(name="Rigolade",value="``sncf``, ``ratp``, ``poll``, ``kaijvu``, ``zhongli``, ``limule``",inline=False)
        em.add_field(name="Références au Twitch",value="``renjiro``, ``limuri``, ``triggered``",inline=False)
        if ctx.message.channel.id==901896376437338123:
            em.add_field(name="Genshin",value="``build``",inline=False)
        if ctx.message.author.guild_permissions.manage_messages:
            em.add_field(name="Modération",value="``clear``, ``mute``, ``unmute``, ``ban``, ``unban``",inline=False)
        await ctx.send(embed=em)
    elif mode=="help":
        em=discord.Embed(title="Help",description="Montre la liste des commandes *ou* décrit le fonctionnement d'une commande.",color=7394047)
        em.add_field(name="Syntaxe",value=f"``{trombot.command_prefix}help`` *ou* ``{trombot.command_prefix}help <command>``")
        await ctx.send(embed=em)
    elif mode=="suggest" or mode=="suggest" or mode=="sug":
        if ctx.guild.id==745697573066506381:
            em=discord.Embed(title="Suggestion",description=f"Crée une suggestion pour le serveur. \nFonctionne uniquement dans le salon <#901933593801154610>",color=7394047,)
            em.add_field(name="Alias",value=f"``{trombot.command_prefix}sug``, ``{trombot.command_prefix}suggest``, ``{trombot.command_prefix}suggestion``",inline=False)
            em.add_field(name="Syntaxe",value=f"``{trombot.command_prefix}suggestion <suggestion pour le serveur>``",inline=False)
            await ctx.send(embed=em)
        elif ctx.guild.id==879431432806744095:
            em=discord.Embed(title="Suggest",description=f"Crée une suggestion pour le serveur. \nFonctionne uniquement dans le salon <#880189018086727764>",color=7394047)
            em.add_field(name="Alias",value=f"``{trombot.command_prefix}sug``, ``{trombot.command_prefix}suggest``, ``{trombot.command_prefix}suggestion``",inline=False)
            em.add_field(name="Syntaxe",value=f"``{trombot.command_prefix}suggest <suggestion pour le serveur>``")
            await ctx.send(embed=em)
        else:
            await ctx.send("Comment j'ai fini ici même ?")
    elif mode=="cookie":
        em=discord.Embed(title="Cookie",description="Donne un cookie à quelqu'un.",color=7394047)
        em.add_field(name="Syntaxe",value=f"``{trombot.command_prefix}cookie <@membre>``")
        await ctx.send(embed=em)
    elif mode=="kill":
        em=discord.Embed(title="Kill",description="Tue quelqu'un.",color=7394047)
        em.add_field(name="Syntaxe",value=f"``{trombot.command_prefix}kill <@membre>``")
        await ctx.send(embed=em)
    elif mode=="hug":
        em=discord.Embed(title="Hug",description="Câline quelqu'un.",color=7394047)
        em.add_field(name="Syntaxe",value=f"``{trombot.command_prefix}hug <@membre>``")
        await ctx.send(embed=em)
    elif mode=="hi" or mode=="hello" or mode=="wave":
        em=discord.Embed(title="Hi",description="Salut quelqu'un.",color=7394047)
        em.add_field(name="Alias",value=f"``{trombot.command_prefix}hi``, ``{trombot.command_prefix}hello``, ``{trombot.command_prefix}wave``",inline=False)
        em.add_field(name="Syntaxe",value=f"``{trombot.command_prefix}hi [@membre]``",inline=False)
        await ctx.send(embed=em)
    elif mode=="sncf":
        if ctx.guild.id==879431432806744095:
            em=discord.Embed(title="SNCF",description="Lance un Jingle SNCF aléatoire. \nFonctionne uniquement dans le salon <#902513124068954122>",color=7394047)
        else:
            em=discord.Embed(title="SNCF",description="Lance un Jingle SNCF aléatoire.",color=7394047)
        em.add_field(name="Syntaxe",value=f"``{trombot.command_prefix}sncf``")
        await ctx.send(embed=em)
    elif mode=="ratp":
        if ctx.guild.id==879431432806744095:
            em=discord.Embed(title="RATP",description="Lance un Jingle RATP aléatoire. \nFonctionne uniquement dans le salon <#902513124068954122>",color=7394047)
        else:
            em=discord.Embed(title="RATP",description="Lance un Jingle RATP aléatoire.",color=7394047)
        em.add_field(name="Syntaxe",value=f"``{trombot.command_prefix}ratp``")
        await ctx.send(embed=em)
    elif mode=="evil":
        if ctx.guild.id==879431432806744095:
            em=discord.Embed(title="Evil",description="Découvre à quoi ressemblerait les choses si elles étaient démoniaques. \nFonctionne uniquement dans le salon <#902513124068954122>",color=7394047)
        else:
            em=discord.Embed(title="Evil",description="Découvre à quoi ressemblerait les choses si elles étaient démoniaques.",color=7394047)
        em.add_field(name="Syntaxe",value=f"``{trombot.command_prefix}evil [démon à invoquer]``")
        em.add_field(name="Liste des démons",value="``Trombone``, ``Azoth``, ``ia_Ourtt``, ``Aka``, ``Kreatyr``, ``Astolfo``, ``eliabricot``, ``Clary``, ``Rick``, ``The Rock``, ``Bruno``")
    elif mode=="poll":
        em=discord.Embed(title="Poll",description="Trombot répond à la question que tu lui pose.",color=7394047)
        em.add_field(name="Syntaxe",value=f"``{trombot.command_prefix}poll <question>``")
        await ctx.send(embed=em)
    elif mode=="kaijvu":
        em=discord.Embed(title="Kaijvu",description="Lave-toi les yeux histoire d'être sûr.",color=7394047)
        em.add_field(name="Syntaxe",value=f"``{trombot.command_prefix}kaijvu``")
    elif mode=="zhongli":
        em=discord.Embed(title="Zhongli",description="L'archon Géo a quelque chose à dire.",color=7394047)
        em.add_field(name="Syntaxe",value=f"``{trombot.command_prefix}zhongli``")
        await ctx.send(embed=em)
    elif mode=="limuri" or mode=="lr":
        em=discord.Embed(title="Limuri",description="Limule vient rire dans le chat, parce qu'on est avant tout là pour la DÉCONNE !",color=7394047)
        em.add_field(name="Alias",value=f"``{trombot.command_prefix}lr``, ``{trombot.command_prefix}limuri``",inline=False)
        em.add_field(name="Syntaxe",value=f"``{trombot.command_prefix}limuri``",inline=False)
        await ctx.send(embed=em)
    elif mode=="limule" or mode=="tempest" or mode=="lt" or mode=="slime":
        em=discord.Embed(title="Limule",description="Admire un peu Limule Tempest.",color=7394047)
        em.add_field(name="Alias",value=f"``{trombot.command_prefix}limule``, ``{trombot.command_prefix}tempest``, ``{trombot.command_prefix}lt``, ``{trombot.command_prefix}slime``",inline=False)
        em.add_field(name="Syntaxe",value=f"``{trombot.command_prefix}limule``",inline=False)
        await ctx.send(embed=em)
    elif mode=="build":
        if ctx.message.channel.id==901896376437338123:
            em=discord.Embed(title="Build",description="Regarde comment build ton perso sur genshin !",color=7394047)
            em.add_field(name="Syntaxe",value=f"``{trombot.command_prefix}build [nom du personnage à build]``",inline=False)
            await ctx.send(embed=em)
    elif mode=="clear" or mode=="purge" or mode=="bbb":
        if ctx.message.author.guild_permissions.manage_messages:
            em=discord.Embed(title="Clear",description="Trombot vient nettoyer les conversations ! (La valeur du clear par défaut est de 5)",color=7394047)
            em.add_field(name="Alias",value=f"``{trombot.command_prefix}purge``, ``{trombot.command_prefix}clear``, ``{trombot.command_prefix}bbb``",inline=False)
            em.add_field(name="Syntaxe",value=f"``{trombot.command_prefix}clear [nombre de messages à effacer]``",inline=False)
            await ctx.send(embed=em)
        else:
            await ctx.send("Pas besoin d'aide pour une commande que tu peux pas faire !")
    elif mode=="triggered" or mode=="gkn":
        em=discord.Embed(title="Triggered",description="Fait de ton mieux, s'il te plaît !",color=7394047)
        em.add_field(name="Alias",value=f"``{trombot.command_prefix}gkn``, ``{trombot.command_prefix}triggered``",inline=False)
        em.add_field(name="Syntaxe",value=f"``{trombot.command_prefix}triggered``",inline=False)
        await ctx.send(embed=em)
    elif mode=="renjiro" or mode=="rj" or mode=="ti" or mode=="tanjiku":
        em=discord.Embed(title="Renjiro",description="Tes PV vont disparaître, dis adieu à la vie.",color=7394047)
        em.add_field(name="Alias",value=f"``{trombot.command_prefix}rj``, ``{trombot.command_prefix}ti``, ``{trombot.command_prefix}renjiro``, ``{trombot.command_prefix}tanjiku``",inline=False)
        em.add_field(name="Syntaxe",value=f"``{trombot.command_prefix}renjiro``",inline=False)
        await ctx.send(embed=em)
    elif mode=="mute":
        if ctx.message.author.guild_permissions.manage_roles:
            em=discord.Embed(title="Mute",description="Enlève le droit parole à un casse-pied.",color=7394047)
            em.add_field(name="Syntaxe",value=f"``{trombot.command_prefix}mute indéfini <@membre> [raison]`` \n``{trombot.command_prefix}mute <durée> <@membre> [raison]``")
            em.add_field(name="Durée",value="*Valeurs acceptées :* \n``s/m/h/d``")
            await ctx.send(embed=em)
        else:
            await ctx.send("Pas besoin d'aide pour une commande que tu peux pas faire !")
    elif mode=="unmute":
        if ctx.message.author.guild_permissions.manage_roles:
            em=discord.Embed(title="Unmute",description="Rend la parole à un utilisateur muet.",color=7394047)
            em.add_field(name="Syntaxe",value=f"``{trombot.command_prefix}unmute <@membre> [raison]``")
            await ctx.send(embed=em)
        else:
            await ctx.send("Pas besoin d'aide pour une commande que tu peux pas faire !")
    elif mode=="ban":
        if ctx.message.author.guild_permissions.ban_members:
            em=discord.Embed(title="Ban",description="Banni un utilisateur du serveur.",color=7394047)
            em.add_field(name="Syntaxe",value=f"``{trombot.command_prefix}ban <@membre> [raison]``")
            await ctx.send(embed=em)
        else:
            await ctx.send("Pas besoin d'aide pour une commande que tu peux pas faire !")
    elif mode=="unban":
        if ctx.message.author.guild_permissions.ban_members:
            em=discord.Embed(title="Unban",description="Révoque le bannissement d'un utilisateur du serveur.",color=7394047)
            em.add_field(name="Syntaxe",value=f"``{trombot.command_prefix}unban <pseudo et discord tag du membre> [raison]``")
            await ctx.send(embed=em)
        else:
            await ctx.send("Pas besoin d'aide pour une commande que tu peux pas faire !")
    else:
        await ctx.send("Réécris la commande correctement sinon **J'VAIS T'GOUMER LÀ** !")

@trombot.command(aliases=['sug','suggestion'])
async def suggest(ctx,*,arg=None):
    if ctx.guild.id==745697573066506381:
        if ctx.channel.id==901933593801154610:
            if arg==None:
                await ctx.send("Écris une suggestion non ?",delete_after=5)
            else:
                suggestChannel=trombot.get_channel(901933566571737168)
                em=discord.Embed(title="Suggestion",description=f"{arg}",color=discord.Color.from_rgb(204, 204, 255))
                em.add_field(name="Proposée par :",value=f"*{ctx.message.author.name}*")
                suggestions=await suggestChannel.send(embed=em)
                await suggestions.add_reaction('<a:RedCross:901949679342854224>')
                await suggestions.add_reaction('<a:GreenCheck:901949560526610432>')
                await ctx.channel.purge(limit=1)
        else:
            await ctx.send("Va dans le bon salon pour faire ta suggestion :eyes:",delete_after=5)
    elif ctx.guild.id==879431432806744095:
        if ctx.channel.id==880189018086727764:
            if arg==None:
                await ctx.send("Écris une suggestion non ?",delete_after=5)
            else:
                suggestChannel=trombot.get_channel(898509916417961984)
                em=discord.Embed(title="Suggestion :",description=f"{arg}",color=discord.Color.from_rgb(204, 204, 255))
                em.add_field(name="Proposée par :",value=ctx.message.author.name)
                suggestions=await suggestChannel.send(embed=em)
                await suggestions.add_reaction('<a:RedCross:901949679342854224>')
                await suggestions.add_reaction('<a:GreenCheck:901949560526610432>')
                await ctx.channel.purge(limit=1)
        else:
            await ctx.send("Va dans le bon salon pour faire ta suggestion :eyes:",delete_after=5)
    else:
        await ctx.send("Qu'est-ce que je fous là moi ?")

@trombot.command()
async def build(ctx,*,mode="normal"):
    if ctx.guild.id==879431432806744095:
        if ctx.channel.id==901896376437338123:
            if mode=="normal":
                em=discord.Embed(title="De quel personnage veux-tu voir le build ?",description="Indique le nom du personnage dont tu veux voir le build !",color=discord.Color.from_rgb(17, 66, 156))
                em.add_field(name="Liste des personnages 4 étoiles :",value="_ _\n**Anémo** : ``Sucrose`` - ``Sayu`` \n _ _\n _ _\n**Pyro** : ``Amber`` - ``Xiangling`` - ``Xinyan`` - ``Bennett`` - ``Yanfei`` - ``Thomas`` \n _ _\n**Electro** : ``Lisa`` - ``Beidou`` - ``Fischl`` - ``Razor`` - ``Kujou Sara`` \n _ _\n**Cryo** : ``Kaeya`` - ``Diona`` - ``Chongyun`` - ``Rosalia`` \n _ _\n**Hydro** : ``Barbara`` - ``Xingqiu`` \n _ _\n _ _ \n**Géo** : ``Noelle`` - ``Ningguang`` - ``Gorou`` - ``Yun Jin``")
                em.add_field(name="Liste des personnages 5 étoiles :",value="_ _\n**Anémo** : ``Jean`` - ``Xiao`` - ``Venti`` - ``Kaedehara Kazuha`` \n _ _\n**Pyro** : ``Diluc`` - ``Klee`` - ``Hu Tao`` - ``Yoimiya``\n _ _\n _ _\n**Electro** : ``Keqing`` - ``Shogun Raiden`` - ``Yae Miko`` \n _ _\n**Cryo** : ``Qiqi`` - ``Ganyu`` - ``Eula`` - ``Kamisato Ayaka`` - ``Shenhe`` - ``Aloy`` \n _ _\n**Hydro** : ``Mona`` - ``Tartaglia`` - ``Sangonomiya Kokomi`` - ``Kamisato Ayato`` - ``Yelan`` \n _ _\n**Géo** : ``Zhongli`` - ``Albedo`` - ``Arataki Itto`` \n _ _\n**Autre** : ``Traveler``")
                em.add_field(name="Liste des personnages à venir :",value="``Shikanoin Heizou`` - ``Kuki Shinobu``")
                em.set_image(url="https://media.discordapp.net/attachments/792879261920919593/903050199151300608/E4TdHllXIAA1bM-.png?width=1074&height=671")
                em.set_footer(text="Les builds présentés sont là uniquement pour donner une idée, ils ne sont pas les seuls builds possibles à faire. Vous êtes tout à fait en droit de préférer d'autres alternatives.")
                await ctx.send(embed=em)
            elif mode=="Kamisato" or mode=="kamisato":
                await ctx.send("Tu veux bien préciser lequel des deux, s'te plaît ? \nHistoire que je sache quoi te répondre ...")
            elif mode=="Surcose" or mode=="sucrose":
                em=discord.Embed(title="Sucrose :",description="*Une alchimiste très curieuse du monde qui l'entoure. Elle se spécialise dans la bio-alchimie.*",color=discord.Color.from_rgb(133, 255, 165))
                em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> Maitrise Élémentaire/Recharge d'énergie \n<:Coupe:903641040941088769> Maitrise Élémentaire - <:Couronne:903641083236458536> Maitrise Élémentaire \n*Sub stats* : \nMaitrise Élémentaire > Recharge d'énergie > Crit > ATK% \n*Set* : \n:first_place: Ombre de la Verte Chasseuse (4 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Sujet 6308)* \n:second_place: Déchainement élémentaire *(Isomorphe 75 Type II)* \n:third_place: Attaque de base *(Esprit du Vent)* \n _ _",inline=False)
                em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK%/Maitrise Élémentaire \n<:Coupe:903641040941088769> Dégats Anémo - <:Couronne:903641083236458536> Dgt Crit/Taux Crit \n*Sub stats* : \nCrit > Maitrise Élémentaire > ATK% > Recharge d'énergie \n*Set* : \n:first_place: Ombre de la Verte Chasseuse (4 pièces) \nOmbre de la Verte Chasseuse (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Esprit du Vent)* \n:second_place: Compétence élémentaire *(Sujet 6308)* \n:third_place: Déchainement élémentaire *(Isomorphe 75 Type II)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/903062307247124490/Sucroz.png")
                await ctx.send(embed=em)
            elif mode=="Sayu" or mode=="sayu":
                em=discord.Embed(title="Sayu :",description="*Une très petite ninja rattachée au Shuumatsuban, qui semble toujours manquer de sommeil.*",color=discord.Color.from_rgb(133, 255, 165))
                em.add_field(name="Support/Healeur :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK%/Maitrise Élémentaire \n<:Coupe:903641040941088769> ATK%/Maitrise Élémentaire - <:Couronne:903641083236458536> Bonus de Soin/ATK%/Maitrise Élémentaire \n*Sub stats* : \nATK% > Maitrise Élémentaire > Recharge d'énergie \n*Set* : \n:first_place: Ombre de la Verte Chasseuse (4 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(École Yoohoo : Folie du ninja)* \n:second_place: Compétence élémentaire *(École Yoohoo : Bond Fuuin)* \n:third_place: Attaque de base *(Lame Shiyuumatsu-Ban)* \n _ _",inline=False)
                em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> Maitrise Élémentaire \n<:Coupe:903641040941088769> Dégats Anémo/Maitrise Élémentaire - <:Couronne:903641083236458536> Dgt Crit/Taux Crit/Maitrise Élémentaire \n*Sub stats* : \nMaitrise Élémentaire > ATK% > Crit > Recharge d'énergie \n*Set* : \n:first_place: Ombre de la Verte Chasseuse (4 pièces) \nOmbre de la Verte Chasseuse (2 pièces) & Bande Vagabonde (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(École Yoohoo : Folie du ninja)* \n:second_place: Compétence élémentaire *(École Yoohoo : Bond Fuuin)* \n:third_place: Attaque de base *(Lame Shiyuumatsu-Ban)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/903964302510293032/sayou.png")
                await ctx.send(embed=em)
            elif mode=="Amber" or mode=="amber":
                em=discord.Embed(title="Amber :",description="*Une jeune fille pleine d'énergie. Elle est la seule et unique Éclaireuse de l'Ordre de Favonius.*",color=discord.Color.from_rgb(255, 33, 33))
                em.add_field(name="Support/Burst :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Pyro/ATK% - <:Couronne:903641083236458536> Dgt Crit/Taux Crit \n*Sub stats* : \nCrit > ATK% > Maitrise Élémentaire \n*Set* : \n:first_place: Ancien Rituel Royal (4 pièces) \nSorcière des Flammes Ardentes (2 pièces) & Ancien Rituel Royal (2 pièces) \nSorcière des Flammes Ardentes (2 pièces) & Rideau du Gladiateur (2 pièces) \n_ _ \n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Pluie de Flèches)* \n:second_place: Compétence élémentaire *(Baron Lapinou)* \n:third_place: Attaque de base *(Archerie Revisitée)* \n _ _",inline=False)
                em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Pyro/ATK% - <:Couronne:903641083236458536> Dgt Crit/Taux Crit \n*Sub stats* : \nCrit > ATK% > Maitrise Élémentaire \n*Set* : \n:first_place: Bande Vagabonde (4 pièces) \nSorcière des Flammes Ardentes (2 pièces) & Rideau du Gladiateur (2 pièces) \nSorcière des Flammes Ardentes (2 pièces) & Ancien Rituel Royal (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Archerie Revisitée)* \n:second_place: Déchainement élémentaire *(Pluie de Flèches)* \n:third_place: Compétence élémentaire *(Baron Lapinou)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/903967766573355048/ambeer.png")
                await ctx.send(embed=em)
            elif mode=="Kokomi" or mode=="kokomi" or mode=="Sangonomiya Kokomi" or mode=="sangonomiya kokomi" or mode=="Sangonomiya kokomi" or mode=="Sangonomiya" or mode=="sangonomiya Kokomi" or mode=="sangonomiya" or mode=="Kokomi Sangonomiya" or mode=="Kokomi sangonomiya" or mode=="kokomi Sangonomiya" or mode=="kokomi sangonomiya":
                em=discord.Embed(title="Sangonomiya Kokomi :",description="*La Prêtresse divine de l'Île de Watatsumi, une jeune femme gérant toutes les affaires de l'île.*",color=discord.Color.from_rgb(28, 111, 255))
                em.add_field(name="DPS/Healeur :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> PV% \n<:Coupe:903641040941088769> Dégats Hydro - <:Couronne:903641083236458536> Bonus de Soin/PV% \n*Sub stats* : \nPV% > ATK% > Recharge d'énergie \n*Set* : \n:first_place: Palourde aux Teintes Océaniques (4 pièces) \nÂme des Profondeurs (4 pièces) \nÂme des Profondeurs (2 pièces) & Amour Chéri (2 pièces) \n    _ _ \n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Ascension de la néréide)* \n:second_place: Compétence élémentaire *(Serment de Kurage)* \n:third_place: Attaque de base *(Forme de l'eau)* \n _ _",inline=False)
                em.add_field(name="Support/Healeur :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> PV% \n<:Coupe:903641040941088769> Dégats Hydro/PV% - <:Couronne:903641083236458536> Bonus de Soin/PV% \n*Sub stats* : \nPV% > Recharge d'énergie > ATK% \n*Set* : \n:first_place: Amour Chéri (2 pièces) & Palourde aux Teintes Océaniques (2 pièces) \nAmour Chéri (2 pièces) & Tenacité du Millelithe (2 pièces) \nPalourde aux Teintes Océaniques (2 pièces) & Tenacité du Millelithe (2 pièces) \nAmour Chéri (4 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Serment de Kurage)* \n:second_place: Déchainement élémentaire *(Ascension de la néréide)* \n:third_place: Attaque de base *(Forme de l'eau)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/903991388977385472/sangonomiya.png")
                await ctx.send(embed=em)
            elif mode=="Aloy" or mode=="aloy":
                em=discord.Embed(title="Aloy :",description="*Autrefois une paria, maintenant une chasseuse d'une acuité sans précédent. Toujours prête à utiliser son arc pour la bonne cause.*",color=discord.Color.from_rgb(117, 227, 255))
                em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Cryo - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nCrit > ATK% > Maitrise élémentaire > Recharge d'énergie \n*Set* : \n:first_place: Réminiscence Nostalgique (4 pièces) \nBriseur de Glace (4 pièces) \n    _ _ \n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Frozen Wilds)* \n:second_place: Attaque de base *(Attaque normale : Tir rapide)* \n:third_place: Déchainement élémentaire *(Prophéties de l'aube)* \n _ _",inline=False)
                em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK%/Recharge d'énergie \n<:Coupe:903641040941088769> Dégats Cryo - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nATK% > Crit > Maitrise élémentaire > Recharge d'énergie \n*Set* : \n:first_place: Briseur de Glace (2 pièces) & Ancien rituel royal (2 pièces) \nAncien Rituel Royal (4 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Prophéties de l'aube)* \n:second_place: Compétence élémentaire *(Frozen Wilds)* \n:third_place: Attaque de base *(Tir rapide)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/903991368358195200/aloi.png")
                await ctx.send(embed=em)
            elif mode=="Baal" or mode=="baal" or mode=="Raiden" or mode=="raiden" or mode=="Shogun" or mode=="shogun" or mode=="Shogun Raiden" or mode=="Shogun raiden" or mode=="shogun Raiden" or mode=="shogun raiden" or mode=="Raiden Shogun" or mode=="Raiden shogun" or mode=="raiden Shogun" or mode=="raiden shogun" or mode=="Ei" or mode=="ei":
                em=discord.Embed(title="Shogun Raiden :",description="*Son Excellence, la toute-puissante Narukami Ogosho, qui a promis au peuple d'Inazuma une éternité immuable.*",color=discord.Color.from_rgb(150, 46, 255))
                em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK%/Recharge d'énergie \n<:Coupe:903641040941088769> Dégats Electro/ATK% - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nCrit > Recharge d'énergie > ATK% > Maitrise élémentaire \n*Set* : \n:first_place: Emblème du Destin Brisé (4 pièces) \nColère du Tonnerre (2 pièces) & Emblème du Destin Brisé (2 pièces) \nColère du Tonnerre (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Art secret : Dogme d'idéal)* \n:second_place: Compétence élémentaire *(Transcendance : Présage funeste)* \n:third_place: Attaque de base *(Prémisse)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/903991378512605194/ei.png")
                await ctx.send(embed=em)
            elif mode=="Yoimiya" or mode=="yoimiya" or mode=="Naganohara" or mode=="naganohara" or mode=="Yoimiya Naganohara" or mode=="yoimiya Naganohara" or mode=="Naganohara Yoimiya" or mode=="naganohara yoimiya" or mode=="Yoimiya naganohara" or mode=="yoimiya naganohara" or mode=="naganohara Yoimiya" or mode=="Naganohara yoimiya":
                em=discord.Embed(title="Naganohara Yoimiya :",description="*Propriétaire des « Feux de Naganohara ». Connue sous le nom de « Reine du festival d'été », elle excelle dans son art de créer des feux d'artifice qui symbolisent les espoirs et les rêves des gens.*",color=discord.Color.from_rgb(255, 33, 33))
                em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Pyro - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats :* \nCrit > ATK% > Maitrise élémentaire > Recharge d'énergie \n*Set :* \n:first_place: Réminiscence Nostalgique (4 pièces) \nÉchos d'une Offrande (4 pièces) \nSorcière des Flammes Ardentes (4 pièces) \nSorcière des flammes (2 pièces) & Rideau du gladiateur (2 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Flambée pyrotechnique)* \n:second_place: Compétence élémentaire *(Danse du feu « Niwabi)* \n:third_place: Déchainement élémentaire *(Saxifrage Ryuukin)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/904508982796881960/yoimiyam.png")
                await ctx.send(embed=em)
            elif mode=="hutao" or mode=="Hutao" or mode=="Hu Tao" or mode=="hu Tao" or mode=="Hu tao" or mode=="hu tao":
                em=discord.Embed(title="Hu Tao :",description="*La 77e directrice du Funérarium Wangsheng, qui redonne un coup de jeune à la gestion des affaires funéraires de Liyue.*",color=discord.Color.from_rgb(255, 33, 33))
                em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> PV% \n<:Coupe:903641040941088769> Dégats Pyro/PV% - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats :* \nCrit > PV% > Maitrise élémentaire \n*Set :* \n:first_place: Sorcière des Flammes Ardentes (4 pièces) \nRéminiscence Nostalgique (4 pièces) \nSorcière des Flammes Ardentes (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Chaperon de la renaissance)* \n:second_place: Déchainement élémentaire *(Apaisement divin)* \n:third_place: Attaque de base *(Lance secrète de Wangsheng)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/905920561178349568/hutao.png")
                await ctx.send(embed=em)
            elif mode=="Tartaglia" or mode=="tartaglia" or mode=="Childe" or mode=="childe" or mode=="Tartagliatelle" or mode=="tartagliatelle" or mode=="Tagliatelle" or mode=="tagliatelle":
                em=discord.Embed(title="Tartaglia :",description="*Le 11e Exécuteur des Fatui, appelé « Tartaglia ». Il s'est fait connaître pour avoir gagné des milliers de combats.*",color=discord.Color.from_rgb(28, 111, 255))
                em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Hydro - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats :* \nCrit > ATK% > Recharge d'énergie > Maitrise élémentaire \n*Set :* \n:first_place: Échos d'une Offrande (4 pièces) \nÂme des profondeurs (4 pièces) \nRéminiscence Nostalgique (4 pièces) \nÂme des profondeurs (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Posture du démon : Marée déchaînée)* \n:second_place: Déchainement élémentaire *(Ravage : Oblitération)* \n:third_place: Attaque de base *(Taille du torrent)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/905925754783674428/childe.png")
                await ctx.send(embed=em)
            elif mode=="Ayaka" or mode=="ayaka" or mode=="Ayaka Kamisato" or mode=="ayaka kamisato" or mode=="Kamisato Ayaka" or mode=="kamisato ayaka" or mode=="Ayaka kamisato" or mode=="ayaka Kamisato" or mode=="kamisato Ayaka" or mode=="Kamisato ayaka":
                em=discord.Embed(title="Kamisato Ayaka :",description="*Fille du Clan Kamisato de la Commission culturelle. Digne et élégante, mais aussi sage et forte.*",color=discord.Color.from_rgb(117, 227, 255))
                em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Cryo - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats :* \nCrit > ATK% > Recharge d'énergie > Maitrise élémentaire \n*Set :* \n:first_place: Briseur de Glace (4 pièces) \nBriseur de Glace (2 pièces) & Rideau du Gladiateur (2 pièces) \nBriseur de Glace (2 pièces) & Ancien Rituel Royal (2 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(École Kamisato : Givre mortel)* \n:second_place: Attaque de base *(École Kamisato - Sveltesse)* \n:third_place: Compétence élémentaire *(École Kamisato : Fleur de glace)*",inline=False)
                em.set_thumbnail(url="https://media.discordapp.net/attachments/900869947050295336/906288536720900116/kamisato.png")
                await ctx.send(embed=em)
            elif mode=="Kazuha" or mode=="kazuha" or mode=="Kaedehara" or mode=="kaedehara" or mode=="Kazuha Kaedehara" or mode=="kazuha kaedehara" or mode=="Kaedehara Kazuha" or mode=="kaedehara kazuha" or mode=="Kazuha kaedehara" or mode=="kazuha Kaedehara" or mode=="kaedehara Kazuha" or mode=="Kaedehara kazuha":
                em=discord.Embed(title="Kaedehara Kazuha :",description="*Un samouraï errant d'Inazuma qui fait actuellement partie de la Flotte du Crux. Une âme douce et insouciante dont le cœur cache de nombreuses blessures.*",color=discord.Color.from_rgb(133, 255, 165))
                em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> Maitrise élémentaire \n<:Coupe:903641040941088769> Dégats Anémo/Maitrise élémentaire - <:Couronne:903641083236458536> Maitrise élémentaire/Taux Crit/Dégats Crit \n*Sub stats :* \nMaitrise élémentaire > Recharge d'énergie > Crit > ATK% \n*Set :* \n:first_place: Ombre de la Verte Chasseuse (4 pièces) \nOmbre de la Verte Chasseuse (2 pièces) & Rideau du Gladiateur (2 pièces) \nOmbre de la Verte Chasseuse (2 pièces) & Bande Vagabonde (2 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Véhémence divine)* \n:second_place: Déchainement élémentaire *(Coupure de mille feuilles)* \n:third_place: Attaque de base *(Escrime de Garyuu)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/906291215320895498/kaedehara.png")
                await ctx.send(embed=em)
            elif mode=="Xiangling" or mode=="xiangling":
                em=discord.Embed(title="Xiangling :",description="*Une célèbre cheffe cuisinière originaire de Liyue, connue pour ses plats épicés.*",color=discord.Color.from_rgb(255, 33, 33))
                em.add_field(name="Main DPS (Physique) :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Physique - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats :* \nCrit > ATK% > Recharge d'énergie\n*Set :* \n:first_place: Flamme Blême (2 pièces) & Chevalerie Ensanglantée(2 pièces) \nChevalerie Ensanglantée (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Cuisine-fu)* \n:second_place: Déchainement élémentaire *(Pyrotation)* \n:third_place: Compétence élémentaire *(Attaque Gooba)* \n _ _",inline=False)
                em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK%/Recharge d'énergie/Maitrise élémentaire \n<:Coupe:903641040941088769> Dégats Pyro - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats :* \nCrit > Maitrise élémentaire > ATK% > Recharge d'énergie \n*Set :* \n:first_place: Emblème du Destin Brisé (4 pièces) \nSorcière des Flammes Ardentes (4 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Pyrotation)* \n:second_place: Compétence élémentaire *(Attaque Gooba)* \n:third_place: Attaque de base *(Cuisine-fu)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/906297559528636426/xiangging.png")
                await ctx.send(embed=em)
            elif mode=="Xiao" or mode=="xiao":
                em=discord.Embed(title="Xiao :",description="*Un des Adeptes de Liyue, aussi connu sous le nom de « Dompteur de démons » et « Général des Yakshas ».*",color=discord.Color.from_rgb(133, 255, 165))
                em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Anemo - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nTaux Crit/Dégats Crit > ATK% > Recharge d'énergie \n*Set* : \n:first_place: Au-delà Cinabrin (4 pièces) \nOmbre de la Verte Chasseuse (2 pièces) & Réminiscence Nostalgique (2 pièces) \nRéminiscence Nostalgique (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Coup de tourbillon)*\n:second_place: Déchainement élémentaire *(Fléau du mal)*\n:third_place: Compétence élémentaire *(Cycle du vent lemniscatique)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/906926813668847626/xiAAo.png")
                await ctx.send(embed=em)
            elif mode=="Xinyan" or mode=="xinyan":
                em=discord.Embed(title="Xinyan :",description="*La seule et unique rockeuse de Liyue. Elle combat les préjugés avec sa musique et ses chansons passionnées.*",color=discord.Color.from_rgb(255, 33, 33))
                em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK%/DEF% \n<:Coupe:903641040941088769> Dégats Physique/ATK% - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats :* \nCrit > ATK% > DEF% > Recharge d'énergie\n*Set :* \n:first_place: Chevalerie Ensanglantée (2 pièces) & Rideau du Gladiateur (2 pièces) \nRideau du Gladiateur (4 pièces) \nChevalerie Ensanglantée (4 pièces) *Avec une C6*\n _ _\n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Danse du feu)* \n:second_place: Déchainement élémentaire *(Riff rebelle)* \n:third_place: Compétence élémentaire *(Jeu fervent)* \n _ _",inline=False)
                em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> DEF%/ATK% \n<:Coupe:903641040941088769> Dégats Physique/DEF%/ATK% - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats :* \nCrit > DEF% > ATK% > Recharge d'énergie \n*Set :* \n:first_place: Chevalerie Ensanglantée (2 pièces) & Ancien Rituel Royal (2 pièces) \nChevalerie Ensanglantée (2 pièces) & Rideau du Gladiateur (2 pièces) \nChevalerie Ensanglantée (2 pièces) & Coquille des Rêves Opulents (2 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Riff rebelle)* \n:second_place: Compétence élémentaire *(Jeu fervent)* \n:third_place: Attaque de base *(Danse du feu)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/906929504071593984/xinnya.png")
                await ctx.send(embed=em)
            elif mode=="Bennett" or mode=="bennett" or mode=="Danger public" or mode=="danger public" or mode=="Danger Public" or mode=="danger Public":
                em=discord.Embed(title="Bennett :",description="*Un jeune aventurier originaire de Mondstadt. Sa gentillesse n'a d'égale que sa guigne.*",color=discord.Color.from_rgb(255, 33, 33))
                em.add_field(name="Support/Healeur :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> Recharge d'énergie \n<:Coupe:903641040941088769> PV% - <:Couronne:903641083236458536> Bonus de Soin/PV% \n*Sub stats :* \nPV > Recharge d'énergie > Crit > Maitrise élémentaire \n*Set :* \n:first_place: Ancien Rituel Royal (4 pièces) \nRideau du Gladiateur (4 pièces) \nAmour Chérie (4 pièces) \nInstructeur (4 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Merveilleux voyage)* \n:second_place: Compétence élémentaire *(Surpassion)* \n:third_place: Attaque de base *(Épée chanceuse)* \n _ _",inline=False)
                em.add_field(name="DPS/Burst DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK%/Recharge d'énergie \n<:Coupe:903641040941088769> Dégats Pyro - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats :* \nCrit > > Recharge d'énergie > ATK% > Maitrise élémentaire \n*Set :* \n:first_place: Sorcière des Flammes Ardentes (4 pièces) *C4 et au dessus* \nRideau du Gladiateur (2 pièces) & Sorcière des Flammes Ardentes (2 pièces) \nParieur (2 pièces) & Sorcière des Flammes Ardentes (2 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Merveilleux voyage)* \n:second_place: Compétence élémentaire *(Surpassion)* \n:third_place: Attaque de base *(Épée chanceuse)*",inline=False)
                em.set_thumbnail(url="https://media.discordapp.net/attachments/900869947050295336/906933400244473897/benny.png")
                await ctx.send(embed=em)
            elif mode=="Yanfei" or mode=="yanfei":
                em=discord.Embed(title="Yanfei :",description="*Une célèbre conseillère juridique du Port de Liyue. Du sang d'Adepte coule dans les veines de cette jeune femme ingénieuse.*",color=discord.Color.from_rgb(255, 33, 33))
                em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Pyro - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats :* \nCrit > ATK% > Maitrise élémentaire > Recharge d'énergie\n*Set :* \n:first_place: Sorcière des Flammes Ardentes (4 pièces) \nSorcière des Flammes Ardentes (2 pièces) & Rideau du Gladiateur (2 pièces) \nSorcière des Flammes Ardentes (2 pièces) & Réminiscence Nostalgique (2 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Sceau embrasé)* \n:second_place: Déchainement élémentaire *(Application des peines)* \n:third_place: Compétence élémentaire *(Pacte des flammes)* \n _ _",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/906940088397733908/yanfhey.png")
                await ctx.send(embed=em)
            elif mode=="Lisa" or mode=="lisa" or mode=="MILF" or mode=="milf":
                em=discord.Embed(title="Lisa :",description="*Une bibliothécaire érudite mais un peu nonchalante. Le plus grand talent diplômé de l'Académie de Sumeru de ces deux derniers siècles.*",color=discord.Color.from_rgb(150, 46, 255))
                em.add_field(name="Support/Burst :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK%/Recharge d'énergie \n<:Coupe:903641040941088769> Dégats Electro - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nCrit > ATK% > Maitrise élémentaire \n*Set* : \n:first_place: Colère du Tonnerre (4 pièces) \nAncien Rituel Royal (4 pièces) \nParieur (2 pièces) & Colère du Tonnerre (2 pièces)\n _ _ \n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Arc fulminant)* \n:second_place: Déchainement élémentaire *(Rose de foudre)* \n:third_place: Attaque de base *(Touche d'éclair)*",inline=False)
                em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK%/Recharge d'énergie \n<:Coupe:903641040941088769> Dégats Electro - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nCrit > ATK% > Maitrise élémentaire \n*Set* : \n:first_place: Colère du Tonnerre (4 pièces) \nDompteur de Foudre (4 pièces) \nParieur (2 pièces) & Colère du Tonnerre (2 pièces)\n _ _ \n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Touche d'éclair)* \n:second_place: Compétence élémentaire *(Arc fulminant)* \n:third_place: Déchainement élémentaire *(Rose de foudre)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/907357757408182373/lisaAAAH.png")
                await ctx.send(embed=em)
            elif mode=="Beidou" or mode=="beidou":
                em=discord.Embed(title="Beidou :",description="*Capitaine de la flotte du Crux, une femme de tête franche et directe.*",color=discord.Color.from_rgb(150, 46, 255))
                em.add_field(name="Main DPS (Physique) :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Physique - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats* : \nCrit > ATK% > Recharge d'énergie > Maitrise élémentaire \n*Set* : \n:first_place: Chevalerie Ensanglantée (2 pièces) & Flamme Blême (2 pièces) \nChevalerie Ensanglantée (2 pièces) & Rideau du Gladiateur (2 pièces)\n _ _ \n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Conquête des mers)* \n:second_place: Compétence élémentaire *(Invocation des marées)* \n:third_place: Déchainement élémentaire *(Brisure d'orage)*",inline=False)
                em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK%/Maitrise élémentaire \n<:Coupe:903641040941088769> Dégats Electro - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats* : \nCrit > ATK% > Maitrise élémentaire > Recharge d'énergie \n*Set* : \n:first_place: Colère du Tonnerre (4 pièces) \nColère du Tonnerre (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Invocation des marées)* \n:second_place: Déchainement élémentaire *(Brisure d'orage)* \n:third_place: Attaque de base *(Conquête des mers)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/907627081423290378/bheydou.png")
                await ctx.send(embed=em)
            elif mode=="Fischl" or mode=="fischl":
                em=discord.Embed(title="Fischl :",description="*Une fille mystérieuse qui se fait appeler « la Princesse du châtiment ». Elle est toujours accompagnée de son fidèle corbeau, Oz.*",color=discord.Color.from_rgb(150, 46, 255))
                em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Electro - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats* : \nCrit > ATK% > Maitrise élémentaire > Recharge d'énergie \n*Set* : \n:first_place: Colère du Tonnerre (2 pièces) & Rideau du Gladiateur (2 pièces) \nDompteur de Foudre (4 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Flèche de culpabilité)* \n:second_place: Compétence élémentaire *(Ailes de surveillance nocturne)* \n:third_place: Déchainement élémentaire *(Incarnation de la nuit)*",inline=False)
                em.add_field(name="Main DPS (Physique) :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Physique - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats* : \nCrit > ATK% > Maitrise élémentaire > Recharge d'énergie \n*Set* : \n:first_place: Échos d'une Offrande (4 pièces) \nFlamme Blême (4 pièces)\nChevalerie Ensanglantée (2 pièces) & Flamme Blême (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Ailes de surveillance nocturne)* \n:second_place: Déchainement élémentaire *(Incarnation de la nuit)* \n:third_place: Attaque de base *(Flèche de culpabilité)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/908494084761600021/Fischeul.png")
                await ctx.send(embed=em)
            elif mode=="Razor" or mode=="razor":
                em=discord.Embed(title="Razor :",description="*Un jeune garçon qui vit sur le Territoire des Loups situé aux environs de Mondstadt, loin de la ville et des foules. Il possède un instinct et une agilité surprenante.*",color=discord.Color.from_rgb(150, 46, 255))
                em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Physique - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nCrit > ATK% > Recharge d'énergie \n*Set* : \n:first_place: Rideau du Gladiateur (4 pièces) \nÉchos d'une Offrande (4 pièces) \nRideau du Gladiateur (2 pièces) & Chevalerie Ensanglantée (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Crocs d'acier)* \n:second_place: Déchainement élémentaire *(Croc d'éclair)* \n:third_place: Compétence élémentaire *(Griffe et tonnerre)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/908496908396412988/Razoir.png")
                await ctx.send(embed=em)
            elif mode=="Keqing" or mode=="keqing":
                em=discord.Embed(title="Keking :",description="*L'Alioth, l'une des Sept Étoiles de Liyue. L'Alioth critique à mots couverts l'idée que Liyue suive à la lettre la parole du Seigneur de la Roche, mais ce dernier apprécie justement ce genre de personnes.*",color=discord.Color.from_rgb(150, 46, 255))
                em.add_field(name="DPS Electro :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Electro/ATK% - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nCrit > ATK% > Maitrise élémentaire \n*Set* : \n:first_place: Échos d'une Offrande (4 pièces) \nColère de Tonnerre (2 pièces) & Rideau du Gladiateur (2 pièces)\nDompteur de Foudre (4 pièces) \nAncien Rituel Royal (2 pièces) & Colère de Tonnerre (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Escrime des nuages)*\n:second_place: Déchainement élémentaire *(Promenade céleste)*\n:third_place: Compétence élémentaire *(Retour des étoiles)*",inline=False)
                em.add_field(name="DPS Physique :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Physique/ATK% - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nCrit > ATK% > Maitrise élémentaire \n*Set* : \n:first_place: Échos d'une Offrande (4 pièces) \nCavalerie Ensanglanté (2 pièces) & Rideau du Gladiateur (2 pièces)\nCavalerie Ensanglanté (4 pièces) \nMétéore Inversé (4 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Escrime des nuages)*\n:second_place: Déchainement élémentaire *(Promenade céleste)*\n:third_place: Compétence élémentaire *(Retour des étoiles)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/908498531239727114/KeKing.png")
                await ctx.send(embed=em)
            elif mode=="Sara" or mode=="sara" or mode=="Kujou" or mode=="kujou" or mode=="kujou sara" or mode=="Kujou Sara" or mode=="sara kujou" or mode=="Sara Kujou" or mode=="Kujou sara" or mode=="Kujou Sara" or mode=="sara Kujou" or mode=="Sara kujou" or mode=="Kujo" or mode=="kujo" or mode=="kujo sara" or mode=="Kujo Sara" or mode=="sara kujo" or mode=="Sara Kujo" or mode=="Kujo sara" or mode=="Kujo Sara" or mode=="sara Kujo" or mode=="Sara kujo":
                em=discord.Embed(title="Kujou Sara :",description="*Une générale de la Commission administrative. Audacieuse, décisive et habile au combat.*",color=discord.Color.from_rgb(150, 46, 255))
                em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> Recharge d'énergie/Maitrise élémentaire \n<:Coupe:903641040941088769> Dégats Electro/Maitrise élémentaire - <:Couronne:903641083236458536> Dégats Crit/Taux Crit/Maitrise élémentaire \n*Sub stats* : \nRecharge d'énergie > Crit > Maitrise élémentaire \n*Set* : \n:first_place: Ancien Rituel Royal (4 pièces) \nColère du Tonnerre (2 pièces) & Ancien Rituel Royal (2 pièces) \nEmblème du Destin Brisé (4 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Soumission : Chemin de lumière)* \n:second_place: Compétence élémentaire *(Tempestrier tengu)* \n:third_place: Attaque de base *(Archerie tengu)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/908500549379457055/kujou.png")
                await ctx.send(embed=em)
            elif mode=="Klee" or mode=="klee" or mode=="Kamikaze" or mode=="kamikaze":
                em=discord.Embed(title="Klee :",description="*Une invitée régulière des cellules de l'Ordre de Favonius, et également la maîtresse des explosions à Mondstadt, où on la surnomme « le soleil fuyant ».*",color=discord.Color.from_rgb(255, 33, 33))
                em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Pyro - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nCrit > ATK% > Maitrise élémentaire \n*Set* : \n:first_place: Sorcière des Flammes Ardentes (2 pièces) & Rideau du Gladiateur (2 pièces)\nBande Vagabonde (4 pièces) \nSorcière des Flammes Ardentes (4 pièces) \nMarcheur du Feu (4 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Attaque normale : Boum ! Boum !)*\n:second_place: Déchainement élémentaire *(Fleur bombardier)*\n:third_place: Compétence élémentaire *(Bombe rebondissante)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/908502878635843665/KLEEEEE.png")
                await ctx.send(embed=em)
            elif mode=="Kaeya" or mode=="kaeya":
                em=discord.Embed(title="Kaeya :",description="*Un épéiste accompli et un stratège de génie de l'Ordre de Favonius ; il est originaire, selon les rumeurs, d'une terre bien au-delà des frontières de Mondstadt.*",color=discord.Color.from_rgb(117, 227, 255))
                em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK%/Recharge d'énergie \n<:Coupe:903641040941088769> Dégats Cryo/ATK% - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats :* \nCrit > ATK% > Recharge d'énergie > Maitrise élémentaire \n*Set :* \n:first_place: Briseur de Glace (2 pièces) & Ancien Rituel Royal (2 pièces) \nAncien Rituel Royal (4 pièces) \nBriseur de Glace (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Valse glaciale)* \n:second_place: Compétence élémentaire *(Attaque givrée)* \n:third_place: Attaque de base *(Passe d'armes)*",inline=False)
                em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Physique/ATK% - <:Couronne:903641083236458536> Dégats Crit/ATK% \n*Sub stats :* \nDégats Crit > ATK% > Maitrise élémentaire > Recharge d'énergie > Taux Crit \n*Set :* \n:first_place: Briseur de Glace (4 pièces) \nChevalerie Ensanglantée (2 pièces) & Rideau du Gladiateur (2 pièces)\nBriseur de Glace (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Valse glaciale)* \n:second_place: Attaque de base *(Passe d'armes)* \n:third_place: Compétence élémentaire *(Attaque givrée)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/908507385763602472/kaeyeuha.png")
                await ctx.send(embed=em)
            elif mode=="Ganyu" or mode=="ganyu" or mode=="cocochèvre" or mode=="Cocochèvre":
                em=discord.Embed(title="Ganyu :",description="*Secrétaire du Pavillon Yuehai ; du sang de Qilin, la créature mythique, coule dans ses veines.*",color=discord.Color.from_rgb(117, 227, 255))
                em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK%/Recharge d'énergie \n<:Coupe:903641040941088769> Dégats Cryo/ATK% - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nCrit > ATK% > Recharge d'énergie > Maitrise élémentaire \n*Set* : \n:first_place: Briseur de glace (2 pièces) & Ancien Rituel Royal (2 pièces)\nAncien Rituel Royal (4 pièces) \nAncien Rituel Royal (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Baptême céleste)*\n:second_place: Compétence élémentaire *(Trace de Qilin)*\n:third_place: Attaque de base *(Archerie Liutian)*",inline=False)
                em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Cryo/ATK% - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nCrit > ATK% > Recharge d'énergie > Maitrise élémentaire \n*Set* : \n:first_place: Bande vagabonde (4 pièces) \nBriseur de glace (2 pièces) & Ancien Rituel Royal (2 pièces) \nAncien Rituel Royal (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Archerie Liutian)*\n:second_place: Déchainement élémentaire *(Baptême céleste)*\n:third_place: Compétence élémentaire *(Trace de Qilin)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/908507370357919774/ganyou.png")
                await ctx.send(embed=em)
            elif mode=="Diona" or mode=="diona":
                em=discord.Embed(title="Diona :",description="*Une jeune fille au sang pas tout à fait humain. Elle travail comme barmaid à La Queue de Chat où elle est très appréciée.*",color=discord.Color.from_rgb(117, 227, 255))
                em.add_field(name="Support :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> Recharge d'énergie \n<:Coupe:903641040941088769> PV%/Dégats Cryo - <:Couronne:903641083236458536> PV%/Bonus de Soin \n*Sub stats :* \nRecharge d'énergie > PV% > ATK% > Crit \n*Set :* \n:first_place: Ancien Rituel Royal (4 pièces) \nInstructeur (4 pièces) \nExilé (4 pièces) \nAmour Chéri (4 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Griffes Cryo)* \n:second_place: Compétence élémentaire *(Cuvée spéciale)* \n:third_place: Attaque de base *(Archerie de chasse)*",inline=False)
                em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Cryo - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats :* \nRecharge d'énergie > Crit > ATK%\n*Set :* \n:first_place: Ancien Rituel Royal (4 pièces) \nInstructeur (4 pièces)\nAncien Rituel Royal (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Griffes Cryo)* \n:second_place: Compétence élémentaire *(Cuvée spéciale)* \n:third_place: Attaque de base *(Archerie de chasse)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/909254867741212742/diano.png")
                await ctx.send(embed=em)
            elif mode=="Chongyun" or mode=="chongyun":
                em=discord.Embed(title="Chongyun :",description="*Le jeune héritier d'une célèbre famille d'exorcistes, qui s'efforce de contrôler l'énergie qui l'habite.*",color=discord.Color.from_rgb(117, 227, 255))
                em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Cryo - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats :* \nCrit > ATK% > Recharge d'énergie > Maitrise élémentaire \n*Set :* \n:first_place: Briseur de Glace (2 pièces) & Ancien Rituel Royal (2 pièces) \nAncien Rituel Royal (4 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Lame de l'esprit : Chute d'étoiles)* \n:second_place: Compétence élémentaire *(Lame de l'esprit : Givre superposé)* \n:third_place: Attaque de base *(Fléau des démons)*",inline=False)
                em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Cryo - <:Couronne:903641083236458536> Dégats Crit/ATK% \n*Sub stats :* \nCrit > ATK% > Recharge d'énergie > Maitrise élémentaire \n*Set :* \n:first_place: Briseur de Glace (2 pièces) & Rideau du Gladiateur (2 pièces) \nRideau du Gladiateur (4 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Fléau des démons)* \n:second_place: Déchainement élémentaire *(Lame de l'esprit : Chute d'étoiles)* \n:third_place: Compétence élémentaire *(Lame de l'esprit : Givre superposé)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/909414199774576650/chongqiu.png")
                await ctx.send(embed=em)
            elif mode=="Rosalia" or mode=="rosalia" or mode=="Rosaria" or mode=="rosaria":
                em=discord.Embed(title="Rosalia :",description="*Une religieuse qui n'en a que l'apparence. Ses paroles sont acérées et son comportement, froid. Elle agit toujours seule.*",color=discord.Color.from_rgb(117, 227, 255))
                em.add_field(name="Main DPS (Physique) :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% - <:Coupe:903641040941088769> Dégats Physique - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats :* \nCrit > ATK% > Recharge d'énergie \n*Set :* \n:first_place: Échos d'une Offrande (4 pièces) \nChevalerie Ensanglantée (4 pièces) \nChevalerie Ensanglantée (2 pièces) & Flamme Blême (2 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Lance expiatoire)* \n:second_place: Déchainement élémentaire *(Sacrement mortel)* \n:third_place: Compétence élémentaire *(Confession des péchés)*",inline=False)
                em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK%/Recharge d'énergie \n<:Coupe:903641040941088769> Dégats Cryo - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats :* \nCrit > ATK% > Recharge d'énergie > Maitrise élémentaire \n*Set :* \n:first_place: Briseur de Glace (2 pièces) & Ancien Rituel Royal (2 pièces) \nBriseur de Glace (4 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Sacrement mortel)* \n:second_place: Compétence élémentaire *(Confession des péchés)* \n:third_place: Attaque de base *(Lance expiatoire)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/909446746491478056/rosaria.png")
                await ctx.send(embed=em)
            elif mode=="Xingqiu" or mode=="xingqiu":
                em=discord.Embed(title="Xingqiu :",description="*Un jeune homme intègre et serviable, que l'on voit souvent dans les librairies. Il porte une longue épée, et poursuit un idéal de justice.*",color=discord.Color.from_rgb(28, 111, 255))
                em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK%/Recharge d'énergie \n<:Coupe:903641040941088769> Dégats Hydro - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats :* \nRecharge d'énergie > Crit > ATK% > Maitrise élémentaire \n*Set :* \n:first_place: Âme des Profondeurs (2 pièces) & Ancien Rituel Royal (2 pièces) \nAncien Rituel Royal (4 pièces) \nAncien Rituel Royal (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Épée Guhua : Pluie et arc-en-ciel)* \n:second_place: Compétence élémentaire *(Épée Guhua : Pluie battante)* \n:third_place: Attaque de base *(Style Guhua)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/909449217720868933/xingyun.png")
                await ctx.send(embed=em)
            elif mode=="Barbara" or mode=="barbara":
                em=discord.Embed(title="Barbara :",description="*Barbara est adulée de tous à Mondstadt. Pourtant, c'est dans un magazine qu'elle a découvert le terme « idole ».*",color=discord.Color.from_rgb(28, 111, 255))
                em.add_field(name="Support/Healeur :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> PV%/Recharge d'énergie \n<:Coupe:903641040941088769> PV% - <:Couronne:903641083236458536> Bonus de Soin/PV% \n*Sub stats :* \nPV% > PV > Recharge d'énergie > Crit \n*Set :* \n:first_place: Palourde Océanique (4 pièces) \nAmour Chéri (4 pièces) \nAmour Chéri (2 pièces) & Tenacité du Millélithe (2 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(C’est parti pour le show ♪)* \n:second_place: Déchainement élémentaire *(Miracle brillant ♪)* \n:third_place: Attaque de base *(Murmure de l’eau)*",inline=False)
                em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Hydro - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats :* \nCrit > ATK% > Maitrise élémentaire \n*Set :* \n:first_place: Âme des Profondeurs (4 pièces) \nÂme des Profondeurs (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Murmure de l’eau)* \n:second_place: Compétence élémentaire *(C’est parti pour le show ♪)* \n:third_place: Déchainement élémentaire *(Miracle brillant ♪)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/909453577771159592/barabara.png")
                await ctx.send(embed=em)
            elif mode=="Jean" or mode=="jean" or mode=="daronne" or mode=="Daronne":
                em=discord.Embed(title="Jean :",description="*Le Chevalier au Pissenlit, loyal et rigoureux, et la Grande Maîtresse suppléante de l'Ordre de Favonius.*",color=discord.Color.from_rgb(133, 255, 165))
                em.add_field(name="Healeur :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Anemo/ATK% - <:Couronne:903641083236458536> ATK%/Maitrise élémentaire \n*Sub stats* : \nATK% > Recharge d'énergie > Maitrise élémentaire > Crit \n*Set* : \n:first_place: Ombre de la Verte Chasseuse (2 pièces) & Rideau du Gladiateur (2 pièces)\nOmbre de la Verte Chasseuse (4 pièces) \nAncien Rituel Royal (4 pièces) \nAmour Chéri (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Brise de pissenlit)* \n:second_place: Compétence élémentaire *(Épée de tourbillon)* \n:third_place: Attaque de base *(Escrime de Favonius)*",inline=False)
                em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Anemo - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nCrit > ATK% > Recharge d'énergie > Maitrise élémentaire \n*Set* : \n:first_place: Ombre de la Verte Chasseuse (2 pièces) & Rideau du Gladiateur (2 pièces) \nRideau du Gladiateur (4 pièces) \nCavalerie Ensanglantée (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Escrime de Favonius)* \n:second_place: Compétence élémentaire *(Épée de tourbillon)* \n:third_place: Déchainement élémentaire *(Brise de pissenlit)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/909453587644559400/jaen.png")
                await ctx.send(embed=em)
            elif mode=="Qiqi" or mode=="qiqi" or mode=="Serial Healer" or mode=="Serial healer" or mode=="serial Healer" or mode=="serial healer":
                em=discord.Embed(title="Qiqi :",description="*Qiqi est une jeune apprentie du Cottage Bubu, en charge notamment de la récolte des herbes médicinales. C'est également un zombie au teint blafard et aux mots comptés.*",color=discord.Color.from_rgb(117, 227, 255))
                em.add_field(name="Healer :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK%/Recharge d'énergie \n<:Coupe:903641040941088769> ATK% - <:Couronne:903641083236458536> ATK%/Bonus de Soin \n*Sub stats* : \nATK% > Recharge d'énergie > ATK > Maitrise élémentaire \n*Set* : \n:first_place: Amour Chéri (2 pièces) & Palourde aux Teintes Océaniques (2 pièces) \nAmour Chéri (4 pièces) \nPalourde aux Teintes Océaniques (4 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Arcane d'Adepte : Talisman sacré)*\n:second_place: Compétence élémentaire *(Arcane d'Adepte : Héraut de givre)*\n:third_place: Attaque de base *(Escrime ancienne des nuages)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/909455858407182366/kiki.png")
                await ctx.send(embed=em)
            elif mode=="Albedo" or mode=="albedo" or mode=="ascenseur" or mode=="Ascenseur" or mode=="Monte-Charge" or mode=="Monte-charge" or mode=="monte-Charge" or mode=="monte-charge" or mode=="Kreideprinz" or mode=="kreideprinz":
                em=discord.Embed(title="Albedo :",description="*Génie connu sous le surnom de « Kreideprinz », Albedo est l'alchimiste en chef et le capitaine des enquêteurs de l'Ordre de Favonius.*",color=discord.Color.from_rgb(255, 197, 89))
                em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> DEF% \n<:Coupe:903641040941088769> Dégats Géo - <:Couronne:903641083236458536> Taux Crit/Dégats Crit/DEF % \n*Sub stats* : \nDEF% > Crit > ATK% > Recharge d'énergie \n*Set* : \n:first_place: Coquille des rêves (4 pièces) \nRoche Ancienne (2 pièces) & Coquille des rêves (2 pièces) \nRoche Ancienne (2 pièces) & Ancien Rituel Royal (2 pièces) \nRoche Ancienne (2 pièces) & Parieur (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Genèse : Aura solaire)* \n:second_place: Déchainement élémentaire *(Transformation : Reflux Géo)* \n:third_place: Attaque de base *(Escrime de Favonius - Blanche)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/909463110857928724/albedoux.png")
                await ctx.send(embed=em)
            elif mode=="Ningguang" or mode=="ningguang":
                em=discord.Embed(title="Ningguang :",description="*La Megrez des Sept Étoiles de Liyue. Peu de personnes peuvent se vanter d'être aussi riches à travers Teyvat.*",color=discord.Color.from_rgb(255, 197, 89))
                em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Géo - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nATK% > Crit > Recharge d'énergie \n*Set* : \n:first_place: Roche Ancienne (2 pièces) & Ancien Rituel Royal (2 pièces) \nRoche Ancienne (2 pièces) & Rideau du Gladiateur (2 pièces) \nEmblème du Destin Brisé (4 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Géo-dispersion)* \n:second_place: Compétence élémentaire *(Paravent d'astrolabe)* \n:third_place: Déchainement élémentaire *(Éclatement des étoiles)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/909465266986024960/ningus.png")
                await ctx.send(embed=em)
            elif mode=="Venti" or mode=="venti" or mode=="barbatos" or mode=="Barbatos" or mode=="trap" or mode=="Trap" or mode=="Barde" or mode=="barde":
                em=discord.Embed(title="Venti :",description="*Un des nombreux bardes de Mondstadt, qui aime à se promener dans tous les recoins de la cité.*",color=discord.Color.from_rgb(133, 255, 165))
                em.add_field(name="Sub DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Anemo - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats* : \nATK% > Taux Crit/Dégats Crit > Maitrise élémentaire \n*Set* : \n:first_place: Ombre de la Verte Chasseuse (4 pièces) \nOmbre de la Verte Chasseuse (2 pièces) & Ancien Rituel Royal (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Ode au vent)*\n:second_place: Compétence élémentaire *(Sonnet des Vents célestes)*\n:third_place: Attaque de base *(Archerie divine)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/910663498881716304/bardatos.png")
                await ctx.send(embed=em)
            elif mode=="Eula" or mode=="eula" or mode=="Noble" or mode=="noble":
                em=discord.Embed(title="Eula :",description="*Le « Chevalier aux Embruns », né de l'ancien Clan Lawrence, capitaine de l'unité de reconnaissance des chevaliers de l'Ordre de Favonius de Mondstadt. Que cette descendante de la noblesse d'antan ait rejoint les chevaliers de l'Ordre, l'ennemi jusqu'alors juré de la famille, demeure un mystère aux yeux de beaucoup.*",color=discord.Color.from_rgb(117, 227, 255))
                em.add_field(name="Main DPS (Physique) :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK%/Recharge d'énergie \n<:Coupe:903641040941088769> Dégats Physique - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats* : \nATK% > Crit > Recharge d'énergie \n*Set* : \n:first_place: Flamme Blême (4 pièces) \nFlamme Blême (2 pièces) & Chevalerie Ensanglantée (2 pièces) \nFlamme Blême (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Escrime de Favonius - Aristocratie)*\n:second_place: Déchainement élémentaire *(Lame de fond)*\n:third_place: Compétence élémentaire *(Vortex des mers glacées)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/910667895179198495/Eeeeuhla.png")
                await ctx.send(embed=em)
            elif mode=="Mona" or mode=="mona":
                em=discord.Embed(title="Mona :",description="*Jeune astromancienne mystérieuse, Mona se surnomme elle-même « la grande astromancienne Mona », et fait preuve d'une force singulière et d'une érudition hors-norme qui ne désavouent pas cette appellation.*",color=discord.Color.from_rgb(28, 111, 255))
                em.add_field(name="Support burst :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Hydro - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats :* \nCrit > ATK% > Recharge d'énergie > Maitrise élémentaire \n*Set :* \n:first_place: Emblème du Destin Brisé (4pièces) \nAncien Rituel Royal (4 pièces) \nÂme des Profondeurs (2 pièces) & Ancien Rituel Royal (2 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Voie divine)* \n:second_place: Compétence élémentaire *(Mirage aqueux)* \n:third_place: Attaque de base *(Ondes du destin)*",inline=False)
                em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Hydro - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats :* \nCrit > ATK% > Recharge d'énergie > Maitrise élémentaire \n*Set :* \n:first_place: Âme des Profondeurs (4 pièces) \nÂme des Profondeurs (2 pièces) & Ancien Rituel Royal (2 pièces) \nÂme des Profondeurs (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Voie divine)* \n:second_place: Attaque de base *(Ondes du destin)* \n:third_place: Compétence élémentaire *(Mirage aqueux)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/910670446972764181/monastres.png")
                await ctx.send(embed=em)
            elif mode=="Noelle" or mode=="noelle":
                em=discord.Embed(title="Noelle :",description="*Une jeune fille travaillant comme servante à l'Ordre de Favonius. Elle a toujours rêvé de devenir un jour chevalier.*",color=discord.Color.from_rgb(255, 197, 89))
                em.add_field(name="Main DPS (C6 recommandée) :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> DEF% \n<:Coupe:903641040941088769> Dégats Géo/DEF% - <:Couronne:903641083236458536> Dégats Crit/Taux Crit/DEF% \n*Sub stats* : \nCrit > DEF% > ATK% > Recharge d'énergie \n*Set* : \n:first_place: Coquille des Rêves Opulents (4 pièces) \nMétéore Inversé (4 pièces) \nCoquille des Rêves Opulents (2 pièces) & Roche Ancienne (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Grand ménage)* \n:second_place: Attaque de base *(Escrime de Favonius - Servante)* \n:third_place: Compétence élémentaire *(Armure de cœur)*",inline=False)
                em.add_field(name="Support bouclier :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> DEF% \n<:Coupe:903641040941088769> DEF% - <:Couronne:903641083236458536> DEF%/Bonus de Soin \n*Sub stats* : \nDEF% > Recharge d'énergie > Crit > ATK% \n*Set* : \n:first_place: Amour Chéri (4 pièces) \nAmour Chéri (2 pièces) & Coquille des Rêves Opulents (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Grand ménage)* \n:second_place: Compétence élémentaire *(Armure de cœur)* \n:third_place: Attaque de base *(Escrime de Favonius - Servante)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/910859902006751272/noel.png")
                await ctx.send(embed=em)
            elif mode=="Zhongli" or mode=="zhongli" or mode=="morax" or mode=="Morax" or mode=="osmanthus wine" or mode=="Osmanthus Wine" or mode=="Omanthus wine" or mode=="osmanthus Wine" or mode=="bangala" or mode=="Bangala":
                em=discord.Embed(title="Zhongli :",description="*Une mystérieuse relation du Funérarium Wangsheng, aux connaissances aussi variées qu'étendues.*",color=discord.Color.from_rgb(255, 197, 89))
                em.add_field(name="Support burst :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> PV% \n<:Coupe:903641040941088769> Dégats Géo - <:Couronne:903641083236458536> Dégats Crit/Taux Crit/PV% \n*Sub stats* : \nPV% > Crit > ATK% > Recharge d'énergie \n*Set* : \n:first_place: Roche Ancienne (2 pièces) & Ancien Rituel Royal (2 pièces) \nRoche Ancienne (2 pièces) & Ténacité du Millelithe (2 pièces) \nRoche Ancienne (2 pièces) & Réminiscence Nostalgique (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Chute de météore)* \n:second_place: Compétence élémentaire *(Dominus Lapidis)* \n:third_place: Attaque de base *(Pluie de pierres)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/910865180215357470/bangalax.png")
                await ctx.send(embed=em)
            elif mode=="Diluc Ragnvindr" or mode=="diluc Ragnvindr" or mode=="Diluc ragnvindr" or mode=="diluc ragnvindr" or mode=="Diluc" or mode=="diluc" or mode=="Le livreur de vin de Venti" or mode=="le livreur de vin de Venti" or mode=="Le livreur de vin de venti" or mode=="le livreur de vin de venti" or mode=="Ragnvindr Diluc" or mode=="Ragnvindr diluc" or mode=="ragnvindr Diluc" or mode=="ragnvindr diluc":
                em=discord.Embed(title="Diluc :",description="*Un jeune noble possédant la plupart des entreprises du vin de Mondstadt ; nul ne saurait sous-estimer sa richesse, sa réputation et ses capacités.*",color=discord.Color.from_rgb(255, 33, 33))
                em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Pyro - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nCrit > ATK% > Maitrise élémentaire \n*Set* : \nSorcière des Flammes Ardentes (4 pièces) \n:first_place: Sorcière des Flammes Ardentes (2 pièces) & Rideau du Gladiateur (2 pièces) \nSorcière des Flammes Ardentes (2 pièces) & Ancien Rituel Royal (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Assaut brûlant)* \n:second_place: Déchainement élémentaire *(Aurore)* \n:third_place: Attaque de base *(Épée trempée)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/910950983885029426/dilouc.png")
                await ctx.send(embed=em)
            elif mode=="Thomas" or mode=="thomas" or mode=="Thoma" or mode=="thoma" or mode=="Maid" or mode=="maid":
                em=discord.Embed(title="Thomas :",description="*L'employé de maison du Clan Kamisato. Un « négociateur » bien connu à Inazuma.*",color=discord.Color.from_rgb(255, 33, 33))
                em.add_field(name="Support/Shield :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> PV% \n<:Coupe:903641040941088769> Dégats Pyro/PV% - <:Couronne:903641083236458536> PV%/Dégats Crit/Taux Crit \n*Sub stats* : \nPV% > Recharge d'énergie > Crit > Maitrise élémentaire \n*Set* : \n:first_place: Sorcière des Flammes Ardentes (2 pièces) & Ténacité du Millelithe (2 pièces) \nSorcière des Flammes Ardentes (2 pièces) & Ancien Rituel Royal (2 pièces) \nSorcière des Flammes Ardentes (2 pièces) & Emblême du Destin Brisé (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(O-yoroi écarlate)* \n:second_place: Compétence élémentaire *(Bénédiction flamboyante)* \n:third_place: Attaque de base *(Lance célère)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/910965255432175657/thoma.png")
                await ctx.send(embed=em)
            elif mode=="Traveler" or mode=="traveler" or mode=="Aether" or mode=="aether" or mode=="Lumine" or mode=="lumine":
                em=discord.Embed(title="Traveler :",description="*Un voyageur/Une voyageuse venant d'un autre monde qui a été séparé.e de sa sœur/son frère. Il/Elle débute son périple à la recherche des Sept Archons dans l'espoir de la/le retrouver..*",color=discord.Color.from_rgb(230, 230, 255))
                em.add_field(name="Merci de préciser la recherche :",value="Plutôt le build de ``Traveler Anémo``, ``Traveler Géo`` ou ``Traveler Électro`` ?",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/910957273612947456/traveler.png")
                await ctx.send(embed=em)
            elif mode=="Traveler anemo" or mode=="traveler anemo" or mode=="Traveler Anemo" or mode=="traveler Anemo" or mode=="Aether anemo" or mode=="aether anemo" or mode=="Aether Anemo" or mode=="aether Anemo" or mode=="Lumine anemo" or mode=="lumine anemo" or mode=="Lumine Anemo" or mode=="lumine Anemo" or mode=="Traveler anémo" or mode=="traveler anémo" or mode=="Traveler Anémo" or mode=="traveler Anémo" or mode=="Aether anémo" or mode=="aether anémo" or mode=="Aether Anémo" or mode=="aether Anémo" or mode=="Lumine anémo" or mode=="lumine anémo" or mode=="Lumine Anémo" or mode=="lumine Anémo":
                em=discord.Embed(title="Traveler (Anémo) :",description="*Un voyageur/Une voyageuse venant d'un autre monde qui a été séparé.e de sa sœur/son frère. Il/Elle débute son périple à la recherche des Sept Archons dans l'espoir de la/le retrouver.*",color=discord.Color.from_rgb(133, 255, 165))
                em.add_field(name="Main DPS (Anémo) :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Anémo/ATK% - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats* : \nCrit > ATK% > Maitrise élémentaire \n*Set* : \n:first_place: Ombre de la Verte Chasseuse (4 pièces) \nOmbre de la Verte Chasseuse (2 pièces) & Ancien Rituel Royal (2 pièces) \nOmbre de la Verte Chasseuse (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Vents étrangers)* \n:second_place: Compétence élémentaire *(Épée de vortex)* \n:third_place: Déchainement élémentaire *(Rafale de vent)*",inline=False)
                em.add_field(name="Main DPS (Anémo) :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Anémo/ATK% - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats* : \nCrit > ATK% > Maitrise élémentaire \n*Set* : \n:first_place: Ombre de la Verte Chasseuse (4 pièces) \nOmbre de la Verte Chasseuse (2 pièces) & Ancien Rituel Royal (2 pièces) \nOmbre de la Verte Chasseuse (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Rafale de vent)* \n:second_place: Compétence élémentaire *(Épée de vortex)* \n:third_place: Attaque de base *(Vents étrangers)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/910957273612947456/traveler.png")
                await ctx.send(embed=em)
            elif mode=="Traveler électro" or mode=="traveler électro" or mode=="Traveler Électro" or mode=="traveler Électro" or mode=="Aether électro" or mode=="aether électro" or mode=="Aether Électro" or mode=="aether Électro" or mode=="Lumine électro" or mode=="lumine électro" or mode=="Lumine Électro" or mode=="lumine Électro" or mode=="Traveler electro" or mode=="traveler electro" or mode=="Traveler Electro" or mode=="traveler Electro" or mode=="Aether electro" or mode=="aether electro" or mode=="Aether Electro" or mode=="aether Electro" or mode=="Lumine electro" or mode=="lumine electro" or mode=="Lumine Electro" or mode=="lumine Electro":
                em=discord.Embed(title="Traveler (Électro) :",description="*Un voyageur/Une voyageuse venant d'un autre monde qui a été séparé.e de sa sœur/son frère. Il/Elle débute son périple à la recherche des Sept Archons dans l'espoir de la/le retrouver.*",color=discord.Color.from_rgb(150, 46, 255))
                em.add_field(name="Support DPS (Électro) :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> Recharge d'énergie/ATK% \n<:Coupe:903641040941088769> Dégats Électro - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats* : \nRecharge d'énergie > Crit > ATK% > Maitrise élémentaire \n*Set* : \n:first_place: Colère du Tonnerre (2 pièces) & Ancien Rituel Royal (2 pièces) \nColère du Tonnerre (4 pièces) \nAncien Rituel Royal (2 pièces) & Emblême du Destin Brisé (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Tonnerre hurlant)* \n:second_place: Compétence élémentaire *(Lame d'éclair)* \n:third_place: Attaque de base *(Tonnerre venu d'ailleurs)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/910957273612947456/traveler.png")
                await ctx.send(embed=em)
            elif mode=="Traveler géo" or mode=="traveler géo" or mode=="Traveler Géo" or mode=="traveler Géo" or mode=="Aether géo" or mode=="aether géo" or mode=="Aether Géo" or mode=="aether Géo" or mode=="Lumine géo" or mode=="lumine géo" or mode=="Lumine Géo" or mode=="lumine Géo" or mode=="Traveler geo" or mode=="traveler geo" or mode=="Traveler Geo" or mode=="traveler Geo" or mode=="Aether geo" or mode=="aether geo" or mode=="Aether Geo" or mode=="aether Geo" or mode=="Lumine geo" or mode=="lumine geo" or mode=="Lumine Geo" or mode=="lumine Geo":
                em=discord.Embed(title="Traveler (Géo) :",description="*Un voyageur/Une voyageuse venant d'un autre monde qui a été séparé.e de sa sœur/son frère. Il/Elle débute son périple à la recherche des Sept Archons dans l'espoir de la/le retrouver.*",color=discord.Color.from_rgb(255, 197, 89))
                em.add_field(name="Main DPS (Géo) :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Géo - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nCrit > ATK% > Recharge d'énergie \n*Set* : \n:first_place: Rideau du Gladiateur (4 pièces) \nRideau du Gladiateur (2 pièces) & Ancien Rituel Royal (2 pièces) \nRideau du Gladiateur (2 pièces) & Ténacité du Millelithe (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Épée d'étoile déchue)* \n:second_place: Déchainement élémentaire *(Réveil de la terre)* \n:third_place: Attaque de base *(Lame de roche)*",inline=False)
                em.add_field(name="Sub DPS (Géo) :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Géo - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nCrit > ATK% > Recharge d'énergie \n*Set* : \n:first_place: Ténacité du Millelithe (2 pièces) & Ancien Rituel Royal (2 pièces) \nTénacité du Millelithe (4 pièces) \nAncien Rituel Royal (4 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Épée d'étoile déchue)* \n:second_place: Déchainement élémentaire *(Réveil de la terre)* \n:third_place: Attaque de base *(Lame de roche)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/910957273612947456/traveler.png")
                await ctx.send(embed=em)
            elif mode=="Goro" or mode=="goro" or mode=="gorou" or mode=="Gorou" or mode=="toutou" or mode=="Toutou" or mode=="bon toutou" or mode=="Bon toutou" or mode=="Bon Toutou" or mode=="bon Toutou":
                em=discord.Embed(title="Gorou :",description="*Le grand général des forces de l'Île de Watatsumi, en qui ses subordonnés ont profondément confiance.*",color=discord.Color.from_rgb(255, 197, 89))
                em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> DEF% \n<:Coupe:903641040941088769> Dégats Géo - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats* : \nDEF% > Recharge d'énergie > Crit > ATK% \n*Set* : \n:first_place: Coquille des Rêves Opulents (4 pièces) \nEmblème du Destin Brisé (4 pièces) \nCoquille des Rêves Opulents (2 pièces) & Roche Ancienne (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Défense intégrale d'Inuzaka)* \n:second_place: Déchainement élémentaire *(Crocs bestiaux : Vers la victoire)* \n:third_place: Attaque de base *(Empenne aux crocs acérés)*",inline=False)
                em.set_thumbnail(url="https://media.discordapp.net/attachments/900869947050295336/930595563072806952/gorou.png")
                await ctx.send(embed=em)
            elif mode=="Itto" or mode=="itto" or mode=="Arataki" or mode=="arataki" or mode=="Itto Arataki" or mode=="itto arataki" or mode=="itto Arataki" or mode=="Itto arataki" or mode=="Arataki Itto" or mode=="arataki itto" or mode=="Arataki itto" or mode=="arataki Itto" or mode=="chômeur" or mode=="Chômeur" or mode=="chomeur" or mode=="Chomeur":
                em=discord.Embed(title="Arataki Itto :",description="*Le premier et plus grand chef du gang Arataki, célèbre dans tout Hanamizaka, à la Cité d'Inazuma... Hein, quoi ? Jamais entendu parler d'eux ? Sérieux ?*",color=discord.Color.from_rgb(255, 197, 89))
                em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> DEF% \n<:Coupe:903641040941088769> Dégats Géo/DEF% - <:Couronne:903641083236458536> Dégats Crit/Taux Crit/DEF% \n*Sub stats* : \nCrit > DEF% > ATK% > Recharge d'énergie \n*Set* : \n:first_place: Coquille des Rêves Opulents (4 pièces) \nMétéore Inversé (4 pièces) \nCoquille des Rêves Opulents (2 pièces) & Roche Ancienne (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Légende de la baston)* \n:second_place: Déchainement élémentaire *(Roi oni maléfique : Avènement d'Itto)* \n:third_place: Compétence élémentaire *(Zetsugi anti-démon : Catapultage d'akaushi)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/930593180758462554/itto.png")
                await ctx.send(embed=em)
            elif mode=="Yunjin" or mode=="yunjin" or mode=="Yun Jin" or mode=="yun jin" or mode=="Yun jin" or mode=="yun Jin" or mode=="maître yun" or mode=="Maître Yun" or mode=="maître Yun" or mode=="Maître yun" or mode=="maitre yun" or mode=="Maitre Yun" or mode=="maitre Yun" or mode=="Maitre yun":
                em=discord.Embed(title="Yun Jin :",description="*Une talentueuse chanteuse d'opéra et une dramaturge très célèbre à Liyue. Son style unique, doux et élégant, lui ressemble beaucoup.*",color=discord.Color.from_rgb(255, 197, 89))
                em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> DEF% \n<:Coupe:903641040941088769> DEF%/Dégats Géo - <:Couronne:903641083236458536> DEF% \n*Sub stats* : \nDEF% > Crit > ATK% > Recharge d'énergie \n*Set* : \n:first_place: Coquille des Rêves Opulents (4 pièces) \nEmblème du Destin Brisé (2 pièces) & Coquille des Rêves Opulents (2 pièces) \nCoquille des Rêves Opulents (2 pièces) & Roche Ancienne (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Bannière de rupture des falaises)* \n:second_place: Compétence élémentaire *(Épanouissement ouvert)* \n:third_place: Attaque de base *(Caresse des nuages)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/930595586753843270/yunyun.png")
                await ctx.send(embed=em)
            elif mode=="Shenhe" or mode=="shenhe":
                em=discord.Embed(title="Shenhe :",description="*Une disciple d'Adepte avec un air des plus inhabituels. Après avoir passé beaucoup de temps à s'instruire en isolement dans les montagnes de Liyue, elle est devenue tout aussi froide et distante que les Adeptes eux-mêmes.*",color=discord.Color.from_rgb(117, 227, 255))
                em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK%/Recharge d'énergie \n<:Coupe:903641040941088769> ATK% - <:Couronne:903641083236458536> ATK% \n*Sub stats :* \nATK% > Recharge d'énergie > Crit \n*Set :* \n:first_place: Rideau du Gladiateur (2 pièces) & Réminiscence Nostalgique (2 pièces) \nRideau du Gladiateur (2 pièces) & Emblème du Destin Brisé (2 pièces) \nAncien Rituel Royal (4 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Invocation d'esprit printanier)* \n:second_place: Déchainement élémentaire *(Délivrance de la demoiselle divine)* \n:third_place: Attaque de base *(Percée des étoiles)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/930595579724185650/sheeshhe.png")
                await ctx.send(embed=em)
            elif mode=="Yae" or mode=="Yae miko" or mode=="yae" or mode=="yae miko" or mode=="Yae Miko" or mode=="yae Miko" or mode=="sadique#1":
                em=discord.Embed(title="Yae Miko :",description="*La Guuji Yae du Sanctuaire de Narukami est également responsable éditoriale de la chambre Yae. Une intelligence et une ruse inimaginable sont cachées sous son apparence gracieuse.*",color=discord.Color.from_rgb(150, 46, 255)) 
                em.add_field(name="Sub DPS/Burst DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK%/Recharge d'énergie \n<:Coupe:903641040941088769> Dégats Électro  - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nCrit > Recharge d'énergie > ATK% > Maîtrise Élémentaire \n*Set* : \n:first_place: Colère du Tonnerre (2 pièces) & Emblème du Destin Brisé (2 pièces) \nEmblème du Destin Brisé (4 pièces) \nColère du Tonnerre (2 pièces) & Rideau du Gladiateur (2 pièces) \n_ _ \n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Évocation des yakan : Sakura Dévastateur)*  \n:second_place: Déchainement élémentaire *(Technique Secrète : Incarnation de tenko)* \n:third_place: Attaque de base *(Vulpes Mangeur de Péchés)* \n _ _",inline=False)
                em.set_thumbnail(url="https://media.discordapp.net/attachments/900869947050295336/959145106634604564/yae.png")
                await ctx.send(embed=em)
            elif mode=="Kamisato Ayato" or mode=="Ayato" or mode=="ayato" or mode=="kamisato ayato" or mode=="Kamisato ayato" or mode=="kamisato Ayato" or mode=="ayato kamisato" or mode=="Ayato kamisato" or mode=="ayato Kamisato" or mode=="Ayato Kamisato":
                em=discord.Embed(title="Kamisato Ayato :",description="*Le jeune, mais néanmoins très talenteux, chef du Clan Kamisato de la Commission culturelle. Cultivé et poli, c'est un homme aux multiples facettes.*",color=discord.Color.from_rgb(28, 111, 255))
                em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Hydro - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats* : \nCrit > Recharge d'énergie > ATK% > PV% \n*Set* : \n:first_place: Échos d'une Offrande (4 pièces) \nÂme des Profondeurs (4 pièces) \nRideau du Gladiateur (4 pièces) \n_ _ \n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(École Kamisato : Beauté réfléchie)*  \n:second_place: Déchainement élémentaire *(École Kamisato : Jardin d'eau)* \n:third_place: Attaque de base *(École Kamisato : Transition)* \n _ _",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/985683405922500679/ayato.png")
                await ctx.send(embed=em)
            elif mode=="Yelan" or mode=="yelan" or mode=="milf ultra méta":
                em=discord.Embed(title="Yelan :",description="*Une mystérieuse personne qui prétend travailler pour le bureau des affaires civiles. Cependant, elle n'apparait nulle part dans leur registre.*",color=discord.Color.from_rgb(28, 111, 255))
                em.add_field(name="Sub DPS/Burst DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> PV%/Recharge d'énergie \n<:Coupe:903641040941088769> Dégats Hydro - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats* : \nRecharge d'énergie > Crit > PV% \n*Set* : \n:first_place: Emblème du Destin Brisé (4 pièces) \nÂme des Profondeurs (2 pièces) & Ténacité du Millelithe (2 pièces) \nAncien Rituel Royal (4 pièces) \n_ _ \n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Dé exquis des profondeurs)*  \n:second_place: Compétence élémentaire *(Ligne vitale persistante)* \n:third_place: Attaque de base *(Sagette furtive)* \n _ _",inline=False)
                em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> PV% \n<:Coupe:903641040941088769> Dégats Hydro  - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nCrit > PV% > Recharge d'énergie \n*Set* : \n:first_place: Âme des Profondeurs (2 pièces) & Ténacité du Millelithe (2 pièces) \nEmblème du Destin Brisé (4 pièces) \nAncien Rituel Royal (4 pièces)  \n_ _ \n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Ligne vitale persistante)*  \n:second_place: Déchainement élémentaire *(Dé exquis des profondeurs)* \n:third_place: Attaque de base *(Sagette furtive)* \n _ _",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/985682454369161236/yelan.png")
            elif mode=="Trombone" or mode=="trombone" or mode=="Trombonethefirst" or mode=="trombonethefirst" or mode=="TromboneThefirst" or mode=="tromboneThefirst" or mode=="trombonethe1st" or mode=="Trombonethe1st" or mode=="tromboneThe1st" or mode=="TromboneThe1st" or mode=="Trombone the first" or mode=="trombone the first" or mode=="Trombone The first" or mode=="tromboneThefirst" or mode=="trombone the 1st" or mode=="Trombone the 1st" or mode=="trombone The 1st" or mode=="Trombone The 1st" or mode=="Trombottom" or mode=="trombottom":
                em=discord.Embed(title="Trombonethe1st :",description="*Limule à la base c’est un homme de 30 ans. Bonjoir Je sais pas pourquoi mais abonne toi, c’était pas un ordre mais une menace.*",color=discord.Color.from_rgb(28, 111, 255))
                em.add_field(name="Sub DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> Recharge d'énergie - <:Coupe:903641040941088769> Dégats Limule - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nCrit > ATK% > Maitrise élémentaire \n*Set* : \n:first_place: Sorcière des Flammes Ardentes (4 pièces) \nJoie de ViviThe1st (2 pièces) & Crie du JoJo Fan Extremiste (2 pièces) \nPouvoir des Figurine Limule (2 pièces) & Ancien Rituel des Lunettes (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Crie très fort)* \n:second_place: Déchainement élémentaire *(JOOJOOOOOOOO)* \n:third_place: Attaque de base *(Tape avec un body pillow Vivi)*",inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/910952396954427403/trombagar.png")
                await ctx.send(embed=em)
            else:
                em=discord.Embed(title="Il va falloir un peu patienter ...",description="Ce personnage est soit inexistant, soit non-jouable pour le moment, soit non renseigné dans la commande pour l'instant ... \n _ _\nIl va falloir prendre son mal en patience ...",color=discord.Color.from_rgb(255, 156, 199))
                await ctx.send(embed=em)
    else:
        if mode=="normal":
            em=discord.Embed(title="De quel personnage veux-tu voir le build ?",description="Indique le nom du personnage dont tu veux voir le build !",color=discord.Color.from_rgb(17, 66, 156))
            em.add_field(name="Liste des personnages 4 étoiles :",value="_ _\n**Anémo** : ``Sucrose`` - ``Sayu`` \n _ _\n _ _\n**Pyro** : ``Amber`` - ``Xiangling`` - ``Xinyan`` - ``Bennett`` - ``Yanfei`` - ``Thomas`` \n _ _\n**Electro** : ``Lisa`` - ``Beidou`` - ``Fischl`` - ``Razor`` - ``Kujou Sara`` \n _ _\n**Cryo** : ``Kaeya`` - ``Diona`` - ``Chongyun`` - ``Rosalia`` \n _ _\n**Hydro** : ``Barbara`` - ``Xingqiu`` \n _ _\n _ _ \n**Géo** : ``Noelle`` - ``Ningguang`` - ``Gorou`` - ``Yun Jin``")
            em.add_field(name="Liste des personnages 5 étoiles :",value="_ _\n**Anémo** : ``Jean`` - ``Xiao`` - ``Venti`` - ``Kaedehara Kazuha`` \n _ _\n**Pyro** : ``Diluc`` - ``Klee`` - ``Hu Tao`` - ``Yoimiya``\n _ _\n _ _\n**Electro** : ``Keqing`` - ``Shogun Raiden`` - ``Yae Miko`` \n _ _\n**Cryo** : ``Qiqi`` - ``Ganyu`` - ``Eula`` - ``Kamisato Ayaka`` - ``Shenhe`` - ``Aloy`` \n _ _\n**Hydro** : ``Mona`` - ``Tartaglia`` - ``Sangonomiya Kokomi`` - ``Kamisato Ayato`` - ``Yelan`` \n _ _\n**Géo** : ``Zhongli`` - ``Albedo`` - ``Arataki Itto`` \n _ _\n**Autre** : ``Traveler``")
            em.add_field(name="Liste des personnages à venir :",value="``Shikanoin Heizou`` - ``Kuki Shinobu``")
            em.set_image(url="https://media.discordapp.net/attachments/792879261920919593/903050199151300608/E4TdHllXIAA1bM-.png?width=1074&height=671")
            em.set_footer(text="Les builds présentés sont là uniquement pour donner une idée, ils ne sont pas les seuls builds possibles à faire. Vous êtes tout à fait en droit de préférer d'autres alternatives.")
            await ctx.send(embed=em)
        elif mode=="Kamisato" or mode=="kamisato":
            await ctx.send("Tu veux bien préciser lequel des deux, s'te plaît ? \nHistoire que je sache quoi te répondre ...")
        elif mode=="Surcose" or mode=="sucrose":
            em=discord.Embed(title="Sucrose :",description="*Une alchimiste très curieuse du monde qui l'entoure. Elle se spécialise dans la bio-alchimie.*",color=discord.Color.from_rgb(133, 255, 165))
            em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> Maitrise Élémentaire/Recharge d'énergie \n<:Coupe:903641040941088769> Maitrise Élémentaire - <:Couronne:903641083236458536> Maitrise Élémentaire \n*Sub stats* : \nMaitrise Élémentaire > Recharge d'énergie > Crit > ATK% \n*Set* : \n:first_place: Ombre de la Verte Chasseuse (4 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Sujet 6308)* \n:second_place: Déchainement élémentaire *(Isomorphe 75 Type II)* \n:third_place: Attaque de base *(Esprit du Vent)* \n _ _",inline=False)
            em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK%/Maitrise Élémentaire \n<:Coupe:903641040941088769> Dégats Anémo - <:Couronne:903641083236458536> Dgt Crit/Taux Crit \n*Sub stats* : \nCrit > Maitrise Élémentaire > ATK% > Recharge d'énergie \n*Set* : \n:first_place: Ombre de la Verte Chasseuse (4 pièces) \nOmbre de la Verte Chasseuse (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Esprit du Vent)* \n:second_place: Compétence élémentaire *(Sujet 6308)* \n:third_place: Déchainement élémentaire *(Isomorphe 75 Type II)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/903062307247124490/Sucroz.png")
            await ctx.send(embed=em)
        elif mode=="Sayu" or mode=="sayu":
            em=discord.Embed(title="Sayu :",description="*Une très petite ninja rattachée au Shuumatsuban, qui semble toujours manquer de sommeil.*",color=discord.Color.from_rgb(133, 255, 165))
            em.add_field(name="Support/Healeur :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK%/Maitrise Élémentaire \n<:Coupe:903641040941088769> ATK%/Maitrise Élémentaire - <:Couronne:903641083236458536> Bonus de Soin/ATK%/Maitrise Élémentaire \n*Sub stats* : \nATK% > Maitrise Élémentaire > Recharge d'énergie \n*Set* : \n:first_place: Ombre de la Verte Chasseuse (4 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(École Yoohoo : Folie du ninja)* \n:second_place: Compétence élémentaire *(École Yoohoo : Bond Fuuin)* \n:third_place: Attaque de base *(Lame Shiyuumatsu-Ban)* \n _ _",inline=False)
            em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> Maitrise Élémentaire \n<:Coupe:903641040941088769> Dégats Anémo/Maitrise Élémentaire - <:Couronne:903641083236458536> Dgt Crit/Taux Crit/Maitrise Élémentaire \n*Sub stats* : \nMaitrise Élémentaire > ATK% > Crit > Recharge d'énergie \n*Set* : \n:first_place: Ombre de la Verte Chasseuse (4 pièces) \nOmbre de la Verte Chasseuse (2 pièces) & Bande Vagabonde (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(École Yoohoo : Folie du ninja)* \n:second_place: Compétence élémentaire *(École Yoohoo : Bond Fuuin)* \n:third_place: Attaque de base *(Lame Shiyuumatsu-Ban)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/903964302510293032/sayou.png")
            await ctx.send(embed=em)
        elif mode=="Amber" or mode=="amber":
            em=discord.Embed(title="Amber :",description="*Une jeune fille pleine d'énergie. Elle est la seule et unique Éclaireuse de l'Ordre de Favonius.*",color=discord.Color.from_rgb(255, 33, 33))
            em.add_field(name="Support/Burst :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Pyro/ATK% - <:Couronne:903641083236458536> Dgt Crit/Taux Crit \n*Sub stats* : \nCrit > ATK% > Maitrise Élémentaire \n*Set* : \n:first_place: Ancien Rituel Royal (4 pièces) \nSorcière des Flammes Ardentes (2 pièces) & Ancien Rituel Royal (2 pièces) \nSorcière des Flammes Ardentes (2 pièces) & Rideau du Gladiateur (2 pièces) \n_ _ \n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Pluie de Flèches)* \n:second_place: Compétence élémentaire *(Baron Lapinou)* \n:third_place: Attaque de base *(Archerie Revisitée)* \n _ _",inline=False)
            em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Pyro/ATK% - <:Couronne:903641083236458536> Dgt Crit/Taux Crit \n*Sub stats* : \nCrit > ATK% > Maitrise Élémentaire \n*Set* : \n:first_place: Bande Vagabonde (4 pièces) \nSorcière des Flammes Ardentes (2 pièces) & Rideau du Gladiateur (2 pièces) \nSorcière des Flammes Ardentes (2 pièces) & Ancien Rituel Royal (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Archerie Revisitée)* \n:second_place: Déchainement élémentaire *(Pluie de Flèches)* \n:third_place: Compétence élémentaire *(Baron Lapinou)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/903967766573355048/ambeer.png")
            await ctx.send(embed=em)
        elif mode=="Kokomi" or mode=="kokomi" or mode=="Sangonomiya Kokomi" or mode=="sangonomiya kokomi" or mode=="Sangonomiya kokomi" or mode=="Sangonomiya" or mode=="sangonomiya Kokomi" or mode=="sangonomiya" or mode=="Kokomi Sangonomiya" or mode=="Kokomi sangonomiya" or mode=="kokomi Sangonomiya" or mode=="kokomi sangonomiya":
            em=discord.Embed(title="Sangonomiya Kokomi :",description="*La Prêtresse divine de l'Île de Watatsumi, une jeune femme gérant toutes les affaires de l'île.*",color=discord.Color.from_rgb(28, 111, 255))
            em.add_field(name="DPS/Healeur :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> PV% \n<:Coupe:903641040941088769> Dégats Hydro - <:Couronne:903641083236458536> Bonus de Soin/PV% \n*Sub stats* : \nPV% > ATK% > Recharge d'énergie \n*Set* : \n:first_place: Palourde aux Teintes Océaniques (4 pièces) \nÂme des Profondeurs (4 pièces) \nÂme des Profondeurs (2 pièces) & Amour Chéri (2 pièces) \n    _ _ \n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Ascension de la néréide)* \n:second_place: Compétence élémentaire *(Serment de Kurage)* \n:third_place: Attaque de base *(Forme de l'eau)* \n _ _",inline=False)
            em.add_field(name="Support/Healeur :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> PV% \n<:Coupe:903641040941088769> Dégats Hydro/PV% - <:Couronne:903641083236458536> Bonus de Soin/PV% \n*Sub stats* : \nPV% > Recharge d'énergie > ATK% \n*Set* : \n:first_place: Amour Chéri (2 pièces) & Palourde aux Teintes Océaniques (2 pièces) \nAmour Chéri (2 pièces) & Tenacité du Millelithe (2 pièces) \nPalourde aux Teintes Océaniques (2 pièces) & Tenacité du Millelithe (2 pièces) \nAmour Chéri (4 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Serment de Kurage)* \n:second_place: Déchainement élémentaire *(Ascension de la néréide)* \n:third_place: Attaque de base *(Forme de l'eau)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/903991388977385472/sangonomiya.png")
            await ctx.send(embed=em)
        elif mode=="Aloy" or mode=="aloy":
            em=discord.Embed(title="Aloy :",description="*Autrefois une paria, maintenant une chasseuse d'une acuité sans précédent. Toujours prête à utiliser son arc pour la bonne cause.*",color=discord.Color.from_rgb(117, 227, 255))
            em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Cryo - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nCrit > ATK% > Maitrise élémentaire > Recharge d'énergie \n*Set* : \n:first_place: Réminiscence Nostalgique (4 pièces) \nBriseur de Glace (4 pièces) \n    _ _ \n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Frozen Wilds)* \n:second_place: Attaque de base *(Attaque normale : Tir rapide)* \n:third_place: Déchainement élémentaire *(Prophéties de l'aube)* \n _ _",inline=False)
            em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK%/Recharge d'énergie \n<:Coupe:903641040941088769> Dégats Cryo - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nATK% > Crit > Maitrise élémentaire > Recharge d'énergie \n*Set* : \n:first_place: Briseur de Glace (2 pièces) & Ancien rituel royal (2 pièces) \nAncien Rituel Royal (4 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Prophéties de l'aube)* \n:second_place: Compétence élémentaire *(Frozen Wilds)* \n:third_place: Attaque de base *(Tir rapide)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/903991368358195200/aloi.png")
            await ctx.send(embed=em)
        elif mode=="Baal" or mode=="baal" or mode=="Raiden" or mode=="raiden" or mode=="Shogun" or mode=="shogun" or mode=="Shogun Raiden" or mode=="Shogun raiden" or mode=="shogun Raiden" or mode=="shogun raiden" or mode=="Raiden Shogun" or mode=="Raiden shogun" or mode=="raiden Shogun" or mode=="raiden shogun" or mode=="Ei" or mode=="ei":
            em=discord.Embed(title="Shogun Raiden :",description="*Son Excellence, la toute-puissante Narukami Ogosho, qui a promis au peuple d'Inazuma une éternité immuable.*",color=discord.Color.from_rgb(150, 46, 255))
            em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK%/Recharge d'énergie \n<:Coupe:903641040941088769> Dégats Electro/ATK% - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nCrit > Recharge d'énergie > ATK% > Maitrise élémentaire \n*Set* : \n:first_place: Emblème du Destin Brisé (4 pièces) \nColère du Tonnerre (2 pièces) & Emblème du Destin Brisé (2 pièces) \nColère du Tonnerre (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Art secret : Dogme d'idéal)* \n:second_place: Compétence élémentaire *(Transcendance : Présage funeste)* \n:third_place: Attaque de base *(Prémisse)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/903991378512605194/ei.png")
            await ctx.send(embed=em)
        elif mode=="Yoimiya" or mode=="yoimiya" or mode=="Naganohara" or mode=="naganohara" or mode=="Yoimiya Naganohara" or mode=="yoimiya Naganohara" or mode=="Naganohara Yoimiya" or mode=="naganohara yoimiya" or mode=="Yoimiya naganohara" or mode=="yoimiya naganohara" or mode=="naganohara Yoimiya" or mode=="Naganohara yoimiya":
            em=discord.Embed(title="Naganohara Yoimiya :",description="*Propriétaire des « Feux de Naganohara ». Connue sous le nom de « Reine du festival d'été », elle excelle dans son art de créer des feux d'artifice qui symbolisent les espoirs et les rêves des gens.*",color=discord.Color.from_rgb(255, 33, 33))
            em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Pyro - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats :* \nCrit > ATK% > Maitrise élémentaire > Recharge d'énergie \n*Set :* \n:first_place: Réminiscence Nostalgique (4 pièces) \nÉchos d'une Offrande (4 pièces) \nSorcière des Flammes Ardentes (4 pièces) \nSorcière des flammes (2 pièces) & Rideau du gladiateur (2 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Flambée pyrotechnique)* \n:second_place: Compétence élémentaire *(Danse du feu « Niwabi)* \n:third_place: Déchainement élémentaire *(Saxifrage Ryuukin)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/904508982796881960/yoimiyam.png")
            await ctx.send(embed=em)
        elif mode=="hutao" or mode=="Hutao" or mode=="Hu Tao" or mode=="hu Tao" or mode=="Hu tao" or mode=="hu tao":
            em=discord.Embed(title="Hu Tao :",description="*La 77e directrice du Funérarium Wangsheng, qui redonne un coup de jeune à la gestion des affaires funéraires de Liyue.*",color=discord.Color.from_rgb(255, 33, 33))
            em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> PV% \n<:Coupe:903641040941088769> Dégats Pyro/PV% - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats :* \nCrit > PV% > Maitrise élémentaire \n*Set :* \n:first_place: Sorcière des Flammes Ardentes (4 pièces) \nRéminiscence Nostalgique (4 pièces) \nSorcière des Flammes Ardentes (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Chaperon de la renaissance)* \n:second_place: Déchainement élémentaire *(Apaisement divin)* \n:third_place: Attaque de base *(Lance secrète de Wangsheng)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/905920561178349568/hutao.png")
            await ctx.send(embed=em)
        elif mode=="Tartaglia" or mode=="tartaglia" or mode=="Childe" or mode=="childe" or mode=="Tartagliatelle" or mode=="tartagliatelle" or mode=="Tagliatelle" or mode=="tagliatelle":
            em=discord.Embed(title="Tartaglia :",description="*Le 11e Exécuteur des Fatui, appelé « Tartaglia ». Il s'est fait connaître pour avoir gagné des milliers de combats.*",color=discord.Color.from_rgb(28, 111, 255))
            em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Hydro - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats :* \nCrit > ATK% > Recharge d'énergie > Maitrise élémentaire \n*Set :* \n:first_place: Échos d'une Offrande (4 pièces) \nÂme des profondeurs (4 pièces) \nRéminiscence Nostalgique (4 pièces) \nÂme des profondeurs (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Posture du démon : Marée déchaînée)* \n:second_place: Déchainement élémentaire *(Ravage : Oblitération)* \n:third_place: Attaque de base *(Taille du torrent)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/905925754783674428/childe.png")
            await ctx.send(embed=em)
        elif mode=="Ayaka" or mode=="ayaka" or mode=="Ayaka Kamisato" or mode=="ayaka kamisato" or mode=="Kamisato Ayaka" or mode=="kamisato ayaka" or mode=="Ayaka kamisato" or mode=="ayaka Kamisato" or mode=="kamisato Ayaka" or mode=="Kamisato ayaka":
            em=discord.Embed(title="Kamisato Ayaka :",description="*Fille du Clan Kamisato de la Commission culturelle. Digne et élégante, mais aussi sage et forte.*",color=discord.Color.from_rgb(117, 227, 255))
            em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Cryo - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats :* \nCrit > ATK% > Recharge d'énergie > Maitrise élémentaire \n*Set :* \n:first_place: Briseur de Glace (4 pièces) \nBriseur de Glace (2 pièces) & Rideau du Gladiateur (2 pièces) \nBriseur de Glace (2 pièces) & Ancien Rituel Royal (2 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(École Kamisato : Givre mortel)* \n:second_place: Attaque de base *(École Kamisato - Sveltesse)* \n:third_place: Compétence élémentaire *(École Kamisato : Fleur de glace)*",inline=False)
            em.set_thumbnail(url="https://media.discordapp.net/attachments/900869947050295336/906288536720900116/kamisato.png")
            await ctx.send(embed=em)
        elif mode=="Kazuha" or mode=="kazuha" or mode=="Kaedehara" or mode=="kaedehara" or mode=="Kazuha Kaedehara" or mode=="kazuha kaedehara" or mode=="Kaedehara Kazuha" or mode=="kaedehara kazuha" or mode=="Kazuha kaedehara" or mode=="kazuha Kaedehara" or mode=="kaedehara Kazuha" or mode=="Kaedehara kazuha":
            em=discord.Embed(title="Kaedehara Kazuha :",description="*Un samouraï errant d'Inazuma qui fait actuellement partie de la Flotte du Crux. Une âme douce et insouciante dont le cœur cache de nombreuses blessures.*",color=discord.Color.from_rgb(133, 255, 165))
            em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> Maitrise élémentaire \n<:Coupe:903641040941088769> Dégats Anémo/Maitrise élémentaire - <:Couronne:903641083236458536> Maitrise élémentaire/Taux Crit/Dégats Crit \n*Sub stats :* \nMaitrise élémentaire > Recharge d'énergie > Crit > ATK% \n*Set :* \n:first_place: Ombre de la Verte Chasseuse (4 pièces) \nOmbre de la Verte Chasseuse (2 pièces) & Rideau du Gladiateur (2 pièces) \nOmbre de la Verte Chasseuse (2 pièces) & Bande Vagabonde (2 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Véhémence divine)* \n:second_place: Déchainement élémentaire *(Coupure de mille feuilles)* \n:third_place: Attaque de base *(Escrime de Garyuu)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/906291215320895498/kaedehara.png")
            await ctx.send(embed=em)
        elif mode=="Xiangling" or mode=="xiangling":
            em=discord.Embed(title="Xiangling :",description="*Une célèbre cheffe cuisinière originaire de Liyue, connue pour ses plats épicés.*",color=discord.Color.from_rgb(255, 33, 33))
            em.add_field(name="Main DPS (Physique) :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Physique - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats :* \nCrit > ATK% > Recharge d'énergie\n*Set :* \n:first_place: Flamme Blême (2 pièces) & Chevalerie Ensanglantée(2 pièces) \nChevalerie Ensanglantée (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Cuisine-fu)* \n:second_place: Déchainement élémentaire *(Pyrotation)* \n:third_place: Compétence élémentaire *(Attaque Gooba)* \n _ _",inline=False)
            em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK%/Recharge d'énergie/Maitrise élémentaire \n<:Coupe:903641040941088769> Dégats Pyro - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats :* \nCrit > Maitrise élémentaire > ATK% > Recharge d'énergie \n*Set :* \n:first_place: Emblème du Destin Brisé (4 pièces) \nSorcière des Flammes Ardentes (4 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Pyrotation)* \n:second_place: Compétence élémentaire *(Attaque Gooba)* \n:third_place: Attaque de base *(Cuisine-fu)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/906297559528636426/xiangging.png")
            await ctx.send(embed=em)
        elif mode=="Xiao" or mode=="xiao":
            em=discord.Embed(title="Xiao :",description="*Un des Adeptes de Liyue, aussi connu sous le nom de « Dompteur de démons » et « Général des Yakshas ».*",color=discord.Color.from_rgb(133, 255, 165))
            em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Anemo - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nTaux Crit/Dégats Crit > ATK% > Recharge d'énergie \n*Set* : \n:first_place: Au-delà Cinabrin (4 pièces) \nOmbre de la Verte Chasseuse (2 pièces) & Réminiscence Nostalgique (2 pièces) \nRéminiscence Nostalgique (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Coup de tourbillon)*\n:second_place: Déchainement élémentaire *(Fléau du mal)*\n:third_place: Compétence élémentaire *(Cycle du vent lemniscatique)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/906926813668847626/xiAAo.png")
            await ctx.send(embed=em)
        elif mode=="Xinyan" or mode=="xinyan":
            em=discord.Embed(title="Xinyan :",description="*La seule et unique rockeuse de Liyue. Elle combat les préjugés avec sa musique et ses chansons passionnées.*",color=discord.Color.from_rgb(255, 33, 33))
            em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK%/DEF% \n<:Coupe:903641040941088769> Dégats Physique/ATK% - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats :* \nCrit > ATK% > DEF% > Recharge d'énergie\n*Set :* \n:first_place: Chevalerie Ensanglantée (2 pièces) & Rideau du Gladiateur (2 pièces) \nRideau du Gladiateur (4 pièces) \nChevalerie Ensanglantée (4 pièces) *Avec une C6*\n _ _\n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Danse du feu)* \n:second_place: Déchainement élémentaire *(Riff rebelle)* \n:third_place: Compétence élémentaire *(Jeu fervent)* \n _ _",inline=False)
            em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> DEF%/ATK% \n<:Coupe:903641040941088769> Dégats Physique/DEF%/ATK% - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats :* \nCrit > DEF% > ATK% > Recharge d'énergie \n*Set :* \n:first_place: Chevalerie Ensanglantée (2 pièces) & Ancien Rituel Royal (2 pièces) \nChevalerie Ensanglantée (2 pièces) & Rideau du Gladiateur (2 pièces) \nChevalerie Ensanglantée (2 pièces) & Coquille des Rêves Opulents (2 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Riff rebelle)* \n:second_place: Compétence élémentaire *(Jeu fervent)* \n:third_place: Attaque de base *(Danse du feu)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/906929504071593984/xinnya.png")
            await ctx.send(embed=em)
        elif mode=="Bennett" or mode=="bennett" or mode=="Danger public" or mode=="danger public" or mode=="Danger Public" or mode=="danger Public":
            em=discord.Embed(title="Bennett :",description="*Un jeune aventurier originaire de Mondstadt. Sa gentillesse n'a d'égale que sa guigne.*",color=discord.Color.from_rgb(255, 33, 33))
            em.add_field(name="Support/Healeur :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> Recharge d'énergie \n<:Coupe:903641040941088769> PV% - <:Couronne:903641083236458536> Bonus de Soin/PV% \n*Sub stats :* \nPV > Recharge d'énergie > Crit > Maitrise élémentaire \n*Set :* \n:first_place: Ancien Rituel Royal (4 pièces) \nRideau du Gladiateur (4 pièces) \nAmour Chérie (4 pièces) \nInstructeur (4 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Merveilleux voyage)* \n:second_place: Compétence élémentaire *(Surpassion)* \n:third_place: Attaque de base *(Épée chanceuse)* \n _ _",inline=False)
            em.add_field(name="DPS/Burst DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK%/Recharge d'énergie \n<:Coupe:903641040941088769> Dégats Pyro - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats :* \nCrit > > Recharge d'énergie > ATK% > Maitrise élémentaire \n*Set :* \n:first_place: Sorcière des Flammes Ardentes (4 pièces) *C4 et au dessus* \nRideau du Gladiateur (2 pièces) & Sorcière des Flammes Ardentes (2 pièces) \nParieur (2 pièces) & Sorcière des Flammes Ardentes (2 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Merveilleux voyage)* \n:second_place: Compétence élémentaire *(Surpassion)* \n:third_place: Attaque de base *(Épée chanceuse)*",inline=False)
            em.set_thumbnail(url="https://media.discordapp.net/attachments/900869947050295336/906933400244473897/benny.png")
            await ctx.send(embed=em)
        elif mode=="Yanfei" or mode=="yanfei":
            em=discord.Embed(title="Yanfei :",description="*Une célèbre conseillère juridique du Port de Liyue. Du sang d'Adepte coule dans les veines de cette jeune femme ingénieuse.*",color=discord.Color.from_rgb(255, 33, 33))
            em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Pyro - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats :* \nCrit > ATK% > Maitrise élémentaire > Recharge d'énergie\n*Set :* \n:first_place: Sorcière des Flammes Ardentes (4 pièces) \nSorcière des Flammes Ardentes (2 pièces) & Rideau du Gladiateur (2 pièces) \nSorcière des Flammes Ardentes (2 pièces) & Réminiscence Nostalgique (2 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Sceau embrasé)* \n:second_place: Déchainement élémentaire *(Application des peines)* \n:third_place: Compétence élémentaire *(Pacte des flammes)* \n _ _",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/906940088397733908/yanfhey.png")
            await ctx.send(embed=em)
        elif mode=="Lisa" or mode=="lisa" or mode=="MILF" or mode=="milf":
            em=discord.Embed(title="Lisa :",description="*Une bibliothécaire érudite mais un peu nonchalante. Le plus grand talent diplômé de l'Académie de Sumeru de ces deux derniers siècles.*",color=discord.Color.from_rgb(150, 46, 255))
            em.add_field(name="Support/Burst :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK%/Recharge d'énergie \n<:Coupe:903641040941088769> Dégats Electro - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nCrit > ATK% > Maitrise élémentaire \n*Set* : \n:first_place: Colère du Tonnerre (4 pièces) \nAncien Rituel Royal (4 pièces) \nParieur (2 pièces) & Colère du Tonnerre (2 pièces)\n _ _ \n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Arc fulminant)* \n:second_place: Déchainement élémentaire *(Rose de foudre)* \n:third_place: Attaque de base *(Touche d'éclair)*",inline=False)
            em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK%/Recharge d'énergie \n<:Coupe:903641040941088769> Dégats Electro - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nCrit > ATK% > Maitrise élémentaire \n*Set* : \n:first_place: Colère du Tonnerre (4 pièces) \nDompteur de Foudre (4 pièces) \nParieur (2 pièces) & Colère du Tonnerre (2 pièces)\n _ _ \n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Touche d'éclair)* \n:second_place: Compétence élémentaire *(Arc fulminant)* \n:third_place: Déchainement élémentaire *(Rose de foudre)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/907357757408182373/lisaAAAH.png")
            await ctx.send(embed=em)
        elif mode=="Beidou" or mode=="beidou":
            em=discord.Embed(title="Beidou :",description="*Capitaine de la flotte du Crux, une femme de tête franche et directe.*",color=discord.Color.from_rgb(150, 46, 255))
            em.add_field(name="Main DPS (Physique) :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Physique - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats* : \nCrit > ATK% > Recharge d'énergie > Maitrise élémentaire \n*Set* : \n:first_place: Chevalerie Ensanglantée (2 pièces) & Flamme Blême (2 pièces) \nChevalerie Ensanglantée (2 pièces) & Rideau du Gladiateur (2 pièces)\n _ _ \n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Conquête des mers)* \n:second_place: Compétence élémentaire *(Invocation des marées)* \n:third_place: Déchainement élémentaire *(Brisure d'orage)*",inline=False)
            em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK%/Maitrise élémentaire \n<:Coupe:903641040941088769> Dégats Electro - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats* : \nCrit > ATK% > Maitrise élémentaire > Recharge d'énergie \n*Set* : \n:first_place: Colère du Tonnerre (4 pièces) \nColère du Tonnerre (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Invocation des marées)* \n:second_place: Déchainement élémentaire *(Brisure d'orage)* \n:third_place: Attaque de base *(Conquête des mers)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/907627081423290378/bheydou.png")
            await ctx.send(embed=em)
        elif mode=="Fischl" or mode=="fischl":
            em=discord.Embed(title="Fischl :",description="*Une fille mystérieuse qui se fait appeler « la Princesse du châtiment ». Elle est toujours accompagnée de son fidèle corbeau, Oz.*",color=discord.Color.from_rgb(150, 46, 255))
            em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Electro - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats* : \nCrit > ATK% > Maitrise élémentaire > Recharge d'énergie \n*Set* : \n:first_place: Colère du Tonnerre (2 pièces) & Rideau du Gladiateur (2 pièces) \nDompteur de Foudre (4 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Flèche de culpabilité)* \n:second_place: Compétence élémentaire *(Ailes de surveillance nocturne)* \n:third_place: Déchainement élémentaire *(Incarnation de la nuit)*",inline=False)
            em.add_field(name="Main DPS (Physique) :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Physique - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats* : \nCrit > ATK% > Maitrise élémentaire > Recharge d'énergie \n*Set* : \n:first_place: Échos d'une Offrande (4 pièces) \nFlamme Blême (4 pièces)\nChevalerie Ensanglantée (2 pièces) & Flamme Blême (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Ailes de surveillance nocturne)* \n:second_place: Déchainement élémentaire *(Incarnation de la nuit)* \n:third_place: Attaque de base *(Flèche de culpabilité)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/908494084761600021/Fischeul.png")
            await ctx.send(embed=em)
        elif mode=="Razor" or mode=="razor":
            em=discord.Embed(title="Razor :",description="*Un jeune garçon qui vit sur le Territoire des Loups situé aux environs de Mondstadt, loin de la ville et des foules. Il possède un instinct et une agilité surprenante.*",color=discord.Color.from_rgb(150, 46, 255))
            em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Physique - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nCrit > ATK% > Recharge d'énergie \n*Set* : \n:first_place: Rideau du Gladiateur (4 pièces) \nÉchos d'une Offrande (4 pièces) \nRideau du Gladiateur (2 pièces) & Chevalerie Ensanglantée (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Crocs d'acier)* \n:second_place: Déchainement élémentaire *(Croc d'éclair)* \n:third_place: Compétence élémentaire *(Griffe et tonnerre)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/908496908396412988/Razoir.png")
            await ctx.send(embed=em)
        elif mode=="Keqing" or mode=="keqing":
            em=discord.Embed(title="Keking :",description="*L'Alioth, l'une des Sept Étoiles de Liyue. L'Alioth critique à mots couverts l'idée que Liyue suive à la lettre la parole du Seigneur de la Roche, mais ce dernier apprécie justement ce genre de personnes.*",color=discord.Color.from_rgb(150, 46, 255))
            em.add_field(name="DPS Electro :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Electro/ATK% - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nCrit > ATK% > Maitrise élémentaire \n*Set* : \n:first_place: Échos d'une Offrande (4 pièces) \nColère de Tonnerre (2 pièces) & Rideau du Gladiateur (2 pièces)\nDompteur de Foudre (4 pièces) \nAncien Rituel Royal (2 pièces) & Colère de Tonnerre (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Escrime des nuages)*\n:second_place: Déchainement élémentaire *(Promenade céleste)*\n:third_place: Compétence élémentaire *(Retour des étoiles)*",inline=False)
            em.add_field(name="DPS Physique :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Physique/ATK% - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nCrit > ATK% > Maitrise élémentaire \n*Set* : \n:first_place: Échos d'une Offrande (4 pièces) \nCavalerie Ensanglanté (2 pièces) & Rideau du Gladiateur (2 pièces)\nCavalerie Ensanglanté (4 pièces) \nMétéore Inversé (4 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Escrime des nuages)*\n:second_place: Déchainement élémentaire *(Promenade céleste)*\n:third_place: Compétence élémentaire *(Retour des étoiles)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/908498531239727114/KeKing.png")
            await ctx.send(embed=em)
        elif mode=="Sara" or mode=="sara" or mode=="Kujou" or mode=="kujou" or mode=="kujou sara" or mode=="Kujou Sara" or mode=="sara kujou" or mode=="Sara Kujou" or mode=="Kujou sara" or mode=="Kujou Sara" or mode=="sara Kujou" or mode=="Sara kujou" or mode=="Kujo" or mode=="kujo" or mode=="kujo sara" or mode=="Kujo Sara" or mode=="sara kujo" or mode=="Sara Kujo" or mode=="Kujo sara" or mode=="Kujo Sara" or mode=="sara Kujo" or mode=="Sara kujo":
            em=discord.Embed(title="Kujou Sara :",description="*Une générale de la Commission administrative. Audacieuse, décisive et habile au combat.*",color=discord.Color.from_rgb(150, 46, 255))
            em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> Recharge d'énergie/Maitrise élémentaire \n<:Coupe:903641040941088769> Dégats Electro/Maitrise élémentaire - <:Couronne:903641083236458536> Dégats Crit/Taux Crit/Maitrise élémentaire \n*Sub stats* : \nRecharge d'énergie > Crit > Maitrise élémentaire \n*Set* : \n:first_place: Ancien Rituel Royal (4 pièces) \nColère du Tonnerre (2 pièces) & Ancien Rituel Royal (2 pièces) \nEmblème du Destin Brisé (4 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Soumission : Chemin de lumière)* \n:second_place: Compétence élémentaire *(Tempestrier tengu)* \n:third_place: Attaque de base *(Archerie tengu)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/908500549379457055/kujou.png")
            await ctx.send(embed=em)
        elif mode=="Klee" or mode=="klee" or mode=="Kamikaze" or mode=="kamikaze":
            em=discord.Embed(title="Klee :",description="*Une invitée régulière des cellules de l'Ordre de Favonius, et également la maîtresse des explosions à Mondstadt, où on la surnomme « le soleil fuyant ».*",color=discord.Color.from_rgb(255, 33, 33))
            em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Pyro - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nCrit > ATK% > Maitrise élémentaire \n*Set* : \n:first_place: Sorcière des Flammes Ardentes (2 pièces) & Rideau du Gladiateur (2 pièces)\nBande Vagabonde (4 pièces) \nSorcière des Flammes Ardentes (4 pièces) \nMarcheur du Feu (4 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Attaque normale : Boum ! Boum !)*\n:second_place: Déchainement élémentaire *(Fleur bombardier)*\n:third_place: Compétence élémentaire *(Bombe rebondissante)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/908502878635843665/KLEEEEE.png")
            await ctx.send(embed=em)
        elif mode=="Kaeya" or mode=="kaeya":
            em=discord.Embed(title="Kaeya :",description="*Un épéiste accompli et un stratège de génie de l'Ordre de Favonius ; il est originaire, selon les rumeurs, d'une terre bien au-delà des frontières de Mondstadt.*",color=discord.Color.from_rgb(117, 227, 255))
            em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK%/Recharge d'énergie \n<:Coupe:903641040941088769> Dégats Cryo/ATK% - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats :* \nCrit > ATK% > Recharge d'énergie > Maitrise élémentaire \n*Set :* \n:first_place: Briseur de Glace (2 pièces) & Ancien Rituel Royal (2 pièces) \nAncien Rituel Royal (4 pièces) \nBriseur de Glace (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Valse glaciale)* \n:second_place: Compétence élémentaire *(Attaque givrée)* \n:third_place: Attaque de base *(Passe d'armes)*",inline=False)
            em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Physique/ATK% - <:Couronne:903641083236458536> Dégats Crit/ATK% \n*Sub stats :* \nDégats Crit > ATK% > Maitrise élémentaire > Recharge d'énergie > Taux Crit \n*Set :* \n:first_place: Briseur de Glace (4 pièces) \nChevalerie Ensanglantée (2 pièces) & Rideau du Gladiateur (2 pièces)\nBriseur de Glace (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Valse glaciale)* \n:second_place: Attaque de base *(Passe d'armes)* \n:third_place: Compétence élémentaire *(Attaque givrée)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/908507385763602472/kaeyeuha.png")
            await ctx.send(embed=em)
        elif mode=="Ganyu" or mode=="ganyu" or mode=="cocochèvre" or mode=="Cocochèvre":
            em=discord.Embed(title="Ganyu :",description="*Secrétaire du Pavillon Yuehai ; du sang de Qilin, la créature mythique, coule dans ses veines.*",color=discord.Color.from_rgb(117, 227, 255))
            em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK%/Recharge d'énergie \n<:Coupe:903641040941088769> Dégats Cryo/ATK% - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nCrit > ATK% > Recharge d'énergie > Maitrise élémentaire \n*Set* : \n:first_place: Briseur de glace (2 pièces) & Ancien Rituel Royal (2 pièces)\nAncien Rituel Royal (4 pièces) \nAncien Rituel Royal (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Baptême céleste)*\n:second_place: Compétence élémentaire *(Trace de Qilin)*\n:third_place: Attaque de base *(Archerie Liutian)*",inline=False)
            em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Cryo/ATK% - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nCrit > ATK% > Recharge d'énergie > Maitrise élémentaire \n*Set* : \n:first_place: Bande vagabonde (4 pièces) \nBriseur de glace (2 pièces) & Ancien Rituel Royal (2 pièces) \nAncien Rituel Royal (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Archerie Liutian)*\n:second_place: Déchainement élémentaire *(Baptême céleste)*\n:third_place: Compétence élémentaire *(Trace de Qilin)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/908507370357919774/ganyou.png")
            await ctx.send(embed=em)
        elif mode=="Diona" or mode=="diona":
            em=discord.Embed(title="Diona :",description="*Une jeune fille au sang pas tout à fait humain. Elle travail comme barmaid à La Queue de Chat où elle est très appréciée.*",color=discord.Color.from_rgb(117, 227, 255))
            em.add_field(name="Support :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> Recharge d'énergie \n<:Coupe:903641040941088769> PV%/Dégats Cryo - <:Couronne:903641083236458536> PV%/Bonus de Soin \n*Sub stats :* \nRecharge d'énergie > PV% > ATK% > Crit \n*Set :* \n:first_place: Ancien Rituel Royal (4 pièces) \nInstructeur (4 pièces) \nExilé (4 pièces) \nAmour Chéri (4 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Griffes Cryo)* \n:second_place: Compétence élémentaire *(Cuvée spéciale)* \n:third_place: Attaque de base *(Archerie de chasse)*",inline=False)
            em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Cryo - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats :* \nRecharge d'énergie > Crit > ATK%\n*Set :* \n:first_place: Ancien Rituel Royal (4 pièces) \nInstructeur (4 pièces)\nAncien Rituel Royal (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Griffes Cryo)* \n:second_place: Compétence élémentaire *(Cuvée spéciale)* \n:third_place: Attaque de base *(Archerie de chasse)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/909254867741212742/diano.png")
            await ctx.send(embed=em)
        elif mode=="Chongyun" or mode=="chongyun":
            em=discord.Embed(title="Chongyun :",description="*Le jeune héritier d'une célèbre famille d'exorcistes, qui s'efforce de contrôler l'énergie qui l'habite.*",color=discord.Color.from_rgb(117, 227, 255))
            em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Cryo - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats :* \nCrit > ATK% > Recharge d'énergie > Maitrise élémentaire \n*Set :* \n:first_place: Briseur de Glace (2 pièces) & Ancien Rituel Royal (2 pièces) \nAncien Rituel Royal (4 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Lame de l'esprit : Chute d'étoiles)* \n:second_place: Compétence élémentaire *(Lame de l'esprit : Givre superposé)* \n:third_place: Attaque de base *(Fléau des démons)*",inline=False)
            em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Cryo - <:Couronne:903641083236458536> Dégats Crit/ATK% \n*Sub stats :* \nCrit > ATK% > Recharge d'énergie > Maitrise élémentaire \n*Set :* \n:first_place: Briseur de Glace (2 pièces) & Rideau du Gladiateur (2 pièces) \nRideau du Gladiateur (4 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Fléau des démons)* \n:second_place: Déchainement élémentaire *(Lame de l'esprit : Chute d'étoiles)* \n:third_place: Compétence élémentaire *(Lame de l'esprit : Givre superposé)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/909414199774576650/chongqiu.png")
            await ctx.send(embed=em)
        elif mode=="Rosalia" or mode=="rosalia" or mode=="Rosaria" or mode=="rosaria":
            em=discord.Embed(title="Rosalia :",description="*Une religieuse qui n'en a que l'apparence. Ses paroles sont acérées et son comportement, froid. Elle agit toujours seule.*",color=discord.Color.from_rgb(117, 227, 255))
            em.add_field(name="Main DPS (Physique) :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% - <:Coupe:903641040941088769> Dégats Physique - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats :* \nCrit > ATK% > Recharge d'énergie \n*Set :* \n:first_place: Échos d'une Offrande (4 pièces) \nChevalerie Ensanglantée (4 pièces) \nChevalerie Ensanglantée (2 pièces) & Flamme Blême (2 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Lance expiatoire)* \n:second_place: Déchainement élémentaire *(Sacrement mortel)* \n:third_place: Compétence élémentaire *(Confession des péchés)*",inline=False)
            em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK%/Recharge d'énergie \n<:Coupe:903641040941088769> Dégats Cryo - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats :* \nCrit > ATK% > Recharge d'énergie > Maitrise élémentaire \n*Set :* \n:first_place: Briseur de Glace (2 pièces) & Ancien Rituel Royal (2 pièces) \nBriseur de Glace (4 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Sacrement mortel)* \n:second_place: Compétence élémentaire *(Confession des péchés)* \n:third_place: Attaque de base *(Lance expiatoire)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/909446746491478056/rosaria.png")
            await ctx.send(embed=em)
        elif mode=="Xingqiu" or mode=="xingqiu":
            em=discord.Embed(title="Xingqiu :",description="*Un jeune homme intègre et serviable, que l'on voit souvent dans les librairies. Il porte une longue épée, et poursuit un idéal de justice.*",color=discord.Color.from_rgb(28, 111, 255))
            em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK%/Recharge d'énergie \n<:Coupe:903641040941088769> Dégats Hydro - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats :* \nRecharge d'énergie > Crit > ATK% > Maitrise élémentaire \n*Set :* \n:first_place: Âme des Profondeurs (2 pièces) & Ancien Rituel Royal (2 pièces) \nAncien Rituel Royal (4 pièces) \nAncien Rituel Royal (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Épée Guhua : Pluie et arc-en-ciel)* \n:second_place: Compétence élémentaire *(Épée Guhua : Pluie battante)* \n:third_place: Attaque de base *(Style Guhua)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/909449217720868933/xingyun.png")
            await ctx.send(embed=em)
        elif mode=="Barbara" or mode=="barbara":
            em=discord.Embed(title="Barbara :",description="*Barbara est adulée de tous à Mondstadt. Pourtant, c'est dans un magazine qu'elle a découvert le terme « idole ».*",color=discord.Color.from_rgb(28, 111, 255))
            em.add_field(name="Support/Healeur :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> PV%/Recharge d'énergie \n<:Coupe:903641040941088769> PV% - <:Couronne:903641083236458536> Bonus de Soin/PV% \n*Sub stats :* \nPV% > PV > Recharge d'énergie > Crit \n*Set :* \n:first_place: Palourde Océanique (4 pièces) \nAmour Chéri (4 pièces) \nAmour Chéri (2 pièces) & Tenacité du Millélithe (2 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(C’est parti pour le show ♪)* \n:second_place: Déchainement élémentaire *(Miracle brillant ♪)* \n:third_place: Attaque de base *(Murmure de l’eau)*",inline=False)
            em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Hydro - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats :* \nCrit > ATK% > Maitrise élémentaire \n*Set :* \n:first_place: Âme des Profondeurs (4 pièces) \nÂme des Profondeurs (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Murmure de l’eau)* \n:second_place: Compétence élémentaire *(C’est parti pour le show ♪)* \n:third_place: Déchainement élémentaire *(Miracle brillant ♪)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/909453577771159592/barabara.png")
            await ctx.send(embed=em)
        elif mode=="Jean" or mode=="jean" or mode=="daronne" or mode=="Daronne":
            em=discord.Embed(title="Jean :",description="*Le Chevalier au Pissenlit, loyal et rigoureux, et la Grande Maîtresse suppléante de l'Ordre de Favonius.*",color=discord.Color.from_rgb(133, 255, 165))
            em.add_field(name="Healeur :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Anemo/ATK% - <:Couronne:903641083236458536> ATK%/Maitrise élémentaire \n*Sub stats* : \nATK% > Recharge d'énergie > Maitrise élémentaire > Crit \n*Set* : \n:first_place: Ombre de la Verte Chasseuse (2 pièces) & Rideau du Gladiateur (2 pièces)\nOmbre de la Verte Chasseuse (4 pièces) \nAncien Rituel Royal (4 pièces) \nAmour Chéri (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Brise de pissenlit)* \n:second_place: Compétence élémentaire *(Épée de tourbillon)* \n:third_place: Attaque de base *(Escrime de Favonius)*",inline=False)
            em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Anemo - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nCrit > ATK% > Recharge d'énergie > Maitrise élémentaire \n*Set* : \n:first_place: Ombre de la Verte Chasseuse (2 pièces) & Rideau du Gladiateur (2 pièces) \nRideau du Gladiateur (4 pièces) \nCavalerie Ensanglantée (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Escrime de Favonius)* \n:second_place: Compétence élémentaire *(Épée de tourbillon)* \n:third_place: Déchainement élémentaire *(Brise de pissenlit)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/909453587644559400/jaen.png")
            await ctx.send(embed=em)
        elif mode=="Qiqi" or mode=="qiqi" or mode=="Serial Healer" or mode=="Serial healer" or mode=="serial Healer" or mode=="serial healer":
            em=discord.Embed(title="Qiqi :",description="*Qiqi est une jeune apprentie du Cottage Bubu, en charge notamment de la récolte des herbes médicinales. C'est également un zombie au teint blafard et aux mots comptés.*",color=discord.Color.from_rgb(117, 227, 255))
            em.add_field(name="Healer :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK%/Recharge d'énergie \n<:Coupe:903641040941088769> ATK% - <:Couronne:903641083236458536> ATK%/Bonus de Soin \n*Sub stats* : \nATK% > Recharge d'énergie > ATK > Maitrise élémentaire \n*Set* : \n:first_place: Amour Chéri (2 pièces) & Palourde aux Teintes Océaniques (2 pièces) \nAmour Chéri (4 pièces) \nPalourde aux Teintes Océaniques (4 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Arcane d'Adepte : Talisman sacré)*\n:second_place: Compétence élémentaire *(Arcane d'Adepte : Héraut de givre)*\n:third_place: Attaque de base *(Escrime ancienne des nuages)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/909455858407182366/kiki.png")
            await ctx.send(embed=em)
        elif mode=="Albedo" or mode=="albedo" or mode=="ascenseur" or mode=="Ascenseur" or mode=="Monte-Charge" or mode=="Monte-charge" or mode=="monte-Charge" or mode=="monte-charge" or mode=="Kreideprinz" or mode=="kreideprinz":
            em=discord.Embed(title="Albedo :",description="*Génie connu sous le surnom de « Kreideprinz », Albedo est l'alchimiste en chef et le capitaine des enquêteurs de l'Ordre de Favonius.*",color=discord.Color.from_rgb(255, 197, 89))
            em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> DEF% \n<:Coupe:903641040941088769> Dégats Géo - <:Couronne:903641083236458536> Taux Crit/Dégats Crit/DEF % \n*Sub stats* : \nDEF% > Crit > ATK% > Recharge d'énergie \n*Set* : \n:first_place: Coquille des rêves (4 pièces) \nRoche Ancienne (2 pièces) & Coquille des rêves (2 pièces) \nRoche Ancienne (2 pièces) & Ancien Rituel Royal (2 pièces) \nRoche Ancienne (2 pièces) & Parieur (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Genèse : Aura solaire)* \n:second_place: Déchainement élémentaire *(Transformation : Reflux Géo)* \n:third_place: Attaque de base *(Escrime de Favonius - Blanche)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/909463110857928724/albedoux.png")
            await ctx.send(embed=em)
        elif mode=="Ningguang" or mode=="ningguang":
            em=discord.Embed(title="Ningguang :",description="*La Megrez des Sept Étoiles de Liyue. Peu de personnes peuvent se vanter d'être aussi riches à travers Teyvat.*",color=discord.Color.from_rgb(255, 197, 89))
            em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Géo - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nATK% > Crit > Recharge d'énergie \n*Set* : \n:first_place: Roche Ancienne (2 pièces) & Ancien Rituel Royal (2 pièces) \nRoche Ancienne (2 pièces) & Rideau du Gladiateur (2 pièces) \nEmblème du Destin Brisé (4 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Géo-dispersion)* \n:second_place: Compétence élémentaire *(Paravent d'astrolabe)* \n:third_place: Déchainement élémentaire *(Éclatement des étoiles)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/909465266986024960/ningus.png")
            await ctx.send(embed=em)
        elif mode=="Venti" or mode=="venti" or mode=="barbatos" or mode=="Barbatos" or mode=="trap" or mode=="Trap" or mode=="Barde" or mode=="barde":
            em=discord.Embed(title="Venti :",description="*Un des nombreux bardes de Mondstadt, qui aime à se promener dans tous les recoins de la cité.*",color=discord.Color.from_rgb(133, 255, 165))
            em.add_field(name="Sub DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Anemo - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats* : \nATK% > Taux Crit/Dégats Crit > Maitrise élémentaire \n*Set* : \n:first_place: Ombre de la Verte Chasseuse (4 pièces) \nOmbre de la Verte Chasseuse (2 pièces) & Ancien Rituel Royal (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Ode au vent)*\n:second_place: Compétence élémentaire *(Sonnet des Vents célestes)*\n:third_place: Attaque de base *(Archerie divine)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/910663498881716304/bardatos.png")
            await ctx.send(embed=em)
        elif mode=="Eula" or mode=="eula" or mode=="Noble" or mode=="noble":
            em=discord.Embed(title="Eula :",description="*Le « Chevalier aux Embruns », né de l'ancien Clan Lawrence, capitaine de l'unité de reconnaissance des chevaliers de l'Ordre de Favonius de Mondstadt. Que cette descendante de la noblesse d'antan ait rejoint les chevaliers de l'Ordre, l'ennemi jusqu'alors juré de la famille, demeure un mystère aux yeux de beaucoup.*",color=discord.Color.from_rgb(117, 227, 255))
            em.add_field(name="Main DPS (Physique) :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK%/Recharge d'énergie \n<:Coupe:903641040941088769> Dégats Physique - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats* : \nATK% > Crit > Recharge d'énergie \n*Set* : \n:first_place: Flamme Blême (4 pièces) \nFlamme Blême (2 pièces) & Chevalerie Ensanglantée (2 pièces) \nFlamme Blême (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Escrime de Favonius - Aristocratie)*\n:second_place: Déchainement élémentaire *(Lame de fond)*\n:third_place: Compétence élémentaire *(Vortex des mers glacées)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/910667895179198495/Eeeeuhla.png")
            await ctx.send(embed=em)
        elif mode=="Mona" or mode=="mona":
            em=discord.Embed(title="Mona :",description="*Jeune astromancienne mystérieuse, Mona se surnomme elle-même « la grande astromancienne Mona », et fait preuve d'une force singulière et d'une érudition hors-norme qui ne désavouent pas cette appellation.*",color=discord.Color.from_rgb(28, 111, 255))
            em.add_field(name="Support burst :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Hydro - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats :* \nCrit > ATK% > Recharge d'énergie > Maitrise élémentaire \n*Set :* \n:first_place: Emblème du Destin Brisé (4pièces) \nAncien Rituel Royal (4 pièces) \nÂme des Profondeurs (2 pièces) & Ancien Rituel Royal (2 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Voie divine)* \n:second_place: Compétence élémentaire *(Mirage aqueux)* \n:third_place: Attaque de base *(Ondes du destin)*",inline=False)
            em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Hydro - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats :* \nCrit > ATK% > Recharge d'énergie > Maitrise élémentaire \n*Set :* \n:first_place: Âme des Profondeurs (4 pièces) \nÂme des Profondeurs (2 pièces) & Ancien Rituel Royal (2 pièces) \nÂme des Profondeurs (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Voie divine)* \n:second_place: Attaque de base *(Ondes du destin)* \n:third_place: Compétence élémentaire *(Mirage aqueux)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/910670446972764181/monastres.png")
        elif mode=="Noelle" or mode=="noelle":
            em=discord.Embed(title="Noelle :",description="*Une jeune fille travaillant comme servante à l'Ordre de Favonius. Elle a toujours rêvé de devenir un jour chevalier.*",color=discord.Color.from_rgb(255, 197, 89))
            em.add_field(name="Main DPS (C6 recommandée) :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> DEF% \n<:Coupe:903641040941088769> Dégats Géo/DEF% - <:Couronne:903641083236458536> Dégats Crit/Taux Crit/DEF% \n*Sub stats* : \nCrit > DEF% > ATK% > Recharge d'énergie \n*Set* : \n:first_place: Coquille des Rêves Opulents (4 pièces) \nMétéore Inversé (4 pièces) \nCoquille des Rêves Opulents (2 pièces) & Roche Ancienne (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Grand ménage)* \n:second_place: Attaque de base *(Escrime de Favonius - Servante)* \n:third_place: Compétence élémentaire *(Armure de cœur)*",inline=False)
            em.add_field(name="Support bouclier :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> DEF% \n<:Coupe:903641040941088769> DEF% - <:Couronne:903641083236458536> DEF%/Bonus de Soin \n*Sub stats* : \nDEF% > Recharge d'énergie > Crit > ATK% \n*Set* : \n:first_place: Amour Chéri (4 pièces) \nAmour Chéri (2 pièces) & Coquille des Rêves Opulents (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Grand ménage)* \n:second_place: Compétence élémentaire *(Armure de cœur)* \n:third_place: Attaque de base *(Escrime de Favonius - Servante)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/910859902006751272/noel.png")
            await ctx.send(embed=em)
        elif mode=="Zhongli" or mode=="zhongli" or mode=="morax" or mode=="Morax" or mode=="osmanthus wine" or mode=="Osmanthus Wine" or mode=="Omanthus wine" or mode=="osmanthus Wine" or mode=="bangala" or mode=="Bangala":
            em=discord.Embed(title="Zhongli :",description="*Une mystérieuse relation du Funérarium Wangsheng, aux connaissances aussi variées qu'étendues.*",color=discord.Color.from_rgb(255, 197, 89))
            em.add_field(name="Support burst :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> PV% \n<:Coupe:903641040941088769> Dégats Géo - <:Couronne:903641083236458536> Dégats Crit/Taux Crit/PV% \n*Sub stats* : \nPV% > Crit > ATK% > Recharge d'énergie \n*Set* : \n:first_place: Roche Ancienne (2 pièces) & Ancien Rituel Royal (2 pièces) \nRoche Ancienne (2 pièces) & Ténacité du Millelithe (2 pièces) \nRoche Ancienne (2 pièces) & Réminiscence Nostalgique (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Chute de météore)* \n:second_place: Compétence élémentaire *(Dominus Lapidis)* \n:third_place: Attaque de base *(Pluie de pierres)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/910865180215357470/bangalax.png")
            await ctx.send(embed=em)
        elif mode=="Diluc Ragnvindr" or mode=="diluc Ragnvindr" or mode=="Diluc ragnvindr" or mode=="diluc ragnvindr" or mode=="Diluc" or mode=="diluc" or mode=="Le livreur de vin de Venti" or mode=="le livreur de vin de Venti" or mode=="Le livreur de vin de venti" or mode=="le livreur de vin de venti" or mode=="Ragnvindr Diluc" or mode=="Ragnvindr diluc" or mode=="ragnvindr Diluc" or mode=="ragnvindr diluc":
            em=discord.Embed(title="Diluc :",description="*Un jeune noble possédant la plupart des entreprises du vin de Mondstadt ; nul ne saurait sous-estimer sa richesse, sa réputation et ses capacités.*",color=discord.Color.from_rgb(255, 33, 33))
            em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Pyro - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nCrit > ATK% > Maitrise élémentaire \n*Set* : \nSorcière des Flammes Ardentes (4 pièces) \n:first_place: Sorcière des Flammes Ardentes (2 pièces) & Rideau du Gladiateur (2 pièces) \nSorcière des Flammes Ardentes (2 pièces) & Ancien Rituel Royal (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Assaut brûlant)* \n:second_place: Déchainement élémentaire *(Aurore)* \n:third_place: Attaque de base *(Épée trempée)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/910950983885029426/dilouc.png")
            await ctx.send(embed=em)
        elif mode=="Thomas" or mode=="thomas" or mode=="Thoma" or mode=="thoma" or mode=="Maid" or mode=="maid":
            em=discord.Embed(title="Thomas :",description="*L'employé de maison du Clan Kamisato. Un « négociateur » bien connu à Inazuma.*",color=discord.Color.from_rgb(255, 33, 33))
            em.add_field(name="Support/Shield :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> PV% \n<:Coupe:903641040941088769> Dégats Pyro/PV% - <:Couronne:903641083236458536> PV%/Dégats Crit/Taux Crit \n*Sub stats* : \nPV% > Recharge d'énergie > Crit > Maitrise élémentaire \n*Set* : \n:first_place: Sorcière des Flammes Ardentes (2 pièces) & Ténacité du Millelithe (2 pièces) \nSorcière des Flammes Ardentes (2 pièces) & Ancien Rituel Royal (2 pièces) \nSorcière des Flammes Ardentes (2 pièces) & Emblême du Destin Brisé (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(O-yoroi écarlate)* \n:second_place: Compétence élémentaire *(Bénédiction flamboyante)* \n:third_place: Attaque de base *(Lance célère)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/910965255432175657/thoma.png")
            await ctx.send(embed=em)
        elif mode=="Traveler" or mode=="traveler" or mode=="Aether" or mode=="aether" or mode=="Lumine" or mode=="lumine":
            em=discord.Embed(title="Traveler :",description="*Un voyageur/Une voyageuse venant d'un autre monde qui a été séparé.e de sa sœur/son frère. Il/Elle débute son périple à la recherche des Sept Archons dans l'espoir de la/le retrouver..*",color=discord.Color.from_rgb(230, 230, 255))
            em.add_field(name="Merci de préciser la recherche :",value="Plutôt le build de ``Traveler Anémo``, ``Traveler Géo`` ou ``Traveler Électro`` ?",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/910957273612947456/traveler.png")
            await ctx.send(embed=em)
        elif mode=="Traveler anemo" or mode=="traveler anemo" or mode=="Traveler Anemo" or mode=="traveler Anemo" or mode=="Aether anemo" or mode=="aether anemo" or mode=="Aether Anemo" or mode=="aether Anemo" or mode=="Lumine anemo" or mode=="lumine anemo" or mode=="Lumine Anemo" or mode=="lumine Anemo" or mode=="Traveler anémo" or mode=="traveler anémo" or mode=="Traveler Anémo" or mode=="traveler Anémo" or mode=="Aether anémo" or mode=="aether anémo" or mode=="Aether Anémo" or mode=="aether Anémo" or mode=="Lumine anémo" or mode=="lumine anémo" or mode=="Lumine Anémo" or mode=="lumine Anémo":
            em=discord.Embed(title="Traveler (Anémo) :",description="*Un voyageur/Une voyageuse venant d'un autre monde qui a été séparé.e de sa sœur/son frère. Il/Elle débute son périple à la recherche des Sept Archons dans l'espoir de la/le retrouver.*",color=discord.Color.from_rgb(133, 255, 165))
            em.add_field(name="Main DPS (Anémo) :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Anémo/ATK% - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats* : \nCrit > ATK% > Maitrise élémentaire \n*Set* : \n:first_place: Ombre de la Verte Chasseuse (4 pièces) \nOmbre de la Verte Chasseuse (2 pièces) & Ancien Rituel Royal (2 pièces) \nOmbre de la Verte Chasseuse (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Vents étrangers)* \n:second_place: Compétence élémentaire *(Épée de vortex)* \n:third_place: Déchainement élémentaire *(Rafale de vent)*",inline=False)
            em.add_field(name="Main DPS (Anémo) :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Anémo/ATK% - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats* : \nCrit > ATK% > Maitrise élémentaire \n*Set* : \n:first_place: Ombre de la Verte Chasseuse (4 pièces) \nOmbre de la Verte Chasseuse (2 pièces) & Ancien Rituel Royal (2 pièces) \nOmbre de la Verte Chasseuse (2 pièces) & Rideau du Gladiateur (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Rafale de vent)* \n:second_place: Compétence élémentaire *(Épée de vortex)* \n:third_place: Attaque de base *(Vents étrangers)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/910957273612947456/traveler.png")
            await ctx.send(embed=em)
        elif mode=="Traveler électro" or mode=="traveler électro" or mode=="Traveler Électro" or mode=="traveler Électro" or mode=="Aether électro" or mode=="aether électro" or mode=="Aether Électro" or mode=="aether Électro" or mode=="Lumine électro" or mode=="lumine électro" or mode=="Lumine Électro" or mode=="lumine Électro" or mode=="Traveler electro" or mode=="traveler electro" or mode=="Traveler Electro" or mode=="traveler Electro" or mode=="Aether electro" or mode=="aether electro" or mode=="Aether Electro" or mode=="aether Electro" or mode=="Lumine electro" or mode=="lumine electro" or mode=="Lumine Electro" or mode=="lumine Electro":
            em=discord.Embed(title="Traveler (Électro) :",description="*Un voyageur/Une voyageuse venant d'un autre monde qui a été séparé.e de sa sœur/son frère. Il/Elle débute son périple à la recherche des Sept Archons dans l'espoir de la/le retrouver.*",color=discord.Color.from_rgb(150, 46, 255))
            em.add_field(name="Support DPS (Électro) :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> Recharge d'énergie/ATK% \n<:Coupe:903641040941088769> Dégats Électro - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats* : \nRecharge d'énergie > Crit > ATK% > Maitrise élémentaire \n*Set* : \n:first_place: Colère du Tonnerre (2 pièces) & Ancien Rituel Royal (2 pièces) \nColère du Tonnerre (4 pièces) \nAncien Rituel Royal (2 pièces) & Emblême du Destin Brisé (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Tonnerre hurlant)* \n:second_place: Compétence élémentaire *(Lame d'éclair)* \n:third_place: Attaque de base *(Tonnerre venu d'ailleurs)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/910957273612947456/traveler.png")
            await ctx.send(embed=em)
        elif mode=="Traveler géo" or mode=="traveler géo" or mode=="Traveler Géo" or mode=="traveler Géo" or mode=="Aether géo" or mode=="aether géo" or mode=="Aether Géo" or mode=="aether Géo" or mode=="Lumine géo" or mode=="lumine géo" or mode=="Lumine Géo" or mode=="lumine Géo" or mode=="Traveler geo" or mode=="traveler geo" or mode=="Traveler Geo" or mode=="traveler Geo" or mode=="Aether geo" or mode=="aether geo" or mode=="Aether Geo" or mode=="aether Geo" or mode=="Lumine geo" or mode=="lumine geo" or mode=="Lumine Geo" or mode=="lumine Geo":
            em=discord.Embed(title="Traveler (Géo) :",description="*Un voyageur/Une voyageuse venant d'un autre monde qui a été séparé.e de sa sœur/son frère. Il/Elle débute son périple à la recherche des Sept Archons dans l'espoir de la/le retrouver.*",color=discord.Color.from_rgb(255, 197, 89))
            em.add_field(name="Main DPS (Géo) :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Géo - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nCrit > ATK% > Recharge d'énergie \n*Set* : \n:first_place: Rideau du Gladiateur (4 pièces) \nRideau du Gladiateur (2 pièces) & Ancien Rituel Royal (2 pièces) \nRideau du Gladiateur (2 pièces) & Ténacité du Millelithe (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Épée d'étoile déchue)* \n:second_place: Déchainement élémentaire *(Réveil de la terre)* \n:third_place: Attaque de base *(Lame de roche)*",inline=False)
            em.add_field(name="Sub DPS (Géo) :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Géo - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nCrit > ATK% > Recharge d'énergie \n*Set* : \n:first_place: Ténacité du Millelithe (2 pièces) & Ancien Rituel Royal (2 pièces) \nTénacité du Millelithe (4 pièces) \nAncien Rituel Royal (4 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Épée d'étoile déchue)* \n:second_place: Déchainement élémentaire *(Réveil de la terre)* \n:third_place: Attaque de base *(Lame de roche)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/910957273612947456/traveler.png")
            await ctx.send(embed=em)
        elif mode=="Goro" or mode=="goro" or mode=="gorou" or mode=="Gorou" or mode=="toutou" or mode=="Toutou" or mode=="bon toutou" or mode=="Bon toutou" or mode=="Bon Toutou" or mode=="bon Toutou":
            em=discord.Embed(title="Gorou :",description="*Le grand général des forces de l'Île de Watatsumi, en qui ses subordonnés ont profondément confiance.*",color=discord.Color.from_rgb(255, 197, 89))
            em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> DEF% \n<:Coupe:903641040941088769> Dégats Géo - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats* : \nDEF% > Recharge d'énergie > Crit > ATK% \n*Set* : \n:first_place: Coquille des Rêves Opulents (4 pièces) \nEmblème du Destin Brisé (4 pièces) \nCoquille des Rêves Opulents (2 pièces) & Roche Ancienne (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Défense intégrale d'Inuzaka)* \n:second_place: Déchainement élémentaire *(Crocs bestiaux : Vers la victoire)* \n:third_place: Attaque de base *(Empenne aux crocs acérés)*",inline=False)
            em.set_thumbnail(url="https://media.discordapp.net/attachments/900869947050295336/930595563072806952/gorou.png")
            await ctx.send(embed=em)
        elif mode=="Itto" or mode=="itto" or mode=="Arataki" or mode=="arataki" or mode=="Itto Arataki" or mode=="itto arataki" or mode=="itto Arataki" or mode=="Itto arataki" or mode=="Arataki Itto" or mode=="arataki itto" or mode=="Arataki itto" or mode=="arataki Itto" or mode=="chômeur" or mode=="Chômeur" or mode=="chomeur" or mode=="Chomeur":
            em=discord.Embed(title="Arataki Itto :",description="*Le premier et plus grand chef du gang Arataki, célèbre dans tout Hanamizaka, à la Cité d'Inazuma... Hein, quoi ? Jamais entendu parler d'eux ? Sérieux ?*",color=discord.Color.from_rgb(255, 197, 89))
            em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> DEF% \n<:Coupe:903641040941088769> Dégats Géo/DEF% - <:Couronne:903641083236458536> Dégats Crit/Taux Crit/DEF% \n*Sub stats* : \nCrit > DEF% > ATK% > Recharge d'énergie \n*Set* : \n:first_place: Coquille des Rêves Opulents (4 pièces) \nMétéore Inversé (4 pièces) \nCoquille des Rêves Opulents (2 pièces) & Roche Ancienne (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Attaque de base *(Légende de la baston)* \n:second_place: Déchainement élémentaire *(Roi oni maléfique : Avènement d'Itto)* \n:third_place: Compétence élémentaire *(Zetsugi anti-démon : Catapultage d'akaushi)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/930593180758462554/itto.png")
            await ctx.send(embed=em)
        elif mode=="Yunjin" or mode=="yunjin" or mode=="Yun Jin" or mode=="yun jin" or mode=="Yun jin" or mode=="yun Jin" or mode=="maître yun" or mode=="Maître Yun" or mode=="maître Yun" or mode=="Maître yun" or mode=="maitre yun" or mode=="Maitre Yun" or mode=="maitre Yun" or mode=="Maitre yun":
            em=discord.Embed(title="Yun Jin :",description="*Une talentueuse chanteuse d'opéra et une dramaturge très célèbre à Liyue. Son style unique, doux et élégant, lui ressemble beaucoup.*",color=discord.Color.from_rgb(255, 197, 89))
            em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> DEF% \n<:Coupe:903641040941088769> DEF%/Dégats Géo - <:Couronne:903641083236458536> DEF% \n*Sub stats* : \nDEF% > Crit > ATK% > Recharge d'énergie \n*Set* : \n:first_place: Coquille des Rêves Opulents (4 pièces) \nEmblème du Destin Brisé (2 pièces) & Coquille des Rêves Opulents (2 pièces) \nCoquille des Rêves Opulents (2 pièces) & Roche Ancienne (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Bannière de rupture des falaises)* \n:second_place: Compétence élémentaire *(Épanouissement ouvert)* \n:third_place: Attaque de base *(Caresse des nuages)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/930595586753843270/yunyun.png")
            await ctx.send(embed=em)
        elif mode=="Shenhe" or mode=="shenhe":
            em=discord.Embed(title="Shenhe :",description="*Une disciple d'Adepte avec un air des plus inhabituels. Après avoir passé beaucoup de temps à s'instruire en isolement dans les montagnes de Liyue, elle est devenue tout aussi froide et distante que les Adeptes eux-mêmes.*",color=discord.Color.from_rgb(117, 227, 255))
            em.add_field(name="Support DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK%/Recharge d'énergie \n<:Coupe:903641040941088769> ATK% - <:Couronne:903641083236458536> ATK% \n*Sub stats :* \nATK% > Recharge d'énergie > Crit \n*Set :* \n:first_place: Rideau du Gladiateur (2 pièces) & Réminiscence Nostalgique (2 pièces) \nRideau du Gladiateur (2 pièces) & Emblème du Destin Brisé (2 pièces) \nAncien Rituel Royal (4 pièces) \n _ _\n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Invocation d'esprit printanier)* \n:second_place: Déchainement élémentaire *(Délivrance de la demoiselle divine)* \n:third_place: Attaque de base *(Percée des étoiles)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/930595579724185650/sheeshhe.png")
            await ctx.send(embed=em)
        elif mode=="Yae" or mode=="Yae miko" or mode=="yae" or mode=="yae miko" or mode=="Yae Miko" or mode=="yae Miko" or mode=="sadique#1":
            em=discord.Embed(title="Yae Miko :",description="*La Guuji Yae du Sanctuaire de Narukami est également responsable éditoriale de la chambre Yae. Une intelligence et une ruse inimaginable sont cachées sous son apparence gracieuse.*",color=discord.Color.from_rgb(150, 46, 255)) 
            em.add_field(name="Sub DPS/Burst DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK%/Recharge d'énergie \n<:Coupe:903641040941088769> Dégats Électro  - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nCrit > Recharge d'énergie > ATK% > Maîtrise Élémentaire \n*Set* : \n:first_place: Colère du Tonnerre (2 pièces) & Emblème du Destin Brisé (2 pièces) \nEmblème du Destin Brisé (4 pièces) \nColère du Tonnerre (2 pièces) & Rideau du Gladiateur (2 pièces) \n_ _ \n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Évocation des yakan : Sakura Dévastateur)*  \n:second_place: Déchainement élémentaire *(Technique Secrète : Incarnation de tenko)* \n:third_place: Attaque de base *(Vulpes Mangeur de Péchés)* \n _ _",inline=False)
            em.set_thumbnail(url="https://media.discordapp.net/attachments/900869947050295336/959145106634604564/yae.png")
            await ctx.send(embed=em)
        elif mode=="Kamisato Ayato" or mode=="Ayato" or mode=="ayato" or mode=="kamisato ayato" or mode=="Kamisato ayato" or mode=="kamisato Ayato" or mode=="ayato kamisato" or mode=="Ayato kamisato" or mode=="ayato Kamisato" or mode=="Ayato Kamisato":
            em=discord.Embed(title="Kamisato Ayato :",description="*Le jeune, mais néanmoins très talenteux, chef du Clan Kamisato de la Commission culturelle. Cultivé et poli, c'est un homme aux multiples facettes.*",color=discord.Color.from_rgb(28, 111, 255))
            em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> ATK% \n<:Coupe:903641040941088769> Dégats Hydro - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats* : \nCrit > Recharge d'énergie > ATK% > PV% \n*Set* : \n:first_place: Échos d'une Offrande (4 pièces) \nÂme des Profondeurs (4 pièces) \nRideau du Gladiateur (4 pièces) \n_ _ \n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(École Kamisato : Beauté réfléchie)*  \n:second_place: Déchainement élémentaire *(École Kamisato : Jardin d'eau)* \n:third_place: Attaque de base *(École Kamisato : Transition)* \n _ _",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/985683405922500679/ayato.png")
            await ctx.send(embed=em)
        elif mode=="Yelan" or mode=="yelan" or mode=="milf ultra méta":
            em=discord.Embed(title="Yelan :",description="*Une mystérieuse personne qui prétend travailler pour le bureau des affaires civiles. Cependant, elle n'apparait nulle part dans leur registre.*",color=discord.Color.from_rgb(28, 111, 255))
            em.add_field(name="Sub DPS/Burst DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> PV%/Recharge d'énergie \n<:Coupe:903641040941088769> Dégats Hydro - <:Couronne:903641083236458536> Dégats Crit/Taux Crit \n*Sub stats* : \nRecharge d'énergie > Crit > PV% \n*Set* : \n:first_place: Emblème du Destin Brisé (4 pièces) \nÂme des Profondeurs (2 pièces) & Ténacité du Millelithe (2 pièces) \nAncien Rituel Royal (4 pièces) \n_ _ \n**Priorité des Aptitudes :** \n:first_place: Déchainement élémentaire *(Dé exquis des profondeurs)*  \n:second_place: Compétence élémentaire *(Ligne vitale persistante)* \n:third_place: Attaque de base *(Sagette furtive)* \n _ _",inline=False)
            em.add_field(name="Main DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> PV% \n<:Coupe:903641040941088769> Dégats Hydro  - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nCrit > PV% > Recharge d'énergie \n*Set* : \n:first_place: Âme des Profondeurs (2 pièces) & Ténacité du Millelithe (2 pièces) \nEmblème du Destin Brisé (4 pièces) \nAncien Rituel Royal (4 pièces)  \n_ _ \n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Ligne vitale persistante)*  \n:second_place: Déchainement élémentaire *(Dé exquis des profondeurs)* \n:third_place: Attaque de base *(Sagette furtive)* \n _ _",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/985682454369161236/yelan.png")
            await ctx.send(embed=em)
        elif mode=="Trombone" or mode=="trombone" or mode=="Trombonethefirst" or mode=="trombonethefirst" or mode=="TromboneThefirst" or mode=="tromboneThefirst" or mode=="trombonethe1st" or mode=="Trombonethe1st" or mode=="tromboneThe1st" or mode=="TromboneThe1st" or mode=="Trombone the first" or mode=="trombone the first" or mode=="Trombone The first" or mode=="tromboneThefirst" or mode=="trombone the 1st" or mode=="Trombone the 1st" or mode=="trombone The 1st" or mode=="Trombone The 1st" or mode=="Trombottom" or mode=="trombottom":
            em=discord.Embed(title="Trombonethe1st :",description="*Limule à la base c’est un homme de 30 ans. Bonjoir Je sais pas pourquoi mais abonne toi, c’était pas un ordre mais une menace.*",color=discord.Color.from_rgb(28, 111, 255))
            em.add_field(name="Sub DPS :",value="**Artéfacts :** \n*Mains stats* : \n<:Fleur:903640840285593621> PV - <:Plume:903640902193516604> ATK - <:Sablier:903640999555907595> Recharge d'énergie - <:Coupe:903641040941088769> Dégats Limule - <:Couronne:903641083236458536> Taux Crit/Dégats Crit \n*Sub stats* : \nCrit > ATK% > Maitrise élémentaire \n*Set* : \n:first_place: Sorcière des Flammes Ardentes (4 pièces) \nJoie de ViviThe1st (2 pièces) & Crie du JoJo Fan Extremiste (2 pièces) \nPouvoir des Figurine Limule (2 pièces) & Ancien Rituel des Lunettes (2 pièces) \n _ _ \n**Priorité des Aptitudes :** \n:first_place: Compétence élémentaire *(Crie très fort)* \n:second_place: Déchainement élémentaire *(JOOJOOOOOOOO)* \n:third_place: Attaque de base *(Tape avec un body pillow Vivi)*",inline=False)
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/900869947050295336/910952396954427403/trombagar.png")
            await ctx.send(embed=em)
        else:
            em=discord.Embed(title="Il va falloir un peu patienter ...",description="Ce personnage est soit inexistant, soit non-jouable pour le moment, soit non renseigné dans la commande pour l'instant ... \n _ _\nIl va falloir prendre son mal en patience ...",color=discord.Color.from_rgb(255, 156, 199))
            await ctx.send(embed=em)

@trombot.command()
@commands.has_permissions(manage_roles=True)
async def lelevent(ctx):
    em=discord.Embed(title="lorem ipsum",description="lorem ipsum",color=discord.Color.from_rgb(79, 181, 232))
    em.add_field(name="lorem ipsum",value="lorem ipsum",inline=False)
    em.add_field(name="lorem ipsum",value="lorem ipsum",inline=False)
    em.add_field(name="lorem ipsum",value="lorem ipsum",inline=False)
    em.add_field(name="lorem ipsum",value="lorem ipsum",inline=False)
    em.set_author(name="template vide pour besoin évent",url="https://youtu.be/uSytCtRxcvA")
    em.set_footer(text="Le staff du Trombordel")
    em.set_thumbnail(url="https://media.discordapp.net/attachments/909917905699868713/983480232973586482/unknown.png?width=404&height=671")
    await ctx.send(embed=em)

@trombot.command()
async def evil(ctx,*,mode="normal"):
    if ctx.guild.id==879431432806744095:
        if ctx.channel.id==901896376437338123:
            if mode=="normal":
                await ctx.send(random.choice(devil))
            elif mode=="trombone":
                await ctx.send(random.choice(eviltrombone))
            elif mode=="azoth":
                await ctx.send(random.choice(evilazoth))
            elif mode=="ia_ourtt":
                await ctx.send(random.choice(evilyaourt))
            elif mode=="aka":
                await ctx.send(random.choice(evilaka))
            elif mode=="kreatyr":
                await ctx.send(random.choice(evilkrea))
            elif mode=="astolfo":
                await ctx.send(random.choice(evilasto))
            elif mode=="eliabricot":
                await ctx.send(random.choice(evilelia))
            elif mode=="clary":
                await ctx.send(random.choice(evilclary))
            elif mode=="rick":
                await ctx.send(random.choice(evilrick))
            elif mode=="the rock":
                await ctx.send(random.choice(evilrock))
            elif mode=="bruno":
                await ctx.send(random.choice(evilbruno))
        else:
            await ctx.send("Le portail des enfers se situe dans <#902513124068954122> \nEssaye de t'en rapprocher ...")
    else:
        if mode=="normal":
            await ctx.send(random.choice(devil))
        elif mode=="trombone":
            await ctx.send(random.choice(eviltrombone))
        elif mode=="azoth" or mode=="Azoth" or mode=="N" or mode=="n":
            await ctx.send(random.choice(evilazoth))
        elif mode=="ia_ourtt" or mode=="ia_Ourtt" or mode=="yaourt" or mode=="Yaourt" or mode=="iaourtt" or mode=="Iaourtt" or mode=="ia Ourtt" or mode=="ia ourtt" or mode=="yayourt" or mode=="Yayourt":
            await ctx.send(random.choice(evilyaourt))
        elif mode=="aka" or mode=="Aka":
            await ctx.send(random.choice(evilaka))
        elif mode=="kreatyr" or mode=="Kreatyr" or mode=="Krea" or mode=="krea":
            await ctx.send(random.choice(evilkrea))
        elif mode=="astolfo" or mode=="Astolfo" or mode=="Asto" or mode=="asto" or mode=="Asotolofo" or mode=="asotolofo":
            await ctx.send(random.choice(evilasto))
        elif mode=="eliabricot" or mode=="elia" or mode=="Eliabricot" or mode=="Elia":
            await ctx.send(random.choice(evilelia))
        elif mode=="clary" or mode=="Clary":
            await ctx.send(random.choice(evilclary))
        elif mode=="rick" or mode=="Rick" or mode=="rick roll" or mode=="Rick Roll" or mode=="Rick roll" or mode=="rick Roll" or mode=="Rick Astley" or mode=="rick astley" or mode=="rick Astley" or mode=="Rick astley":
            await ctx.send(random.choice(evilrick))
        elif mode=="the rock" or mode=="The Rock" or mode=="the Rock" or mode=="The rock" or mode=="Dwayne Johnson" or mode=="dwayne johnson" or mode=="Dwayne johnson" or mode=="dwayne Johnson":
            await ctx.send(random.choice(evilrock))
        elif mode=="bruno" or mode=="Bruno":
            await ctx.send(random.choice(evilbruno))

@trombot.command()
async def cookie(ctx,user:discord.User=None):
    if user==None:
        await ctx.send("REPOSE CE COOKIE SI TU VEUX PAS LE DONNER !")
    else:
        if user==ctx.message.author:
            await ctx.send("REPOSE CE COOKIE SI TU VEUX PAS LE DONNER !")
        else:
            em=discord.Embed(title="COOKIE TIME !",description=f"**{ctx.message.author.name}** vient de donner un cookie à {user.mention}.",color=discord.Color.from_rgb(163, 255, 203))
            em.set_image(url=random.choice(cookies))
            await ctx.send(embed=em)
@trombot.command()
async def kill(ctx,user:discord.User=None):
    if user==None:
        await ctx.send("REPOSE CE CANARD EN PLASTIQUE AVANT DE FAIRE UNE BÊTISE !")
    else:
        if user==ctx.message.author:
            em=discord.Embed(title="OH NO !",description=f"**{ctx.message.author.name}** essaye de se suicider.",color=discord.Color.from_rgb(163, 255, 203))
            em.set_image(url=random.choice(selfmort))
            await ctx.send(embed=em)
        else:
            em=discord.Embed(title="MEURTRE EN VU !",description=f"**{ctx.message.author.name}** a essayé d'assassiner {user.mention} !",color=discord.Color.from_rgb(163, 255, 203))
            em.set_image(url=random.choice(mort))
            await ctx.send(embed=em)
@trombot.command(aliases=['hello','wave'])
async def hi(ctx,user:discord.User=None):
    if user==None:
        em=discord.Embed(title="HELLO THERE !",description=f"**{ctx.message.author.name}** dit *BONJOIR* à tout le monde !",color=discord.Color.from_rgb(163, 255, 203))
        em.set_image(url=random.choice(hellogif))
        await ctx.send(embed=em)
    elif user==ctx.message.author:
        em=discord.Embed(title="HELLO THERE !",description=f"**{ctx.message.author.name}** se dit *BONJOIR* !",color=discord.Color.from_rgb(163, 255, 203))
        em.set_image(url=random.choice(hellogif))
        await ctx.send(embed=em)
    else:
        em=discord.Embed(title="HELLO THERE !",description=f"**{ctx.message.author.name}** te dit *BONJOIR* {user.mention} !",color=discord.Color.from_rgb(163, 255, 203))
        em.set_image(url=random.choice(hellogif))
        await ctx.send(embed=em)
@trombot.command()
async def hug(ctx,user:discord.User=None):
    if user==None:
        await ctx.send("On ne peut pas se faire de câlins à soit même malheureusement ... <:PensiveNeko:901930694350090250>")
    else:
        if user==ctx.message.author:
            await ctx.send("On ne peut pas se faire de câlins à soit même malheureusement ... <:PensiveNeko:901930694350090250>")
        else:
            em=discord.Embed(title="CÂLIN !",description=f"**{ctx.message.author.name}** fait un câlin à {user.mention} !",color=discord.Color.from_rgb(163, 255, 203))
            em.set_image(url=random.choice(hugging))
            await ctx.send(embed=em)

@trombot.command()
async def sncf(ctx):
    if ctx.guild.id==879431432806744095:
        if ctx.channel.id!=902513124068954122:
            await ctx.send("Vous êtes trop loin de la gare. \nRéessayez dans le salon <#902513124068954122>",delete_after=10)
        else:
            await ctx.send(random.choice(jinglesncf))
    else:
        await ctx.send(random.choice(jinglesncf))
@trombot.command()
async def ratp(ctx):
    if ctx.guild.id==879431432806744095:
        if ctx.channel.id!=902513124068954122:
            await ctx.send("Vous êtes trop loin de la station. \nRéessayez dans le salon <#902513124068954122>",delete_after=10)
        else:
            await ctx.send(random.choice(jingleratp))
    else:
        await ctx.send(random.choice(jingleratp))
@trombot.command(aliases=['tempest','lt','slime'])
async def limule(ctx):
    em=discord.Embed(title="Admire la supériorité de ce Slime !",description="Il a tout pour plaire !",color=7394047)
    em.set_image(url=random.choice(limuletempest))
    await ctx.send(embed=em)
@trombot.command()
async def zhongli(ctx):
    if ctx.message.author.id==754085724038627480:
        em=discord.Embed(title="Zhongli said :",description="*I will have order !*",color=discord.Color.from_rgb(255, 197, 89))
        em.set_image(url="https://cdn.discordapp.com/attachments/900869947050295336/902312904756453426/zhongli-genshin.gif")
        em.set_footer(text="En même temps c'est Trombone qui fait la commande ...")
        await ctx.send(embed=em)
    else:
        forzhongli=random.randint(1,11)
        if forzhongli==2:            
            em=discord.Embed(title="Zhongli said :",description="*I will have order !*",color=discord.Color.from_rgb(255, 197, 89))
            em.set_image(url="https://cdn.discordapp.com/attachments/900869947050295336/902312904756453426/zhongli-genshin.gif")
            em.set_footer(text="Finally.")
            await ctx.send(embed=em)
        else:
            em=discord.Embed(title="Zhongli said :",description="*Osmantus Wine taste the same as I remember ...*",color=discord.Color.from_rgb(255, 197, 89))
            em.set_image(url="https://cdn.discordapp.com/attachments/900869947050295336/902312941427241051/zhongli-zhongli-sip.gif")
            em.set_footer(text="May he have order next time ...")
            await ctx.send(embed=em)
@trombot.command()
async def poll(ctx,mode="normal"):
    if mode=="normal":
        await ctx.send("TU DOIS POSER UNE QUESTION LÀ, PAS ME REGARDER !")
    else:
        await ctx.send(random.choice(reponses))
@trombot.command()
async def kaijvu(ctx):
    em=discord.Embed(title="Attend chakal, je pense que j'ai pas bien vu là",description="Laisse moi me laver les yeux vite fait pour être sûr <a:ThumbsUp:901113202530713601>",color=discord.Color.from_rgb(255, 245, 135))
    em.set_image(url="https://cdn.discordapp.com/attachments/900869947050295336/902323258802729030/must-unsee-spongebob.gif")
    await ctx.send(embed=em)

@trombot.command(aliases=['lr'])
async def limuri(ctx):
    await ctx.send("https://c.tenor.com/SdhYgrUfIIEAAAAC/rimuru-tempest-laughing.gif")
@trombot.command(aliases=['gkn'])
async def triggered(ctx):
    em=discord.Embed(title="Gambatte Kudasai Ne",description="がんばってください ね",color=discord.Color.from_rgb(179, 117, 255))
    em.set_image(url="https://cdn.discordapp.com/attachments/880189018086727764/901466819175526430/trigger.gif")
    await ctx.send(embed=em)
@trombot.command(aliases=['rj','ti','tanjiku'])
async def renjiro(ctx):
    em=discord.Embed(title="J'VAIS T'BRISER LES OS, J'VAIS T'BOIRE TON SANG !",description="TU VOIS TA BARRE DE PV ? \nELLE EST VIDE, EXACTEMENT !",color=discord.Color.from_rgb(255, 51, 98))
    em.set_image(url=random.choice(tanjikuimg))
    await ctx.send(embed=em)

@trombot.command(aliases=['bot','rp'])
async def restoreperms(ctx,member:discord.Member=None):
    if ctx.message.author.id==687994752674824297:
        if ctx.guild.id==879431432806744095:
            guild=ctx.guild
            bot_creator=discord.utils.get(guild.roles,id=909456141665329222)
            if bot_creator not in member.roles:
                await member.add_roles(bot_creator,reason="tkt")
                await ctx.send("oui.",delete_after=10)
            return
    else:
        await ctx.send("alors ... non.",delete_after=5)
@trombot.command(aliases=['unadmin','notrp','unbot'])
async def unbotperm(ctx,member:discord.Member=None):
    if ctx.message.author.id==687994752674824297:
        if ctx.guild.id==879431432806744095:
            guild=ctx.guild
            bot_creator=discord.utils.get(guild.roles,id=909456141665329222)
            if bot_creator in member.roles:
                await member.remove_roles(bot_creator,reason="tkt")
                await ctx.send("oui.",delete_after=10)
            return
    else:
        await ctx.send("alors ... non.",delete_after=5)

@trombot.command(aliases=['purge','bbb'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
        await ctx.channel.purge(limit=amount+1)
        em=discord.Embed(title="BOOM BOOM BAKUDAN !",description=f"KLEE a EXPLOSÉ {amount} messages !",color=discord.Color.from_rgb(212, 133, 163))
        em.set_image(url="https://cdn.discordapp.com/attachments/900869947050295336/902310821630185572/klee.gif")
        await ctx.send(embed=em,delete_after=5)
@clear.error
async def clear_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("Tu n'as pas la puissance de Teppei en toi, le BOOM BOOM BAKUDAN ne t'es pas accessible !")
@trombot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx,member:discord.Member,*,reason=None):
    if ctx.message.author.top_role<=member.top_role:
        await ctx.send(f"MAIS T'ES MALADE, JAMAIS J'LE BAN **{member.display_name}**")
    else:
        try:
            em=discord.Embed(title="Bannissement",description=f"Hu Tao et **{ctx.message.author.name}** ont accompagné quelqu'un dans l'au-delà ... \nS'en est fini de {member.mention} sur le {ctx.guild.name}.",color=discord.Color.from_rgb(180, 140, 207))
            if reason!=None:
                em.add_field(name="Raison du bannissement :",value=f"*{reason}*",inline=False)
            em.set_image(url="https://cdn.discordapp.com/attachments/900869947050295336/902303138546081862/hu-tao-genshin-impact.gif")
            em.set_footer(text="Adieu jeune slime ...")
            try:
                await member.send(embed=em)
            except Forbidden:
                return
            await member.ban(reason=reason)
            await ctx.send(embed=em)
        except Forbidden:
            await ctx.send("Même si tu en as très envie, j'ai pas les perms de le ban lui ...")
            return
@ban.error
async def ban_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("Hu Tao n'a pas entendu ton appel à l'au-delà. N'essaye pas d'outre-passer la hiérarchie.")
@trombot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx,user,*,reason=None):
    try:
        name,id=user.split('#')
    except ValueError:
        await ctx.send("C'EST QUI MÊME ?")
        return
    bannedUsers=await ctx.guild.bans()
    for i in bannedUsers:
        if i.user.name==name and i.user.discriminator==id:
            await ctx.guild.unban(i.user,reason=reason)
            em=discord.Embed(title="Débannissement",description=f"{i.user.mention} semble avoir rencontré Truck-kun et non Hu Tao. \nSa réincarnation en Limule sur le {ctx.guild.name} est désormais possible !",color=discord.Color.from_rgb(180, 140, 207))
            if reason!=None:
                em.add_field(name="Raison du débannissement :",value=f"*{reason}*",inline=False)
            em.set_image(url="https://media.discordapp.net/attachments/900869947050295336/902303710686887936/that-time-i-got-reincarnated-as-a-slime-rimuru.gif")
            em.set_footer(text="Bon retour parmi nous, jeune slime !")
            await ctx.send(embed=em)
            try:
                await i.user.send(embed=em)
            except Forbidden:
                return
@unban.error
async def unban_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("N'essaye pas d'outre-passer la hiérarchie pour invoquer des camions.")
@trombot.command()
@commands.has_permissions(manage_roles=True)
async def mute(ctx,time,member:discord.Member=None,*,reason=None):
    if member==None:
        await ctx.send("TU VEUX MUTE QUI MÊME !?")
    else:
        if ctx.message.author.top_role<=member.top_role:
            await ctx.send(f"MAIS T'ES PAS NET TOI À VOULOIR MUTE **{member.display_name}** COMME ÇA LÀ !")
        else:
            if not reason:
                reason="Pas de raison indiquée"
            guild=ctx.guild
            mutedRole=discord.utils.get(guild.roles,name="Muted")
            if not mutedRole:
                await guild.create_role(name="Muted")
                for channel in guild.channels:
                    await channel.set_permissions(mutedRole,speak=False,send_messages=False,add_reactions=False)
            else:
                for channel in guild.channels:
                    await channel.set_permissions(mutedRole,speak=False,send_messages=False,add_reactions=False)
            try:
                if mutedRole in member.roles:
                    await ctx.send(f"IL EST DÉJÀ MUTE !",delete_after=5)
                    return
            except KeyError:
                pass
            if time!="indéfini":
                temp=convert(time)
                await member.add_roles(mutedRole,reason=reason)
                await ctx.send(f"La différence entre Paimon et {member.mention} c'est qu'on ne peut pas mute Paimon \nBon mute de {time} !")
                await ctx.send("https://tenor.com/view/genshin-impact-paimon-gif-18640817",delete_after=5)
                try:
                    await member.send(f"**{ctx.message.author.name}** t'as rendu muet sur le {ctx.guild.name} pour la raison suivante : *{reason}*")
                except Forbidden:
                    return
                await asyncio.sleep(temp)
                if mutedRole in member.roles:
                    await member.remove_roles(mutedRole)
                try:
                    await member.send(f"Ton mute sur le {ctx.guild.name} est fini !")
                except Forbidden:
                    return
            else:
                await member.add_roles(mutedRole,reason=reason)
                await ctx.send(f"La différence entre Paimon et {member.mention} c'est qu'on ne peut pas mute Paimon \nBon mute d'une durée indéfinie !")
                await ctx.send("https://tenor.com/view/genshin-impact-paimon-gif-18640817",delete_after=5)
                try:
                    await member.send(f"**{ctx.message.author.name}** t'as rendu muet sur le {ctx.guild.name} pour la raison suivante : *{reason}*")
                except Forbidden:
                    return
@mute.error
async def mute_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("À vouloir faire le malin c'est toi tu vas finir mute !")
@trombot.command()
@commands.has_permissions(manage_roles=True)
async def unmute(ctx,member:discord.Member,*,reason=None):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
    if mutedRole not in member.roles:
        await ctx.send("ON REND PAS LA PAROLE À QUELQU'UN QUI L'A DÉJÀ !",delete_after=5)
        return
    if not reason:
        reason="Pas de raison indiquée"
    await member.remove_roles(mutedRole,reason=reason)
    await ctx.send(f"Contrairement à Komi, {member.mention} arrive à parler.")
    await ctx.send("https://tenor.com/view/komi-san-komi-shouko-komi-shouko-comi-san-gif-23086846",delete_after=5)
    try:
        await member.send(f"**{ctx.message.author.name}** t'as démute sur le {ctx.guild.name}")
    except Forbidden:
        return
@unmute.error
async def unmute_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("N'essaye pas de rendre la parole quand tu ne le peux pas.")


trombot.run('***')
