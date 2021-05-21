import logging
import boto3
import re
import os
from urllib.parse import unquote
from boto3.dynamodb.conditions import Key, Attr

logger = logging.getLogger()
logger.setLevel(logging.INFO)



class NotifyAPIUtilities:

    def __init__(self):
        pass

    def notifications_query(event):
        logger.info("Event: Account ID : %s", event)
        response = {}
        query_response = {"notifications": []}
        if "query" in event:
            logger.info("Event: query : %s", event["query"])
            if "account_id" in event["query"]:
                logger.info("Event: query : %s", event["query"]["account_id"])
                account_id = event["query"]["account_id"]                
                return query_response
        return response

    def bhcaccounts_query(event):
        logger.info("Event: Account ID : %s", event)
        response = {}
        query_response = {"bhc_accounts": []}
        if "query" in event:
            logger.info("Event: query : %s", event["query"])
            return query_response
        return response

    def get_q_mpa(event):
        logger.info("Event : %s", event)
        response = {}
        lst = []
        query_response = {"mpas": []}
        if "query" in event:
            logger.info("Event: query : %s", event["query"])
            for i in response['Items']:
                query_response['mpas'].append(i['mpa'])
            return query_response
        return response

    def get_acctype(event):
        logger.info("Event: MPA ID : %s", event)
        response = {}
        query_response = {"singlempa": []}
        if "query" in event:
            logger.info("Event: query : %s", event["query"])
            if "mpa_id" in event["query"]:
                logger.info("Event: query : %s", event["query"]["mpa_id"])
                mpa_id = event["query"]["mpa_id"]
                logger.info("Event: query : %s", event["query"])
                for i in response['Items']:
                    query_response['singlempa'].append(i['accounttype'])
                query_response['singlempa'] = list(set(query_response['singlempa'])) 
                return query_response
        return response

    def get_accsid(event):
        logger.info("Event: Accounts id : %s", event)
        response = {}
        query_response = {"accids": []}
        if "query" in event:
            logger.info("Event: query : %s", event["query"])
            if "mpa_id" in event["query"]:
                logger.info("First Event: query : %s", event["query"]["mpa_id"])
                if "acc_type" in event["query"]:
                    logger.info("Second Event: query : %s", event["query"]["acc_type"])
                    mpa_id = event["query"]["mpa_id"]
                    acc_type = event["query"]["acc_type"]
                    logger.info("Event: query : %s", event["query"])
                    logger.info(response)
                    for i in response['Items']:
                        query_response['accids'].append(i['accountId'])
                    return query_response
                    logger.info(response)
        return response


def lambda_handler(event, context):
    logger.info("Received the event %s context %s", event, context)
    # if "method" in event:
    result = getattr(NotifyAPIUtilities, event)(event)
    logger.info("Done!!!--->%s", result)
    return result
    # else:
    #     msg = {"error": "invalid operation"}
    #     return msg
