from enum import Enum


class GenderType(str, Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"


class BodyType(str, Enum):
    SLIM = "Slim"
    ATHLETIC = "Athletic"
    AVERAGE = "Average"
    CURVY = "Curvy"
    FULL_FIGURE = "Full Figure"
    HEAVYSET = "Heavyset"


class EthnicityType(str, Enum):
    ASIAN = "Asian"
    BLACK = "Black / African Descent"
    LATIN = "Latin / Hispanic"
    EAST_INDIAN = "East Indian"
    MIDDLE_EASTERN = "Middle Eastern"
    MIXED = "Mixed"
    NATIVE_AMERICAN = "Native American"
    PACIFIC_ISLANDER = "Pacific Islander"
    WHITE = "White / Caucasian"
    OTHER = "Other"


class RelationshipStatus(str, Enum):
    SINGLE = "Single"
    DIVORCED = "Divorced"
    SEPARATED = "Separated"
    WIDOWED = "Widowed"
    OPEN = "Open"
    MARRIED = "Married"


class DrinkStatus(str, Enum):
    NON_DRINKER = "Non Drinker"
    SOCIAL_DRINKER = "Social Drinker"
    HEAVY_DRINKER = "Heavy Drinker"


class SmokeStatus(str, Enum):
    NON_SMOKER = "Non Smoker"
    LIGHT_SMOKER = "Light Smoker"
    HEAVY_SMOKER = "Heavy Smoker"


class EducationLevel(str, Enum):
    HIGH_SCHOOL = "High School"
    SOME_COLLEGE = "Some College"
    ASSOCIATES_DEGREE = "Associates Degree"
    BACHELORS_DEGREE = "Bachelors Degree"
    GRADUATE_DEGREE = "Graduate Degree"
    PHD = "PhD / Post Doctoral"
    MD = "MD / Medical Doctor"
    JD = "JD / Attorney"


class OccupationType(str, Enum):
    TECHNOLOGY = "Technology"
    HEALTHCARE = "Healthcare"
    EDUCATION = "Education"
    FINANCE = "Finance"
    GOVERNMENT = "Government"
    RETAIL = "Retail"
    HOSPITALITY = "Hospitality"
    CONSTRUCTION = "Construction"
    TRANSPORTATION = "Transportation"
    ENTERTAINMENT = "Entertainment"
    OTHER = "Other"


class AnnualIncomeLevel(str, Enum):
    BELOW_20000 = "< 20000"
    FROM_20000_TO_50000 = "20000 - 50000"
    FROM_50000_TO_100000 = "50000 - 100000"
    FROM_100000_TO_200000 = "100000 - 200000"
    FROM_200000_TO_500000 = "200000 - 500000"
    FROM_500000_TO_1000000 = "500000 - 1000000"
    ABOVE_1000000 = "> 1000000"


class NetWorthLevel(str, Enum):
    BELOW_50000 = "< 50000"
    FROM_50000_TO_100000 = "50000 - 100000"
    FROM_100000_TO_500000 = "100000 - 500000"
    FROM_500000_TO_1000000 = "500000 - 1000000"
    FROM_1000000_TO_5000000 = "1000000 - 5000000"
    FROM_5000000_TO_10000000 = "5000000 - 10000000"
    ABOVE_10000000 = "> 10000000"


class SeekingTags(str, Enum):
    TRUE_LOVE = "True Love"
    ACTIVE_LIFESTYLE = "Active lifestyle"
    EMOTIONAL_CONNECTION = "Emotional connection"
    LONG_TERM = "Long-term"
    ALL_ETHNICITIES = "All ethnicities"
    INVESTOR = "Investor"
    LIFE_OF_LEISURE = "Life of leisure"
    LUXURY_LIFESTYLE = "Luxury lifestyle"
    MARRIAGE_MINDED = "Marriage minded"
    MENTORSHIP = "Mentorship"
    MONOGAMOUS = "Monogamous"
    NON_MONOGAMOUS = "Non-monogamous"
    NO_STRINGS_ATTACHED = "No strings attached"
    OPEN_RELATIONSHIP = "Open relationship"
    PLATONIC = "Platonic"
    ROMANCE = "Romance"
    TRAVEL_TO_YOU = "Travel to you"
    TRAVEL_WITH_ME = "Travel with me"
