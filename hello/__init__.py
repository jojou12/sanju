import webbrowser
import time
#print("hello")
#a="nielit"
#print (a)
url1="https://www.youtube.com/watch?v=qWnzMwT6SKo"
url2="https://www.youtube.com"
url3="https://www.facebook.com"
i=0
while(i<3):
    time.sleep(15)
    webbrowser.open_new(url1)
    time.sleep(15)
    webbrowser.open_new(url2)
    time.sleep(15)
    webbrowser.open_new(url3)
    i=i+1