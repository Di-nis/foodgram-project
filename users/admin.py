from django.contrib.auth.admin import UserAdmin

UserAdmin.list_filter = ("username", "email")
UserAdmin.list_display = ("id", "username",
                          "email", "first_name",
                          "last_name", "is_staff"
                          )
