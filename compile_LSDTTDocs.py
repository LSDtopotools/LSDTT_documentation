# -*- coding: utf-8 -*-
"""
    @author: smudd
    This program automates compilation of the LSDTopoTools documentation. 
"""


import os
import subprocess
from glob import glob

def compile_LSDTT_Docs():
    
    # First get all the directories
    doc_directory = os.getcwd()+os.sep
    build_directory = doc_directory+"html_build"+os.sep
    images_directory = build_directory+"images"+os.sep
    
    print("The doc directory is: "+ doc_directory)

    
    # create an image directory if none exists
    if not os.access(images_directory,os.F_OK):
        print("I didn't find an images directory so I am making one.")
        os.mkdir(images_directory)
    
    # Now go through all the documentation folders adding the html files
    for dirname in glob(doc_directory+"LSDTT*"):
        print("This directory is: "+ dirname+os.sep)
        
        
        
        # Call bundle exec from the directory
        print("Compiling the html.")
        os.chdir(dirname)
        
        # Check to see if a gemfile.lock is in the directory
        if (os.path.isfile('./Gemfile.lock')):
            print("I found a gemfile.lock file.")
            print("If compilation fails, you can try to delete this file.")
        
        subprocess.call(['bundle','exec','rake','book:build_html'])
        
        # copy the html file into the html build directory
        for htmlname in glob(dirname+os.sep+"*.html"):
            split_line = htmlname.split(os.sep)
            new_html = doc_directory+'html_build'+os.sep+split_line[-1]
            #print("The old location of the file is:")
            #print(htmlname)
            
            #print("The new location of the file is:")
            #print(new_html)
            subprocess.call(['cp',htmlname,new_html])
            
        # Search for an image directory
        if os.access(dirname+os.sep+"images",os.F_OK):
            #print("I found an images directory")
            for imagename in glob(dirname+os.sep+"images"+os.sep+"*"):
                #print("The image name is: ")
                #print(imagename)
                split_line = imagename.split(os.sep)
                new_image = doc_directory+'html_build'+os.sep+"images"+os.sep+split_line[-1]
                subprocess.call(['cp',imagename,new_image])
        
        
        os.chdir(doc_directory)
        
        # now copy the files into the html build directory
        
    
    
if __name__ == "__main__":
    print("Welcome to the script that compiles LSDTopoTools documentation!")
    print("For this to work you need our Ruby + Asciidoctor toolchain installed.")
    print("You can do that using our docker container.")
    print("===========================================")
    print("Instructions:")
    print("https://hub.docker.com/r/lsdtopotools/lsdtt_docs_docker")
    compile_LSDTT_Docs()   