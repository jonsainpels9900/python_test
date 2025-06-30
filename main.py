import data


@classmethod
    def setup_class(cls):
    # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
    from selenium.webdriver import DesiredCapabilities
    capabilities = DesiredCapabilities.CHROME
    capabilities["goog:loggingPrefs"] = {"browser": "ALL"}
    cls.driver = webdriver.Chrome()

    class TestUrbanRoutes():
        # Open the app - update the URL after starting the server
        driver = webdriver.Chrome()
        driver.get('https://cnt-986db0a1-d57e-4859-848a-5ccc40487886.containerhub.tripleten-services.com')

        # Create an instance for the POM class
        # urban_routes_page is the instance you created from UrbanRoutesPage
        urban_routes_page = UrbanRoutesPage(driver)

        # Use the POM methods to perform actions on the page

        def test_self_routes(self):
            urban_routes_page.enter_from_location('East 2nd Street, 601')
            urban_routes_page.enter_to_location('1300 1st Street')

        def test_select_plan(self):
            urban_routes_page.click_custom_option('Custom')
            urban_routes_page.click_taxi_icon('Taxi')
            urban_routes_page.click_call_a_taxi('Call a Taxi')
            urban_routes_page.click_supportive('Supportive')

        def test_fill_phone_number(self):
            urban_routes_page.enter_phone_number(2027021987)

        def test_fill_card(self):
            urban_routes_page.click_payment_method('Payment Method')
            urban_routes_page.click_add_a_card('Add Card')
            urban_routes_page.enter_card_number(12340004321)
            urban_routes_page.enter_code(12)
            urban_routes_page.click_link('Link')

        def test_comment_for_driver(self):
            urban_routes_page.enter_message_to_the_driver('Please bring utensils')

        def test_order_blankets_and_hankerchiefs(self):
            urban_routes_page.click_blankets_and_hankerchiefs('Blankets and hankerchiefs')

        def test_order_2_ice_creams(self):
            for number in range(2):
            urban_routes_page.click_ice_cream('Ice cream')










@classmethod
    def teardown_class(cls):
    cls.driver.quit()


