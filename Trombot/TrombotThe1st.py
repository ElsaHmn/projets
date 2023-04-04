import re
import datetime
from re import search
import discord
from discord import channel
from discord import member
from discord import guild
from discord.errors import NotFound
from discord.ext import commands, tasks
from discord import embeds
from discord import message
import random
import asyncio
from discord.ext.commands.converter import Converter, Greedy
from discord.ext.commands.errors import BadArgument
from discord.object import Object


trombot = commands.Bot(command_prefix="$", description="Trombot The 1st est dans la place.")
trombot.remove_command("help")


cookies=["https://c.tenor.com/1uZ2QLZeWQoAAAAC/nom-anime.gif","https://c.tenor.com/zluE5zNOkOkAAAAC/cute-eating.gif","https://c.tenor.com/rEx8468XVocAAAAC/anime-food.gif","https://c.tenor.com/J7f31OFMDFYAAAAC/anime-cookie.gif","https://c.tenor.com/45eglhkpWRoAAAAd/one-piece-carrot.gif","https://c.tenor.com/bBRCCeAYPU8AAAAC/cookie-mashiro.gif","https://c.tenor.com/g-WBixuZUnsAAAAC/anime-animegirl.gif","https://c.tenor.com/zEWVjcnOt1IAAAAC/anime-eating.gif"]
selfmort=["https://c.tenor.com/pM38Ryi6yRYAAAAC/noragomi.gif","https://c.tenor.com/r2NG3OuR7c8AAAAC/anime-vegetables.gif","https://c.tenor.com/CetnCMrSaEIAAAAC/ruru-suicide-show.gif"]
mort=["https://c.tenor.com/FpCsR78Irs0AAAAC/91days-angelo-lagusa.gif","https://c.tenor.com/VbJZVpft8pUAAAAC/fate-grand-order-babylonia.gif","https://c.tenor.com/xAwZBtBnBr4AAAAC/astolfo-trap-of-argalia.gif","https://c.tenor.com/1ybUFYQpNDgAAAAC/death-note-light-yagami.gif","https://c.tenor.com/CHMT9obzVEEAAAAC/tensei-shitara-slime-datta-ken-that-time-i-got-reincarnated-as-a-slime.gif","https://c.tenor.com/Ze50E1rW44UAAAAC/akudama-drive.gif","https://c.tenor.com/_lIIhhr5E_sAAAAC/megumin-kono-suba-gods-blessing-on-this-wonderful-world.gif","https://c.tenor.com/-UbmVOLixPcAAAAC/killing-anime-girl.gif"]
jinglesncf=["https://cdn.discordapp.com/attachments/900869947050295336/901805345742155776/tartine.mp4","https://cdn.discordapp.com/attachments/900869947050295336/901624309200588810/pates.mp4","https://cdn.discordapp.com/attachments/900869947050295336/901253663178244146/oubli.mp4","https://cdn.discordapp.com/attachments/900869947050295336/901246881177419776/daronnage.mp4","https://cdn.discordapp.com/attachments/900869947050295336/900878676520996904/debat.mp4"]
jingleratp=["https://cdn.discordapp.com/attachments/900869947050295336/901771950249099345/ligne_16.mp4","https://cdn.discordapp.com/attachments/900869947050295336/901771778152603668/GAS.mp4","https://cdn.discordapp.com/attachments/900869947050295336/901635865955143690/promotion.mp4","https://cdn.discordapp.com/attachments/900869947050295336/901635871030259752/traps.mp4"]
reponses=["Ça me parait évident en fait","J'en sais rien moi, je connais que Limule et Vivi dans la vie","Est-ce que j'ai fini de build ma Hu Tao décemment ? Tu as ta réponse.","Demande plutôt à BarnaB, c'est pas mon problème ça.","Tu veux pas aller boire de la potion de Konoha au lieu de me poser des questions ?","Alors par contre déso, mais je te réponds plus tard, là j'ai la crémaillère de mon meilleur pote et j'avais oublié *ahah*.","Essaye de trouver la puissance de Teppei pour voir si ça t'aide.","Je sais pas, mais **ACHÈTE UNE FIGURINE DE LIMULE** !"]
tanjiku=["https://media.discordapp.net/attachments/779498004880162836/901549689764196422/tobecontinued.png","https://media.discordapp.net/attachments/779498004880162836/901549997995196436/tobecontinued.png"]
hellogif=["https://c.tenor.com/0g-1USdD66MAAAAC/anime-girl.gif","https://c.tenor.com/PLb9vltH5acAAAAC/gerger.gif","https://c.tenor.com/ESVgd3T5YlcAAAAC/demon-slayer-anime.gif","https://c.tenor.com/EERR4LXoJBoAAAAC/hi-wave.gif","https://c.tenor.com/FMpLzF4UJhwAAAAC/kisumi-wave.gif","https://c.tenor.com/thNxDWlG1EcAAAAC/killua-zoldyck-anime.gif","https://c.tenor.com/MIXsMsU90KMAAAAC/hey-hello.gif"]
hugging=["https://c.tenor.com/Qw4m3inaSZYAAAAC/crying-anime-kyoukai-no-kanata-hug.gif","https://c.tenor.com/2lr9uM5JmPQAAAAC/hug-anime-hug.gif","https://c.tenor.com/xIuXbMtA38sAAAAd/toilet-bound-hanakokun.gif","https://c.tenor.com/0vl21YIsGvgAAAAC/hug-anime.gif","https://c.tenor.com/ztEJgrjFe54AAAAC/hug-anime.gif","https://c.tenor.com/4n3T2I239q8AAAAC/anime-cute.gif","https://c.tenor.com/9e1aE_xBLCsAAAAC/anime-hug.gif","https://c.tenor.com/Ct4bdr2ZGeAAAAAC/teria-wang-kishuku-gakkou-no-juliet.gif"]
forzhongli=random.randint(1,11)


class BannedUser(Converter):
    async def convert(self,ctx,arg):
        if ctx.guild.me.guild_permissions.ban_members:
            if arg.isdigit():
                try:
                    return (await ctx.guild.fetch_ban(Object(id=int(arg)))).user
                except NotFound:
                    raise BadArgument
        banned=[e.user for e in await ctx.guild.bans()]
        if banned:
            if (user:=search(lambda u: str(u)==arg,banned)) is not None:
                return user
            else:
                raise BadArgument


@trombot.event
async def on_ready():
    print("Limule on the road.")
    cpstatus.start()
status=["Être the First","Choisir entre Vivi et Limule","Farm les artéfacts de Hu Tao sur Genshin","Se réincarner en Slime"]
@tasks.loop(seconds=30)
async def cpstatus():
    game=discord.Game(random.choice(status))
    await trombot.change_presence(status=discord.Status.online, activity=game)


@trombot.command()
async def help(ctx,mode="normal"):
    if mode=="normal":
        em=discord.Embed(title="Liste des commandes",description=f"Pour connaître toutes les commandes sur le bout des doigts. Le préfix du bot est {trombot.command_prefix}.",color=7394047)
        em.add_field(name="Aide",value="``help``",inline=False)
        em.add_field(name="Interactions",value="``cookie``, ``hi``, ``kill``, ``hug``",inline=False)
        em.add_field(name="Rigolade",value="``sncf``, ``ratp``, ``poll``, ``kaijvu``, ``zhongli``",inline=False)
        em.add_field(name="Références au Twitch",value="``renjiro``, ``limuri``, ``triggered``",inline=False)
        em.add_field(name="Modération",value="``clear``, ``mute``, ``unmute``, ``ban``, ``unban``",inline=False)
        await ctx.send(embed=em)
    elif mode=="help":
        em=discord.Embed(title="Help",description="Montre la liste des commandes *ou* décrit le fonctionnement d'une commande.",color=7394047)
        em.add_field(name="Syntaxe",value=f"``{trombot.command_prefix}help`` *ou* ``{trombot.command_prefix}help <command>``")
        await ctx.send(embed=em)
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
        em.add_field(name="Syntaxe",value=f"``{trombot.command_prefix}hi <@membre>``",inline=False)
        await ctx.send(embed=em)
    elif mode=="sncf":
        em=discord.Embed(title="SNCF",description="Lance un Jingle SNCF aléatoire.",color=7394047)
        em.add_field(name="Syntaxe",value=f"``{trombot.command_prefix}sncf``")
        await ctx.send(embed=em)
    elif mode=="ratp":
        em=discord.Embed(title="RATP",description="Lance un Jingle RATP aléatoire.",color=7394047)
        em.add_field(name="Syntaxe",value=f"``{trombot.command_prefix}ratp``")
        await ctx.send(embed=em)
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
    elif mode=="clear" or mode=="purge" or mode=="bbb":
        em=discord.Embed(title="Clear",description="Trombot vient nettoyer les conversations ! (La valeur du clear par défaut est de 5)",color=7394047)
        em.add_field(name="Alias",value=f"``{trombot.command_prefix}purge``, ``{trombot.command_prefix}clear``, ``{trombot.command_prefix}bbb``",inline=False)
        em.add_field(name="Syntaxe",value=f"``{trombot.command_prefix}clear [nombre de messages à effacer]``",inline=False)
        await ctx.send(embed=em)
    elif mode=="triggered" or mode=="gkn":
        em=discord.Embed(title="Triggered",description="Fait de ton mieux, s'il te plaît !",color=7394047)
        em.add_field(name="Alias",value=f"``{trombot.command_prefix}gkn``, ``{trombot.command_prefix}triggered``",inline=False)
        em.add_field(name="Syntaxe",value=f"``{trombot.command_prefix}triggered``",inline=False)
        await ctx.send(embed=em)
    elif mode=="renjiro" or mode=="rj":
        em=discord.Embed(title="Renjiro",description="Tes PV vont disparaître, dis adieu à la vie.",color=7394047)
        em.add_field(name="Alias",value=f"``{trombot.command_prefix}rj``, ``{trombot.command_prefix}renjiro``",inline=False)
        em.add_field(name="Syntaxe",value=f"``{trombot.command_prefix}renjiro``",inline=False)
        await ctx.send(embed=em)
    elif mode=="mute":
        em=discord.Embed(title="Mute",description="Enlève le droit parole à un casse-pied.",color=7394047)
        em.add_field(name="Syntaxe",value=f"``{trombot.command_prefix}mute <@membre> <durée (nombre de secondes uniquement)> [raison]``")
        await ctx.send(embed=em)
    elif mode=="unmute":
        em=discord.Embed(title="Unmute",description="Rend la parole à un utilisateur muet.",color=7394047)
        em.add_field(name="Syntaxe",value=f"``{trombot.command_prefix}unmute <@membre> [raison]``")
        await ctx.send(embed=em)
    elif mode=="ban":
        em=discord.Embed(title="Ban",description="Banni un utilisateur du serveur.",color=7394047)
        em.add_field(name="Syntaxe",value=f"``{trombot.command_prefix}ban <@membre> [raison]``")
        await ctx.send(embed=em)
    elif mode=="unban":
        em=discord.Embed(title="Unban",description="Révoque le bannissement d'un utilisateur du serveur.",color=7394047)
        em.add_field(name="Syntaxe",value=f"``{trombot.command_prefix}unban <id du membre> [raison]``")
        await ctx.send(embed=em)
    else:
        await ctx.send("Réécris la commande correctement sinon **J'VAIS T'GOUMER LÀ** !")


@trombot.command()
async def cookie(ctx,user:discord.User=None):
    if user==None:
        await ctx.send("REPOSE CE COOKIE SI TU VEUX PAS LE DONNER !")
    else:
        await ctx.send(f"**{ctx.message.author.name}** vient de donner un cookie à {user.mention}.")
        await ctx.send(random.choice(cookies))
@trombot.command()
async def kill(ctx,user:discord.User=None):
    if user==None:
        await ctx.send("REPOSE CE CANARD EN PLASTIQUE AVANT DE FAIRE UNE BÊTISE !")
    else:
        if user==ctx.message.author:
            await ctx.send(f"**{ctx.message.author.name}** essaye de se suicider.")
            await ctx.send(random.choice(selfmort))
        else:
            await ctx.send(f"**{ctx.message.author.name}** a essayé d'assassiner {user.mention} !")
            await ctx.send(random.choice(mort))
@trombot.command(aliases=['hello','wave'])
async def hi(ctx,user:discord.User=None):
    if user==None:
        await ctx.send(f"**{ctx.message.author.name}** dit *BONJOIR* à tout le monde !")
        await ctx.send(random.choice(hellogif))
    else:
        await ctx.send(f"**{ctx.message.author.name}** te dit *BONJOIR* {user.mention} !")
        await ctx.send(random.choice(hellogif))
@trombot.command()
async def hug(ctx,user:discord.User=None):
    if user==None:
        await ctx.send("On ne peut pas se faire de câlins à soit même malheureusement ... <:PensiveNeko:901930694350090250>")
    else:
        await ctx.send(f"**{ctx.message.author.name}** fait un câlin à {user.mention} !")
        await ctx.send(random.choice(hugging))


@trombot.command()
async def sncf(ctx):
    await ctx.send(random.choice(jinglesncf))
@trombot.command()
async def ratp(ctx):
    await ctx.send(random.choice(jingleratp))
@trombot.command()
async def zhongli(ctx):
    if ctx.message.author.id==754085724038627480:
        await ctx.send("I will have order !")
        await ctx.send("https://tenor.com/view/zhongli-genshin-impact-liyue-geo-gif-19063890")
    else:
        if forzhongli<=2:
            await ctx.send("I will have order !")
            await ctx.send("https://tenor.com/view/zhongli-genshin-impact-liyue-geo-gif-19063890")
        else:
            await ctx.send("Osmantus Wine taste the same as I remember ...")
            await ctx.send("https://c.tenor.com/a8V7SS1K3dsAAAAC/zhongli-zhongli-sip.gif")
@trombot.command()
async def poll(ctx,mode="normal"):
    if mode=="normal":
        await ctx.send("TU DOIS POSER UNE QUESTION LÀ, PAS ME REGARDER !")
    else:
        await ctx.send(random.choice(reponses))
@trombot.command()
async def kaijvu(ctx):
    await ctx.send("Attend chakal, je pense que j'ai pas bien vu là, laisse moi me laver les yeux vite fait pour être sûr <a:ThumbsUp:901113202530713601>")
    await ctx.send("https://tenor.com/view/must-unsee-spongebob-washing-eyes-cant-look-gif-14237119")


@trombot.command(aliases=['lr'])
async def limuri(ctx):
    await ctx.send("https://c.tenor.com/SdhYgrUfIIEAAAAC/rimuru-tempest-laughing.gif")
@trombot.command(aliases=['gkn'])
async def triggered(ctx):
    await ctx.send("Gambatte Kudasai Ne \nがんばってください ね")
    await ctx.send("https://cdn.discordapp.com/attachments/880189018086727764/901466819175526430/trigger.gif")
@trombot.command(aliases=['rj'])
async def renjiro(ctx):
    await ctx.send("J'VAIS T'BRISER LES OS, J'VAIS T'BOIRE TON SANG !")
    await ctx.send(random.choice(tanjiku))


@trombot.command(aliases=['purge','bbb'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(f"BOOM BOOM BAKUDAN ! \nKLEE a EXPLOSÉ {amount} messages ! \nhttps://c.tenor.com/2W8NkLvBiSEAAAAC/klee.gif",delete_after=5)
@clear.error
async def clear_error(ctx,error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Tu n'as pas la puissance de Teppei en toi, le BOOM BOOM BAKUDAN ne t'es pas accessible !")
@trombot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx,member:discord.Member,*,reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"Hu Tao et **{ctx.message.author.name}** ont accompagné {member.mention} dans l'au-delà, il ne pourra plus rejoindre ce serveur.")
    await ctx.send("https://tenor.com/view/hu-tao-genshin-impact-genshin-impact-hu-tao-hu-tao-dance-gif-23101290")
@ban.error
async def ban_error(ctx,error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Hu Tao n'a pas entendu ton appel à l'au-delà. N'essaye pas d'outre-passer la hiérarchie.")
@trombot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx,targets:Greedy[BannedUser],reason=None):
    for target in targets:
        await ctx.guild.unban(target,reason=reason)
        await ctx.send(f"{target.mention} semble avoir rencontré Truck-kun et non Hu Tao. Il s'est réincarné en Limule !")
        await ctx.send("https://c.tenor.com/I37tFK1CaDwAAAAC/that-time-i-got-reincarnated-as-a-slime-rimuru.gif")
@unban.error
async def unban_error(ctx,error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("N'essaye pas d'outre-passer la hiérarchie pour invoquer des camions.")
@trombot.command()
@commands.has_permissions(manage_roles=True)
async def mute(ctx,member:discord.Member,time=0,reason=None):
    if not member:
        await ctx.send("TU VEUX MUTE QUI MÊME !?")
    else:
        if time==0:
            await ctx.send("La durée c'est pas une option en fait !")
        else:
            if not reason:
                reason="Pas de raison indiquée"
            guild = ctx.guild
            mutedRole = discord.utils.get(guild.roles, name="Muted")
            if not mutedRole:
                mutedRole = await guild.create_role(name="Muted")
                for channel in guild.channels:
                    await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True)
            try:
                if mutedRole in member.roles:
                    await ctx.send(f"IL EST DÉJÀ MUTE **{member.display_name}** !",delete_after=5)
                    return
            except KeyError:
                pass
            await member.add_roles(mutedRole, reason=reason)
            await ctx.send(f"La différence entre Paimon et {member.mention} c'est qu'on ne peut pas mute Paimon \nBon mute de {time} secondes !")
            await ctx.send("https://tenor.com/view/genshin-impact-paimon-gif-18640817",delete_after=5)
            await member.send(f"**{ctx.message.author.name}** t'as rendu muet sur le {ctx.guild.name} pour la raison suivante : {reason}")
            await asyncio.sleep(time)
            await member.remove_roles(mutedRole)
            await member.send(f"Ton mute sur le {ctx.guild.name} est fini !")
@mute.error
async def mute_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("À vouloir faire le malin c'est toi tu vas finir mute !")
@trombot.command()
@commands.has_permissions(manage_roles=True)
async def unmute(ctx,member: discord.Member,*,reason=None):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
    if mutedRole not in member.roles:
        await ctx.send("ON REND PAS LA PAROLE À QUELQU'UN QUI L'A DÉJÀ !",delete_after=5)
        return
    if not reason:
        reason="Pas de raison indiquée"
    await member.remove_roles(mutedRole,reason=reason)
    await ctx.send(f"Contrairement à Komi, {member.mention} arrive à parler.")
    await ctx.send("https://tenor.com/view/komi-san-komi-shouko-komi-shouko-comi-san-gif-23086846",delete_after=5)
    await member.send(f"**{ctx.message.author.name}** t'as démute sur le {ctx.guild.name} pour la raison suivante : {reason}")
@unmute.error
async def unmute_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("N'essaye pas de rendre la parole quand tu ne le peux pas.")


trombot.run('OTAwMTI4NjQ3MjcxMzA5MzQz.YW80IQ.hiEobos4_5aIow4XelvWBKlJD_A')