from fastapi import FastAPI,Response,UploadFile,File
import requests
from fastapi.responses import FileResponse
from rembg import remove
from PIL import Image
import io
from base64 import encodebytes


app = FastAPI()

output_path = 'output.png'


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
            encoded_img = ''
            with open('image.jpg','wb') as image:
                image.write(file)
                image.close()
            with open('image.jpg', 'rb') as i:
                with open(output_path, 'wb') as o:
                    input = i.read()
                    output = remove(input)
                    o.write(output)


            #read the image
            im = Image.open(output_path)

            #rotate image
            angle = -90
            out = im.rotate(angle, expand=True)
            out.save('rotate-output.png')
            def get_response_image(image_path):
                pil_img = Image.open(image_path, mode='r') # reads the PIL image
                byte_arr = io.BytesIO()
                pil_img.save(byte_arr, format='PNG') # convert the PIL image to byte array
                encoded_img = encodebytes(byte_arr.getvalue()).decode('ascii') # encode as base64
                return encoded_img
            encoded_img = get_response_image('rotate-output.png')

            return {"img_in_bytes": encoded_img}


        except Exception:
            return {"message": "There was an error uploading the file"}
        finally:
            return {"img_in_bytes": encoded_img}

# api_endpoint = "https://remove-bg-api.herokuapp.com/"
# "content-type": "multipart/form-data"