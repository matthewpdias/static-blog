import os
import boto3
import yaml

#setup s3 client
s3 = boto3.resource('s3')

#set the name of the bucket using the name of the current dir. This requires the dir name EXACTLY MATCHES THE BUCKET NAME
dirname = os.path.basename(os.getcwd())

#supported file mime types so content is presented correctly
mime_types = { ".txt":"text/plain", ".html":"text/html", ".jpg" : "image/jpeg", ".png" : "image/png", ".mpeg" : "audio/mpeg", ".ogg" : "audio/ogg", ".mp4" : "video/mp4", ".json" : "application/json", ".js" : "application/javascript" }

#get the files in the current dir. Currently only supports "flat" dirs with no subdirs
for filename in os.listdir():

    try:
        mime = '.' + filename.split('.', 1)[-1]
    except:
        print('WARNING: Unsupported file extension: %s', filename.split('.', 1)[-1])
        print('WARNING: %s will not be uploaded..', filename)
        mime = '.'

    #do not upload any dot files (like .git) or nonsupported files
    if (filename[0] == '.' || mime == '.'):
        pass
    else:
        #open and upload the current file to s3
        with open(filename, 'rb') as data:
            s3.Bucket(dirname).put_object(Key=filename, Body=data, ACL='public-read', ContentType=mime_types[mime])
