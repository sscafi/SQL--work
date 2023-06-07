
# SQL and parameter is sent off separately to the database driver.
cursor.execute("select user_id, user_name from users where email = ?", email)

for row in cursor.fetchall():
  print row.user_id, row.user_name
# This code sample illustrate good practice when trying to protect against SQL injection.