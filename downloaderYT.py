from __future__ import unicode_literals
import youtube_dl

musicas=['https://www.youtube.com/watch?v=6G6Fi1CVawU','https://www.youtube.com/watch?v=QMvE0yFnR0I','https://www.youtube.com/watch?v=4jZBwyG7HPs','https://www.youtube.com/watch?v=zrymjzHlYEw']
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '128',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    for musica in musicas:
    	try:
    		ydl.download([musica])
	except:
		print "Error"
		pass
