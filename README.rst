==================================
mts2mov - Mac AVCHD cutters friend
==================================

mts2mov is a little helper script for converting MTS-files from AVCHD-cameras to mov containers. After this the footage can easily be imported with Final Cut.

**DISCLAIMER:** In the current state the script is a bit ugly and a kind of hacked, but it works perfectly for me. But I can't quarante that this script works for in all cases and that it doesn't damage everything.

Installation
------------
You need ffmpeg installed and usable via Terminal - it have to be in your PATH.

All you have to do then is to simply clone the repository and execute ./mts2mov in a Terminal giving it the needed parameters.

Usage
-----
    Usage: mts2mov.py -i INPUT_FOLDER -o OUTPUT_FOLDER

    Options:
      --version             show program's version number and exit
      -h, --help            show this help message and exit
      -i INPUT_FOLDER, --input=INPUT_FOLDER
                            AVCHD-Folder
      -o OUTPUT_FOLDER, --output=OUTPUT_FOLDER
                            Output-Folder
      -d, --date-filename   Use file creation date (Filesystem value, not read
                            from metadata)
      -n FILENAME_PREFIX, --filename-prefix=FILENAME_PREFIX
                            Output filename prefix
      -v, --verbose         Be verbose and print the ffmpeg output here