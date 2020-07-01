
def test_fill_feedback_form_valid_data(app):
    # открываем тестовую страницу
    app.open_base_page()
    # проверяем что находимся на странице обратной связи
    app.feedback_page.should_be_base_page_url()
    # проверяем что есть селект выбора клиники
    app.feedback_page.should_be_clinic_selection()
    # выбираем другую клинику в селекте
    app.feedback_page.choose_another_clinic()
    # заполняем поле названия и адреса другой клиники
    app.feedback_page.fill_another_clinic()
    # проверяем что есть звезды для оценки тщательности обследования
    app.feedback_page.should_be_stars_of_assessment_of_survey_thoroughness()
    # выбираем рандомно звезду для оценки тщательности обследования
    app.feedback_page.choose_star_of_assessment_of_survey_thoroughness()
    # проверяем что есть звезды для оценки эффективности лечения
    app.feedback_page.should_be_stars_of_assessment_of_treatment_effectiveness()
    # выбираем рандомно звезду для оценки эффективности лечения
    app.feedback_page.choose_star_of_assessment_of_treatment_effectiveness()
    # проверяем что есть звезды для оценки отношения к пациенту
    app.feedback_page.should_be_stars_of_attitude_towards_the_patient()
    #выбираем рандомно звезду для оценки отношения к пациенту
    app.feedback_page.choose_star_of_attitude_towards_the_patient()
    # проверяем что есть звезды для оценки информирования пациента
    app.feedback_page.should_be_stars_of_assessment_of_patient_informing()
    # выбираем рандомно звезду для оценки информирования пациента
    app.feedback_page.choose_star_of_assessment_of_patient_informing()
    # проверяем что есть звезды для совета врача
    app.feedback_page.should_be_stars_of_advise_doctor()
    # выбираем рандомно звезду для совета врача
    app.feedback_page.choose_star_of_advise_doctor()
    # проверяем что есть поле ввода Понравилось
    app.feedback_page.should_be_input_field_liked()
    # заполняем поlе ввода Понравилось
    app.feedback_page.fill_input_field_liked()
    # проверяем что есть поле ввода Не Понравилось
    app.feedback_page.should_be_input_field_not_liked()
    # заполняем поле ввода Не Понравилось
    app.feedback_page.fill_input_field_not_liked()
    # проверяем что есть поле ввода Коментарий
    app.feedback_page.should_be_input_field_comment()
    # заполняем поле ввода Коментарий
    app.feedback_page.fill_input_field_not_comment()
    #  проверяем что есть поле для ввода номера телефона
    app.feedback_page.should_be_field_for_entering_phone()
    # вводим номер телефона
    app.feedback_page.fill_field_for_entering_phone()
    # должна быть кнопка подтверждения номера телефона
    app.feedback_page.should_be_confirm_phone_number_button()
    # кликнуть по кнопке подтверждения номера телефона
    app.feedback_page.click_confirm_phone_number_button()
    # проверка что появилась надпись с предложением перезвонить по бесплатному номеру для подтверждения телефона
    app.feedback_page.should_be_call_number_inscription()