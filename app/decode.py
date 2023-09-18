from stegano import Image_from_Image

decoded_image = Image_from_Image(src_img="../statics/outputs_encode/stegano_encode_1425199.png",
                                 key=18144000, memorize=1, dest_h_img_size=1080, dest_w_img_size=700)

decoded_image.image_from_image()
