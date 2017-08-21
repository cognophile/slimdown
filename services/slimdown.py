import os
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