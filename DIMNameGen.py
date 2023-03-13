#!/usr/bin/env python3
# Author: AnalogMan
# Modified Date: 2023-03-13
# Purpose: Generates Bandai Vital Bracelet Name Sprites for DIM modifications
# Usage: DIMNameGen [-h] [-n name]
# Requirements: Pillow (pip3 install Pillow)

from sys import version_info, exit
if version_info <= (3,2,0):
    print('\nPython version 3.2.0+ needed to run this script.')
    exit(1)

try: 
    from PIL import Image, ImageOps # pip3 import Pillow
except:
    print('\nDependancies missing:\npip3 install Pillow\n')
    exit(1)

import os
import argparse

def load_file(file_name: str) -> str:
        return os.path.join(os.path.dirname(__file__), file_name)

def cleanFilename(sourcestring,  removestring = "%:/,.\\[]<>*?"):
    """Clean a string by removing selected characters.

    Creates a legal and 'clean' source string from a string by removing some 
    clutter and  characters not allowed in filenames.
    A default set is given but the user can override the default string.

    Args:
        | sourcestring (string): the string to be cleaned.
        | removestring (string): remove all these characters from the string (optional).

    Returns:
        | (string): A cleaned-up string.

    Raises:
        | No exception is raised.
    """
    #remove the undesireable characters
    return ''.join([c for c in sourcestring if c not in removestring])

def main():
    
    print('\n======== DIM Name Generator ========\n\n')

    # Arg parser for program options
    parser = argparse.ArgumentParser(description='Create name sprites from string for Bandai Vital Bracelet DIM modification')
    parser.add_argument('-n', '--name', help='The name string to have generated')
    
    # Check passed arguments
    args = parser.parse_args()

    # Attempt to open alphabet sprite sheet and complain if cannot
    try:
        charsheet = Image.open(load_file("assets/VB_Alphabet_ENG.png"))
    except:
        print("Font Sprite Sheet missing: VB_Alphabet_ENG.png")
        exit(1)

    # Dictionary map letters to alphabet sprite sheet
    letters = {}
    letters["A"] = charsheet.crop((0, 0, 9, 15))
    letters["B"] = charsheet.crop((10, 0, 17, 15))
    letters["C"] = charsheet.crop((18, 0, 26, 15))
    letters["D"] = charsheet.crop((27, 0, 35, 15))
    letters["E"] = charsheet.crop((36, 0, 41, 15))
    letters["F"] = charsheet.crop((42, 0, 47, 15))
    letters["G"] = charsheet.crop((48, 0, 58, 15))
    letters["H"] = charsheet.crop((59, 0, 67, 15))
    letters["I"] = charsheet.crop((68, 0, 70, 15))
    letters["J"] = charsheet.crop((71, 0, 77, 15))
    letters["K"] = charsheet.crop((78, 0, 86, 15))
    letters["L"] = charsheet.crop((87, 0, 92, 15))
    letters["M"] = charsheet.crop((93, 0, 105, 15))

    letters["N"] = charsheet.crop((106, 0, 116, 15))
    letters["O"] = charsheet.crop((117, 0, 127, 15))
    letters["P"] = charsheet.crop((128, 0, 135, 15))
    letters["Q"] = charsheet.crop((136, 0, 146, 15))
    letters["R"] = charsheet.crop((147, 0, 154, 15))
    letters["S"] = charsheet.crop((155, 0, 163, 15))
    letters["T"] = charsheet.crop((164, 0, 170, 15))
    letters["U"] = charsheet.crop((171, 0, 179, 15))
    letters["V"] = charsheet.crop((180, 0, 190, 15))
    letters["W"] = charsheet.crop((191, 0, 204, 15))
    letters["X"] = charsheet.crop((205, 0, 215, 15))
    letters["Y"] = charsheet.crop((216, 0, 224, 15))
    letters["Z"] = charsheet.crop((225, 0, 234, 15))

    letters[" "] = charsheet.crop((235, 0, 239, 15))
    letters["-"] = charsheet.crop((240, 0, 244, 15))
    letters[":"] = charsheet.crop((245, 0, 247, 15))
    letters["."] = charsheet.crop((248, 0, 250, 15))
    letters["("] = charsheet.crop((251, 0, 255, 15))
    letters[")"] = charsheet.crop((256, 0, 260, 15))
    
    letters["1"] = charsheet.crop((261, 0, 264, 15))
    letters["2"] = charsheet.crop((265, 0, 270, 15))
    letters["3"] = charsheet.crop((271, 0, 276, 15))
    letters["4"] = charsheet.crop((277, 0, 281, 15))
    letters["5"] = charsheet.crop((282, 0, 287, 15))
    letters["6"] = charsheet.crop((288, 0, 294, 15))
    letters["7"] = charsheet.crop((295, 0, 300, 15))
    letters["8"] = charsheet.crop((301, 0, 307, 15))
    letters["9"] = charsheet.crop((308, 0, 314, 15))
    letters["0"] = charsheet.crop((315, 0, 321, 15))
    
    # List of serif letters
    serif = ["A", "M", "S", "V", "W"]

    white = (255, 255, 255)
    green = (0, 255, 0)

    if args.name:
        name = args.name.upper()
    else:
        name = input("Type name: ").upper()

    # Check that only supported characters are in name string
    for elem in name:
        try:
            letters[elem]
        except:
            print("Could not find letter " + repr(elem) + " in character sheet.")
            print("Available characters: \"A-Z -:.() 0-9\"")
            exit(1)
    
    # Check if official Bandai sprite exists
    if not os.path.exists("output"):
        os.makedirs("output")
    
    if os.path.isfile(load_file("assets/" + name + ".png")):
        print("String found amoung official Bandai sprites. Using official sprite.")
        print("Saving file to output/" + name + ".png")
        Image.open(load_file("assets/" + name + ".png")).convert("RGB").save("output/" + name + ".png")
        print("Completed Successfully.")
        exit(0)
            

    # Create starter name sprite
    canvas_w = 80
    namesprite = Image.new("RGB", (canvas_w, 15), green)

    # Set X position padding
    x = 1

    # Iterate through each letter, check how close the two adjoining letters are and add space if too close.
    for elem in name:
        x += 1
        y = 3

        # If the current X position for the next letter would go beyond the sprites current width, increase width another 80px
        if x + letters[elem].width > canvas_w:
            namesprite = ImageOps.expand(namesprite, (0, 0, 80, 0), green)
            canvas_w += 80

        # This simulates the kerning style from the officially released Vital Hero name sprites
        while y <= 12:
            if letters[elem].getpixel((0, y)) != white:
                y+=1
                continue

            if (
                namesprite.getpixel((x-2, y)) == white or
                namesprite.getpixel((x-2, y-1)) == white or
                namesprite.getpixel((x-2, y-2)) == white or
                namesprite.getpixel((x-2, y+1)) == white or
                namesprite.getpixel((x-2, y+2)) == white
            ):

                x += 1

            else:
                y += 1

        # Add letter into name sprite canvas
        namesprite.paste(letters[elem], (x, 0))
        x += letters[elem].width
        
    # Get width of actual text
    text_w = canvas_w - 1
    y = 3
    while text_w > 0:
        if namesprite.getpixel((text_w, y)) == white:
            break
        elif y < 12:
            y = y + 1
        else:
            text_w = text_w - 1
            y = 3
    # Remove two pixel border on left side
    text_w = text_w - 2
    
    # Determine left padding based on canvas width
    lmargin = 0
    if canvas_w == 80:
        # Center sprite with a left margin of at least 2px
        x = (80 - text_w) // 2
        lmargin = x - 2
    elif canvas_w == 160:
        # Add a 3px or 4px left margin based on wether the first letter is serif
        x = 3 if (name[0] in serif) else 4
        if text_w + x > 160:
            lmargin = 0
        else:
            lmargin = x - 2
    else:
        # Add a 5px or 6px left margin based on wether the first letter is serif
        x = 5 if (name[0] in serif) else 6
        if text_w + x > 240:
            lmargin = 0
        else:
            lmargin = x - 2
    if lmargin < 0:
        lmargin = 0
        
    # TODO: Check if right margin is at least 2x. If not, use alternate MON kerning
    if name[-3::1] == "MON":
        if (text_w + 2 + lmargin) > (canvas_w - 3):
            if (text_w + 2 + lmargin) == (canvas_w - 1):
                x = canvas_w - 36
            else:
                x = canvas_w - 37
            namesprite.paste(letters["M"], (x, 0))
            namesprite.paste(letters[" "], (x+12, 0))
            namesprite.paste(letters["O"], (x+13, 0))
            namesprite.paste(letters[" "], (x+23, 0))
            namesprite.paste(letters["N"], (x+24, 0))
            namesprite.paste(letters[" "], (x+34, 0))
       
    # Create new canvas to paste into
    namesprite2 = Image.new("RGB", (canvas_w, 15), green)
    tmp = namesprite.copy()
    namesprite2.paste(tmp, (lmargin,0))
        

    print("Creating sprite " + name + ", width: " + str(canvas_w) + "px")
    
    # Save result to output folder       
    print("Saving file to output/" + cleanFilename(name) + ".png")
    namesprite2.save("output/" + cleanFilename(name) + ".png")

    print("Completed Successfully.")

if __name__ == '__main__':
    main()
