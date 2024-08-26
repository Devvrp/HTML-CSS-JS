import time
from threading import Thread
import sys

lyrics = [
    (" Halo ", 0.09),
    (" Nama ", 0.09),
    (" Saya ", 0.09),
    (" Devin  ", 0.09),
    (" Raditya ", 0.09),
    (" Pratama ", 0.09),
]
delays = [0, 5.0, 11.0, 17.0, 20.8, 35.0]

def animate_text(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    threads = []
    for i in range(len(lyrics)):
        lyrics, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delay[i], speed))
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()