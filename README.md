# SteganoGraphy
___
## Image in Image

Imagine you have some images and want to send to your friend or something like this.
you can post them simply in a social media or send with email.
bot you don't want anybody can see those.

What does it mean?
simply, you want to send them or even post in a social media bot no one can't see them unless your friend.

How you can do this?
so first you should have two Images, one for post in social media and it is a normal image and second one 
is your main images. now you can `Hide` your main image in the first one and nobody can not extract that without
your permissions(with parameters).
___
### In Visually

![main image](statics/images/img2.jpg)

you have this one and want to send to your friend but not in the common ways.
so you pick another image and then hide this one in that one and send that to your friend
or even post in internet.

![first image](statics/images/img1.jpg)

the main image will hide in this image.
___
### How does the output look like?
![encoded image](statics/outputs_encode/stegano_encode_1425199.png)

interesting :)

this is so much similar to the base image but the big difference is that this one includes
another image. we can not understand it, even if we can find out this image includes data
still can not extract data.
___
### Extracted Data
![decoded image](statics/outputs_decode/stegano_decode_1425199.jpg)

here our hided image in the base image.
___
### Usage
* `stegano.py` file is the main logic.
* `encode.py` file encode an image in another.
* `decode.py` file decode an image from another image.


`encode.py` file has two outputs, first the encoded image and second is a `file.txt` file that include
details and parameters that require for decoding the image.
___
### Details
text file with needed information is like this:
* file name: stegano_encode_1425199
* memorize: 1
* height: 1080
* width: 700
* key: 18144000
___
#### Last Words
after encoding an image simply send encoded image and text file togather.

then for decoding should use the information in text file to decode the encoded image.
