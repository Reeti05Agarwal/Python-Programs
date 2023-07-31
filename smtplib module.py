import smtplib 

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()
  
# Authentication
s.login("mariacoding0507@gmail.com", "Maria@code0507")
  
# message to be sent
message = "DEMO MESSAGE"
  
# sending the mail
s.sendmail("mariacodint0507@gmail.com", "reeti@subrij.com", message)
  
# terminating the session
s.quit()
