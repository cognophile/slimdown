import unittest
from helpers.filehelper import FileHelper 

class Test_FileHelper(unittest.TestCase):
    
    def test_filenameToMarkdown_returnsFilenameWithMarkdownExtension(self):
        Helper = FileHelper()
        filename = 'example.html'
        expected = 'example.md'
        
        result = Helper.filenameToMarkdown(filename)
        
        self.assertEqual(result, expected)

    def test_isFileHtml_returnsTrueIfFileHasHtmlExtension(self):
        Helper = FileHelper()
        filename = 'example.html'
        
        result = Helper.isFileHtml(filename)
        
        self.assertTrue(result)

    def test_isFileHtml_returnsFalseIfFileHasTxtExtension(self):
        Helper = FileHelper()
        filename = 'example.txt'
        
        result = Helper.isFileHtml(filename)
        
        self.assertFalse(result) 
        
    def test_duplicateMarkdownFile_passIfFilenameReturnedHasCopyAppended(self):
        Helper = FileHelper()
        filename = 'example.md'
        
        expected = 'example-copy.md'
        result = Helper.duplicateMarkdownFile(filename)
        
        self.assertEqual(result, expected)

    def test_duplicateMarkdownFile_failsIfFileTypeGivenIsNotMarkdown(self):
        Helper = FileHelper()
        filename = 'example.txt'
        
        expected = 'example-copy.md'
        result = Helper.duplicateMarkdownFile(filename)
        
        self.assertNotEqual(result, expected)           

if __name__ == '__main__':
    unittest.main()