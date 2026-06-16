import os
import sys
from PIL import Image
from PIL.ExifTags import TAGS
from pystyle import Center, Colorate, Colors, Anime
from colorama import Fore
import os

os.system('cls')
print(Colorate.Horizontal(Colors.blue_to_cyan,"""
▄▄▄▄  ▄▄▄  ▄▄▄▄                                 
▀███  ███  ███▀                                 
 ███  ███  ███ ██ ██ ███▄███▄ ████▄ ██ ██ ▄█▀▀▀ 
 ███▄▄███▄▄███ ██ ██ ██ ██ ██ ██ ██ ██ ██ ▀███▄ 
  ▀████▀████▀  ▀██▀█ ██ ██ ██ ████▀ ▀██▀█ ▄▄▄█▀ 
                              ██                
                              ▀▀                

                ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                ┃ Author : Wumpus             ┃
                ┃ Discord: .gg/datas          ┃
                ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                          
"""))
def get_image_metadata(image_path):
    if not os.path.exists(image_path):
        print(Fore.RED + "Erreur")
        return
    
    try:
        with Image.open(image_path) as img:
            print(f"Format : {img.format}")
            print(f"Mode : {img.mode}")
            print(f"Size : {img.size} pixels")
            
            exif_data = img._getexif()
            if exif_data:
                print("\n--- Metadatas EXIF ---")
                for tag_id, value in exif_data.items():
                    tag = TAGS.get(tag_id, tag_id)
                    print(f"{tag}: {value}")
            else:
                print("No Metadatas finds.")
    except Exception as e:
        print(Fore.RED + f"Erreur : {e}")

if __name__ == "__main__":
    image_path = input("Image Path : ")
    get_image_metadata(image_path)
    input(Fore.RED + "Press enter to exit..")