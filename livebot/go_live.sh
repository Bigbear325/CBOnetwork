ffmpeg -re -loop 1 -framerate 2 -i ./pieces/%00d.png -i ./1MG.ogg -c:a aac -s 256x256 -ab 128k -maxrate 2048k -bufsize 2048k -framerate 30 -g 60 -strict experimental -f flv rtmp://a.rtmp.youtube.com/live2/*******