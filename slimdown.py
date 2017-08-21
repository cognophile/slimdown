#!/usr/bin/env python3
import os
from argparse import ArgumentParser

from helpers.filehelper import FileHelper
from helpers.mdurlhelper import MarkdownUrlHelper
from services.htmltomd import HtmlToMarkdown

class Slimdown():
    def __init__(self):
        self.__markdownOutput = []

    def __setMarkdownOutput(self, data):
        self.__markdownOutput = data

    def parse(self, htmlFile):
        """Passes the HTML file to the Markdown parser. Gets the resulting md and stores it in its own property"""
        htmlToMdParser = HtmlToMarkdown()
        htmlToMdParser.readFile(htmlFile)
        self.__setMarkdownOutput(htmlToMdParser.getMarkdown())
    
    def __writeToFile(self, mdFile):
        """Write selfs markdown data to file"""
        with open(mdFile, 'a') as writer:
            for line in self.__markdownOutput: 
                writer.write(line)

    def outputMarkdown(self, mdFile):
        """Public method to coordinate the writing out of markdown"""
        if os.path.exists(mdFile):
            os.remove(mdFile)

        self.__writeToFile(mdFile)


# Execution point 
Slimdown = Slimdown()
FileHelper = FileHelper()
UrlHelper = MarkdownUrlHelper()
ArgParser = ArgumentParser(description='Simple HTML to Markdown converting.')

ArgParser.add_argument('-f', '--file', dest='fileName', required=True, help="the path of the file to read", metavar="FILE")    
path = ArgParser.parse_args()
htmlFile = path.fileName

if FileHelper.isFileHtml(htmlFile):
    try:
        Slimdown.parse(htmlFile)

        mdFile = FileHelper.filenameToMarkdown(htmlFile)
        Slimdown.outputMarkdown(mdFile)

        UrlHelper.repair_links(mdFile)

    except FileNotFoundError:
        print("Supplied file or path cannot be found: '{}'".format(htmlFile))
    except Exception as ex:
        print("An error occured. Please, try again: ", ex)
else:
    print("Incorrect file type. Ensure the file is '.html'.")