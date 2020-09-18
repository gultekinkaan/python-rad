import time
import requests
import sys
from pydub import AudioSegment
DELAY = 1 * 1 * 1
while True:
    t = time.localtime()
    out = ("%d-%d-%d%-d-%d-%d" % (t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec))
    time.sleep(DELAY)


    files_path = "C:\\Users\\hp\\PycharmProjects\\orenıoz\\"
    file_name = out

    startMin = 1
    startSec = 00

    endMin = 3
    endSec = 00

    startTime = startMin * 1 * 1+ startSec * 1
    endTime = endMin * 1 * 1 + endSec * 1

    song = AudioSegment.from_mp3(files_path + file_name + '.mp3')
    extract = song[startTime: endTime]

    extract.export(file_name + '-extract.mp3', format="mp3")

    stream_url = "http://scturkmedya.radyotvonline.com/stream/80/"
    r = requests.get(stream_url, stream=True)
    with open(out, 'wb') as f:
        try:
            for block in r.iter_content(1024):
                f.write(block)
        except KeyboardInterrupt:
            pass
