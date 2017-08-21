import os

class FileHelper():
    """Helper functions for manipulating files"""
    def filenameToMarkdown(self, filename):
        """Create a markdown file path of the passed filename"""        
        if filename is None:
            raise TypeError

        return os.path.splitext(filename)[0] + '.md'

    def isFileHtml(self, filename):
        """Determine whether a file has a '.html' extension"""
        if filename is None:
            raise TypeError

        if os.path.splitext(filename)[1] == '.html':
            return True

    def duplicateMarkdownFile(self, filename):
        
        if filename is None:
            raise TypeError

        if os.path.splitext(filename)[1] != '.md':
            print("Argument must be of '.md' format")
        else:
            return os.path.splitext(filename)[0] + '-copy' + '.md'
        
    def removeFile(self, filename):
        try:
            os.remove(filename)
        
        except OSError as ex:
            print("Unable to remove file: ", ex)
        except Exception as ex:
            print("An error occured when attempting to remove a file: ", ex)
            
    def renameFile(self, source, destination):
        try:
            os.rename(source, destination)
        
        except OSError as ex:
            print("Unable to rename file: ", ex)
        except Exception as ex:
            print("An error occured when attempting to rename a file: ", ex)