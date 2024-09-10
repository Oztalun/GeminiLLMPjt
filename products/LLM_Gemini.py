# import google.generativeai as genai
# import os

# API_KEY = genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
# print(API_KEY)






# 모델 나열
# for item in genai.list_models():
#     print(item.name)

from . import config
API_KEY = config.GOOGLE_API_KEY
import google.generativeai as genai
from IPython.display import display, Markdown

def Get_Answer(query):
    genai.configure(api_key=API_KEY)

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"{query} 상품 목록이야. 여기서 두개의 상품을 추천해줘. 대답은 추천해준 두개의 상품의 id값만 보내줘. 다음은 답장 예시야. 1 4")
    return response.text