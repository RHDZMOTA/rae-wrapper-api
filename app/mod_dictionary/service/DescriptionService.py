from util import RaeConsultor


class DescriptionService(object):

    def __init__(self):
        self.RAE = RaeConsultor()

    def get_description(self, word):
        try:
            description = self.RAE.get_definition(word)
        except Exception as e:
            description = {
                "error": "Service Error; something went wrong."
            }
        return description

    def close_service(self):
        self.RAE.close_connection()

