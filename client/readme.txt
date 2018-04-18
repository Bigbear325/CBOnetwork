cat *.JPG | ffmpeg -framerate 0.25 -f image2pipe -i - output.mkv
