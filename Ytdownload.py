from pytube import YouTube
from pydub import AudioSegment
import os
link=input("Enter the Link: $ ")
#link='https://www.youtube.com/watch?v=koRuW3dbFQs'

def downloadmp3(link):
    yt=YouTube(link)


    name=(yt.title).replace('|','').replace(",",'')

    cmd1='mv "%s.mp4" "%s.m4a"'%(name,name)
    cmd2='ffmpeg -v 5 -y -i "%s.m4a" -acodec libmp3lame -ac 2 -ab 192k "%s.mp3"'%(name,name)
    cmd3='mv "%s.mp3" /home/srv333/Music/'%name
    cmd4='rm -f "%s.m4a"'%name

    print("\n"+name+'.mp4')
    yt.streams.get_by_itag(140).download()
    print("Song downloaded...")


    os.system(cmd1)
    print("Conversion part 1 completed.\n Proceeding to further conversion...")


    os.system(cmd2)
    print("Conversion completed!!!\n Moving the audio...")


    os.system(cmd3)
    print("Song ready to play!!!\n Cleaning the spattered shit now...")


    os.system(cmd4)


#PASOORI\ -\ ALI\ SETHI\ X\ SHAE\ GILL\ \ \(Coke\ Studio\)\ \ DGZi\ Music.mp4 
#PASOORI\ -\ ALI\ SETHI\ X\ SHAE\ GILL\ \ (Coke\ Studio)\ \ DGZi\ Music.mp4

#O\ O\ Jaane\ Jaana\ Full\ Song\ with\ Lyrics\ \ Pyar\ Kiya\ Toh\ Darna\ Kya\ \ Salman\ Khan\ Kajol.mp4
#O\ O\ Jaane\ Jaana\ Full\ Song\ with\ Lyrics\ \ Pyar\ Kiya\ Toh\ Darna\ Kya\ \ Salman\ Khan,\ Kajol.mp4