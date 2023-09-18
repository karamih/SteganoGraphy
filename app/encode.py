from stegano import Image_In_Image

encoded_image = Image_In_Image(src_img="../statics/images/img1.jpg",
                               dest_img="../statics/images/img2.jpg",
                               memorize=1, dest_h_img_size=1080, dest_w_img_size=700)

encoded_image.image_in_image()
