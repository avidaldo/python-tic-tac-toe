import openai

openai.api_key = "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"

print(openai.Completion.create(engine="text-davinci-003", prompt="This is a test", max_tokens=2048)
      .choices[0].text)