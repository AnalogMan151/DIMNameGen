# DIM Name Gen
A utility to generate Bandai Vital Bracelet compatible name sprites

Usage: DIMNameGen.exe [-h] [-n NAME]

Running the utility by itself will bring up a prompt to type a name. The name will be saved into an output folder.
Passing the argument -n followed by a name in quotations will generate that name without the interactive prompt.

Included in the repo is an example batch file for bulk creating sprites. Create a TXT file with the names you want, one per line, then drag and drop the TXT file onto the BAT file. It will generate all the names in the TXT and name the folder the same as the TXT filename. 

This utility was written in python and converted to stand-alone executable with Nuitka.

To use the python script:

Usage: DIMNameGen.py [-h] [-n NAME]

1. Click the green Code button  towards the top followed by Download ZIP. Extract the files to any folder.
2. You will need an install of python3. Either from https://www.python.org/ or from the Windows Store.
3. Once python is installed you will need to install the Pillow dependency by opening terminal/command prompt and typing `pip install Pillow`
4. Once Pillow is installed you can run the script from terminal/command prompt with `python DIMNameGen.py` or use the included BAT file to make use of the TXT file drag and drop.