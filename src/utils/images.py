# notes
'''
This file is used for handling anything image related.
'''

# package imports
import base64
import os



def get_asset_img(img_file_name):
    '''
    '''
    cwd = os.getcwd()
    img_path = os.path.join(cwd, 'src/assets', img_file_name)
    img_tunel = base64.b64encode(open(img_path, 'rb').read())
    img_encoded = 'data:image/png;base64,{}'.format(img_tunel.decode())
    return img_encoded