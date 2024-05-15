from django.db import models
from viewflow.workflow.models import Process


class SavableProcess(Process):
    text = models.TextField()
