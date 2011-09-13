#!/usr/bin/python

from optparse import OptionParser,OptionGroup

import re
import sys
import os
from stat import *
import subprocess
import shlex
import hashlib
import time
import datetime


options = None
args = None
mts_file_list = []


def find_files():
    global options, args, mts_file_list
    
    recursive_find_mts(options.input_folder, mts_file_list)

def recursive_find_mts(dir, mts_list):
    for item in os.listdir(dir):
        if os.path.isfile("%s/%s" % (dir, item)) and ('.mts' in item.lower()):
            mts_list.append("%s/%s" % (dir, item))
        elif os.path.isdir("%s/%s" % (dir, item)):
            recursive_find_mts("%s/%s" % (dir ,item), mts_file_list)


def convert():
    global options, args, mts_file_list
    
    for file in mts_file_list:
        mts_regex = re.compile('\.mts', re.IGNORECASE)
        out_filename = mts_regex.sub('.mov', os.path.basename(file))
        if options.date_filename:
            ctime_str = datetime.datetime.fromtimestamp(os.stat(file)[ST_CTIME]).strftime('%Y-%m-%d_%H-%M-%S')
            out_filename = "%s_%s" % (ctime_str, out_filename)
        if not (options.filename_prefix == None):
            out_filename = "%s_%s" % (options.filename_prefix, out_filename)
        
        ffmpeg_cmd = "ffmpeg -i '%s' -vcodec copy -acodec pcm_s16le '%s/%s'" % (file, options.output_folder, out_filename)
        exec_cmd(ffmpeg_cmd)


def exec_cmd(cmd):
    out=subprocess.PIPE
    if options.verbose:
        print "Executing:"
        print cmd + "\n"
        out=None
    process = subprocess.Popen(shlex.split(cmd), stdout=out, stderr=out)
    if process.wait() != 0:
        print "Something went wrong."
        if not options.verbose:
            print "You may use verbose (non-quiet mode)."


def parse_args():
    global options, args

    parser = OptionParser(usage="%prog -i INPUT_FOLDER -o OUTPUT_FOLDER", version="%prog 0.1")
    
    # directory options
    parser.add_option("-i", "--input", dest="input_folder", help="AVCHD-Folder")
    parser.add_option("-o", "--output", dest="output_folder", help="Output-Folder")
    parser.add_option("-d", "--date-filename", action="store_true", dest="date_filename", help="Use file creation date (Filesystem value, not read from metadata)")
    parser.add_option("-n", "--filename-prefix", dest="filename_prefix", help="Output filename prefix")
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False, help="Be verbose and print the ffmpeg output here")
    
    (options, args) = parser.parse_args()

    if (options.output_folder == None) or (options.input_folder == None) or not (os.path.isdir(options.output_folder) or os.path.isdir(options.input_folder)):
            print >> sys.stderr, "Error: You have to give an input folder and an output folder!\n"
            parser.print_help()
            exit(1)


def main():
    print "Starting mts2mov.py at '%s'\n\n" % (time.ctime())
    
    parse_args()
    find_files()
    convert()
    
    print "\n\nEnding mts2mov.py at '%s'" % (time.ctime())


if __name__ == "__main__":
    main()