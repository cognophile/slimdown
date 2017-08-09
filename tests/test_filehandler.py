import unittest
from helpers.filehelper import FileHelper 

class Test_FileHandler(unittest.TestCase):
    
    def test_filenameToMarkdown_returnsFilenameWithMarkdownExtension(self):
        helper = FileHelper()
        fileName = 'example.html'
        expected = 'example.md'
        
        result = helper.filenameToMarkdown(fileName)
        
        self.assertEqual(result, expected)

    def test_isFileHtml_returnsTrueIfFileHasHtmlExtension(self):
        helper = FileHelper()
        fileName = 'example.html'
        
        result = helper.isFileHtml(fileName)
        
        self.assertTrue(result)

    def test_isFileHtml_returnsFalseIfFileHasTxtExtension(self):
        helper = FileHelper()
        fileName = 'example.txt'
        
        result = helper.isFileHtml(fileName)
        
        self.assertFalse(result)        

if __name__ == '__main__':
    unittest.main()