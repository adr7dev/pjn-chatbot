import subprocess
import webbrowser

aliases = [
    # alias, open name, close name
    ["chrome", "google-chrome", "chrome"],
    ["brave", "brave-browser", "brave"]
]

def proceedCommand(command):
    if(("app-open" in command) or ("app-close" in command)):
        appName = command.split()[1]
        subprocessName = ""
        subprocessKillName = ""
        for alias in aliases:
            if(appName == alias[0]):
                subprocessName = alias[1]
                if(len(alias) > 2):
                    subprocessKillName = alias[2]
                break
        
        if("app-open" in command):
            if(subprocessName == ""):
                try:
                    subprocess.Popen([appName], stderr=subprocess.DEVNULL)
                except subprocess.CalledProcessError:
                    print("Error while opening the app!")
            else:
                subprocess.Popen([subprocessName], stderr=subprocess.DEVNULL)
        else:
            if(subprocessKillName != ""):
                subprocess.run(["killall", subprocessKillName])
            elif(subprocessName != ""):
                subprocess.run(["killall", subprocessName])
            else:
                subprocess.run(["killall", appName])
                

    if("website" in command):
        address = command.split()[1]
        webbrowser.open(address, 2)

    if("file" in command):
        location = command.split()[1]
        subprocess.Popen(["xdg-open " + location + " 2> /dev/null"], shell=True) 
        
