export default defineI18nLocale(async locale => {
  return {
    hello: 'Hello, {name}!',
    min_number_hours: "minimum 0 hours | minimum 1 hour | minimum {n} hours",
    language: "Language"
  }
})
