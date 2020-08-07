from environs import Env
from selenium import webdriver

from actions.login import login
from actions.logout import logout
from actions.customized import (
    customized_pondlets,
    customized_vocabularies,
    customized_grammar_sentences,
)


def main():
    env = Env()
    env.read_env()
    url = env('URL')
    account = env('ACCOUNT')
    password = env('PASSWORD')

    driver = webdriver.Firefox()
    driver.set_window_position(0, 0)
    driver.set_window_size(700, 700)
    driver.get(url)

    login(driver, account, password)
    customized_pondlets(driver, 'customized_pondlets.txt')
    customized_vocabularies(driver, 'customized_vocabularies.txt')
    customized_grammar_sentences(driver, 'customized_grammar_sentences.txt')
    logout(driver)

    driver.close()


if __name__ == '__main__':
    main()
