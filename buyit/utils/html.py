from django.utils.html import format_html

def image_to_html(image, username):
    """
    Render image to html img tag or jdenticon if no image exit
    """

    if image is None:
        html_svg_tag = f'<img class="avatar-img rounded user-pic" src="https://avatars.dicebear.com/api/jdenticon/{username}.svg"/>'
        return format_html(html_svg_tag)
        
    html_image_tag = f'<img src="{image}" class="avatar-img rounded user-pic">'

    return format_html(html_image_tag)

def image_to_html_profile(image, username):
    """
    Render image to html img tag or jdenticon if no image exit
    """
    if image is None:
        html_svg_tag = f'<img class="avatar-img user-pic rounded-circle border border-white border-3" src="https://avatars.dicebear.com/api/jdenticon/{username}.svg" data-bs-toggle="modal" data-bs-target="#modalUploadProfilePic" title="Upload profile image" alt=""/>'
        return format_html(html_svg_tag)
        
    html_image_tag = f'<img src="{image}" class="avatar-img user-pic rounded-circle border border-white border-3" title="Upload profile image" data-bs-toggle="modal" data-bs-target="#modalUploadProfilePic" title="Upload profile image" alt="" />'

    return format_html(html_image_tag)

def image_to_html_edit(image, username):
    """
    Render image to html img tag or jdenticon if no image exit
    """

    if image is None:
        html_svg_tag = f'<img src="https://avatars.dicebear.com/api/jdenticon/{username}.svg"  id="image" />'
        return format_html(html_svg_tag)
        
    html_image_tag = f'<img src="{image}" id="image" >'

    return format_html(html_image_tag)

def image_to_html_small(image, username):
    """
    Render image to html img tag or jdenticon if no image exit
    """

    if image is None:
        html_svg_tag = f'<img class="avatar-img rounded-circle user-pic" src="https://avatars.dicebear.com/api/jdenticon/{username}.svg" />'
        return format_html(html_svg_tag)
        
    html_image_tag = f'<img src="{image}" class="avatar-img user-pic rounded-circle" />'

    return format_html(html_image_tag)