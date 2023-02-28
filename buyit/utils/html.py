from django.utils.safestring import SafeString


def rating_to_html(value, show_rating=True):
    """
    Converts rating to html font-awesome icon
    """

    rating_num = ""

    if not value:
        return SafeString("<strong>Not yet rated</strong>")

    value = round(value, 1)

    integer, remainder = divmod(value, 1)
    html_rating = '<ul class="list-inline">'

    for _ in range(int(integer)):
        html_rating += (
            '<li class="list-inline-item me-0 small">'
            + '<i class="fas fa-star text-warning"></i></li>'
        )

    if show_rating:
        rating_num = f"{value}/5.0"

    if remainder > 0.5:
        html_rating += (
            '<li class="list-inline-item me-0 small">'
            + f'<i class="fas fa-star text-warning"></i>{rating_num}</li>'
        )

    elif remainder > 0:
        html_rating += (
            '<li class="list-inline-item me-0 small">' +
            f'<i class="fas fa-star-half-alt text-warning">\
                </i>{rating_num}</li>'
        )
    else:
        html_rating += f"&nbsp;{rating_num}"

    html_rating += "</ul>"

    return SafeString(html_rating)
