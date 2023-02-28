def store_image_upload_path(instance, file_name):
    return f"{instance._meta.app_label}/{instance._meta.model_name}/{instance.name}/{file_name}"

def store_product_gallery_upload_path(instance, file_name):
    return f"{instance._meta.app_label}/{instance._meta.model_name}/{instance.product.name}/{file_name}"

def profile_image_upload_path(instance, file_name):
    # file_folder = "Books"
    return f"{instance._meta.app_label}/{instance._meta.model_name}/{instance.get_full_name()}/{file_name}"

def default_profile_image():
    return "default/user-default.png"

def default_cover_image():
    return "default/cover-default.png"

def cover_image_upload_path(instance, file_name):
    file_folder = "Cover_images"
    return f"{instance.username}/{file_folder}/{file_name}"