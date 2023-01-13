from aritek.utils.settings import get_env_variable

# Sending email configuration
EMAIL_HOST_USER = get_env_variable(
    "ADMIN_EMAIL_ADDRESS", "info@aritekconsulting.com"
)

EMAIL_HOST_PASSWORD = get_env_variable("ADMIN_EMAIL_PASSWORD", "")

EMAIL_PORT = get_env_variable("EMAIL_PORT", 587)

EMAIL_HOST = get_env_variable("EMAIL_HOST", "smtp.gmail.com")

EMAIL_USE_TLS = True

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

SERVER_EMAIL = EMAIL_HOST_USER

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

ADMINS = []
for admin in get_env_variable("ADMINS", "-").split(", "):
    if admin:
        admin = tuple(admin.split(":", 1))
        if len(admin) == 2:
            ADMINS.append(admin)
