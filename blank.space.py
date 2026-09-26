import time
import sys

lirik = [
    "Boys only want love if it's torture...",
    "Don't say I didn't, say I didn't warn ya...",
    "Boys only want love if it's torture...",
    "Don't say I didn't, say I didn't warn ya...",
]

for baris in lirik:
    for huruf in baris:
        print(huruf,end="",flush=True)
        time.sleep(0.11)
    print()
    time.sleep(0.30)
