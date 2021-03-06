import glob
import numpy as np
from moviepy.editor import *

width=640
height=480

def main():
    image_list = glob.glob(r'IMAGE NAME')
    print(image_list)

    image_list.sort()


    clips = [] 
    for m in image_list:
        clip = ImageClip(m).set_duration('00:00:00.50')
        clip = clip.resize(newsize=(width,height))
        clips.append(clip)


    concat_clip = concatenate_videoclips(clips, method="compose")
    concat_clip.write_videofile(r"output2.mp4", fps=24,write_logfile=True,)
    
if __name__ == '__main__':
    main()
