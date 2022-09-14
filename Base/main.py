import time
import keyboard
from pystyle import Colors, Colorate

print(Colorate.Horizontal(Colors.rainbow, """
      
 █████╗ ███████╗██╗  ██╗    ███████╗ ██████╗██████╗ ██╗██████╗ ████████╗
██╔══██╗██╔════╝██║ ██╔╝    ██╔════╝██╔════╝██╔══██╗██║██╔══██╗╚══██╔══╝
███████║█████╗  █████╔╝     ███████╗██║     ██████╔╝██║██████╔╝   ██║   
██╔══██║██╔══╝  ██╔═██╗     ╚════██║██║     ██╔══██╗██║██╔═══╝    ██║   
██║  ██║██║     ██║  ██╗    ███████║╚██████╗██║  ██║██║██║        ██║   
╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝                                                                                                                                                             
      """))

print("Press F2 to start the scipt !")
print("Hold F3 a few seconds to stop the script !")

azerty = "z"
qwerty = "w"

def afk():
    loop = True
    while loop:
        if keyboard.is_pressed("F3"):
            loop = False
        else:
            time.sleep(2)
            keyboard.press_and_release("escape")
            time.sleep(0.5)
            keyboard.press_and_release("escape")
            time.sleep(0.5)
            keyboard.press(azerty)
            time.sleep(1)
            keyboard.release(azerty)
            keyboard.press(qwerty)
            time.sleep(1)
            keyboard.release(qwerty)
            time.sleep(0.5)
            keyboard.press("s")
            time.sleep(1)
            keyboard.release("s")

start = True
while start:
    if keyboard.is_pressed("F2"):
        print("\nScript successfully start :)")
        start = False 
        afk()

        
        


            
