"""
This code sample is a starter tutorial to show  how to create Alexa skill (app) using AWS Lambda.

For the full code sample visit https://github.com/sriramcvn/alexa-lambda-tutorial-list-aws-services
"""

from __future__ import print_function
import random

def lambda_handler(event, context):
    """
    print application id received from input request from Alexa Skill.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    CHANGEME: replace with application id for your Alexa skill
    """
    if (event['session']['application']['applicationId'] !=
            "amzn1.ask.skill.3d41faf7-cace-47e3-8c6a-19a04b80740e"):
        raise ValueError("Invalid Application ID")

    SKILL_INFO = {
        'name': "Service Map",
        'invocation': "service map",
        'allservices': "AWS services are categorized under Security, Compute, Storage, Database, Migration, Network etc.",
        'slot_name': "awsservice",
        'slot_responses': {
            "security": "Services in {} category are IAM, Cognito, GuardDuty, Inspector, Amazon Macie, Certificate Manager, CloudHSM, Directory Service, WAF & Shield, and Artifact",
            "compute": "Services in {} category are EC2, Lightsail, ECS, Lambda, Batch and ElasticBeanstalk",
            "storage": "Services in {} category are S3, EFS, Glacier and Storage Gateway",
            "database": "Services in {} category are RDS, DynamoDB, ElastiCache and Amazon Redshift",
            "migration" : "Services in {} category are AWS Migration Hub, Application Discovery Service, Database Migration Service, Server Migration Service and Snowball",
            "network": "Services in {} category are VPC, CloudFront, Route53, API Gateway and Direct Connect",
        },
    }

    INTENTS = {
        "SkillInfoIntent": get_info_response,
        "SkillMainIntent": get_main_response,
        "SkillSlotIntent": get_slot_response,
        "AMAZON.HelpIntent": get_help_response,
        "AMAZON.CancelIntent": handle_session_end_request,
        "AMAZON.StopIntent": handle_session_end_request,
    }

    if event['session']['new']:
        on_session_started(
            {'requestId': event['request']['requestId']},
            event['session']
        )

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'], SKILL_INFO)
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'], SKILL_INFO, INTENTS)
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'], SKILL_INFO)


def on_session_started(request, session):
    """ Called when the session starts """

    info = "on_session_started requestId={} sessionId={}"
    print(info.format(request['requestId'], session['sessionId']))


def on_launch(request, session, skill):
    """ Called when the user launches the skill without specifying what they want """

    return get_welcome_response(skill)


def on_intent(request, session, skill, intents):
    """ Called when the user specifies an intent for this skill """

    intent = request['intent']
    intent_name = request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name in intents:
        return intents[intent_name](skill, request)
    else:
        raise ValueError("Invalid intent")


def on_session_ended(request, session, skill):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here

# --------------- Functions that control the skill's behavior ------------------


def get_welcome_response(skill):
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to the {} skill. To get some examples of what this skill can do, ask for help now.".format(skill['name'])
    reprompt_text = speech_output
    should_end_session = False

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_info_response(skill, request):
    session_attributes = {}
    card_title = "{} Info".format(skill['name'])
    speech_output = "{} is designed to list aws services in a category".format(skill['name'], skill['name'])
    reprompt_text = speech_output
    should_end_session = False

    return build_response(session_attributes, build_speechlet_response(card_title,speech_output,reprompt_text,should_end_session))


def get_help_response(skill, request):
    session_attributes = {}
    card_title = "Help"
    speech_output = "To use the {} skill, try saying... list AWS services..., or list services under Compute. For information about this skill, then say... what is {}".format(skill['name'], skill['invocation'])
    reprompt_text = speech_output
    should_end_session = False

    return build_response(session_attributes, build_speechlet_response(card_title,speech_output,reprompt_text,should_end_session))


def handle_session_end_request(skill, request):
    card_title = "{} Ended".format(skill['name'])
    should_end_session = True
    speech_output = "Thank you for using the {} skill!".format(skill['name'])

    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def get_main_response(skill, request):
    session_attributes = {}
    card_title = "{}".format(skill['name'])
    should_end_session = False

    response = skill['allservices']

    speech_output = response
    reprompt_text = speech_output

    return build_response(session_attributes, build_speechlet_response(card_title,speech_output,reprompt_text,should_end_session))

def get_slot_response(skill, request):
    session_attributes = {}
    card_title = "{}".format(skill['name'])
    should_end_session = False

    slot_key = request["intent"]["slots"][skill['slot_name']]
    print(slot_key)
    if 'value' in slot_key:
        slot_value = slot_key["value"]

        if slot_value.isalpha():
            slot = slot_value
    else:
        slot = "compute"

    print(slot)
    response = skill['slot_responses'][slot]

    print(response)
    speech_output = response.format(slot)
    reprompt_text = speech_output

    return build_response(session_attributes, build_speechlet_response(card_title,speech_output,reprompt_text,should_end_session))


# --------------- Helpers that build all of the responses ----------------------


def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }
