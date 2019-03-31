from __future__ import print_function
import json
from botocore.vendored import requests

# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
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


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to Betcy's Alexa Skill. Let's make a bet."
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Please make a bet with your friend."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for using Betcy's Alexa skill. Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))



def who_is_the_receiver(intent, session):

    card_title = intent['name']
    session_attributes = {}
    should_end_session = False
    name=intent['slots']['tofriend']['value']
    speech_output = "I will create a smart contract between you and "+ name +". What is your bet?"
    reprompt_text = "I will create a smart contract between you and "+ name +". What is your bet?"
    url = "https://www.jsonstore.io/54298701bfa16f8c77653c87b9008c3f3a681c74ca82c59649efc9159f910e46"
    pay={'receiver': name}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Accept': 'text/plain'
    }
    response = requests.request("POST", url, data=json.dumps(pay), headers=headers)
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def what_is_the_bet(intent,session):
    
    card_title = intent['name']
    session_attributes = {}
    should_end_session = False
    name=intent['slots']['betmade']['value']
    speech_output = "Your bet is on "+ name +". What is your wager?"
    reprompt_text = "Your bet is on "+ name +". What is your wager?"
    url="https://www.jsonstore.io/f69f67573b1097131a3d0dd3238f05c01eb95d943adc8ec173d9b903f0989419"
    pay={'receiver': name}
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Accept': 'text/plain'
    }
    response = requests.request("POST", url, data=json.dumps(pay), headers=headers)
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def what_is_the_wager(intent,session):
    
    card_title = intent['name']
    session_attributes = {}
    should_end_session = False
    name=intent['slots']['productid']['value']
    speech_output = "Your wager is Macy's product with web id "+ str(name) +". When is your commit date?"
    reprompt_text = "Your wager is Macy's product with web id "+ str(name) +". When is your commit date?"
    url = "https://www.jsonstore.io/cc18fd5358601223f518adc547cb765a84d85d34fbdfe3466b55d6e454f29bf1"
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache"
    }
    response = requests.request("POST", url, data=name, headers=headers)
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def what_is_the_committDate(intent,session):
    
    card_title = intent['name']
    session_attributes = {}
    should_end_session = False
    name=intent['slots']['committDate']['value']
    speech_output = "Your bet is due on "+ name +". I'm deploying it on the Ethereum Blockchain."
    reprompt_text = "Your bet is due on "+ name +". I'm deploying it on the Ethereum Blockchain."
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))



# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "MakeaBet":
        return who_is_the_receiver(intent, session)
    elif intent_name == "Bets":
        return what_is_the_bet(intent, session)
    elif intent_name == "Stake":
        return what_is_the_wager(intent, session)
    elif intent_name == "Date":
        return what_is_the_committDate(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.
    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
