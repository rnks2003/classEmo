import ollama
import cv2

import os
os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/bin/ffmpeg"

from fer import FER

detector = FER(mtcnn=True)

msg = 'Hello'
response = ollama.chat(model='phi',messages=[{'role':'user','content':msg}])

state = True
reiter = 0

while True and reiter < 3:
    if state: 
        msg = input('Prompt : ')
        msgLen  = len(msg)
    
    if msg!='exit' : response = ollama.chat(model='phi',messages=[{'role':'user','content':msg}])
    else : break

    print(response['message']['content'])
    
    frame = cv2.imread('/Users/rnks/Pictures/Photo Booth Library/Pictures/Photo on 24-05-24 at 3.41 PM.jpg',1)[:,:720,:]
    emotion, score = detector.top_emotion(frame)
    
    if emotion != 'happy' : 
        state = False
        msg = f'Could you regenerate response for ""{ msg[36:msgLen] if len(msg)!=msgLen else msg}"" in a simplar form ? I am not happy with this response...'
        reiter += 1
    
    else: state = True
    print("\n\n>>>\n\n")
    