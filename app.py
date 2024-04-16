import streamlit as st
import openai

# load my open ai api key
# key = open("open_ai_api_key.txt")

# OPENAI_API_KEY = key.read()

openai.api_key = ["OPENAI_API_KEY"]

def chat_with_gpt(prompt):
  try:
    response = openai.completions.create(
      model="gpt-3.5-turbo-instruct",
      prompt=f"For the given code identify the errors{prompt} and give the corrected code and give explanation for it also",
      max_tokens=200,
      temperature=0,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )

    corrected_code = ""

    st.write("AI Response...")
    st.write(response.choices[0].text.strip())

    results = response.choices[0].text.strip().split("\n\n")

    for result in results:
        lines = result.strip().split("\n")
        if lines[0].startswith("Correction:"):
            codes = '\n'.join(lines[1:])
            corrected_code += f"#{codes}"
            explanation = ""
            if len(lines) > 1 and lines[1].startswith("Explanation:"):
                explanation = lines[1]
            st.code(corrected_code, language='python')
            if explanation:
               st.write(explanation)
  except Exception as e:
    print(e)

def main():
  st.title("☃️ AI Code Reviewer - A GenAI App")
  prompt = st.text_area("Enter your python code here:")
  if st.button("Review"):
    with st.spinner("Analyzing code..."):
      chat_with_gpt(prompt)

if __name__ == "__main__":
  main()