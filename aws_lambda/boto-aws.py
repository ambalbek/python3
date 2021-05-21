import datetime, boto3
import logging
logging.basicConfig(level=logging.INFO)
health = boto3.client('health')


def lambda_handler(event, context):
    events_paginator = health.get_paginator('describe_events')
    
    # lets get data for last 7 days 
    events_pages = events_paginator.paginate(filter={
        'startTimes': [
            {
                'from': datetime.datetime.now() - datetime.timedelta(days=7)
            }
        ],
        'eventStatusCodes': ['open', 'upcoming']
    })

    number_of_matching_events = 0
    for events_page in events_pages:
        for event in events_page['events']:
            number_of_matching_events += 1
            event_details(event)

    if number_of_matching_events == 0:
        return 'There are no AWS Health events that match the given filters'
