import asyncio
import discord

client = discord.Client()

# 생성된 토큰을 입력해준다.
token = "NzQ0NjE2MDM3MTc3MjI5Mzkx.XzlzuQ.1zz7j4awagT5SHSm0GylAq7Q4Zk"

# 봇이 구동되었을 때 보여지는 코드
@client.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    print("================")

# 봇이 특정 메세지를 받고 인식하는 코드

@client.event
async def on_message(message):
    global roles
    if message.content.startswith("!dm"):
        author = message.guild.get_member(int(message.content.split(' ')[1][3:21]))
        msg = message.content[26:]
        embed = discord.Embed(color=0x949494,
                              title='Maintain 공지사항',
                              description=msg,
                              timestamp=message.created_at)
        embed.set_footer(text=f"From. Maintain",
                         icon_url='https://media.discordapp.net/attachments/741008741616320625/762263805484859422/95fe80a27dbe773f.png?width=473&height=463')
        await author.send(embed=embed)
        embed = discord.Embed(color=0x949494,
                              title='DM이 전송되었습니다.',
                              description=msg,
                              timestamp=message.created_at)
        embed.set_footer(text=f"From. Maintain",
                         icon_url='https://media.discordapp.net/attachments/741008741616320625/762263805484859422/95fe80a27dbe773f.png?width=473&height=463')
        await message.channel.send(embed=embed)






client.run("NzQ0NjE2MDM3MTc3MjI5Mzkx.XzlzuQ.1zz7j4awagT5SHSm0GylAq7Q4Zk")
