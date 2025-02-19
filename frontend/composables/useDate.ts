export const useDate = () => {
  const { locale } = useI18n()

  const formatDate = (dateString: string): string => {
    const date = new Date(dateString)
    return date.toLocaleString(locale.value, {
      year: 'numeric',
      month: 'numeric',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    })
  }

  return { formatDate }
}
