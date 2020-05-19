from playsound import playsound


def play_async(clip):
    playsound( clip, False)


def play_sync(clip):
    playsound( clip, True)