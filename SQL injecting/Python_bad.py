# String concatenation is vulnerable.
cursor.execute("select user_id, user_name from users where email = '%s'" % email)

for row in cursor.fetchall():
  print row.user_id, row.user_name

# This code sample illustrate bad practice when trying to protect against SQL injection.