import os
from together import Together



def modelanswer(data: str):
    client = Together(api_key=os.getenv("API_KEY"))

    response = client.chat.completions.create(
        model="meta-llama/Llama-4-Scout-17B-16E-Instruct",
        messages=[
            {
                "role": "system",
                "content": "Respond only with valid JSON (not Python dicts). Use double quotes for all strings and keys.",
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Here are the subtitles I have provided of a particular YouTube video. I want you to summarize the subtitles by first finding out a perfect title, then the concepts they taught in a heading and description format. The keys should be `title`, and then a nested JSON with listname 'concepts' within `heading` and `description`.",
                    },
                    {"type": "text", "text": data},
                ],
            },
        ],
    )

    return response.choices[0].message.content
