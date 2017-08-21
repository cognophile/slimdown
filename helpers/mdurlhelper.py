import re
import os
from helpers.filehelper import FileHelper

class MarkdownUrlHelper():
    """Provides URL formatting repair functionality for markdown files"""
    LINK_TEXT = 5
    HYPERLINK = 2
    BROKEN_URL_PATTERN = r'(\[\])(\(http[s]?:\/\/(?:www.?)?([^?#]*)\.(.+)\))(.+)'
        
    def __init__(self):
        self.FileHelper = FileHelper()

    
    def repair_links(self, originalFile):
        """Repairs the specific misformatting of inline markdown links in the markdown file passed in"""
        if not originalFile:
            print("Filename appears to be incorrect. Unable to repair links.")
            return
        
        fileCopy = self.FileHelper.duplicateMarkdownFile(originalFile)
        self.__copyContents(originalFile, fileCopy)

    def __copyContents(self, originalFile, fileCopy):
        """Coordinates correcting links while copying file contents"""
        if os.path.exists(fileCopy):
            os.remove(fileCopy)

        urlRegex = self.__compileRegex()

        try:        
            with open(originalFile, 'r') as input, open(fileCopy, 'w') as output:
                for line in input:
                    match = urlRegex.search(line, re.IGNORECASE)
            
                    if match: 
                        newLine = self.__buildNewLine(match, line, self.__getUrlPattern())
                        output.write(newLine)
                    else:
                        output.write(line)
        except IOError as ex:
            print("Unable to read '{0}' or write to '{1}' to fix links: ".format(originalFile, fileCopy), ex)

        self.FileHelper.removeFile(originalFile)
        self.FileHelper.renameFile(fileCopy, originalFile)

    def __compileRegex(self):
        """"Returns the compiled broken url pattern Regex (SRE_pattern)"""
        return re.compile(self.__getUrlPattern())

    def __getUrlPattern(self):
        return self.BROKEN_URL_PATTERN

    def __buildNewLine(self, match, line, pattern):
        """Returns the line contents with correct markdown inline link formatting"""
        url = "[{0}]{1}".format(match.group(self.LINK_TEXT), match.group(self.HYPERLINK))
        return re.sub(pattern, url, line)