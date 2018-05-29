#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 16:57:15 2018

@author: sbk
"""
import urllib

def read_text():
    quotes = open("/Users/sbk/PythonUdacity/python_udacity/movie_quotes.txt")
    contents = quotes.read()
    quotes.close()
    check_profanity(contents)
 
def check_profanity(check):
    conn = urllib.urlopen("http://www.wdylike.appspot.com/?q="+check)
    output = conn.read()
    conn.close()
    if "true" in output:
        print "Profinity Alert !!"
    elif "false" in output:
        print "All good words"
    else:
        print "Some error with document!"

read_text()