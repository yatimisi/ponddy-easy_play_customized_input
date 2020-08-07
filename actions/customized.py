import os

from environs import Env
from selenium.webdriver.support.ui import Select

from utils.utils import wait_xpath, wait_url


env = Env()
env.read_env()
dashboard = env('URL')
addlink = "//a[@class='addlink' and @href='/admin/{model_path}/add/']"
addanother = "//input[@type='submit' and @name='_addanother']"
success = "//li[@class='success']"


def get_file_path(file_name):
    return os.path.join('data', file_name)


def customized_pondlets(driver, file_name):
    """
        1. Open txt and read to data
        2. Go path to model add
        3. Wait loading to model add router
        4. Input data
        5. Click save and add another
        6. Wait success
        7. Return step-3 or click logo for back to dashboard
    """
    file_path = get_file_path(file_name)
    data = []

    with open(file_path) as file:
        data = file.readlines()

    driver.find_element_by_xpath(
        addlink.format(model_path='customized_pondlet/customizedpondlet')
    ).click()

    for row in data:
        items = row[:-1].split('\t')

        input_value = {
            'title': items[0],
            'level': items[1],
            'lang': items[2],
            'author': items[3],
            'date': items[4],
        }

        wait_xpath(driver, addanother)

        driver.find_element_by_id('id_title').send_keys(input_value['title'])

        driver.find_element_by_id('id_level').clear()
        driver.find_element_by_id('id_level').send_keys(input_value['level'])

        Select(driver.find_element_by_id('id_lang')
               ).select_by_value(input_value['lang'])

        driver.find_element_by_id('id_author').send_keys(input_value['author'])

        if input_value['date'].lower() == 'today':
            driver.find_element_by_link_text('Today').click()
        else:
            driver.find_element_by_id(
                'id_finalized_date').send_keys(input_value['date'])

        driver.find_element_by_xpath(addanother).click()
        wait_xpath(driver, success)

    driver.find_element_by_id('site-name').click()
    wait_url(driver, dashboard)


def customized_vocabularies(driver, file_name):
    """
        1. Open txt and read to data
        2. Go path to model add
        3. Wait loading to model add router
        4. Input data
        5. Click save and add another
        6. Wait success
        7. Return step-3 or click logo for back to dashboard
    """
    file_path = get_file_path(file_name)
    data = []

    with open(file_path) as file:
        data = file.readlines()

    driver.find_element_by_xpath(
        addlink.format(model_path='customized_pondlet/customizedvocabulary')
    ).click()

    for row in data:
        items = row[:-1].split('\t')

        input_value = {
            'customized': items[0],
            'dictionary': items[1],
            'translation': items[2],
            'level': items[3],
            'puzzle_flag': items[4],
            'wordle_flag': items[5],
        }

        wait_xpath(driver, addanother)

        select_customized = driver.find_element_by_id('id_customized')
        select_customized.find_element_by_xpath(
            f"//option[contains(text(),'{input_value['customized']}')]") \
            .click()

        driver.find_element_by_id('id_dictionary_object_id').send_keys(
            input_value['dictionary'])

        driver.find_element_by_id('id_translation').send_keys(
            input_value['translation'])

        driver.find_element_by_id('id_level').send_keys(input_value['level'])

        if input_value['puzzle_flag'].lower() == 'true':
            driver.find_element_by_id('id_puzzle_flag').click()

        if input_value['wordle_flag'].lower() == 'true':
            driver.find_element_by_id('id_wordle_flag').click()

        driver.find_element_by_xpath(addanother).click()
        wait_xpath(driver, success)

    driver.find_element_by_id('site-name').click()
    wait_url(driver, dashboard)


def customized_grammar_sentences(driver, file_name):
    """
        1. Open txt and read to data
        2. Go path to model add
        3. Wait loading to model add router
        4. Input data
        5. Click save and add another
        6. Wait success
        7. Return step-3 or click logo for back to dashboard
    """
    file_path = get_file_path(file_name)
    data = []

    with open(file_path) as file:
        data = file.readlines()

    driver.find_element_by_xpath(
        addlink.format(
            model_path='customized_pondlet/customizedgrammarsentence')
    ).click()

    for row in data:
        items = row[:-1].split('\t')

        input_value = {
            'customized': items[0],
            'grammarsentence': items[1],
            'grammar': items[2],
            'execflag_rearrangement': items[3],
            'execflag_cloze': items[4],
            'execexif_cloze_simp': items[5],
            'execexif_cloze_trad': items[6],
            'simp_close_candidates': items[7],
            'trad_close_candidates': items[8],
        }

        wait_xpath(driver, addanother)

        if input_value['customized'] != "":
            select_customized = driver.find_element_by_id('id_customized')
            select_customized.find_element_by_xpath(
                f"//option[contains(text(),'{input_value['customized']}')]") \
                .click()

            driver.find_element_by_id('id_grammarsentence_object_id') \
                .send_keys(input_value['grammarsentence'])

            driver.find_element_by_id('id_grammar_object_id').send_keys(
                input_value['grammar'])

            if input_value['execflag_rearrangement'].lower() == 'true':
                driver.find_element_by_id('id_execflag_rearrangement').click()

            if input_value['execflag_cloze'].lower() == 'true':
                driver.find_element_by_id('id_execflag_cloze').click()

            driver.find_element_by_id('id_execexif_cloze_simp').send_keys(
                input_value['execexif_cloze_simp'])

            driver.find_element_by_id('id_execexif_cloze_trad').send_keys(
                input_value['execexif_cloze_trad'])

            driver.find_element_by_id('id_simp_close_candidates').send_keys(
                input_value['simp_close_candidates'])

            driver.find_element_by_id('id_trad_close_candidates').send_keys(
                input_value['trad_close_candidates'])

            driver.find_element_by_xpath(addanother).click()
            wait_xpath(driver, success)

    driver.find_element_by_id('site-name').click()
    wait_url(driver, dashboard)
