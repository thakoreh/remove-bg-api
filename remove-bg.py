from fastapi import FastAPI,Response,UploadFile,File
import requests
from fastapi.responses import FileResponse
from rembg import remove

app = FastAPI()

output_path = 'output.jpg'


@app.get('/')
def home():
    return "Welcome to Home Page"

@app.post('/upload/')
async def postImg(file: bytes = File()):
    if not file:
        return {"message": "No file sent"}
    else:
        try:
            output=''
            with open('image.jpg','wb') as image:
                image.write(file)
                image.close()
            with open('image.jpg', 'rb') as i:
                with open(output_path, 'wb') as o:
                    input = i.read()
                    output = remove(input)
                    o.write(output)
            return {"file_output": output}
        except Exception:
            return {"message": "There was an error uploading the file"}
        finally:
            return {"message": "There was an error uploading the file"}

# api_endpoint = "https://remove-bg-api.herokuapp.com/"
# "content-type": "multipart/form-data"