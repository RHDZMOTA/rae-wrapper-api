from selenium import webdriver


def get_relevant_ids(ids):
    flag_a0 = False
    flag_redesSociales = False
    relevant_ids = []
    for i in ids:
        id_name = i.get_attribute("id")
        flag_a0 = ("a0" == id_name) or flag_a0
        flag_redesSociales = ("redesSociales" == id_name) or flag_redesSociales
        if (flag_a0) and (not flag_redesSociales):
            relevant_ids.append(id_name)
    return relevant_ids[1:] if len(relevant_ids) else []


class RaeConsultor(object):

    url = "http://dle.rae.es/?w="

    def __init__(self):
        self.browser = webdriver.PhantomJS()
        self.browser.set_window_size(1120, 550)


    @staticmethod
    def valid_word(word):
        return not any([(num in word) for num in "0123456789"])

    def get_definition(self, word):
        if not self.valid_word(word):
            return {
                "error": "Word contains numbers."
            }
        word_url = self.url + str(word)
        self.browser.get(word_url)
        try:
            results = self.browser.find_element_by_id("resultados")
            if "no está registrada en el Diccionario" in results.text:
                return {
                    "error": results.text.split(".")[0] + "."
                }
            word_found = results.find_element_by_class_name("f").text
            word_phonetics = results.find_element_by_class_name("par").text
            ids = results.find_elements_by_xpath('//*[@id]')
            relevant_ids = get_relevant_ids(ids)
            definition = ""
            if len(relevant_ids):
                for i in relevant_ids[1:]:
                    definition += results.find_element_by_id(i).text + "\n"
            return {
                "original-word": word,
                "suggested-word": word_found,
                "phonetics": word_phonetics,
                "definitions": definition
            }
        except Exception as e:
            return {
                "error": "Unexpected error: " + str(e)
            }

    def close_connection(self):
        self.browser.quit()

