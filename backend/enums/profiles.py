from enum import Enum


class GenderType(str, Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


class BodyType(str, Enum):
    SLIM = "slim"
    ATHLETIC = "athletic"
    AVERAGE = "average"
    CURVY = "curvy"
    FULL_FIGURE = "full_figure"
    HEAVYSET = "heavyset"


class EthnicityType(str, Enum):
    ASIAN = "asian"
    BLACK_AFRICAN_DESCENT = "black_african_descent"
    LATIN_HISPANIC = "latin_hispanic"
    EAST_INDIAN = "east_indian"
    MIDDLE_EASTERN = "middle_eastern"
    MIXED = "mixed"
    NATIVE_AMERICAN = "native_american"
    PACIFIC_ISLANDER = "pacific_islander"
    WHITE_CAUCASIAN = "white_caucasian"
    OTHER = "other"


class RelationshipStatus(str, Enum):
    SINGLE = "single"
    DIVORCED = "divorced"
    SEPARATED = "separated"
    WIDOWED = "widowed"
    OPEN = "open"
    MARRIED = "married"


class DrinkStatus(str, Enum):
    NON_DRINKER = "non_drinker"
    SOCIAL_DRINKER = "social_drinker"
    HEAVY_DRINKER = "heavy_drinker"


class SmokeStatus(str, Enum):
    NON_SMOKER = "non_smoker"
    LIGHT_SMOKER = "light_smoker"
    HEAVY_SMOKER = "heavy_smoker"


class EducationLevel(str, Enum):
    HIGH_SCHOOL = "high_school"
    SOME_COLLEGE = "some_college"
    ASSOCIATES_DEGREE = "associates_degree"
    BACHELORS_DEGREE = "bachelors_degree"
    GRADUATE_DEGREE = "graduate_degree"
    PHD_POST_DOCTORAL = "phd_post_doctoral"
    MD_MEDICAL_DOCTOR = "md_medical_doctor"
    LAWYER_ATTORNEY = "lawyer_attorney"


class OccupationType(str, Enum):
    TECHNOLOGY = "technology"
    HEALTHCARE = "healthcare"
    EDUCATION = "education"
    FINANCE = "finance"
    GOVERNMENT = "government"
    RETAIL = "retail"
    HOSPITALITY = "hospitality"
    CONSTRUCTION = "construction"
    TRANSPORTATION = "transportation"
    ENTERTAINMENT = "entertainment"
    OTHER = "other"


class AnnualIncomeLevel(str, Enum):
    BELOW_20000 = "below_20000"
    FROM_20000_TO_50000 = "from_20000_to_50000"
    FROM_50000_TO_100000 = "from_50000_to_100000"
    FROM_100000_TO_200000 = "from_100000_to_200000"
    FROM_200000_TO_500000 = "from_200000_to_500000"
    FROM_500000_TO_1000000 = "from_500000_to_1000000"
    ABOVE_1000000 = "above_1000000"


class NetWorthLevel(str, Enum):
    BELOW_50000 = "below_50000"
    FROM_50000_TO_100000 = "from_50000_to_100000"
    FROM_100000_TO_500000 = "from_100000_to_500000"
    FROM_500000_TO_1000000 = "from_500000_to_1000000"
    FROM_1000000_TO_5000000 = "from_1000000_to_5000000"
    FROM_5000000_TO_10000000 = "from_5000000_to_10000000"
    ABOVE_10000000 = "above_10000000"


class SeekingTags(str, Enum):
    TRUE_LOVE = "true_love"
    ACTIVE_LIFESTYLE = "active_lifestyle"
    EMOTIONAL_CONNECTION = "emotional_connection"
    LONG_TERM = "long_term"
    ALL_ETHNICITIES = "all_ethnicities"
    INVESTOR = "investor"
    LIFE_OF_LEISURE = "life_of_leisure"
    LUXURY_LIFESTYLE = "luxury_lifestyle"
    MARRIAGE_MINDED = "marriage_minded"
    MENTORSHIP = "mentorship"
    MONOGAMOUS = "monogamous"
    NON_MONOGAMOUS = "non_monogamous"
    NO_STRINGS_ATTACHED = "no_strings_attached"
    OPEN_RELATIONSHIP = "open_relationship"
    PLATONIC = "platonic"
    ROMANCE = "romance"
    TRAVEL_TO_YOU = "travel_to_you"
    TRAVEL_WITH_ME = "travel_with_me"
