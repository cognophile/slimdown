#!/usr/bin/env python3
import os
from argparse import ArgumentParser

from helpers.filehelper import FileHelper
from services.htmltomd import HtmlToMarkdown

class Slimdown():
    markdownOutput = []

    def __setMarkdownOutput(self, data):
        self.markdownOutput = data

    def parse(self, htmlFile):
        htmlToMdParser = HtmlToMarkdown()
        htmlToMdParser.readFile(htmlFile)
        self.__setMarkdownOutput(htmlToMdParser.getMarkdown())
    
    def __writeToFile(self, mdFile):
        with open(mdFile, 'a') as writer:
            for line in self.markdownOutput: 
                writer.write(line)

    def outputMarkdown(self, htmlFile):
        helper = FileHelper()
        mdFile = helper.filenameToMarkdown(htmlFile)
        
        if os.path.exists(mdFile):
            os.remove(mdFile)

        self.__writeToFile(mdFile)


# Execution point 
slimdown = Slimdown()
helper = FileHelper()
argumentParser = ArgumentParser(description='Simple HTML to Markdown converting.')

argumentParser.add_argument('-f', '--file', dest='fileName', required=True, help="the path of the file to read", metavar="FILE")    
path = argumentParser.parse_args()
htmlFile = path.fileName

if helper.isFileHtml(htmlFile):
    try:
        slimdown.parse(htmlFile)
        slimdown.outputMarkdown(htmlFile)

    except FileNotFoundError:
        print("Supplied file or path cannot be found: '{}'".format(htmlFile))
    except Exception as ex:
        print("An error occured. Please, try again: ", ex)
else:
    print("Incorrect file type. Ensure the file is '.html'.")

