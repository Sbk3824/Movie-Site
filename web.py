import webbrowser
import time

print "Break Started From", time.ctime()
for i in range(3):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=VQ2EyU75p2o&start_radio=1&list=RDVQ2EyU75p2o")
