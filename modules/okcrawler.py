#!/usr/bin/env python

# This is my :local: content imports. My ::stuff: here, so :it::went::to::the::top.:
from puley import Labeled, Node, Eye

# These are all the Pythonic imports I need
import os, sys, re
import requests
import sqlalchemy
import BeautifulSoup
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
##############################################################

#
# Utility function
#
def echo(something, **context):
    print "echo! -> [something] -> {context} -> **&STDOUT"

#
# Walks about a path (directory)
#   Returns: Filtered Content
#    Pass filters through constraints:: 'match_filters' => ? and 'miss_filters'
#  Openbsd "Style" LOL
#
def walk_path(path, **constraints):
    print "walkabout! -> matching! -> [filtered file-info]"
    filtered = []

    match_filters = []
    miss_filters = []

    match_filters= constraints['match_filters']
    miss_filters = constraints['miss_filters']

    # pattern = re.compile(r'.*\.png')


    filtered = [ lambda x: x not in miss_filters for x in iter(filtered) ]
    filtered = constraints['match_filters'] # easy patch

    return filtered

#
# Reads out a file and RETURNS FILE content OBJECT
#   LOL that is simply the file in [lines]
#   PASS all needed info in the constraints, please
#
def readout_file(name, **constraints):
    print "readout_file! -> {constraints} -> [File contents ]"
    lines = []
    with open(name) as f:
        for line in f:
            lines.append(line)
    return lines

#
#  Takes what's left of {readout_file} and {DUMPS} it on the disk.. erhmmm.. solidst... erhm...
#   harddrive erhm.... whatever.. "LOCAL" PERSISTENCY "PROVIDER"...
#  LOCAL means LOCALLY ENTWINED, "CONSIDERATIONS"
#
def dump_file(contents, **context):
    print "dump_file! -> filesystem!?"
    local_path = context['dumpfile_location']
    local_filename = context['filename']
    with open(local_filename, 'wb') as f:
        f.write(contents)
        f.flush()

#
# Give me an URL and I Giv you RESPONSE object... LOL REQ/RESP.
#
def download_file(url, **postguide):
    print "download_file! -> response!?"
    local_filename = url.split('/')[-1]
    postguide.update(filename = local_filename)

    r = requests.get(url) #, stream=True)
    return r

#
# This parses contents..
#
def parse_out(contents, **context):
    print "parse_out! Parsing!?"
    soup = BeautifulSoup(contents)
    targets=soup.findAll('a') #,{'class':'institution'})

    links = []
    for each_target in targets:
        print each_target['href']+","+each_target.string
    return links

#
# Upon PARSE-age EVENT, this gathers the links...
#
def gather_links(links, **context):
    print "gather_links! gather_links"
    pass

#
# Ha. Ha. MAin functionality... for now this is a SINGLE module, NO PACKAGING. LOL.
#
if __name__ == "__main__":

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
#  yeah it's a HARSH little BORG that needs LOCKS for that on EACH instantation instance
#    e.g when a Borg exemplar is being chosen by the m = Mk(locks = {'locks'...})
#     This file needs to be seen by a Hacker or a seasoned Professional (such as me ;)) OLOL!
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

#:~snip snip::~ ~section@file
############################################################################
# WARNING WARNING WARNING!
# This is unfinished, botched-up, taken-again, did something else, DESIGN
#  Hail Eris! Hail Multi-threading! Hail Objects!
#
############################################################################
############################################################################
# License: BSD Style mothaf$&cka! LOL "Style"... I am so ronery right-now
# This file's going to Zed... fo! science! Fo Edumacacion! LOLer kopteeeer!
#&        ## Functional... here I come... So wasaterd right now...
# Freedom Kode!
# NEXT? Ichooser, iCollectOrz, the damned word... gone.. in the :past:
# Ah yes! It's... iFinderz,... Finda.py... findar.py...
# This CRAWLER collects mainly META-DATA
# This .CRAWLER: was made to _((collect? Meta-data))
# Yes. It can be used for DIRTY DEEDS by EVIL Nature'd People (Tm: EVIL-ness META-PHYSICAL ESSAY commin'
# ... HAAAEEET moar. G-P-F*cking-El for iFinda...
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$-
#$--
# $VALUE::default_value:: --check=file.system.ok --fsck=online /etc/*? Restored.
# End.
# This? Charmi line
# Also? (Alf? **Charmi .is. not Charm, it's an interpreter)
#  Tag-line? ** Charmy language, Charmi interpreter. KILLER of SQL.
# Help:: {! wave ~ completed ~ 0 !}
#               #          #
#  Tag-line? (advertising:: *Charm, [this is]Charm, Killer of S?Q??L??)
#  Tag-line? Hacking | (eating;: **dead projects) | (Default? Reading; Writting; Integrating ** Al-at-once)
#  Tag-line??
#     Bro:: Zed.Satani--sta
#&        Bro:: I love.. you... not in a sexual way, I promise... :'-/
#
#&(plug-bait)
# YAML + Charmi => Destroya!? Of Worlds!? Yeeeesssssss... a pinch of $vil is needed...
# !/bin/cat[out]/put:: LOL? LOL! LOL? LOLERKOPTER. LULZy file
#############################################################################
# Clean line, Clean bill of Health, also, non-taker of Creddits and Debbits
#############################################################################
# ASCII ART:: <<= LOL =>>=> @at your kode man.. No Automake.am, such a looooserrr! LOL
# YAML!!
# something: Here
#              -also here! LOL
# something: Else
#              --also here! Ahahahahahah
# Stackish? a]] b]] c]] what was it again, dawg? ** why not friends anymore, long time no -see ( want to -destroy u)
# In a FAIR fight ... I studied Ai-ki-do as a small child.. KAN you BEAR the MIGHT of my BREATH-LOLZ!?
# K'heeeeeeeeeee'Aye!!!
#:~