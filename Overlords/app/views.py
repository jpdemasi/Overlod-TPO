from django.shortcuts import render
from app.models import User
from app import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')

@api_view(['GET'])
def get_data(request):
    data_user = User.objects.all()
    serializer = serializers.UserSerializer(data_user, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_data(request):
    serializer = serializers.UserSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
        response = {'status': 'OK',
                    'message': 'Datos añadidos existosamente',
                    'data': serializer.data}
        return Response (data = response, status=status.HTTP_201_CREATED)
    response = {'status': 'Error',
                'message': 'No se pudo crear la petición',
                'data': serializer.errors}
    return Response (data = response, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def del_data(request, id):
    try:
      user1 = User.objects.get(pk=id)
    except User.DoesNotExist:
         return Response(status=status.HTTP_404_NOT_FOUND,data='Recurso no encontrado')
    user1.delete()
    return Response ({'message': 'Se eliminó el registro'},status=status.HTTP_200_OK)

@api_view(['PUT'])
def edit_data(request, id):
    try:
        user_data = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response (status=status.HTTP_404_NOT_FOUND,data='Recurso no encontrado')
    serializer = serializers.UserSerializer(user_data, data=request.data)
    if serializer.is_valid():
        serializer.save()
        response = {'status':'Ok',
                    'message':'Registros actualizados con éxito',
                    'data':serializer.data}
        return Response(data=response)
    
    response = {'status':'Error',
                'message':'No se pudieron modificar los registros',
                'errors':serializer.errors}
    return Response(data=response, status=status.HTTP_400_BAD_REQUEST)


def usuario(request):
    if request.method == 'POST':
        # Procesar la solicitud para agregar un usuario
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')

        # Realizar operaciones de base de datos o cualquier otra lógica necesaria

        # Devolver una respuesta JSON
        return JsonResponse({'mensaje': 'Usuario agregado correctamente'})

    elif request.method == 'PUT':
        # Procesar la solicitud para modificar un usuario
        usuario_id = int(request.PUT.get('id'))
        nuevo_nombre = request.PUT.get('nombre')
        nuevo_email = request.PUT.get('email')

        # Realizar operaciones de base de datos o cualquier otra lógica necesaria

        # Devolver una respuesta JSON
        return JsonResponse({'mensaje': 'Usuario modificado correctamente'})

    elif request.method == 'DELETE':
        # Procesar la solicitud para borrar un usuario
        usuario_id = int(request.DELETE.get('id'))

        # Realizar operaciones de base de datos o cualquier otra lógica necesaria

        # Devolver una respuesta JSON
        return JsonResponse({'mensaje': 'Usuario eliminado correctamente'})

    else:
        # Si la solicitud no es POST, PUT o DELETE, devolver un error
        return JsonResponse({'error': 'Método no permitido'}, status=405)