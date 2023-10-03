from boto3.session import Session


class EngineConnectionS3:
    def __init__(self):
        session = Session(aws_access_key_id="AKIA4XX3GNSABTIP3B6A",
                          aws_secret_access_key="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")
        s3_session = session.resource('s3')
        self.bucket_s3 = s3_session.Bucket('reportsbucket78')