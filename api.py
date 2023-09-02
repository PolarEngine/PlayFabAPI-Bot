from discord import commands
import discord
import requests

title_id = "63FDD"
dev_Secret = "123"
catalog_Version = "DLC"



bot = discord.Bot()

@bot.slash_command()
@commands.has_role("Owners")
async def grantitemtouser(ctx , playfabid : str , itemid : str):
    grantresult = requests.post(url=f"https://{title_id}.playfabapi.com/Server/GrantItemsToUser", json={"ItemIds" : itemid, "PlayFabId" : playfabid, "CatalogVersion" : catalog_Version}, headers={"X-SecretKey" : dev_Secret})
    if grantresult.status_code == 200:
            await ctx.respond('PlayFab API Has Successfully Gave The Item To That User' , ephemeral=True)
    elif grantresult.status_code == 400:
            await ctx.respond('Sorry , PlayFab API could not succcessfully complete that request.', ephemeral=True)



bot.run("example bot token")
