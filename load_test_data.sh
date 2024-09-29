#!/bin/bash

# URL de la API
BASE_URL="https://improved-space-umbrella-w4w7wwj9vvc975w-3001.app.github.dev/api"
#"http://localhost:5000/api"

# Crear productos con variantes para la tienda Zero Waste
echo "Creando productos de Zero Waste..."

# Desodorante sólido (Variantes)
curl -X POST $BASE_URL/products -H "Content-Type: application/json" -d '{
    "sku": "HIG-DEO-EUC",
    "name": "Desodorante sólido - Eucalipto",
    "description": "Desodorante sólido con fragancia de eucalipto. Envase retornable.",
    "price": 4.00,
    "stock": 120,
    "category": "Higiene",
    "active": true,
    "stock_threshold": 10
}'

curl -X POST $BASE_URL/products -H "Content-Type: application/json" -d '{
    "sku": "HIG-DEO-LAV",
    "name": "Desodorante sólido - Lavanda",
    "description": "Desodorante sólido con fragancia de lavanda. Envase retornable.",
    "price": 4.00,
    "stock": 100,
    "category": "Higiene",
    "active": true,
    "stock_threshold": 10
}'

curl -X POST $BASE_URL/products -H "Content-Type: application/json" -d '{
    "sku": "HIG-DEO-MEN",
    "name": "Desodorante sólido - Menta",
    "description": "Desodorante sólido con fragancia de menta. Envase retornable.",
    "price": 4.00,
    "stock": 80,
    "category": "Higiene",
    "active": true,
    "stock_threshold": 10
}'

curl -X POST $BASE_URL/products -H "Content-Type: application/json" -d '{
    "sku": "HIG-DEO-NOF",
    "name": "Desodorante sólido - Sin fragancia",
    "description": "Desodorante sólido sin fragancia. Envase retornable.",
    "price": 4.00,
    "stock": 90,
    "category": "Higiene",
    "active": true,
    "stock_threshold": 10
}'

# Champú sólido (Variantes)
curl -X POST $BASE_URL/products -H "Content-Type: application/json" -d '{
    "sku": "HIG-SHA-SEC",
    "name": "Champú sólido - Cabello seco",
    "description": "Champú sólido ideal para cabello seco. Envase retornable.",
    "price": 5.00,
    "stock": 100,
    "category": "Higiene",
    "active": true,
    "stock_threshold": 20
}'

curl -X POST $BASE_URL/products -H "Content-Type: application/json" -d '{
    "sku": "HIG-SHA-GRA",
    "name": "Champú sólido - Cabello graso",
    "description": "Champú sólido ideal para cabello graso. Envase retornable.",
    "price": 5.00,
    "stock": 90,
    "category": "Higiene",
    "active": true,
    "stock_threshold": 20
}'

curl -X POST $BASE_URL/products -H "Content-Type: application/json" -d '{
    "sku": "HIG-SHA-NOR",
    "name": "Champú sólido - Cabello normal",
    "description": "Champú sólido ideal para cabello normal. Envase retornable.",
    "price": 5.00,
    "stock": 15,
    "category": "Higiene",
    "active": true,
    "stock_threshold": 20
}'

curl -X POST $BASE_URL/products -H "Content-Type: application/json" -d '{
    "sku": "HIG-SHA-TOD",
    "name": "Champú sólido - Todo tipo de cabello",
    "description": "Champú sólido ideal para todo tipo de cabello. Envase retornable.",
    "price": 5.00,
    "stock": 20,
    "category": "Higiene",
    "active": true,
    "stock_threshold": 30
}'

# Protector solar (Variantes)
curl -X POST $BASE_URL/products -H "Content-Type: application/json" -d '{
    "sku": "CUP-SUN-MAL",
    "name": "Protector solar - Muy alta protección",
    "description": "Protector solar con muy alta protección, biodegradable. Envase retornable.",
    "price": 8.50,
    "stock": 75,
    "category": "Cuidado Personal",
    "active": true,
    "stock_threshold": 15
}'

curl -X POST $BASE_URL/products -H "Content-Type: application/json" -d '{
    "sku": "CUP-SUN-ALT",
    "name": "Protector solar - Alta protección",
    "description": "Protector solar con alta protección, biodegradable. Envase retornable.",
    "price": 8.50,
    "stock": 65,
    "category": "Cuidado Personal",
    "active": true,
    "stock_threshold": 15
}'

curl -X POST $BASE_URL/products -H "Content-Type: application/json" -d '{
    "sku": "CUP-SUN-MED",
    "name": "Protector solar - Media alta protección",
    "description": "Protector solar con media alta protección, biodegradable. Envase retornable.",
    "price": 8.50,
    "stock": 85,
    "category": "Cuidado Personal",
    "active": true,
    "stock_threshold": 15
}'

curl -X POST $BASE_URL/products -H "Content-Type: application/json" -d '{
    "sku": "CUP-SUN-NOR",
    "name": "Protector solar - Protección normal",
    "description": "Protector solar con protección normal, biodegradable. Envase retornable.",
    "price": 8.50,
    "stock": 70,
    "category": "Cuidado Personal",
    "active": true,
    "stock_threshold": 15
}'

# Crema antimosquito (Variantes)
curl -X POST $BASE_URL/products -H "Content-Type: application/json" -d '{
    "sku": "CUP-MOS-CIT",
    "name": "Crema antimosquito - Citronela",
    "description": "Crema antimosquito con citronela. Envase retornable.",
    "price": 6.00,
    "stock": 50,
    "category": "Cuidado Personal",
    "active": true,
    "stock_threshold": 10
}'

curl -X POST $BASE_URL/products -H "Content-Type: application/json" -d '{
    "sku": "CUP-MOS-EUC",
    "name": "Crema antimosquito - Eucalipto",
    "description": "Crema antimosquito con eucalipto. Envase retornable.",
    "price": 6.00,
    "stock": 55,
    "category": "Cuidado Personal",
    "active": true,
    "stock_threshold": 10
}'

curl -X POST $BASE_URL/products -H "Content-Type: application/json" -d '{
    "sku": "CUP-MOS-LAV",
    "name": "Crema antimosquito - Lavanda",
    "description": "Crema antimosquito con lavanda. Envase retornable.",
    "price": 6.00,
    "stock": 60,
    "category": "Cuidado Personal",
    "active": true,
    "stock_threshold": 10
}'

curl -X POST $BASE_URL/products -H "Content-Type: application/json" -d '{
    "sku": "CUP-MOS-NOF",
    "name": "Crema antimosquito - Sin fragancia",
    "description": "Crema antimosquito sin fragancia. Envase retornable.",
    "price": 6.00,
    "stock": 65,
    "category": "Cuidado Personal",
    "active": true,
    "stock_threshold": 10
}'

echo "Productos creados."



# Crear 18 usuarios (9 mujeres, 9 hombres, 3 administradores)
echo "Creando usuarios..."

for i in {1..9}; do
  curl -X POST $BASE_URL/users -H "Content-Type: application/json" -d "{\"username\": \"UserMale$i\", \"email\": \"usermale$i@example.com\", \"password\": \"password$i\", \"role\": \"user\"}"
done

for i in {1..9}; do
  curl -X POST $BASE_URL/users -H "Content-Type: application/json" -d "{\"username\": \"UserFemale$i\", \"email\": \"userfemale$i@example.com\", \"password\": \"password$i\", \"role\": \"user\"}"
done



echo "Usuarios creados...sin admin"

# Crear 12 carritos
echo "Creando carritos..."

for i in {1..12}; do
  curl -X POST $BASE_URL/cart -H "Content-Type: application/json" -d "{\"user_id\": $i}"
done

echo "Carritos creados."

# Añadir múltiples productos a cada carrito
echo "Añadiendo productos a los carritos..."

# Carrito 1
curl -X POST $BASE_URL/cart_items -H "Content-Type: application/json" -d '{
    "cart_id": 1,
    "product_id": 1,
    "quantity": 2
}'
curl -X POST $BASE_URL/cart_items -H "Content-Type: application/json" -d '{
    "cart_id": 1,
    "product_id": 2,
    "quantity": 1
}'

# Carrito 2
curl -X POST $BASE_URL/cart_items -H "Content-Type: application/json" -d '{
    "cart_id": 2,
    "product_id": 3,
    "quantity": 3
}'
curl -X POST $BASE_URL/cart_items -H "Content-Type: application/json" -d '{
    "cart_id": 2,
    "product_id": 4,
    "quantity": 1
}'

# Carrito 3
curl -X POST $BASE_URL/cart_items -H "Content-Type: application/json" -d '{
    "cart_id": 3,
    "product_id": 1,
    "quantity": 4
}'
curl -X POST $BASE_URL/cart_items -H "Content-Type: application/json" -d '{
    "cart_id": 3,
    "product_id": 3,
    "quantity": 2
}'

# Carrito 4
curl -X POST $BASE_URL/cart_items -H "Content-Type: application/json" -d '{
    "cart_id": 4,
    "product_id": 2,
    "quantity": 5
}'
curl -X POST $BASE_URL/cart_items -H "Content-Type: application/json" -d '{
    "cart_id": 4,
    "product_id": 4,
    "quantity": 1
}'

# Repetir el mismo patrón para los siguientes carritos...
# Carrito 5
curl -X POST $BASE_URL/cart_items -H "Content-Type: application/json" -d '{
    "cart_id": 5,
    "product_id": 1,
    "quantity": 2
}'
curl -X POST $BASE_URL/cart_items -H "Content-Type: application/json" -d '{
    "cart_id": 5,
    "product_id": 3,
    "quantity": 1
}'

# Carrito 6
curl -X POST $BASE_URL/cart_items -H "Content-Type: application/json" -d '{
    "cart_id": 6,
    "product_id": 2,
    "quantity": 3
}'
curl -X POST $BASE_URL/cart_items -H "Content-Type: application/json" -d '{
    "cart_id": 6,
    "product_id": 4,
    "quantity": 2
}'

curl -X POST $BASE_URL/cart_items -H "Content-Type: application/json" -d '{
    "cart_id": 6,
    "product_id": 15,
    "quantity": 10
}'


# Añadir productos a más carritos para evitar carritos vacíos
for i in {7..9}; do
  curl -X POST $BASE_URL/cart_items -H "Content-Type: application/json" -d "{\"cart_id\": $i, \"product_id\": 5, \"quantity\": 3}"
  curl -X POST $BASE_URL/cart_items -H "Content-Type: application/json" -d "{\"cart_id\": $i, \"product_id\": 12, \"quantity\": 2}"
    curl -X POST $BASE_URL/cart_items -H "Content-Type: application/json" -d "{\"cart_id\": $i, \"product_id\": 16, \"quantity\": 1}"
done

# Crear órdenes después de que los carritos tengan productos
echo "Creando órdenes..."

for i in {1..3}; do
  curl -X POST $BASE_URL/orders -H "Content-Type: application/json" -d "{\"cart_id\": $i,  \"status\": \"pending\"}"
done

for i in {4..6}; do
  curl -X POST $BASE_URL/orders -H "Content-Type: application/json" -d "{\"cart_id\": $i,  \"status\": \"shipped\"}"
done

for i in {7..9}; do
  curl -X POST $BASE_URL/orders -H "Content-Type: application/json" -d "{\"cart_id\": $i,  \"status\": \"delivered\"}"
done

echo "Órdenes creadas."

