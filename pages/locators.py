from selenium.webdriver.common.by import By

class FeedbackLocators:
    CLINICK_SELECTOR = (By.CSS_SELECTOR, ".b-address-select .b-select__trigger")
    ANOTHER_CLINIC = (By.CSS_SELECTOR, ".b-address-select li:nth-child(2) span")
    ANOTHER_CLINIC_INPUT_FIELD = (By.CSS_SELECTOR, "[name = 'lpuaddr_text']")
    STARS_SURVEY_THOROUGHNESS = (By.CSS_SELECTOR, ".b-rate-form.send_rate_form .b-stars:nth-child(4) .b-stars__star")
    STARS_TREATMENT_EFFECTIVENESS = (By.CSS_SELECTOR, ".b-rate-form.send_rate_form .b-stars:nth-child(5) .b-stars__star")
    ATTITUDE_TOWARDS_THE_PATIENT = (By.CSS_SELECTOR, ".b-rate-form.send_rate_form .b-stars:nth-child(6) .b-stars__star")
    STARS_PATIENT_INFORMING = (By.CSS_SELECTOR, ".b-rate-form.send_rate_form .b-stars:nth-child(7) .b-stars__star")
    STARS_ADVISE_DOCTOR = (By.CSS_SELECTOR, ".b-rate-form.send_rate_form .b-stars:nth-child(8) .b-stars__star")
    INPUT_FIELD_LIKED = (By.CSS_SELECTOR, "[name='comment_plus']")
    INPUT_FIELD_NOT_LIKED = (By.CSS_SELECTOR, "[name='comment_minus']")
    FIELD_COMMENT = (By.CSS_SELECTOR, "[name='comment']")
    PHONE_CONFIRM_FIELD = (By.CSS_SELECTOR, ".b-phone-confirm__number")
    PHONE_CONFIRM_BUTTON = (By.CSS_SELECTOR, ".b-phone-confirm__confirm.b-button.b-button_blue")
