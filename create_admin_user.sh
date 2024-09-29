#!/bin/bash

# Ejecutar el script de creación del usuario administrador dentro del contenedor backend
docker compose exec backend python /app/create_admin.py

