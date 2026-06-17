#before running the script install the rembg library (pip install rembg)
#also install (pip install "rembg[cpu]")

from rembg import remove
from PIL import Image
import os

print("--- Background Remover ---")
print()

while True:  #Loop
    path = input("Enter your image path here: ")
    path = path.strip()
    path = path.replace('"', '')  
    path = path.replace("'", '')   
    path = path.strip()

    if not os.path.exists(path):
        print("File path not found! Please try again.")

    else:
        base, ext = os.path.splitext(path)
        output_path = base + "_no_background.png"
        print("\nOpening image...")
        
        input_image = Image.open(path)
        print("Removing background....")
        print("This may few second,please wait.")

        output_image = remove(input_image)
        output_image.save(output_path)
        
        print("Removing background done!")
        print("Saved as:", output_path)
    print()
    again = input("Do you want to remove another background> (y/n)")
    again = again.strip().lower()

    if again == "n":
        print("Thanks for using removebg!")
        break
