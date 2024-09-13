# lab-climate-change
Exploring Climate Change through Data

## Requirements

Update `./mnt/airflow/airflow.cfg`. Specify the credentials of your email service provider.

```
smtp_host = 
smtp_starttls = True
smtp_ssl = False
# Example: smtp_user = airflow
smtp_user =
# Example: smtp_password = airflow
smtp_password =
smtp_port = 
smtp_mail_from = 
smtp_timeout = 30
smtp_retry_limit = 5
```

For Google Mail, you can follow the instructions to create an app key.
- Article: [Sign in with app passwords](https://support.google.com/accounts/answer/185833?hl=en)
- Page: [Google App passwords](https://myaccount.google.com/apppasswords)

## Starting the container

Execute `start.sh` to start the container, and `stop.sh` to stop it. These scripts use docker compose.
