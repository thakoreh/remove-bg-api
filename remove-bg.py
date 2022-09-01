from fastapi import FastAPI,Response
import requests
from fastapi.responses import FileResponse
from rembg import remove

app = FastAPI()


# input_path = r'D:\mexico\20220506_111806.jpg'
output_path = 'output.jpg'

# with open(payload, 'rb') as i:
#     with open(output_path, 'wb') as o:
#         input = i.read()
#         output = remove(input)
#         o.write(output)

@app.get('/')
def home():
    return "Welcome to Home Page"

@app.post('/upload')
def postImg():
    with open(payload, 'rb') as i:
        with open(output_path, 'wb') as o:
            input = i.read()
            output = remove(input)
            o.write(output)
