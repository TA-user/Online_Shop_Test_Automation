from .base_page import BasePage
from .main_page_locators import MainPageLocators, SearchCarsTabLocators, CalendarWidgetLocators
from utils.text_formatter import TextFormatter


class MainPage(BasePage):
    def click_accept_cookie_popup_button(self):
        self.element_interactions.click_element(MainPageLocators.ACCEPT_COOKIES_BUTTON)

    def open_search_cars_tab(self):
        self.element_interactions.click_element(MainPageLocators.SEARCH_FLIGHTS_TAB)


class MainPageSearchFlightsTab(BasePage):
    pass


class MainPageSearchHotelsTab(BasePage):
    pass


class MainPageCarHireTab(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPageCarHireTab, self).__init__(*args, **kwargs)
        self.pick_up_location = None
        self.pick_up_year_month_day = None
        self.pick_up_time = None
        self.drop_off_year_month_day = None
        self.drop_off_time = None

    def perform_car_sharing(self, pick_up_location: str, pick_up_year_month_day: str, pick_up_time: str,
                            drop_off_year_month_day: str, drop_off_time: str):
        self.pick_up_year_month_day = pick_up_year_month_day
        self.pick_up_time = pick_up_time
        self.drop_off_year_month_day = drop_off_year_month_day
        self.drop_off_time = drop_off_time
        self.choose_pick_up_location()
        self.choose_pick_up_date()
        self.choose_drop_off_date()
        self.choose_pick_up_time()
        self.choose_drop_off_time()
        self.click_submit_button()

    def choose_pick_up_location(self, pick_up_location):
        self.element_interactions.send_text_in_field(SearchCarsTabLocators.CAR_LOCATION, pick_up_location)
        self.element_interactions.click_element(SearchCarsTabLocators.FIRST_ITEM_LOCATION_DROPDOWN)

    def choose_date(self, date: str):
        date_nt = TextFormatter.date_formatter(date)
        pick_up_date_month_locator = CalendarWidgetLocators.get_calendar_month_button_locator(date_nt.month_name)
        self.element_interactions.click_element(pick_up_date_month_locator)
        pick_up_date_day_locator = CalendarWidgetLocators.get_calendar_day_button_locator(date)
        self.element_interactions.click_element(pick_up_date_day_locator)

    def choose_time(self, time):
        element_in_time_ddm_locator = CalendarWidgetLocators.get_time_in_ddm_locator(time)
        self.element_interactions.click_element(element_in_time_ddm_locator)

    def choose_pick_up_date(self, date: str):
        self.element_interactions.click_element(SearchCarsTabLocators.PICK_UP_FORM)
        self.choose_date(date)

    def choose_drop_off_date(self, date: str):
        self.element_interactions.click_element(SearchCarsTabLocators.DROP_OFF_FORM)
        self.choose_date(date)

    def choose_pick_up_time(self, time: str):
        self.element_interactions.click_element(SearchCarsTabLocators.PICK_UP_TIME_FORM)
        self.choose_time(time)

    def choose_drop_off_time(self, time: str):
        self.element_interactions.click_element(SearchCarsTabLocators.DROP_OFF_TIME_FORM)
        self.choose_time(time)

    def click_submit_button(self):
        self.element_interactions.click_element(SearchCarsTabLocators.SEARCH_CARS_BUTTON)