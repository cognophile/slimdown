from html.parser import HTMLParser

class HtmlToMarkdown(HTMLParser):
    generatedMarkdown = []
    supportedInline = ['b', 'strong', 'i', 'em', 'strike', 'code', 'pre']
    reverseTags = ['em']
    
    # Here be dragons: 
    # Flag used due to procedural nature of HTMLParser which continues
    # to call all handle_* methods within .feed() and would add newlines as Data
    # for any tags not supported by Slimdown yet. 
    continueToProcessFlag = True
    
    htmlMarkdownBindings = {
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
        md = self.__removeFromOutput(self.generatedMarkdown, '\t')
        return md

    def __setContinueToProcessFlag(self, val):
        self.continueToProcessFlag = val
    
    def __getContinueToProcessFlag(self):
        return self.continueToProcessFlag


    # Overriden HTMLParser methods
    def handle_starttag(self, tag, attrs):
        openTag = tag.lower()
        if openTag in self.htmlMarkdownBindings:
            md = self.htmlMarkdownBindings.get(openTag)
            self.generatedMarkdown.append(md)
            
            if openTag == 'a':
                url = dict(attrs).get('href')
                self.generatedMarkdown.append('({0})'.format(url))            
        else: 
            self.__setContinueToProcessFlag(False)

    def handle_data(self, data):
        if self.__getContinueToProcessFlag() == True:
            self.generatedMarkdown.append(data)
        else: 
            self.__setContinueToProcessFlag(True)

    def handle_endtag(self, tag):
        closeTag = tag.lower()
        
        if self.__getContinueToProcessFlag() == True: 
            if closeTag in self.supportedInline:
                if closeTag in self.htmlMarkdownBindings:
                    
                    md = self.htmlMarkdownBindings.get(closeTag)
                    if closeTag in self.reverseTags:
                        md = md[::-1]
                    
                    self.generatedMarkdown.append(md)
        else:
            self.__setContinueToProcessFlag(True)