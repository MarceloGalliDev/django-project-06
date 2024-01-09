# pylint: disable = C0115, C0114

from rest_framework.exceptions import APIException  # type: ignore


class CantFollowYoursef(APIException):
    status_code = 403
    default_detail = "You can't follow yourself."
    default_code = "Forbidden"
