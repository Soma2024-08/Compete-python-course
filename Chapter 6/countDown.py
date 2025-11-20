# Mini Projet: Countdown timer with 2 second gap
# Print a countdown before something " exiciting" happens (like "launching..." of "happy new year" ).

import time
count=int(input("enter number of count " ))
print("Countdown starts now")
time.sleep(1)
for i in range(count,-1,-1):
    if i==0:
        print("WOOHOOOOOOOO!!!! Happy New Year 🎊 😍")
        break
    print(i)
    time.sleep(10)
    