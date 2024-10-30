from django.core.management.base import BaseCommand, CommandError, CommandParser
from dynamodb.utils.DynamoDBInterface import Movies
import boto3
import os


class Command(BaseCommand):
    help = "Crear tabla en base de datos de dynamo db"

    def handle(self, *args, **options):
        public_key = "AKIAQ4NSA5YQSGK77YXI"
        secret_key = os.environ["AWS_PRIVATE_KEY"]
        session = boto3.Session(
            aws_access_key_id=public_key,
            aws_secret_access_key=secret_key,
            region_name="eu-west-3"
        )
        dynamodb = session.resource('dynamodb')
        m = Movies(dynamodb)
        m.create_table("JoanMovies")