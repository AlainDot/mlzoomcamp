print('************** V 001 ************* ')

print(' > import ')
from io import BytesIO
from urllib import request
from PIL import Image
import numpy as npy

# When run in local (not able to load the runtime in local windows...)
#import tensorflow.lite as tflite
# When run in Docker 
import tflite_runtime.interpreter as tflite

print(' > functions ')
def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img

def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.Resampling.NEAREST )
    return img


print(' > variables ')
strFilOut = 'dino-vs-dragon-v2.tflite'

#urlImg = 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Smaug_par_David_Demaret.jpg/1280px-Smaug_par_David_Demaret.jpg'
urlImg = 'https://upload.wikimedia.org/wikipedia/en/e/e9/GodzillaEncounterModel.jpg'

def predict(url):

    print('   > load interpreter ')
    interpreter = tflite.Interpreter(model_path=strFilOut)
    interpreter.allocate_tensors()

    input_details = interpreter.get_input_details()
    input_index = input_details[0]['index']
    output_details = interpreter.get_output_details()
    output_index = output_details[0]['index']


    print('   > load image ')
    img = download_image(url)
    imgRes = prepare_image(img, (150,150))
    x = npy.array(imgRes , dtype='float32') / 255
    X = npy.array([x])

    print('   > prediction ')
    interpreter.set_tensor(input_index, X)

    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)

    pred = float(preds[0,0])
    print( '   * prediction =' , pred )
    jsoRes = { 'prediction' : pred}
    return(jsoRes)


def lambda_handler(event, context):
    url = event['url']
    res = predict(url)
    return res

if __name__ == "__main__":
    print(' > Test predict() ')
    res = predict(urlImg)
    print(' > res = ' , res )
    
    print(' > Test lambda_handler() ')
    res = lambda_handler(event={'url': urlImg} , context=() )
    print(' > res = ' , res)
