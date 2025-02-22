export default defineI18nLocale(async locale => {
  return {
    header: {
      about_us: "About Us",
      howItWorks: "How it Works",
      login: "Log in",
      register: "Register",
      search: "Search",
      interests: "Interests",
      messages: "Messages",
      view_profile: "View Profile",
      edit_profile: "Edit Profile",
      settings: "Settings",
      log_out: "Log out"
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
        title: "Home",
        description: "Home Seek Hub",
        keywords: "Home, Seek, Hub"
      },
      about: {
        title: "About Us",
        description: "About Seek Hub",
        keywords: "About, Seek, Hub"
      },
      login: {
        title: "Login to your account",
        have_account: "Don't have an account?",
        register: "Register",
        log_in: "Log in",
        forgot_your_password: "Forgot your password?",
        reset_password: "Reset password",
        error: "Invalid email or password."
      },
      register: {
        title: "Create an account",
        description: "Register Seek Hub",
        keywords: "Register, Seek, Hub",
        have_account: "Already have an account?",
        log_in: "Log in",
        register: "Register",
        email_unique: "A user with this email already exists.",
        email_valid1: "An email address must have an @-sign.",
        email_valid2: "There must be something after the @-sign.",
        email_valid3: "The part after the @-sign is not valid. It should have a period.",
        email_valid4: "An email address cannot end with a period.",
        password_valid1: "Password must be at least 8 characters long.",
        password_valid2: "Password must contain at least one digit.",
        password_valid3: "Password must contain at least one uppercase letter.",
        password_valid4: "Password must contain at least one special character (e.g. @, $, !, %, *, ?, &).",
        confirm_password_not_match: "Passwords do not match.",
        birthday_valid: "Input should be a valid date, input is too short.",
        success1: "You have successfully registered!",
        success2: "Please check your email.",
        success3: "You have been sent an email with a link that you need to click on to activate your account.",
        help: "By clicking Sign up, you agree to the terms of use."
      },
      profile: {
        title: "Profile",
        update_profile: "Update profile",
        upload_photo: "Upload photo",
        make_private: "Make private",
        make_public: "Make public",
        make_primary: "Make primary",
        make_non_primary: "Make non-primary",
        you_want_remove_photo: "Are you sure you want to delete this photo?",
        photo_information_will_lost: "All information associated with this photo will be lost."
      },
      error: {
        text404: "The page you were looking for does not exist.",
        action_text: "Go Home"
      }
    },
    user: {
      email: "Email",
      password: "Password",
      confirm_password: "Confirm password",
      name: "Name",
      birthday: "Birthday",
      profile: {
        gender: "Gender",
        heading: "Heading",
        city: "City",
        height: "Height",
        height_suffix: "sm",
        body_type: "Body type",
        ethnicity: "Ethnicity",
        relationship_status: "Relationship status",
        children: "Children",
        drink: "Attitude to alcohol",
        smoke: "Attitude to smoking",
        education: "Education",
        occupation: "Occupation",
        annual_income: "Annual income",
        net_worth: "Net worth",
        about: "About me",
        about_hint: "Maximum 5000 character",
        gender_preference: "Gender preference",
        age_preference: "Age preference",
        seeking_tags: "Seeking tags"
      }
    },
    types: {
      gender_type: {
        male: "Male",
        female: "Female",
        other: "Other"
      },
      body_type: {
        slim: "Slim",
        athletic: "Athletic",
        average: "Average",
        curvy: "Curvy",
        full_figure: "Full Figure",
        heavyset: "Heavyset"
      },
      ethnicity_type: {
        asian: "Asian",
        black_african_descent: "Black / African Descent",
        latin_hispanic: "Latin / Hispanic",
        east_indian: "East Indian",
        middle_eastern: "Middle Eastern",
        mixed: "Mixed",
        native_american: "Native American",
        pacific_islander: "Pacific Islander",
        white_caucasian: "White / Caucasian",
        other: "Other"
      },
      relationship_status: {
        single: "Single",
        divorced: "Divorced",
        separated: "Separated",
        widowed: "Widowed",
        open: "Open",
        married: "Married"
      },
      drink_status: {
        non_drinker: "Non Drinker",
        social_drinker: "Social Drinker",
        heavy_drinker: "Heavy Drinker"
      },
      smoke_status: {
        non_smoker: "Non Smoker",
        light_smoker: "Light Smoker",
        heavy_smoker: "Heavy Smoker"
      },
      education_level: {
        high_school: "High School",
        some_college: "Some College",
        associates_degree: "Associates Degree",
        bachelors_degree: "Bachelors Degree",
        graduate_degree: "Graduate Degree",
        phd_post_doctoral: "PhD / Post Doctoral",
        md_medical_doctor: "MD / Medical Doctor",
        lawyer_attorney: "Lawyer / Attorney"
      },
      occupation_type: {
        technology: "Technology",
        healthcare: "Healthcare",
        education: "Education",
        finance: "Finance",
        government: "Government",
        retail: "Retail",
        hospitality: "Hospitality",
        construction: "Construction",
        transportation: "Transportation",
        entertainment: "Entertainment",
        other: "Other"
      },
      annual_income_level: {
        below_20000: "below 20,000",
        from_20000_to_50000: "from 20,000 to 50,000",
        from_50000_to_100000: "from 50,000 to 100,000",
        from_100000_to_200000: "from 100,000 to 200,000",
        from_200000_to_500000: "from 200,000 to 500,000",
        from_500000_to_1000000: "from 500,000 to 1,000,000",
        above_1000000: "above 1,000,000"
      },
      net_worth_level: {
        below_50000: "below 50,000",
        from_50000_to_100000: "from 50,000 to 100,000",
        from_100000_to_500000: "from 100,000 to 500,000",
        from_500000_to_1000000: "from 500,000 to 1,000,000",
        from_1000000_to_5000000: "from 1,000,000 to 5,000,000",
        from_5000000_to_10000000: "from 5,000,000 to 10,000,000",
        above_10000000: "above 10,000,000"
      },
      gender_preference: {
        male: "Men",
        female: "Women",
        other: "Others"
      },
      seeking_tags: {
        true_love: "True Love",
        active_lifestyle: "Active lifestyle",
        emotional_connection: "Emotional connection",
        long_term: "Long-term",
        all_ethnicities: "All ethnicities",
        investor: "Investor",
        life_of_leisure: "Life of leisure",
        luxury_lifestyle: "Luxury lifestyle",
        marriage_minded: "Marriage minded",
        mentorship: "Mentorship",
        monogamous: "Monogamous",
        non_monogamous: "Non-monogamous",
        no_strings_attached: "No strings attached",
        open_relationship: "Open relationship",
        platonic: "Platonic",
        romance: "Romance",
        travel_to_you: "Travel to you",
        travel_with_me: "Travel with me"
      }
    },
    base_btn: {
      cancel: "Cancel",
      close: "Close",
      upload: "Upload",
      yes_i_am_sure: "Yes, I am sure",
      no_cancel: "No, cancel"
    },
    hello: "Hello, {name}!",
    min_number_hours: "minimum 0 hours | minimum 1 hour | minimum {n} hours",
    language: "Language"
  }
})
