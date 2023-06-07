
def current_user(email)
   User.find_by_email(email)
end


# This code sample illustrate good practice when trying to protect against SQL injection.