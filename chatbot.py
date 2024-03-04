import g4f

content="" ""
def chatbot(content):
        response = g4f.ChatCompletion.create(
            model = g4f.models.gpt_4,
            # model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": content}],
    )
        return response
def savol(savol, mavzu=""):
        if mavzu=="tibbiyot":
                content = f"Savolim tibbiyot bilan bog'liq. {savol}ga tibbiyot yo'nalishida javob ber"
        elif mavzu== "dasturlash":
                content = f"Savolim dasturlash bilan bog'liq. {savol}ga dasturlash yo'nalishida javob ber " 
        else:
                content = f"Ushbu savolga o'zbek tilida javob ber. Savol - {savol}"
        javob = chatbot(content)
        return javob
print(savol("Xatolik"))
print(32*"*")
print(savol("Xatolik","tibbiyot"))
print(32*"*")
# from g4f.client import Client

# client = Client()
# response = client.images.generate(
#   model="gemini",
#   prompt="nazi logo in red flag",
# )
# image_url = response.data[0].url