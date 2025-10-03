from pytubefix import YouTube

url="https://www.youtube.com/watch?v=tfh6cd8AauQ"

YouTube(url).streams.first().download()