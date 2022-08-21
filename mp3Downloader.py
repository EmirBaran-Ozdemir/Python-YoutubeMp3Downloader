import re
from pytube import Playlist

YOUTUBE_STREAM_AUDIO = '140' 
DOWNLOAD_DIR = 'Link\\to\\preferred\\download\\folder' # Example: C:\\Users\\Username\\Desktop

playlist = Playlist('Paste full url here') # Example "https://www.youtube.com/playlist?list=PLtxwDkm517C9ln6Lf3xzbweSOW1V8UzC7"

# Empty video fix
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

for index,url in playlist.video_urls:
    print(f"Link{index}:{url}")
# Downloading and converting video extensions to .mp3
for video in playlist.videos:
    audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
    audioStream.download(output_path=DOWNLOAD_DIR)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)