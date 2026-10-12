#Variables
temperature = 0.7
max_tokens = 1024
is_streaming = False
content_box = None

# Type Hints
model_name: str = "gemini-2.0-flash"
temperature: float = 0.7
max_tokens: int = 1024
is_streaming: bool = False
content_box: str|None = None
print(type(model_name))

#Strings: immutable | String formatting
#old version
name = "LLM"
score = 97.3
print("Hello %s"%name)
print("score %.1f"%score)

#f -string(py 3.6+)
print(f"Hello {name}")
print(f"score: {score:.1f}")

#Expressions inside f-sttrings
word_limit = 200
print(f"{'over' if word_limit > 150 else 'under'}limit")
data = {"topic":"RAG"}
print(f"topic: {data['topic']}")

#format specifier
pi = 3.14159265
print(f"pi:{pi:.2f}")

#debugging =
temp = 0.7
print(f"{temp=}")

#multi line f-strings formatting
user_input = "What is langchain?"
content_text = "langchain is a framework for building LLM apps"
system_prompt = f"""
you are a helpful ai tutor
content provide: {content_text}
student question: {user_input}
Instructions:
-Answer based only on content above
-If the answer is not in the content,say "I don't know"
-Keep your answer under 3 sentences
""".strip()
print(system_prompt)

#Lists: ordered mutable, heterogenous sequences
#In Gen AI: Chat history,chunks of retreived documents
#Token sequence
chat_history: list[dict] = [
    {"role":"user","content":"What is an LLM"},
    {"role":"assintent","content":"A LLM  isna neural n/w trained on vest amounts of text"},
]

#Access
first_msg = chat_history[0]
print(first_msg)
print(chat_history[-1]["content"]) #last elemet

#modify
chat_history.append({"role":"user","content":"What is an RAG"})
print(chat_history)
chat_history.pop(0)
print(chat_history)

#Iterate
for msg in chat_history:
    print(f"{msg['role'].upper()}:{msg['content']}")

# list od documnet chunks
chunks:list[str] = [
    "RAG stands for retreival agumentes generation",
    "it combines a retreiver with a generator",
]

# Filter the chunks based on length
valid_chunks = [c for c in chunks if len(c.split())>=6]
print(chunks)