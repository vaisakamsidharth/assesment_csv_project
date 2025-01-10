from django.shortcuts import render
import csv
from io import TextIOWrapper
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserModel
from .serializers import UserSerializer


class CsvUploadView(APIView):

    def post(self,request,*args,**kwargs):
        #getting file
        file = request.FILES.get('file')

        # check the file is csv or not
        if not file:
            return Response(
                {"error": "No file provided."},
                status=status.HTTP_400_BAD_REQUEST
            )
        # this condition is written in this file is not csv then shown http error
        if not file.name.endswith('.csv'):
            return Response(
                {"error occured" : "only supported csv files"},
                status=status.HTTP_400_BAD_REQUEST
            )
        #decoding the file
        file_decode = TextIOWrapper(file.file, encoding='utf-8')
        read = csv.DictReader(file_decode)
        saved_records = []
        errors = []
        total_records = 0

        for index, row in enumerate(read):
            total_records += 1
            serializer = UserSerializer(data=row)
            if serializer.is_valid():
                # Avoid duplicate emails
                if not UserModel.objects.filter(email=row.get('email')).exists():
                    serializer.save()
                    saved_records.append(serializer.data)
                else:
                    errors.append({"row": index + 1, "errors": "Duplicate email."})
            else:
                errors.append({"row": index + 1, "errors": serializer.errors})
        
        return Response({
            "total_records": total_records,
            "saved_records": len(saved_records),
            "rejected_records": len(errors),
            "errors": errors,
        }, status=status.HTTP_200_OK)