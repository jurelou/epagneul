import numpy as np
import pandas as pd
from epagneul.core.changefinder import ChangeFinder
from epagneul.models.relationships import RelationshipType
import datetime

def adetection(counts, users, starttime, tohours):
    count_array = np.zeros((10, len(users), tohours + 1))
    cfdetect = {}
    for _, event in counts.iterrows():
        column = int(
            (
                datetime.datetime.strptime(event["dates"], "%Y-%m-%d  %H:%M:%S")
                - starttime
            ).total_seconds()
            / 3600
        )
        try:
            row = users.index(event["username"])
        except ValueError:
            continue
        if event["event"] == RelationshipType.SUCCESSFULL_LOGON:
            count_array[0, row, column] = event["count"]
        elif event["event"] == RelationshipType.FAILED_LOGON:
            count_array[1, row, column] = event["count"]
        elif event["event"] == RelationshipType.TGT_AES_REQUEST:
            count_array[2, row, column] = event["count"]
        elif event["event"] == RelationshipType.TGT_DES_REQUEST:
            count_array[3, row, column] = event["count"]
        elif event["event"] == RelationshipType.TGT_RC4_REQUEST:
            count_array[4, row, column] = event["count"]
        elif event["event"] == RelationshipType.TGS_REQUEST:
            count_array[5, row, column] = event["count"]
        elif event["event"] == RelationshipType.TGT_FAILED:
            count_array[6, row, column] = event["count"]
        elif event["event"] == RelationshipType.NTLM_REQUEST:
            count_array[7, row, column] = event["count"]
        elif event["event"] == RelationshipType.NETWORK_CONNECTION:
            count_array[8, row, column] = event["count"]
        elif event["event"] == RelationshipType.LOGON_EXPLICIT_CREDS:
            count_array[9, row, column] = event["count"]

    count_sum = np.sum(count_array, axis=0)
    count_average = count_sum.mean(axis=0)
    num = 0
    for udata in count_sum:
        cf = ChangeFinder(r=0.04, order=1, smooth=10)
        ret = []
        for i in count_average:
            cf.update(i)

        for i in udata:
            score = cf.update(i)
            ret.append(round(score[1], 2))
        cfdetect[users[num]] = max(ret)
        num += 1

    return cfdetect
