from boto3.session import Session


class EngineConnectionSqs:
    def __init__(self):
        session = Session(aws_access_key_id="AKIA4XX3GNSABTIP3B6A",
                          aws_secret_access_key="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")
        self.sqs = session.resource('sqs')