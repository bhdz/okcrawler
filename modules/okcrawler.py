#!/usr/bin/env python

# This is my :local: content imports. My ::stuff: here, so :it::went::to::the::top.:
from okcrawli.pulo import Labeled, Node, Eye
from okcrawli.iface import *

# These are all the Pythonic imports I need


#from yaml import *

# Haha! We .forgot: about _that_ guy.
import threading

#######################################################
# Public Interface::
#  All functions: here::
#   must :accept::
#       *) ONE ARGUMENT and
#       *) A keyword dictionary
# These are PUBLIC interface so they should be left
#   DE-COUPLED as much as possible
#  ONE FUNCTION, ONE UNIT, ONE TRANSLATION
#  This .is. single-threaded for now.
#
######################################################
######################################################
#
# Sheme for Three-Group Pool-Threaded
#  Software
#
# Three-thread:groups!!
# Thread-group:: One    ::Pool1 !and Pool2 ::
#   This thread-group DOWNLOADS and PASSES info to the other groups
#
# Thread-group: Two     ::Pool1 ::
#   This one parses _ONLY_
#
# Thread-group Three:   ::Pool1 ::
#   This one aggrees and DUMPS info
#
##############################################################

def check_walk_path():
    paths = walk_path("/home/dakkar/Desktop/do", 
                      filters = ['*.xml', '*.dat', '*.index', '*.java'],
                      only_files = True)
    for p in paths:
        print "path =", p
        
def check_readout_file():
    contents = readout_file('/home/dakkar/Desktop/words')
    print "<", contents,">"
    print dump_file(contents, path = '/home/dakkar/Desktop', filename = "words.2")
    
def check_download_file():
    the_file = download_file(
                "http://i.fappyness.com/processed/Z1Rv4LxZUFVJ4yHg94IcGWaV8glIFH.jpg")

    dump_file(the_file['response'].content, path = '/home/dakkar/Desktop', 
              filename = the_file['local_filename'])
#
# Ha. Ha. MAin functionality... for now this is a SINGLE module, NO PACKAGING. LOL.

def check_parse_out():
    the_file = download_file('http://fappyness.com/')
    

    contents = the_file['response'].content
    dump_file(contents, path = "/home/dakkar/Desktop", filename = "out.html")
    tags = parse_out(contents)
    for tag in tags:
        print "tag['href'] =", tag['href']

def check_gather_links():
    pass

if __name__ == "__main__":
    #check_walk_path()
    #check_readout_file()
    #check_download_file()
    check_parse_out()
    
def main():
    constraints =  {'listage': True,
                    'simple': True,
                    'dumpfile_location': 'okkrawler.d/',
                    'match_filters': ['xxx.crawl'],
                    'miss_filters': None
                    }

    downloaded = []
    filenames = walk_path(os.curdir, **constraints )
    print "filenames>>", filenames

    for filename in filenames:
        lines = readout_file(filename, **constraints)

        print "bytes>>", lines

        for line in lines:
            response = download_file(line, **constraints)
            links = parse_out(response, **constraints)

    processed = []
    links = [] # `Finally!
    for uri in iter(processed):
        contents = download_file(uri, **constraints)
        links.append(parse_out(contents))
    gather_links(links)

#
# A much needed Borg, this DOES something LOCALLY...
# RAdical DEsign, RAdiCAL iDEAS
#
def os_mkdir_p(directory, **options):
    pass

# The Borg in question. Needed for further Expanding of this Story (okcrawling@okcrawler)
# This Borg should work like this... Each state is NOTED and before calling the 'os_*' functions
# It should::
#  1) LOCK all OS resources for everyone in THIS process SPACe
#  2) wait for them processors to stop porcessing
#  3) Do it's dirty bizz, and you know..
#  4|*) Release all locking, and unlock the ADRESS SPACE for '*'
class Mk(object):
    __state_funcs = {
        'os_mkdir_p': None,
        'os_touch': None,
        'os_write_out': None,
        'os_read_in': None,
    }
    def __init__(self, first, *arguments, **context):
        # WE certainly DON'T need no stinkin' Sniggletton!!
        self.__dict__ = Mk.__state_funcs

