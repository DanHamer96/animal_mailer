# Animal Mailer - Project Overview

## Table of contents
* [About](#about)
* [Technologies](#technologies)
* [Example Output](#example-output)


## About
My aim for this project was to implement the smtplib module in Python. I wanted to learn how this module works while also putting it to good use. 
My girlfriend loves dogs & cows - so to start her day off right, the code will email her a cute dog or cow picture every morning! 

The script is scheduled to run locally on a cron job every morning:

`crontab -e`

`0 9  * * * /Users/dannyhamer96/anaconda3/bin/python3.6 /Users/dannyhamer96/PycharmProjects/animal_mailer/animal_mailer.py`

## Technologies
This project makes use of the following technologies: 

#### Languages:
- [Python 3.6](https://www.python.org)

#### Libraries:
- [smptlib](https://docs.python.org/3/library/smtplib.html)
- [pandas](https://pandas.pydata.org/docs/)
- [datetime](https://docs.python.org/3/library/datetime.html)
- [email](https://docs.python.org/3/library/email.message.html)
- [imghdr](https://docs.python.org/3/library/imghdr.html)

## Example Output
Below is an example output email generated by this script:

![example_output](https://user-images.githubusercontent.com/74738364/111072192-5d1ac980-84d1-11eb-9b4a-e4e069d9ec98.jpg)

