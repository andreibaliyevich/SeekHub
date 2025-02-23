export default defineI18nLocale(async locale => {
  return {
    header: {
      about_us: "О нас",
      howItWorks: "Как это работает",
      login: "Войти",
      register: "Зарегистрироваться",
      search: "Поиск",
      interests: "Интересы",
      messages: "Сообщения",
      view_profile: "Посмотреть профиль",
      edit_profile: "Редактировать профиль",
      settings: "Настройки",
      log_out: "Выйти"
    },
    footer: {
      description: "SeekHub — эксклюзивная платформа для амбициозных и успешных людей, которые ценят качество во всем.",
      rules: "Правила",
      advertising: "Реклама",
      our_logos: "Наши Логотипы",
      feedback: "Обратная связь",
      more_about_seekhub: "Подробнее о SeekHub",
      analytics: "Аналитика",
      career_at_seekhub: "Карьера в SeekHub",
      terms_of_use: "Условия использования",
      privacy_policy: "Политика конфиденциальности",
      advertising_and_promotion: "Реклама и продвижение"
    },
    pages: {
      home: {
        title: "Главная",
        description: "Главная Seek Hub",
        keywords: "Главная, Seek, Hub"
      },
      about: {
        title: "О нас",
        description: "О Seek Hub",
        keywords: "О, Seek, Hub"
      },
      login: {
        title: "Вход в аккаунт",
        have_account: "У вас нет аккаунта?",
        register: "Зарегистрироваться",
        log_in: "Войти",
        forgot_your_password: "Забыли свой пароль?",
        reset_password: "Сбросить пароль",
        error: "Неверный email или пароль."
      },
      register: {
        title: "Создать аккаунт",
        description: "Зарегистрироваться Seek Hub",
        keywords: "Зарегистрироваться, Seek, Hub",
        have_account: "У вас уже есть аккаунт?",
        log_in: "Войти",
        register: "Зарегистрироваться",
        email_unique: "Пользователь с таким адресом электронной почты уже существует.",
        email_valid1: "Адрес электронной почты должен содержать знак @.",
        email_valid2: "После знака @ должно быть что-то еще.",
        email_valid3: "Часть после знака @ недопустима. Там должна быть точка.",
        email_valid4: "Адрес электронной почты не может заканчиваться точкой.",
        password_valid1: "Пароль должен быть длиной не менее 8 символов.",
        password_valid2: "Пароль должен содержать хотя бы одну цифру.",
        password_valid3: "Пароль должен содержать хотя бы одну заглавную букву.",
        password_valid4: "Пароль должен содержать хотя бы один специальный символ (например, @, $, !, %, *, ?, &).",
        confirm_password_not_match: "Пароли не совпадают.",
        birthday_valid: "Ввод должен быть допустимой датой, ввод слишком короткий.",
        success1: "Вы успешно зарегистрировались!",
        success2: "Пожалуйста, проверьте свою электронную почту.",
        success3: "Вам отправлено электронное письмо со ссылкой, по которой необходимо перейти для активации учетной записи.",
        help: "Нажимая «Зарегистрироваться», вы соглашаетесь с условиями использования."
      },
      profile: {
        title: "Профиль",
        update_profile: "Обновить профиль",
        upload_photo: "Загрузить фото",
        make_private: "Сделать приватным",
        make_public: "Сделать публичным",
        make_primary: "Сделать основным",
        make_non_primary: "Сделать неосновным",
        you_want_remove_photo: "Вы уверены, что хотите удалить это фото?",
        photo_information_will_lost: "Вся информация, связанная с этой фотографией, будет потеряна."
      },
      error: {
        text404: "Страница, которую вы искали, не существует.",
        action_text: "На главную"
      }
    },
    user: {
      email: "Электронная почта",
      password: "Пароль",
      confirm_password: "Подтвердите пароль",
      date_joined: "Дата регистрации",
      name: "Имя",
      birthday: "День рождения",
      is_verified: "Профиль проверен!",
      not_verified: "Профиль не проверен!",
      profile: {
        gender: "Пол",
        heading: "Заголовок",
        city: "Город",
        height: "Рост",
        height_suffix: "см",
        body_type: "Тип телосложения",
        ethnicity: "Этническая принадлежность",
        relationship_status: "Семейное положение",
        children: "Дети",
        drink: "Отношение к алкоголю",
        smoke: "Отношение к курению",
        education: "Образование",
        occupation: "Род занятий",
        annual_income: "Годовой доход",
        net_worth: "Собственный капитал",
        about: "О себе",
        gender_preference: "Гендерные предпочтения",
        age_preference: "Возрастные предпочтения",
        seeking_tags: "Поисковые теги",
        max_character: "Максимум {number} символов"
      }
    },
    types: {
      gender_type: {
        male: "Мужчина",
        female: "Женщина",
        other: "Другое"
      },
      body_type: {
        slim: "Стройное телосложение",
        athletic: "Атлетическое телосложение",
        average: "Среднее телосложение",
        curvy: "Изогнутые формы",
        full_figure: "Полная фигура",
        heavyset: "Крупное телосложение"
      },
      ethnicity_type: {
        asian: "Азиат",
        black_african_descent: "Темнокожий / Африканское происхождение",
        latin_hispanic: "Латиноамериканец / Испаноязычный",
        east_indian: "Выходец из Индии",
        middle_eastern: "Ближневосточное происхождение",
        mixed: "Смешанное происхождение",
        native_american: "Коренной американец",
        pacific_islander: "Выходец с островов Тихого океана",
        white_caucasian: "Белый / Европейское происхождение",
        other: "Другое"
      },
      relationship_status: {
        single: "Холост / Не замужем",
        divorced: "Разведен(а)",
        separated: "В раздельном проживании",
        widowed: "Вдова / Вдовец",
        open: "Открытые отношения",
        married: "Женат / Замужем"
      },
      drink_status: {
        non_drinker: "Непьющий",
        social_drinker: "Социально выпивающий",
        heavy_drinker: "Пьяница"
      },
      smoke_status: {
        non_smoker: "Некурящий",
        light_smoker: "Легкий курильщик",
        heavy_smoker: "Заядлый курильщик"
      },
      education_level: {
        high_school: "Университет",
        some_college: "Колледж",
        associates_degree: "Степень младшего специалиста",
        bachelors_degree: "Степень бакалавра",
        graduate_degree: "Ученая степень",
        phd_post_doctoral: "Кандидат наук / Постдокторант",
        md_medical_doctor: "Доктор медицины / Врач",
        lawyer_attorney: "Юрист / Адвокат"
      },
      occupation_type: {
        technology: "Технологии",
        healthcare: "Здравоохранение",
        education: "Образование",
        finance: "Финансы",
        government: "Государственный сектор",
        retail: "Розничная торговля",
        hospitality: "Гостиничный бизнес",
        construction: "Строительство",
        transportation: "Транспорт",
        entertainment: "Индустрия развлечений",
        other: "Другое"
      },
      annual_income_level: {
        below_20000: "менее 20,000",
        from_20000_to_50000: "от 20,000 до 50,000",
        from_50000_to_100000: "от 50,000 до 100,000",
        from_100000_to_200000: "от 100,000 до 200,000",
        from_200000_to_500000: "от 200,000 до 500,000",
        from_500000_to_1000000: "от 500,000 до 1,000,000",
        above_1000000: "более 1,000,000"
      },
      net_worth_level: {
        below_50000: "менее 50,000",
        from_50000_to_100000: "от 50,000 до 100,000",
        from_100000_to_500000: "от 100,000 до 500,000",
        from_500000_to_1000000: "от 500,000 до 1,000,000",
        from_1000000_to_5000000: "от 1,000,000 до 5,000,000",
        from_5000000_to_10000000: "от 5,000,000 до 10,000,000",
        above_10000000: "более 10,000,000"
      },
      gender_preference: {
        male: "Мужчины",
        female: "Женщины",
        other: "Другие"
      },
      seeking_tags: {
        true_love: "Настоящая любовь",
        active_lifestyle: "Активный образ жизни",
        emotional_connection: "Эмоциональная связь",
        long_term: "Долгосрочные отношения",
        all_ethnicities: "Все этнические группы",
        investor: "Инвестор",
        life_of_leisure: "Жизнь в удовольствие",
        luxury_lifestyle: "Роскошный образ жизни",
        marriage_minded: "Ориентирован на брак",
        mentorship: "Наставничество",
        monogamous: "Моногамные отношения",
        non_monogamous: "Немоногамные отношения",
        no_strings_attached: "Без обязательств",
        open_relationship: "Открытые отношения",
        platonic: "Платонические отношения",
        romance: "Романтика",
        travel_to_you: "Путешествие к вам",
        travel_with_me: "Путешествие со мной"
      }
    },
    base_btn: {
      cancel: "Отмена",
      close: "Закрыть",
      upload: "Загрузить",
      yes_i_am_sure: "Да, я уверен",
      no_cancel: "Нет, отменить"
    },
    hello: "Привет, {name}!",
    min_number_hours: "минимум 0 часов | минимум 1 час | минимум {n} часа | минимум {n} часов",
    language: "Язык"
  }
})
