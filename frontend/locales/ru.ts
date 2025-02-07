export default defineI18nLocale(async locale => {
  return {
    header: {
      about_us: 'О нас',
      howItWorks: 'Как это работает',
      login: 'Войти',
      register: 'Зарегистрироваться'
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
        title: 'Главная',
        description: 'Главная Seek Hub',
        keywords: 'Главная, Seek, Hub'
      },
      about: {
        title: 'О нас',
        description: 'О Seek Hub',
        keywords: 'О, Seek, Hub'
      },
      error: {
        text404: "Страница, которую вы искали, не существует.",
        action_text: "На главную"
      }
    },
    hello: 'Привет, {name}!',
    min_number_hours: 'минимум 0 часов | минимум 1 час | минимум {n} часа | минимум {n} часов',
    language: 'Язык'
  }
})
