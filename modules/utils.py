import math, hashlib
from random import randint


def generate_random_id():
    return hashlib.md5(f"asopnm`dasd {randint(0, 255)}-{randint(-255, 255)}".encode("utf-8")).hexdigest()


def distance(d1, d2):
    x1 = d1[0] + d1[2]/2
    y1 = d1[1] + d1[3]/2

    x2 = d2[0] + d2[2]/2
    y2 = d2[1] + d2[3]/2

    dx = x2 - x1
    dy = y2 - y1
    return int(math.sqrt(dx**2 + dy**2))


def colliderect(r1, r2, xy=["not", "not"], tolerance=10):
    if r1.colliderect(r2):
        if abs(r2.top - r1.bottom) < tolerance:
            xy = [xy[0], "bottom"]
        elif abs(r2.bottom - r1.top) < tolerance:
            xy = [xy[0], "top"]

        if abs(r2.left - r1.right) < tolerance:
            xy = ["right", xy[1]]
        elif abs(r2.right - r1.left) < tolerance:
            xy = ["left", xy[1]]
    else:
        xy = ["not", "not"]

    return xy


def collidelist(r1, list_, xy=["not", "not"], tolerance=10):
    xy = ["not", "not"]
    for r2 in list_:
        if r1.colliderect(r2):
            if abs(r2.top - r1.bottom) < tolerance:
                xy = [xy[0], "bottom"]
            elif abs(r2.bottom - r1.top) < tolerance:
                xy = [xy[0], "top"]

            if abs(r2.left - r1.right) < tolerance:
                xy = ["right", xy[1]]
            elif abs(r2.right - r1.left) < tolerance:
                xy = ["left", xy[1]]

    return xy


index = 0
def timer_per_second(secs, func_, fps):
    global index
    index += 1
    if index >= fps * secs:
        index = 0
        func_()
        return True # success
    else:
        return False # not, yet :)
