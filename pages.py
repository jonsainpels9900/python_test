from selenium.webdriver.common.by import By


class UrbanRoutesPage
    FROM_LOCATOR (By.ID, 'from')
    TO_LOCATOR (By.ID, 'to')
    CUSTOM_OPTION_LOCATOR (By. XPATH, '//div[text()="Custom"]')
    TAXI_ICON_LOCATOR (By. XPATH, '//img[@src="/static/media/taxi-active.b0be3054.svg"]')
    CALL_A_TAXI_BUTTON_LOCATOR (By. XPATH, '//button[@class="button round"]')
    SUPPORTIVE_BUTTON_LOCATOR (By. XPATH, '//img[@src="/static/media/kids.27f92282.svg"]')
    PHONE_NUMBER_LOCATOR (By.ID, 'phone_number')
    PAYMENT_METHOD_BUTTON_LOCATOR (By. XPATH, '//button[@class="pp-value-text"]')
    ADD_A_CARD_LOCATOR (By. XPATH, '//button[@class="pp-title"]')
    CARD_NUMBER_LOCATOR (By.ID, 'card_number')
    CODE_LOCATOR (By.ID, 'code')
    LINK_BUTTON_LOCATOR (By. XPATH, '//button[@class="button full"]')
    MESSAGE_TO_THE_DRIVER_LOCATOR (By.ID, 'message_to_the_driver')
    BLANKETS_AND_HANKERCHIEFS_LOCATOR (By. XPATH, '//button[@class="r-sw-label"]')
    ICE_CREAM_LOCATOR (By. XPATH, '//button[@class="r-counter-label"]')

    def __init__(self):
        self.driver = driver

    def enter_from_location(self, from_text):
        self.driver.find_element(*self.FROM_LOCATOR).send.keys(from_text)

    def enter_to_location(self, to_text):
        self.driver.find_element(*self.TO_LOCATOR).send.keys(to_text)

    def click_custom_option(self):
        self.driver.find_element(*self.CUSTOM_OPTION_LOCATOR).click()

    def click_taxi_icon(self):
        self.driver.find_element(*self.TAXI_ICON_LOCATOR).click()

    def click_call_a_taxi(self):
        self.driver.find_element(*self.CALL_A_TAXI_BUTTON_LOCATOR).click()

    def click_supportive(self):
        self.driver.find_element(*self.SUPPORTIVE_BUTTON_LOCATOR).click()

    def enter_phone_number(self, phone_number_text):
        self.driver.find_element(*self.PHONE_NUMBER_LOCATOR).send_keys(phone_number_text)

    def click_payment_method(self):
        self.driver.find_element(*self.PAYMENT_METHOD_BUTTON_LOCATOR).click()

    def click_add_a_card(self):
        self.driver.find_element(*self.ADD_A_CARD_LOCATOR).click()

    def enter_card_number(self, card_number_text):
        self.driver.find_element(*self.CARD_NUMBER_LOCATOR).send_keys(card_number_text)

    def enter_code(self, code_text):
        self.driver.find_element(*self.CODE_LOCATOR).send_keys(code_text)

    def click_link(self):
        self.driver.find_element(*self.LINK_BUTTON_LOCATOR).click()

    def enter_message_to_the_driver(self, message_to_the_driver_text):
        self.driver.find_element(*self.MESSAGE_TO_THE_DRIVER_LOCATOR).send_keys(message_to_the_driver_text)

    def click_blankets_and_hankerchiefs(self):
        self.driver.find_element(*self.BLANKETS_AND_HANKERCHIEFS_LOCATOR).click()

    def click_ice_cream(self):
        self.driver.find_element(*self.ICE_CREAM_LOCATOR).click()



