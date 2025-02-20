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
        email: "Email",
        password: "Пароль",
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
        email: "Электронная почта",
        password: "Пароль",
        confirm_password: "Подтвердите пароль",
        name: "Имя",
        select_date: "Выберите дату",
        birthday: "День рождения",
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
        name: "Имя",
        birthday: "День рождения",
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
