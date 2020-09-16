import pandas as pd
import boto3
import datetime



def getEMRMetrics():

    session = boto3.Session(
    aws_access_key_id="****",
    aws_secret_access_key="****",
    )
    
    cwHandle =  session.client('cloudwatch')
    metrics=cwHandle.get_metric_statistics(
        Period=300,
        StartTime=datetime.datetime.utcnow() - datetime.timedelta(seconds=600),
        EndTime=datetime.datetime.utcnow(),
        MetricName='CoreNodesRunning',
        Namespace='AWS/ElasticMapReduce',
        Statistics=['Minimum'],
        Dimensions=[{'Name':'JobFlowId', 'Value':'j-17QUZSO21W4BS'}]
        )
    
    print(metrics)


getEMRMetrics()   










