# MentorMe

### Contribution Guidelines
[See here](https://github.com/TheHacktech/Resources/blob/master/CONTRIBUTION_GUIDELINES.md)

### Project Goal
We want to have a way for hackers to reach out to mentors during the hackathon. This would involve, at the very least, having a Slack integration that allows hackers to request help (what they need help on, where they are located, etc.) and a way for mentors to accept an incoming help request. Sort of like Uber for mentorship.  

### Set-up
Install [SlackClient](https://github.com/slackapi/python-slackclient)

Create a file called `config.py` in the root directory. Put the following in it:

```python
SLACK_TOKEN = "insert slack_token here"
```

Then run `python mentorbot.py`.
