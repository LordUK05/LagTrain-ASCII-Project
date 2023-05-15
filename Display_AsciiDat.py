#display asciidata
import os,time
dat = open("DAT_200.asciidata","r")
content = dat.read()
frames = content.split("¬")
time.sleep(1)

count = 0
os.system("Music.mp3")
time.sleep(0.2)
for each in frames:
    count=count+1
    last_call = time.perf_counter()
    print(frames[count]+str(count))
    time.sleep(0.0877777)
    
    
