import tweepy
import time
import shutil, pathlib, os
import moviepy as mp
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from random import randint



ACCESS_KEY = "xxx"
ACCESS_SECRET = "xxx"
CONSUMER_KEY = "xxx"
CONSUMER_SECRET = "xxx"
BEARER_TOKEN = "xxx"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(
    ACCESS_KEY,
    ACCESS_SECRET,
)

# this is the syntax for twitter API 2.0. It uses the client credentials that we created
newapi = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    access_token=ACCESS_KEY,
    access_token_secret=ACCESS_SECRET,
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
)

# Create API object using the old twitter APIv1.1
api = tweepy.API(auth)

part = os.path.abspath(os.path.dirname(__file__) + "/Newfolder")

img = []
mediaa = []

# it's for control every run process
last_post_count = open("kayit.txt")
i = int(last_post_count.read())

def paylas(mediacount, mediaa, pathh):

    for images in os.listdir(pathh):
        # check if the image ends with jpg and take the first image that you find
        if images.endswith(".txt"):
            txt = images

    with open(part2 + "/" + txt, 'r', encoding="utf-8") as file:
        data = file.read().rstrip()

    data = str(sorted(os.listdir(part))[i])[:10] + "\n" + data[:267] + ""
    print(data)

    media_w = []



    for s in range(mediacount):
        media_w.append(api.media_upload(os.path.join(pathh, mediaa[s])))

        #media_w[s] = api.media_upload(os.path.join(pathh, mediaa[s]))

    if mediacount == 1:
        newapi.create_tweet(text=data, media_ids=[media_w[0].media_id])
    elif mediacount == 2:
        newapi.create_tweet(text=data, media_ids=[media_w[0].media_id, media_w[1].media_id])
    elif mediacount == 3:
        newapi.create_tweet(text=data, media_ids=[media_w[0].media_id, media_w[1].media_id, media_w[2].media_id])
    else:
        newapi.create_tweet(text=data, media_ids=[media_w[0].media_id, media_w[1].media_id, media_w[2].media_id, media_w[3].media_id])

    file_extensions = []
    for f in range(int(mediacount)-1):
        file_extensions.append(pathlib.Path(mediaa[f]).suffix)

    mediaa.clear()


while i < len(os.listdir(part)):

    try:
        print(str(i) + "/" + str(len(os.listdir(part))))

        part2 = os.path.abspath(part + "/" + sorted(os.listdir(part))[i])

        if os.path.abspath(part2 + "/" + sorted(os.listdir(part2))[2]).endswith(".mp4"):
            print("videogeldi")
            vidname = str(os.path.abspath(part2 + "/" + sorted(os.listdir(part2))[2]))


            clip = VideoFileClip(vidname)

            if clip.duration > 119:
                print("oldu")
                new_vidname = str(os.path.abspath(part2 + "/" + str(randint(3)) + "_" + sorted(os.listdir(part2))[2]))
                ffmpeg_extract_subclip(vidname, 0, 119, targetname=new_vidname)


                mediaa.append(new_vidname)
            else:
                mediaa.append(vidname)


            paylas(1, mediaa, os.path.abspath(part2))

            print("videopaylasildi")


        else:
            a = 0
            for images in os.listdir(os.path.abspath(part2)):
                # check if the image ends with jpg and take the first image that you find
                if images.endswith(".jpg"):
                    print(os.path.abspath(part2 + "/" + images))
                    img.append(os.path.abspath(part2 + "/" + images))
                    a = a + 1

                elif images.endswith(".txt"):
                    txt = images

            paylas(a, img, os.path.abspath(part2))
            img.clear()


        i = i + 1

        z = open("kayit.txt", "w")
        z.close()

        r = open("kayit.txt", "a")
        r.write(str(i))

        time.sleep(920)

    except Exception as error:
       print("bir hata oldu, 1 saat sonra  tekrar denenecek \n", str(error))
       time.sleep(3600)



