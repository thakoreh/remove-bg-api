from fastapi import FastAPI,Response,UploadFile,File
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
async def postImg(file: UploadFile = File(...)):
    if not file:
        return {"message": "No file sent"}
    else:
        try:
            with open(file.filename, 'rb') as i:
                with open(file.filename, 'wb') as o:
                    input = i.read()
                    output = remove(input)
                    o.write(output)
        except Exception:
            return {"message": "There was an error uploading the file"}
        finally:
            return {"message": "There was an error uploading the file"}

# api_endpoint = "https://remove-bg-api.herokuapp.com/"