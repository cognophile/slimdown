import os

class FileHelper():
    def filenameToMarkdown(self, htmlFile):        
        if not htmlFile:
            return htmlFile
        return os.path.splitext(htmlFile)[0] + '.md'

    def isFileHtml(self, htmlFile):
        if not htmlFile:
            return htmlFile

        if os.path.splitext(htmlFile)[1] == '.html':
            return True