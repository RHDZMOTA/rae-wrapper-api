from selenium import webdriver


browser = webdriver.PhantomJS()
browser.set_window_size(1120, 550)

word = "5"
url = "http://dle.rae.es/?w=" + word


browser.get(url)


results = browser.find_element_by_id("resultados")





word_found = results.find_element_by_class_name("f").text
word_phonetics = results.find_element_by_class_name("par").text

ids = results.find_elements_by_xpath('//*[@id]')
flag_a0 = False
flag_redesSociales = False
relevant_ids = []
for i in ids:
    id_name = i.get_attribute("id")
    flag_a0 = ("a0" == id_name) or flag_a0
    flag_redesSociales = ("redesSociales" == id_name) or flag_redesSociales
    if (flag_a0) and (not flag_redesSociales):
        relevant_ids.append(id_name)
relevant_ids = relevant_ids[1:]

results.find_element_by_id(relevant_ids[3]).text



browser.quit()
