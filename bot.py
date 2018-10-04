import discord
from discord.ext.commands import Bot
import requests
from random import randint, choice
import tweepy
import urllib
import os
import file_creator

# init of random things:
vc_list = [
    'Rich Bois Inc.',
    'Aristo LLC',
    'Copper Coin Corp.'
]


# init of tweepy
auth = tweepy.OAuthHandler(consumer_key="N2V8HohQGHk95x4YIyPFbMQT0",
                           consumer_secret="KaoNqJcGrLCGu02h12tp6uoGaCmuD8zIZAF1fWgHCQlqzb0My9")
auth.set_access_token("997314301491900416-mvjX4Rk43XcfVod7sAwiMZGTWj96yST",
                      "6m5riAC0BvrB6qfpYB8JsGZy0uSBCCFWahuavE0eZ4IAm")
twit = tweepy.API(auth)

# init of search
subscription_key = "1bbd8638cb804e77973bab990f2e5588"
search_url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"

# init of discord bot
client = Bot(description=":I", command_prefix=".")


@client.event
async def on_ready():
    print("-- Connected --")


@client.event
async def on_member_join(ctx, member):
    await client.send_message(ctx.message.channel, "Welcome bitch ass nigga" + str(member))


@client.event
async def on_member_leave(ctx, member):
    await client.send_message(ctx.message.channel, "Bye bitch ass nigga" + str(member))
    file_creator.remove_user(str(member))


@client.command(pass_context=True)
async def img(ctx, *args):
    q = ""
    for i in args:
        q = q + " " + i
    search_term = str(q)
    print("searching for" + search_term)
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    params = {"q": search_term}
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()

    thumbnail_urls = [img["thumbnailUrl"] for img in search_results["value"][:16]]

    channel = ctx.message.channel

    try:
        thumbnail_urls_post = thumbnail_urls[randint(0, 5)]
        urllib.request.urlretrieve(thumbnail_urls_post, "img.jpg")

        await client.send_file(destination=channel, fp="img.jpg")
        os.remove("img.jpg")
    except IndexError:
        await client.say("There is no image" + search_term)


@client.command()
async def grabtweet(person):
    try:
        tweet = twit.user_timeline(person, count=1)
        status = tweet[0]
        await client.say(status.text)
    except IndexError:
        await client.say("There is no status to retrieve.")


@client.command()
async def randomtweet(person):
    try:
        tweet = twit.user_timeline(person, count=20)
        status = tweet[randint(0, 20)]
        await client.say(status.text)
    except IndexError:
        await client.say("There is no status to retrieve.")


@client.command()
async def tweet(*args):
    g = ""
    for i in args:
        g = g + " " + i
    print(g)
    twit.update_status(g)
    await client.say("You sent: " + str(g) + "\nhttps://twitter.com/tylercambroski?lang=en")


@client.command(pass_context=True)
async def info(ctx):
    server = ctx.message.server
    channel = ctx.message.channel
    embed = discord.Embed(title="Hey its uncy iroh :)", description=":))))))))", color=0xeee657)

    # give info about you here
    embed.add_field(name="Author", value="drosh boiiii")
    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{server.member_count}")
    # give users a link to invite this bot to their server-
    embed.add_field(name="Invite", value="https://discordapp.com/api/oauth2/authorize?client_id=446705819900182548&permissions=8&redirect_uri=https%3A%2F%2Fdiscordapp.com&response_type=code&scope=identify%20connections%20email%20guilds%20rpc.api%20gdm.join%20guilds.join%20rpc%20messages.read%20webhook.incoming%20rpc.notifications.read%20bot")

    await client.send_message(destination=channel, embed=embed)


@client.command(pass_context=True)
async def user_reset(ctx):
    file_creator.remove_files()  # remove all files in user folder


@client.command(pass_context=True)
async def start(ctx, company_name):
    sender = str(ctx.message.author)
    s = sender.split("#")
    message = file_creator.create_company(s[0], company_name)
    await client.send_message(destination=ctx.message.channel, content=message)


@client.command(pass_context=True)
async def vc(ctx):
    sender = str(ctx.message.author)
    s = sender.split("#")
    offer_list = []

    for i in range(3):
        money = randint(1000000, 3000000)
        choose_vc = choice(vc_list)
        percentage = randint(5, 20)
        offer_list.append("%s: $%d, %d\n" % (choose_vc, money, percentage))

    embed = discord.Embed(title="VC Offers", description="Choose Wisely", color=0xeee657)
    embed.add_field(name='Offer 1:', value=offer_list[0])
    embed.add_field(name='Offer 2:', value=offer_list[1])
    embed.add_field(name='Offer 3:', value=offer_list[2])

    # save the offers
    # save that they received offers
    # make it an if else to see if they have offers or not.
    await client.send_message(destination=ctx.message.channel, embed=embed)
# RUN
if __name__ == "__main__":
    client.run('NDQ2NzA1ODE5OTAwMTgyNTQ4.DeCDFA.7YyurilMYe_Tb7w4BzrQCyL3iyE')
