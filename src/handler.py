
import json
import logging


class StaticJsonContent:
    def __init__(self, content_file, object_constructor):
        with open(content_file, "r") as fh:
            self.content = object_constructor(json.load(fh))
            logging.debug("Loaded content: %s" % self.content.as_json())

    def get(self, data):
        return self.content

