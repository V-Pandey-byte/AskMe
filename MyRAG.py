# AI API
#
import ollama
model = "llama3.1"

class MyRAG:
    def chatWithMe (self, query):
        prompt = query
        stream = ollama.chat(model=model, messages=[{"role": "user", "content": prompt,}], stream=True)
        for chunk in stream:
                print(chunk['message']['content'],end='')
        print("")

myRag = MyRAG()
inputQuery = input("Ask me: ")
while inputQuery != "exit":
    myRag.chatWithMe(inputQuery)
    print("*" * 100)
    inputQuery = input("Ask me: ")

print("Goodbye!")
