class analysedText(object):
    
    def __init__ (self, text):

        # TODO: Remove the punctuation from <text> and make it lower case.
        self.text = text
        bufferTxt = self.text.lower()
        for i in [".", ",", "!", "?"]:
            bufferTxt = bufferTxt.replace(i, "")
        

        # TODO: Assign the formatted text to a new attribute called "fmtText"
        self.fmtText = bufferTxt
        
        pass
    
    def freqAll(self):    

        # TODO: Split the text into a list of words
        wList = self.fmtText.split(" ")
        wSet = set(wList)
        wDict = {}

        # TODO: Create a dictionary with the unique words in the text as keys
        # and the number of times they occur in the text as values
        for i in wSet:
            wFreq = wList.count(i)
            
            wDict.update({i : wFreq})
        
      
        return wDict
    
    def freqOf(self, word):

        # TODO: return the number of occurrences of <word> in <fmtText>
        wList = self.fmtText.split(" ")

        return wList.count(word)
    
teste = analysedText("You can run the code cell below to test your functions to ensure they are working correctly. First execute the code cell in which you implemented your solution, then execute the code cell to test your implementation.")
print(teste.fmtText)
a = teste.freqAll()
print(a['then'])
print(teste.freqOf("cell"))
