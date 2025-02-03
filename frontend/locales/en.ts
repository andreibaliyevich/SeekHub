export default defineI18nLocale(async locale => {
  return {
    header: {
      about_us: 'About Us',
      howItWorks: 'How it Works',
      login: 'Log in',
      register: 'Register'
    },
    footer: {
      description: "SeekHub — an exclusive platform for ambitious and successful individuals who value quality in every connection.",
      rules: "Rules",
      advertising: "Advertising",
      our_logos: "Our Logos",
      feedback: "Feedback",
      more_about_seekhub: "More about SeekHub",
      analytics: "Analytics",
      career_at_seekhub: "Career at SeekHub",
      terms_of_use: "Terms of Use",
      privacy_policy: "Privacy Policy",
      advertising_and_promotion: "Advertising and promotion"
    },
    pages: {
      home: {
        title: 'Home',
        description: 'Home Seek Hub',
        keywords: 'Home, Seek, Hub'
      },
      about: {
        title: 'About Us',
        description: 'About Seek Hub',
        keywords: 'About, Seek, Hub'
      }
    },
    hello: 'Hello, {name}!',
    min_number_hours: 'minimum 0 hours | minimum 1 hour | minimum {n} hours',
    language: 'Language'
  }
})
