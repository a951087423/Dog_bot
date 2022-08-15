import asyncio
import discord
client = discord.Client()


@client.event
async def on_ready():
    print('目前登入身份：', client.user)
    game = discord.Game('泓展的老二')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "<commands":
        await message.channel.send("這些是狗狗的指令列表↓↓↓\n"
        "1. 法鬥\n" "2. 菜狗\n" "3. 可樂狗\n" "4. 你\n" "5. 賴\n"
        "6. 美女\n" "7. 拍拍\n" "8. suck\n" "9. 6\n""10. 看\n"
        "11. 豬\n" "12. dinter\n" "13. 飯")


    if message.content == "法鬥":
        await message.channel.send("你又怎樣")
    if message.content == "菜狗":
        await message.channel.send("https://cdn.discordapp.com/attachments/578951256140283926/1006827976345780284/d6c481f51c184360a119ee65c9b73ada.mp4")
    if message.content == "可樂狗":
        await message.channel.send("https://cdn.discordapp.com/attachments/678241700753178634/1002580041902854235/IMG_1290.png")
    if message.content == "你":
        await message.channel.send("<@561191499442946049> 你！！！")
    if message.content == "妳":
        await message.channel.send("<@561191499442946049> 你！！！")
    if message.content == "賴":
        await message.channel.send("<@652094533982748683> 我有大！要不要飛！ \n倒了倒了倒了！\n我拉補我拉補我拉補！")
    if message.content == "美女":
        await message.channel.send("https://cdn.discordapp.com/attachments/593417203907428385/1007966682280644658/unknown.png")
    if message.content == "拍拍":
        await message.channel.send("https://cdn.discordapp.com/attachments/578951256140283926/1007319677413904394/A12705CE-5554-46B9-AF8D-5CC5416585B0.mov")
    if message.content == "suck":
        await message.channel.send("https://cdn.discordapp.com/attachments/987595268566450228/1007320085431599134/BEEC173E-EE80-4A77-8313-FD999B49CD1C.jpg\n" "<@682274304825884673>")
    if message.content == "6":
        await message.channel.send("6")
    if message.content == "看":
        await message.channel.send("https://cdn.discordapp.com/emojis/937590546640281660.webp?size=48&quality=lossless")
    if message.content == "豬":
        await message.channel.send("<@581704499945799691>")
    if message.content == "dinter":
        await message.channel.send("https://www.youtube.com/watch?v=81DyLNFZiD4&list=LL&index=72")
    if message.content == "飯":
        await message.channel.send("https://cdn.discordapp.com/attachments/678241700753178634/1008380821138313318/unknown.png")


client.run('TOKEN')