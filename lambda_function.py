from __future__ import print_function
import os
import subprocess
import boto3
client = boto3.client('budgets')

#Set this to your Slack Incoming Webhook URL (https://api.slack.com/apps)
webhook = "https://hooks.slack.com/services/T02XXX7V/B9R0YXXXU/3Cb0XXX9MGKIfhM6gXXXR6V"

#Set this string to the name of the AWS Budget you wish to monitor
budgetName = "Monthly AWS Budget"

#Set this value to your account ID
accID = '123443214608'

#Lambda entry point
def lambda_handler(event, context):
    getBudget()
    return 'All good.'

def getBudget():
    print('Getting budget info')
    res = client.describe_budget(AccountId=accID, BudgetName=budgetName)
    
    #Get budget details
    limit = str(res['Budget']['BudgetLimit']['Amount'])[:7]
    act = str(res['Budget']['CalculatedSpend']['ActualSpend']['Amount'])[:7]
    forecast = str(res['Budget']['CalculatedSpend']['ForecastedSpend']['Amount'])[:7]
    
    #Post billing info to Slack
    #slack("Budget name is %s" % res['Budget']['BudgetName'])
    slack("Billing report! Monthly AWS budget of $" + limit + '.\n\nActual spend so far this month: $' + act + '. Forecast spend for this month: $' + forecast + '.')

def slack(message):
    data = "'{\"text\":\"" + message + " \"}'"
    type = "'Content-type: application/json'"
    command = ["curl -X POST -H " + type + " --data " + data + " " + webhook]

    print('Sending message: ' + message + ' data: ' + data + ' command: ' + str(command))

    try:
        subprocess.check_output(command,shell=True,stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
        quit('Error posting to slack')
    
    return 'ok'
