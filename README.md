# alexa-lambda-tutorial-list-aws-services
Starter tutorial for Alexa Skill that invokes a lambda function to list aws services

## How it works:

Amazon Echo -> Alexa Skill -> AWS Lambda Function -> Alexa Skill -> Amazon Echo


### Pre-Requisites:

1) Amazon Developer account.
   *Tip: Create with your amazon.com account to directly test with your personal Amazon echo device.
2) AWS Account:
   Free tier account would be sufficient.


### Implemetation:

#### Phase 1 (Amazon Developer Account) - Create Alexa Skill and Configure Intent, Slot types and Utterances
1) Login to Developer Console https://developer.amazon.com/home.html
2) Click on Alexa -> Alexa Skills Kit (Get Started) -> Add a New Skill
3) Skill Information Screen (enter following information): 
   a) Name - Service Map
   b) Invocation Name - service map
      *Tip: Invocation Name to match in Lambda function*
   c) Save
   d) Copy "Application Id"  (Tip: Look above Name once Save is greyed out)
      *Note: This needs to be entered in Lambda function - look for CHANGEME in Lambda function*
   e) Click Next
 4) Interaction Model
   a) Intent Schema -> Copy contents from intent_schema.txt
   b) Custom Slot Type: LIST_OF_AWS_SERVICES
   c) Values: Copy contents from custom_slot_types.txt
   d) Click Button "Add"
   e) Utterances -> Copy contents from utterances.txt

#### Phase 2 (AWS Account) - Create IAM Role, Lambda function and configure input Alexa trigger

#### Phase 3 (Amazon Developer Account)

### Testing:

#### Using Developer Console:

#### Using Echo Device:


Happy Programming with Alexa!

