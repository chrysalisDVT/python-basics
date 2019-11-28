import boto3
import click
from hvac_util import access_key,access_secret


@click.command("upload-data")
@click.option('--path',default="wdir",help="Uploads data to s3")
def upload_data(path):
    a=1

if __name__=='__main__':
    upload_data()