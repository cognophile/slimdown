#!/usr/bin/env python3
from argparse import ArgumentParser

from services.slimdown import Slimdown
from helpers.filehelper import FileHelper
from helpers.mdurlhelper import MarkdownUrlHelper

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