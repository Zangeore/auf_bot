from .. import loader, utils
from requests import get
import os
from gtts import gTTS
from PIL import Image, ImageDraw, ImageFont
import random


class AUFmod(loader.Module):

    strings = {
        "name": "AUFmod"
    }

    async def client_ready(self, client, db):
        self.client = client

    @loader.owner
    async def aufcmd(self, message):

        wolf=["main.jpg", "main1.jpg", "main2.jpg", "main3.jpg", "main4.jpg"]
        url = "https://raw.githubusercontent.com/Zangeore/auf_bot/main/"
        ctt = utils.get_args_raw(message)
        olf=random.choice(get(url+wolf))
        await message.edit("Жизнь ворам, Брат!!! Цитата в процессе. ")
        im = Image.open(url+olf)
        draw = ImageDraw.Draw(im)
        # font = ImageFont.truetype(<font-file>, <font-size>)
        font = ImageFont.truetype(get(url+"main.ttf"), 50)
        # draw.text((x, y),"Sample Text",(r,g,b))
        draw.text((20, 340), ctt, (0, 0, 0), font=font)
        im.save("1.jpg")
        tts = gTTS(text=ctt, lang='ru')
        tts.save("main.mp3")

        os.system("ffmpeg -loop 1 -i 1.jpg -i main.mp3 -c:v libx265  -strict \
        experimental -b:a 192k -shortest wolf.mp4 -y")


        os.system("ffmpeg -i wolf.mp4 -acodec copy -vcodec libx265   \
        -f mpegts vid1.webm -y")
        os.system("ffmpeg -i "+get(url+main.mp4)+" -acodec copy -vcodec libx265   \
        -f mpegts vid2.webm -y")
        os.system('ffmpeg -i "concat:vid1.webm|vid2.webm" out.mp4 -y')






        send=open("out.mp4", "rb")
        await message.client.send_video(message.to_id, output, reply_to=reply)
