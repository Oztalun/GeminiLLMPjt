# GeminiLLMPjt
## Development Perion
- 2024.09.05 ~ 2024.09.10

## 💻 Development Environment
|Programming Language| python 3.10|
|:----------------:|:----------------:|
| Web Framework | Django 4.2|
| Database | SQLite|
| IDE | Vs code |
| Version Control | Git, Github |
| Backend | Python, Django |
| Frontend | HTML, CSS, Bootstrap, JS |
| Database | Django ORM, SQLite |
| LLM | Gemini AI API |

## 
### how to call Gemini ai api
```python
# hide api key
from . import config
API_KEY = config.GOOGLE_API_KEY

# call ai api
import google.generativeai as genai
from IPython.display import display, Markdown
def Get_Answer(query):
    genai.configure(api_key=API_KEY)

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"write question")
    return response.text
```

### gemini recommend product
![alt text](image-2.png)


api recommend 5 products and display recommended products


![alt text](image-1.png)

## ERD Diagram
[Gemini_LLM_ERD](https://dbdiagram.io/d/SpartaLLMProject-66d9d8eceef7e08f0ed1d09a)
![alt text](image-3.png)