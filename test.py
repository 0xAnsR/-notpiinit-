from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message);
