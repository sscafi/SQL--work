def current_user(email)
  User.where("email = '" + email + "'")
end


# This code sample illustrate bad practice when trying to protect against SQL injection.