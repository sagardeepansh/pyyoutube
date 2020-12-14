from pytube import YouTube

url = input("Enter Youtube Link")
ytd = YouTube(url).streams.first().download()
print(ytd)