# Overview

Wraps AWS python SDK to send and revieve messages to Pie's SQS and SNS

# Prerequisites
* Python 3.8.8

# Setup
```
python setup.py
```

# TLDR
Sends message to Policies SQS queue that was created for disperate events
1. checkout Polices spike/INS-1337-native-spike
2. run in debug locally 
3. put break point in SqsHappenedHandler
4. run `python send_sqs.py`

# Integration with Policy Management
Squad IPA will configure EventBridge to route Policy Management events to SNS topics or SQS queues owned by Squad IPA.  This spike sends messages directly to the SNS or SQS topics created for Native Messages.  Next POC step is to consume messages from EventBridge.  

# Required Solution Modifications

## Pie Shared Repo

Endpoint project updated to use v5.3.1+ of NServiceBus.AmazonSQS library required to support native integration as documented at https://docs.particular.net/transports/sqs/native-integration.

https://github.com/PieInsurance/Shared/compare/3.0/feature/dev...3.0/spike/INS-1337-upgrade-aws-sqs contiain required mods to Shared.

## Squad IPA Repos

Squad IPA solutions wanting to consume native messages must update Pie Shared package reference to version with required mods.  Pie Shared pre release build 3.0.2104.2936-INS-1337-upgrade-aws-sqs has required mods.

Policies spike/INS-1337-native-spike is already updated. 

# Notes
* ISqsHappened is not required to be in Message.Contracts
* Workers appSettings.Development.json sets the MessageTransport for this spike.  This is only needed to test locally
* Still need to convert a few example from the original node spike.  (e.g. sending SNS, sending IDecisionIssued event, sending Commands)
* This did ont spike recieving messages in this library
