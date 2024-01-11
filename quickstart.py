import os
from openai import AzureOpenAI
   
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),  
    api_version="2023-12-01-preview",
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    )

response = client.chat.completions.create(
    model="GPT35TURBO16K",
    messages = [{"role":"system", "content":"bạn là giáo viên toán người Việt",
                "role" : "user", "content" : "viết một đoạn văn miêu tả người yêu cũ"}]
)
print(response.choices[0].message.content)