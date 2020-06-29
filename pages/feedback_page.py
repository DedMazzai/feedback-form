from .locators import FeedbackLocators
import random
import time


class FeedbackPage:
    def __init__(self, app):
        self.app = app

    def should_be_base_page_url(self):
        browser = self.app.browser
        test_url = browser.current_url
        assert "doctor/12/" in test_url, "It's not Test Url!"

    def should_be_clinic_selection(self):
        assert self.app.base_page.is_element_present(*FeedbackLocators.CLINICK_SELECTOR), \
            "Clinick selector is not present"

    def choose_another_clinic(self):
        self.app.base_page.click_element(*FeedbackLocators.CLINICK_SELECTOR)
        self.app.base_page.click_element(*FeedbackLocators.ANOTHER_CLINIC)

    def fill_another_clinic(self):
        content = "Тестовая клиника"
        self.app.base_page.fill_input_field(*FeedbackLocators.ANOTHER_CLINIC_INPUT_FIELD, content)

    def choose_star_of_assessment(self, how, what):
        browser = self.app.browser
        random_star = random.randrange(1, 5)
        stars = browser.find_elements(how, what)
        stars[random_star].click()

    def should_be_stars_of_assessment_of_survey_thoroughness(self):
        assert self.app.base_page.is_element_present(*FeedbackLocators.STARS_SURVEY_THOROUGHNESS),\
            "Stars of assessment of survey thoroughness is not present"

    def choose_star_of_assessment_of_survey_thoroughness(self):
        self.choose_star_of_assessment(*FeedbackLocators.STARS_SURVEY_THOROUGHNESS)

    def should_be_stars_of_assessment_of_treatment_effectiveness(self):
        assert self.app.base_page.is_element_present(*FeedbackLocators.STARS_TREATMENT_EFFECTIVENESS),\
            "Stars of assessment of treatment effectiveness is not present"

    def choose_star_of_assessment_of_treatment_effectiveness(self):
        self.choose_star_of_assessment(*FeedbackLocators.STARS_TREATMENT_EFFECTIVENESS)

    def should_be_stars_of_attitude_towards_the_patient(self):
        assert self.app.base_page.is_element_present(*FeedbackLocators.ATTITUDE_TOWARDS_THE_PATIENT),\
            "Stars of ATTITUDE TOWARDS THE PATIENT is not present"

    def choose_star_of_attitude_towards_the_patient(self):
        self.choose_star_of_assessment(*FeedbackLocators.ATTITUDE_TOWARDS_THE_PATIENT)

    def should_be_stars_of_assessment_of_patient_informing(self):
        assert self.app.base_page.is_element_present(*FeedbackLocators.STARS_PATIENT_INFORMING), \
            "STARS of PATIENT INFORMING is not present"

    def choose_star_of_assessment_of_patient_informing(self):
        self.choose_star_of_assessment(*FeedbackLocators.STARS_PATIENT_INFORMING)

    def should_be_stars_of_advise_doctor(self):
        assert self.app.base_page.is_element_present(*FeedbackLocators.STARS_ADVISE_DOCTOR), \
            "STARS of ADVISE DOCTOR is not present"

    def choose_star_of_advise_doctor(self):
        self.choose_star_of_assessment(*FeedbackLocators.STARS_ADVISE_DOCTOR)

    def should_be_input_field_liked(self):
        assert self.app.base_page.is_element_present(*FeedbackLocators.INPUT_FIELD_LIKED), \
            "INPUT FIELD LIKED is not present"

    def fill_input_field_liked(self):
        content = "Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест " \
                  "Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест"
        self.app.base_page.fill_input_field(*FeedbackLocators.INPUT_FIELD_LIKED, content)

    def should_be_input_field_not_liked(self):
        assert self.app.base_page.is_element_present(*FeedbackLocators.INPUT_FIELD_NOT_LIKED), \
            "INPUT FIELD NOT LIKED is not present"

    def fill_input_field_not_liked(self):
        content = "Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест " \
                  "Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест"
        self.app.base_page.fill_input_field(*FeedbackLocators.INPUT_FIELD_NOT_LIKED, content)

    def should_be_input_field_comment(self):
        assert self.app.base_page.is_element_present(*FeedbackLocators.FIELD_COMMENT), \
            "FIELD COMMENT is not present"

    def fill_input_field_not_comment(self):
        content = "Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест " \
                  "Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест Тест"
        self.app.base_page.fill_input_field(*FeedbackLocators.FIELD_COMMENT, content)

    def should_be_field_for_entering_phone(self):
        assert  self.app.base_page.is_element_present(*FeedbackLocators.PHONE_CONFIRM_FIELD), \
            "PHONE CONFIRM FIELD is not present"

    def fill_field_for_entering_phone(self):
        content = "9000000000"
        self.app.base_page.fill_input_field(*FeedbackLocators.PHONE_CONFIRM_FIELD, content)

    def should_be_confirm_phone_number_button(self):
        assert self.app.base_page.is_element_present(*FeedbackLocators.PHONE_CONFIRM_BUTTON), \
            "PHONE CONFIRM BUTTON is not present"

    def click_confirm_phone_number_button(self):
        self.app.base_page.click_element(*FeedbackLocators.PHONE_CONFIRM_BUTTON)

    def confirm_phone_number_button_is_not_present(self):
        self.app.base_page.is_not_element_present(*FeedbackLocators.PHONE_CONFIRM_BUTTON)
        time.sleep(5)



