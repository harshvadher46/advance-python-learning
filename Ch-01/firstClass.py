class llms:
    def __init__(self,query):
        self.query = query
    
    def openai(self):
        return f"OpenAI response to {self.query}"

    def anthropic(self):
        return f"Anthropic response to {self.query}"

    def llama2(self):
        return f"llama2 response to {self.query}"  
    
object1 = llms("Hello, This is is harsh and i am learning Data Engineering")
print(object1.openai())
