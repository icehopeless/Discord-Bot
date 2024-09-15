import google.generativeai as genai

genai.configure(api_key='AIzaSyAmIDXpyneAYEi53bt46yLngzvzg6glcvU')

model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("Qual e a linguagem de programacao mais usada no mundo")
print(response.text)

