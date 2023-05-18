from pytube import Playlist , YouTube
import time , sys , os

# Colors
red= "\u001b[31m"
green= "\u001b[32m"
blue= "\u001b[34m"
nc= "\033[0m" 


print(f'''
{green}██████╗     {blue}██╗     ███████╗ █████╗ ██████╗ ███╗   ██╗
{green}██╔══██╗    {blue}██║     ██╔════╝██╔══██╗██╔══██╗████╗  ██║
{green}██║  ██║    {blue}██║     █████╗  ███████║██████╔╝██╔██╗ ██║
{green}██║  ██║    {blue}██║     ██╔══╝  ██╔══██║██╔══██╗██║╚██╗██║
{green}██████╔╝    {blue}███████╗███████╗██║  ██║██║  ██║██║ ╚████║
{green}╚═════╝     {blue}╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                {red}Author : {blue}Mohammed Khalid
                {red}Version: {green}1.0
''')


# Disply Slow Words
def displaySlow(words , date=0.01):
    for char in words:
        print(char, end='', flush=True)
        time.sleep(date)

# Error handle
def handle_error(type, value, traceback):
    error = f"\n{red}Error !! , Please enter the data correctly , Or check your internet connection 2>"
    displaySlow(error)

sys.excepthook = handle_error

# Choose Quality Videos
def quality():
    start = 1
    end = 6

    q = int(input(f'''\n{blue}[ 1 ](144)P
[ 2 ](240)P
[ 3 ](360)P
{green}[ 4 ](480)P
[ 5 ](720)P
[ 6 ](1080)P
    >>> {nc}'''))
    ob = {
        1 : 144 ,
        2 : 240 ,
        3 : 360 ,
        4 : 480 ,
        5 : 720 ,
        6 : 1080
    }
    if q >= start or q <= end:

        return  ob[q]
    else:
        print (f"{red}You chose the wrong thing{nc}")


# Generate Directory
def Dir(name):
    x = os.path.abspath(os.path.dirname(__file__))
    path = x + '/' + name

    if not os.path.exists(path):
        os.mkdir(path)

    return path



word = f'''
{green}[ 1 ] {blue}PlayList

{green}[ 2 ] {blue}specific video

     {red}>>>{nc} '''
displaySlow(word)

check = input("")

def Display ():
    i= 1
    for video in playlist.videos:
        print (f"{green}[ {i} ] {nc}{video.title}")
        i+=1


# Displaying video titles from the playlist if you want to exclude certain videos
def Display_Titel_Videos():
    
    Display()
    x = f"{green}\n    Example: {red}2,5,8,20{nc}"
    displaySlow(x)

    num_videos = input(": ")
    return num_videos


# If the user enters spaces
def remove_spaces(string):
    x = string.replace(" ", "") .split (",")
    n =[]
    for i in x:
        v = int(i)
        t = v - 1
        n.append(t)

    return n


# return Download video links
def select_videos(execlude , st):
    arr = []
    ex = execlude
    i = 1
    for index, video in enumerate(playlist.videos):
        if index in ex :
            i+=1
            continue
        if st == True:
            print (f"{green}[ {i} ] {nc}{video.title}") 
        
        arr.append(video.watch_url)
        i+=1
        
    return arr


def download(q , arr, file) :
    i = 1

    for url in arr:
        # create a Video object
        yt=YouTube(url)

        # get the first video stream that matches the file extension and resolution
        stream = yt.streams.filter(file_extension='mp4', resolution=f'{q}p').first()

        # download the video to the specified save path with the title as the filename
        filename = f'{yt.title}.mp4'
        print(f"{green}[ {i} ] {nc}{filename}")
        stream.download( output_path=file,filename=filename)

        # increase the downloaded videos count
        i += 1
    x= f"\n{green}Download completed successfully{nc}, injoy \n"
    displaySlow(x)


if check == '1':

    # URL of the playlist here
    x = f"{green}Enter URL PlayList Videos -> {nc}"
    displaySlow(x)
    playlist_url = input("")

    x = f'''
{blue}Do You Want To Exclude Certain Videos From The PlayList ? [{green} y {nc}/ {red}n{blue} ] -> {nc}'''
    displaySlow(x)

    check_sbicific_videos = input('')
    
    if check_sbicific_videos.lower() == 'y' or check_sbicific_videos .lower() == 'yes':
        
        # create a Playlist object
        playlist = Playlist(playlist_url)
        print(f"{green}Ensure that the Internet connection is stable{nc}\n")
        
        num_vid = remove_spaces(Display_Titel_Videos())
        
        arr = select_videos(num_vid,True)
        q = str(quality())
        
        save_file = Dir(playlist.title)
        download(q , arr , save_file)


    elif check_sbicific_videos.lower() == 'n' or check_sbicific_videos.lower() == 'no':
        
        playlist = Playlist(playlist_url)
        q = str(quality())
        print(f"{green}Ensure that the Internet connection is stable{nc}\n")
        
        video = YouTube(f"{playlist}")
        arr = select_videos(remove_spaces("0"),False)
        save_file = Dir(playlist.title)

        download(q , arr , save_file)


elif check == '2':

    x = f"{green}Enter URL PlayList Videos -> {nc}"
    displaySlow(x)
    playlist_url = input("")
    
    q = str(quality())

    yt=YouTube(playlist_url)
    save_file = Dir("Videos")

    # get the first video stream that matches the file extension and resolution
    stream = yt.streams.filter(file_extension='mp4', resolution=f'{q}p').first()

    # download the video to the specified save path with the title as the filename
    filename = f'{yt.title}.mp4'
    print (f"{green}[1] {nc}{filename}")
    stream.download(output_path=save_file,filename=filename)
    
    
    x= f"{green}Download completed successfully{nc}, injoy"
    displaySlow(x)


