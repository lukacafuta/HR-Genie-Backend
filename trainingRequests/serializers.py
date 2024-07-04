from rest_framework import serializers
from .models import TrainingRequest  # import the model here

class TrainingRequestSerializerPrivate(serializers.ModelSerializer):

    # TODO: add the join with CustomUser -> names
    # TODO: add also join with UserProfile -> approver
    class Meta:
        # look at the CustomUser model and give me all the fields
        model = TrainingRequest
        #fields = '__all__'
        fields = ['id', 'trainingURL', 'title', 'description', 'price', 'statusApproval', 'completionCertificate', 'statusAdvancement']
        #exclude = ['password']

    pass
