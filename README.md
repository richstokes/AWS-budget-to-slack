# AWS-budget-to-slack
AWS Lambda function posts billing updates to your Slack channel. Built for Python3.6

Requires you to create a Slack API application with an incoming webhook. 

Trigger the function with a CloudWatch event set to your desired interval. 

For example, you could set the schedule to "rate(7 days)" to get a billing update in Slack once per week.
