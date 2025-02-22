export const useProfileOptions = () => {
  const { t } = useI18n()

  const genderOptions = computed(() => {
    return [
      { value: 'male', title: t('types.gender_type.male') },
      { value: 'female', title: t('types.gender_type.female') },
      { value: 'other', title: t('types.gender_type.other') }
    ]
  })

  const bodyOptions = computed(() => {
    return [
      { value: 'slim', title: t('types.body_type.slim') },
      { value: 'athletic', title: t('types.body_type.athletic') },
      { value: 'average', title: t('types.body_type.average') },
      { value: 'curvy', title: t('types.body_type.curvy') },
      { value: 'full_figure', title: t('types.body_type.full_figure') },
      { value: 'heavyset', title: t('types.body_type.heavyset') }
    ]
  })

  const ethnicityOptions = computed(() => {
    return [
      { value: 'asian', title: t('types.ethnicity_type.asian') },
      { value: 'black_african_descent', title: t('types.ethnicity_type.black_african_descent') },
      { value: 'latin_hispanic', title: t('types.ethnicity_type.latin_hispanic') },
      { value: 'east_indian', title: t('types.ethnicity_type.east_indian') },
      { value: 'middle_eastern', title: t('types.ethnicity_type.middle_eastern') },
      { value: 'mixed', title: t('types.ethnicity_type.mixed') },
      { value: 'native_american', title: t('types.ethnicity_type.native_american') },
      { value: 'pacific_islander', title: t('types.ethnicity_type.pacific_islander') },
      { value: 'white_caucasian', title: t('types.ethnicity_type.white_caucasian') },
      { value: 'other', title: t('types.ethnicity_type.other') }
    ]
  })

  const relationshipOptions = computed(() => {
    return [
      { value: 'single', title: t('types.relationship_status.single') },
      { value: 'divorced', title: t('types.relationship_status.divorced') },
      { value: 'separated', title: t('types.relationship_status.separated') },
      { value: 'widowed', title: t('types.relationship_status.widowed') },
      { value: 'open', title: t('types.relationship_status.open') },
      { value: 'married', title: t('types.relationship_status.married') }
    ]
  })

  const drinkOptions = computed(() => {
    return [
      { value: 'non_drinker', title: t('types.drink_status.non_drinker') },
      { value: 'social_drinker', title: t('types.drink_status.social_drinker') },
      { value: 'heavy_drinker', title: t('types.drink_status.heavy_drinker') }
    ]
  })

  const smokeOptions = computed(() => {
    return [
      { value: 'non_smoker', title: t('types.smoke_status.non_smoker') },
      { value: 'light_smoker', title: t('types.smoke_status.light_smoker') },
      { value: 'heavy_smoker', title: t('types.smoke_status.heavy_smoker') }
    ]
  })

  const educationOptions = computed(() => {
    return [
      { value: 'high_school', title: t('types.education_level.high_school') },
      { value: 'some_college', title: t('types.education_level.some_college') },
      { value: 'associates_degree', title: t('types.education_level.associates_degree') },
      { value: 'bachelors_degree', title: t('types.education_level.bachelors_degree') },
      { value: 'graduate_degree', title: t('types.education_level.graduate_degree') },
      { value: 'phd_post_doctoral', title: t('types.education_level.phd_post_doctoral') },
      { value: 'md_medical_doctor', title: t('types.education_level.md_medical_doctor') },
      { value: 'lawyer_attorney', title: t('types.education_level.lawyer_attorney') }
    ]
  })

  const occupationOptions = computed(() => {
    return [
      { value: 'technology', title: t('types.occupation_type.technology') },
      { value: 'healthcare', title: t('types.occupation_type.healthcare') },
      { value: 'education', title: t('types.occupation_type.education') },
      { value: 'finance', title: t('types.occupation_type.finance') },
      { value: 'government', title: t('types.occupation_type.government') },
      { value: 'retail', title: t('types.occupation_type.retail') },
      { value: 'hospitality', title: t('types.occupation_type.hospitality') },
      { value: 'construction', title: t('types.occupation_type.construction') },
      { value: 'transportation', title: t('types.occupation_type.transportation') },
      { value: 'entertainment', title: t('types.occupation_type.entertainment') },
      { value: 'other', title: t('types.occupation_type.other') }
    ]
  })

  const annualIncomeOptions = computed(() => {
    return [
      { value: 'below_20000', title: t('types.annual_income_level.below_20000') },
      { value: 'from_20000_to_50000', title: t('types.annual_income_level.from_20000_to_50000') },
      { value: 'from_50000_to_100000', title: t('types.annual_income_level.from_50000_to_100000') },
      { value: 'from_100000_to_200000', title: t('types.annual_income_level.from_100000_to_200000') },
      { value: 'from_200000_to_500000', title: t('types.annual_income_level.from_200000_to_500000') },
      { value: 'from_500000_to_1000000', title: t('types.annual_income_level.from_500000_to_1000000') },
      { value: 'above_1000000', title: t('types.annual_income_level.above_1000000') }
    ]
  })

  const netWorthOptions = computed(() => {
    return [
      { value: 'below_50000', title: t('types.net_worth_level.below_50000') },
      { value: 'from_50000_to_100000', title: t('types.net_worth_level.from_50000_to_100000') },
      { value: 'from_100000_to_500000', title: t('types.net_worth_level.from_100000_to_500000') },
      { value: 'from_500000_to_1000000', title: t('types.net_worth_level.from_500000_to_1000000') },
      { value: 'from_1000000_to_5000000', title: t('types.net_worth_level.from_1000000_to_5000000') },
      { value: 'from_5000000_to_10000000', title: t('types.net_worth_level.from_5000000_to_10000000') },
      { value: 'above_10000000', title: t('types.net_worth_level.above_10000000') }
    ]
  })

  const genderPreferenceOptions = computed(() => {
    return [
      { value: 'male', title: t('types.gender_preference.male') },
      { value: 'female', title: t('types.gender_preference.female') },
      { value: 'other', title: t('types.gender_preference.other') }
    ]
  })

  const seekingTagsOptions = computed(() => {
    return [
      { value: 'true_love', title: t('types.seeking_tags.true_love') },
      { value: 'active_lifestyle', title: t('types.seeking_tags.active_lifestyle') },
      { value: 'emotional_connection', title: t('types.seeking_tags.emotional_connection') },
      { value: 'long_term', title: t('types.seeking_tags.long_term') },
      { value: 'all_ethnicities', title: t('types.seeking_tags.all_ethnicities') },
      { value: 'investor', title: t('types.seeking_tags.investor') },
      { value: 'life_of_leisure', title: t('types.seeking_tags.life_of_leisure') },
      { value: 'luxury_lifestyle', title: t('types.seeking_tags.luxury_lifestyle') },
      { value: 'marriage_minded', title: t('types.seeking_tags.marriage_minded') },
      { value: 'mentorship', title: t('types.seeking_tags.mentorship') },
      { value: 'monogamous', title: t('types.seeking_tags.monogamous') },
      { value: 'non_monogamous', title: t('types.seeking_tags.non_monogamous') },
      { value: 'no_strings_attached', title: t('types.seeking_tags.no_strings_attached') },
      { value: 'open_relationship', title: t('types.seeking_tags.open_relationship') },
      { value: 'platonic', title: t('types.seeking_tags.platonic') },
      { value: 'romance', title: t('types.seeking_tags.romance') },
      { value: 'travel_to_you', title: t('types.seeking_tags.travel_to_you') },
      { value: 'travel_with_me', title: t('types.seeking_tags.travel_with_me') }
    ]
  })

  return {
    genderOptions,
    bodyOptions,
    ethnicityOptions,
    relationshipOptions,
    drinkOptions,
    smokeOptions,
    educationOptions,
    occupationOptions,
    annualIncomeOptions,
    netWorthOptions,
    genderPreferenceOptions,
    seekingTagsOptions
  }
}
