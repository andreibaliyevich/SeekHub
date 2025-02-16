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
        email: "Email",
        password: "Password",
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
        email: "Email",
        password: "Password",
        confirm_password: "Confirm password",
        name: "Name",
        select_date: "Select date",
        birthday: "Birthday",
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
      error: {
        text404: "The page you were looking for does not exist.",
        action_text: "Go Home"
      }
    },
    hello: "Hello, {name}!",
    min_number_hours: "minimum 0 hours | minimum 1 hour | minimum {n} hours",
    language: "Language"
  }
})
