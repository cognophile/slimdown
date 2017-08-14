from html.parser import HTMLParser

class HtmlToMarkdown(HTMLParser):
    __generatedMarkdown = []
    __supportedInline = ['b', 'strong', 'i', 'em', 'strike', 'code', 'pre']
    __blacklistedTags = ['script', 'iframe']
    __reverseTags = ['em']
    
    # Here be dragons: 
    # Flag used due to procedural nature of HTMLParser which continues
    # to call all handle_* methods within .feed() and would add newlines as Data
    # for any tags not supported by Slimdown yet. 
    __continueToProcessFlag = True
    
    __htmlMarkdownBindings = {
                                'h1':'# ', 'h2':'## ', 'h3':'### ','h4':'#### ','h5':'##### ',
                                'h6':'###### ', 'p':'', 'li':'- ', 'a':'[]', 'b':'**', 'strong':'**',
                                'i':'_', 'em':'**_', 'strike':'~~', 'code':'`', 'pre':'```', 'br':'\n',
                                'hr':'---'
                           }

    def __init__(self):
        HTMLParser.__init__(self)

    def readFile(self, htmlFile):
        with open(htmlFile, 'r') as html:
            for line in html:
                self.__convertToMarkdown(line)

    def __convertToMarkdown(self, line):
        self.feed(line)

    def __removeFromOutput(self, listToRemoveFrom, itemToRemove):
        return [val for val in listToRemoveFrom if itemToRemove not in val]

    def getMarkdown(self):
        md = self.__removeFromOutput(self.__generatedMarkdown, '\t')
        return md

    def __setContinueToProcessFlag(self, val):
        self.__continueToProcessFlag = val
    
    def __getContinueToProcessFlag(self):
        return self.__continueToProcessFlag


    # Overriden HTMLParser methods
    def handle_starttag(self, tag, attrs):
        openTag = tag.lower()
        if openTag in self.__blacklistedTags:
            self.__setContinueToProcessFlag(False)
            return 
        elif openTag in self.__htmlMarkdownBindings:
            md = self.__htmlMarkdownBindings.get(openTag)
            self.__generatedMarkdown.append(md)
            
            if openTag == 'a':
                url = dict(attrs).get('href')
                self.__generatedMarkdown.append('({0})'.format(url))            
        else: 
            self.__setContinueToProcessFlag(False)
        
    def handle_data(self, data):
        if self.__getContinueToProcessFlag() == True:
            self.__generatedMarkdown.append(data)
        else: 
            self.__setContinueToProcessFlag(True)

    def handle_endtag(self, tag):
        closeTag = tag.lower()
        
        if self.__getContinueToProcessFlag() == True: 
            if closeTag in self.__supportedInline:
                if closeTag in self.__htmlMarkdownBindings:
                    md = self.__htmlMarkdownBindings.get(closeTag)
                    
                    if closeTag in self.__reverseTags:
                        md = md[::-1]
                    
                    self.__generatedMarkdown.append(md)
        else:
            self.__setContinueToProcessFlag(True)