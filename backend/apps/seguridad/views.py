# from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection
from rest_framework import status
from .serializers import MenuSerializer


# Create your views here.

# def execute_function(query, params):
#     """Ejecuta una función de PostgreSQL con los parámetros dados."""
#     with connection.cursor() as cursor:
#         cursor.execute(query, params)
#         if cursor.description:
#             columns = [col[0] for col in cursor.description]
#             return [dict(zip(columns, row)) for row in cursor.fetchall()]
#         return []

from django.db import connection

def execute_function(query, params=None):
    with connection.cursor() as cursor:
        cursor.execute(query, params or [])
        if cursor.description:
            columns = [col[0] for col in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]
        return []


@api_view(['GET'])
# def listar_menus(request):
#     """Listar menús con los parámetros especificados."""
#     _offset = request.GET.get('offset', 0)
#     _limit = request.GET.get('limit', 10)
#     id_modulo_ = request.GET.get('id_modulo', None)
#     menu_nombre_ = request.GET.get('menu_nombre', None)
#     menu_estado_ = request.GET.get('menu_estado', None)
    
#     # Convertir `menu_estado_` a booleano
#     if menu_estado_ is not None:
#         menu_estado_ = True if menu_estado_ == 'true' else False

#     query = """
#     SELECT * FROM public.listar_menus_grid_list(%s, %s, %s, %s, %s)
#     """
#     params = (_offset, _limit, id_modulo_, menu_nombre_, menu_estado_)

#     menus = execute_function(query, params)
    
#     if menus:
#         serializer = MenuSerializer(data=menus, many=True)
#         if serializer.is_valid():
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     else:
#         return Response({'error': 'No se encontraron datos'}, status=status.HTTP_404_NOT_FOUND)


def listar_menus(request):
    """Listar menús con los parámetros especificados."""
    query = """
    SELECT * FROM public.listar_menus()
    """

    # Ejecutar la función PostgreSQL y obtener los resultados
    menus = execute_function(query)
    
    print(menus)  

    if menus:
        serializer = MenuSerializer(data=menus, many=True)
        if serializer.is_valid():
            return Response(serializer.validated_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'No se encontraron datos'}, status=status.HTTP_404_NOT_FOUND)