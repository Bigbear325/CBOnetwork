#! /bin/bash

VBR="2500k"                                   
FPS="30"                                      
QUAL="medium"                                 
YOUTUBE_URL="rtmp://a.rtmp.youtube.com/live2" 

SOURCE="/Users/lzhmbp/Documents/GitHub/CBOnetwork/twitpy/client/out/output.mp4"            
KEY="xxb0-fbky-24sc-a2s0"

ffmpeg \
    -i "$SOURCE" -deinterlace \
    -vcodec libx264 -pix_fmt yuv420p -preset $QUAL -r $FPS -g $(($FPS * 2)) -b:v $VBR \
    -acodec libmp3lame -ar 44100 -threads 6 -qscale 3 -b:a 712000 -bufsize 512k \
    -f flv "$YOUTUBE_URL/$KEY"
