#sudo apt-get install ibus-m17n
#sudo chmod 777 /usr/share/m17n
#sudo chmod 777 /usr/share/m17n/icon
#docker run -p 6070:80 dorowu/ubuntu-desktop-lxde-vnc
import subprocess
import time


logo = """
bbbbbbbb
b::::::b              iiii   jjjj                                         ffffffffffffffff      iiii
b::::::b             i::::i j::::j                                        f::::::::::::::::f   i::::i
b::::::b              iiii   jjjj                                         f::::::::::::::::::f  iiii
 b:::::b                                                                  f::::::fffffff:::::f
 b:::::bbbbbbbbb    iiiiiiijjjjjjj   ooooooooooo yyyyyyy           yyyyyyyf:::::f      ffffff iiiiiiii xxxxxxx      xxxxxxx
 b::::::::::::::bb  i:::::ij:::::j oo:::::::::::ooy:::::y         y:::::y f:::::f             i::::::i  x:::::x    x:::::x
 b::::::::::::::::b  i::::i j::::jo:::::::::::::::oy:::::y       y:::::y  f::::::::::::f       i::::i   x:::::x  x:::::x
 b:::::bbbbb:::::::b i::::i j::::jo:::::ooooo:::::o y:::::y     y:::::y   f::::::::::::f       i::::i    x:::::xx:::::x
 b:::::b    b::::::b i::::i j::::jo::::o     o::::o  y:::::y   y:::::y    f:::::::ffffff       i::::i     x::::::::::x
 b:::::b     b:::::b i::::i j::::jo::::o     o::::o   y:::::y y:::::y     f:::::::ffffff       i::::i      x::::::::x
 b:::::b     b:::::b i::::i j::::jo::::o     o::::o    y:::::y:::::y      f:::::f              i::::i      x::::::::x
 b:::::b     b:::::b i::::i j::::jo::::o     o::::o     y:::::::::y       f:::::f              i::::i     x::::::::::x
 b:::::bbbbbb::::::bi::::::ij::::jo:::::ooooo:::::o      y:::::::y       f:::::::f            i::::::i   x:::::xx:::::x
 b::::::::::::::::b i::::::ij::::jo:::::::::::::::o       y:::::y        f:::::::f            i::::::i  x:::::x  x:::::x
 b:::::::::::::::b  i::::::ij::::j oo:::::::::::oo       y:::::y         f:::::::f            i::::::i x:::::x    x:::::x
 bbbbbbbbbbbbbbbb   iiiiiiiij::::j   ooooooooooo        y:::::y          fffffffff            iiiiiiiixxxxxxx      xxxxxxx
                            j::::j                     y:::::y
                  jjjj      j::::j                    y:::::y
                 j::::jj   j:::::j                   y:::::y
                 j::::::jjj::::::j                  y:::::y
                  jj::::::::::::j                  yyyyyyy
                    jjj::::::jjj
                       jjjjjj
                by Ahamed Alif (Alva) 
                github:https://github.com/AhamedAlif
"""

print(logo)



def run_command(command):
    subprocess.run(command, shell=True, check=True)

def main():

    try:      
        
        print("Updating package lists...")
        run_command("sudo apt update")
        print("Package lists updated.")
        
        time.sleep(1)
        run_command("clear")

        print("Upgrading packages...")
        run_command("sudo apt upgrade -y")
        print("Packages upgraded.")
        
        time.sleep(1)
        run_command("clear")
        
        print("Installing requirement...")
        run_command("sudo apt-get install --reinstall ibus-m17")
        print("Install successful ")
        
        time.sleep(1)
        run_command("clear")
        
        print("Giveing permission...")
        run_command("sudo chmod 777 /usr/share/m17n")
        run_command("sudo chmod 777 /usr/share/m17n/icons")
        print("Successful")
        
        time.sleep(1)
        run_command("clear")
        
        print("Downloading Bijoy_Linux")
        run_command("cd Bijoy_Linux")
        print("Downloaded")
        
        
        time.sleep(1)
        run_command("clear")
        
        print("Copying file...")
        run_command("sudo cp 'bn-bijoyClassic.png' 'bn-bijoyUnicode.png' /usr/share/m17n/icons")
        print("File Copyed")
        
        time.sleep(1)
        run_command("clear")
        
        print("Moving file...")
        run_command("mv bn-bijoyClassic.mim /usr/share/m17n/bn-bijoyClassic.mim") 
        run_command("mv bn-bijoy.png /usr/share/m17n/icons/bn-bijoyClassic.png ")
        run_command("mv bn-bijoy.mim /usr/share/m17n/bn-bijoyUnicode.mim")
        run_command("mv bn-bijoy.png /usr/share/m17n/icons/bn-bijoyUnicode.png")
        print("File moved...")
        
        time.sleep(0.5)
        
        print("Restarting ibus..")
        run_command("sudo chmod 777 /var/lib/dpkg/info/m17n-db.list")
        
        file_path = "/var/lib/dpkg/info/m17n-db.list"
        lines_to_add = [
    "/usr/share/m17n/icons/bn-bijoyClassic.png",
    "/usr/share/m17n/bn-bijoyClassic.mim",
    "/usr/share/m17n/icons/bn-bijoyUnicode.png",
    "/usr/share/m17n/bn-bijoyUnicode.mim"
    ]
        with open(file_path, "a") as file:
            for line in lines_to_add:
                file.write(line + "\n")
        print("Lines added successfully.")

        
        
    except subprocess.CalledProcessError as e:
        print("An error occurred:")
        print(e.stderr)

if __name__ == "__main__":
    main()
