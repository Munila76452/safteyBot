import os
from openai import AzureOpenAI

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY")

# add this line
deployment = "gpt-4o"

client = AzureOpenAI(
    api_key=subscription_key,
    api_version="2024-12-01-preview",
    azure_endpoint=endpoint
)

def ask_llm(prompt):

    response = client.chat.completions.create(
        model=deployment,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
