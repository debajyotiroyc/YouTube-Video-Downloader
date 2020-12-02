
 from pytube import YouTube
 link=input("ENTER THE LINK OF THE VIDEO THAT YOU WANT TO DOWNLOAD: ")

 yt=YouTube(link)
 print(" The Title of the video is: ",yt.title)

 video=yt.streams.first()
 path=input("ENTER THE PATH WHERE YOU WANT TO DOWNLOAD THE VIDEO: ")

 #the video now gets downloaded after the following command executes.
 video.download(path)
#you can also do like this:
 video.download('F:/')

