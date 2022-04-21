import time

with open('jpeg_still_list.txt', 'w') as jpeg_list:
    from subprocess import check_call  
    count = 0
    tlcount = 0
    while True:
        check_call(["raspistill", "-w", "1920", "-h",
                    "1080", "-q", "80", "-o", "frames{}.jpg".format(count)])
        jpeg_list.write("frames{}.jpg".format(count))
        time.sleep(60)
        count += 1
        if count == 180:
            count = 0
        check_call(["mencoder", "-nosound", "-ovc", "lavc", "-lavcopts",
                    "vcodec=mpeg4:aspect=16/9:vbitrate=8000000", "-vf",
                    "scale=1920:1080", "-o", "lol", "-mf",
                    "type=jpeg:fps=24", "mf://@jpeg_still_list.txt"])
