# pylint: disable = C0115, C0114

import json
from rest_framework.renderers import JSONRenderer  # type: ignore


class ProfileJsonRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context["response"].status_code
        errors = data.get('Errors', None)

        if errors is not None:
            return super(ProfileJsonRenderer, self).render(data)
        return json.dumps({"status_code": status_code, "profile": data})


class ProfilesJsonRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context["response"].status_code
        errors = data.get('Errors', None)

        if errors is not None:
            return super(ProfilesJsonRenderer, self).render(data)
        return json.dumps({"status_code": status_code, "profiles": data})
