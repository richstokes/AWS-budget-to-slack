# AWS-budget-to-slack
AWS Lambda function posts billing updates to your Slack channel. Built for Python3.6

## Requirements

Create a Slack API application with an incoming webhook. 

Trigger the function with a CloudWatch event set to your desired interval. For example, you could set the schedule to "rate(7 days)" to get a billing update in Slack once per week.

Give the Lambda function read-only access to your billing info.


## Example Slack post
![AWS-to-slack report](https://raw.githubusercontent.com/richstokes/AWS-budget-to-slack/master/example.png)
