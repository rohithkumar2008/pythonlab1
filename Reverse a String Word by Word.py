class RevExample:
    def __init__(self, word):
        
        rev = reversed(word.split())
        self.result = " ".join(rev)

    def display(self):
        print(self.result)


sentence = "good things take time"
obj = RevExample(sentence)
obj.display()
