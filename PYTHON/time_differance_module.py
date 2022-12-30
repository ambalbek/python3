#!/usr/bin/env python3
import datetime
def time_diff(snapcreated):
    now= datetime.datetime.now(datetime.timezone.utc)
    diff = now - snapcreated
    return diff.days#