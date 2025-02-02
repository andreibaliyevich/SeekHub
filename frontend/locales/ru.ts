export default defineI18nLocale(async locale => {
  return {
    hello: 'Привет, {name}!',
    min_number_hours: "минимум 0 часов | минимум 1 час | минимум {n} часа | минимум {n} часов",
    language: "Язык"
  }
})
