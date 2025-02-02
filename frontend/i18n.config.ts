function pluralSlavicRule(
  choice: number,
  choicesLength: number,
  orgRule: any
): number {
  if (choice === 0) {
    return 0
  }

  const teen = choice > 10 && choice < 20
  if (!teen && choice % 10 === 1) {
    return 1
  }
  if (!teen && choice % 10 >= 2 && choice % 10 <= 4) {
    return 2
  }

  return choicesLength < 4 ? 2 : 3
}

export default defineI18nConfig(() => ({
  legacy: false,
  globalInjection: true,
  locale: 'en',
  fallbackLocale: 'en',
  pluralRules: {
    ru: pluralSlavicRule
  }
}))
