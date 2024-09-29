"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Product, ProductImage, Cart, CartItem, Order, OrderItem, Address
from api.utils import generate_sitemap, APIException
from flask_cors import CORS

from flask import Blueprint, request, jsonify, render_template,redirect, url_for, flash, get_flashed_messages, session,jsonify
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash,check_password_hash
#from app import app, db
from datetime import datetime
#from app.forms import SignupForm, SigninForm
import cloudinary.uploader

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

# ----------------------------------------------------------------------------------------------------------------
# 							ENDPOINTS
# ----------------------------------------------------------------------------------------------------------------

# ----------------------
# USER ROUTES
# ----------------------

@api.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')  # Hash the plain password
    user = User(username=data['username'], email=data['email'], password_hash=hashed_password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'id': user.id}), 201
    
@api.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    return jsonify([
        {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'role': user.role
        }
        for user in users
    ])



@api.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    return jsonify({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'role': user.role
    })

@api.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'message': 'User not found'}), 404

    # Actualizar solo los campos presentes en la solicitud
    if 'username' in data:
        user.username = data['username']
    if 'email' in data:
        user.email = data['email']
    if 'role' in data:
        user.role = data['role']
    if 'password_hash' in data:
        user.password_hash = data['password_hash']

    db.session.commit()
    return jsonify({'message': 'User updated'})


@api.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted'})


# ----------------------
# PRODUCT ROUTES
# ----------------------

@api.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    # Crear el producto utilizando todos los campos necesarios
    product = Product(
        sku=data['sku'],
        name=data['name'],
        description=data.get('description', ''),  # Valor por defecto si no se proporciona descripción
        price=data['price'],
        stock=data.get('stock', 0),  # Si no se proporciona, el stock será 0 por defecto
        category=data['category'],
        active=data.get('active', True),  # Por defecto, el producto estará activo
        stock_threshold=data.get('stock_threshold')  # Puede ser nulo si no se proporciona
    )
    db.session.add(product)
    db.session.commit()
    return jsonify({'id': product.id}), 201


@api.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get(product_id)
    if product is None:
        return jsonify({'message': 'Product not found'}), 404

    # Obtener todas las imágenes asociadas al producto
    product_images = ProductImage.query.filter_by(product_id=product.id).all()

    # Crear una lista de URLs de las imágenes
    images = [{"url": image.url} for image in product_images]

    # Devolver el JSON del producto incluyendo las imágenes
    return jsonify({
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'stock': product.stock,
        'images': images  # Añadir la lista de imágenes al JSON de respuesta
    })


@api.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    product = Product.query.get(product_id)
    if product is None:
        return jsonify({'message': 'Product not found'}), 404
    product.name = data['name']
    product.description = data['description']
    product.price = data['price']
    db.session.commit()
    return jsonify({'message': 'Product updated'})

@api.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product is None:
        return jsonify({'message': 'Product not found'}), 404
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted'})
# ----------------------
# CART ROUTES
# ----------------------

@api.route('/cart', methods=['POST'])
def create_cart():
    data = request.get_json()
    user_id = data['user_id']
    if not User.query.get(user_id):
        return jsonify({'message': 'User not found'}), 404
    cart = Cart(user_id=user_id)
    db.session.add(cart)
    db.session.commit()
    return jsonify({'id': cart.id}), 201

@api.route('/cart/<int:cart_id>', methods=['GET'])
def get_cart(cart_id):
    cart = Cart.query.get(cart_id)
    if not cart:
        return jsonify({'message': 'Cart not found'}), 404
    return jsonify({
        'id': cart.id,
        'user_id': cart.user_id,
        'items': [{'product_id': item.product_id, 'quantity': item.quantity} for item in cart.items]
    })

@api.route('/cart/<int:cart_id>', methods=['DELETE'])
def delete_cart(cart_id):
    cart = Cart.query.get(cart_id)
    if not cart:
        return jsonify({'message': 'Cart not found'}), 404
    db.session.delete(cart)
    db.session.commit()
    return jsonify({'message': 'Cart deleted'})


# ----------------------
# CART ITEM ROUTES
# ----------------------

# add stock validation
@api.route('/cart_items', methods=['POST'])
def add_cart_item():
    data = request.get_json()
    cart = Cart.query.get(data['cart_id'])
    product = Product.query.get(data['product_id'])

    if not cart:
        return jsonify({'message': 'Cart not found'}), 404
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    
    # Verificar si hay suficiente stock
    if product.stock < data['quantity']:
        return jsonify({'message': f'Only {product.stock} units available'}), 400

    # Agregar el producto al carrito
    cart_item = CartItem(cart_id=data['cart_id'], product_id=data['product_id'], quantity=data['quantity'])
    db.session.add(cart_item)
    db.session.commit()

    flash('Product added to cart!', 'success')
    flash_message = [str(category) + ": " + str(message) for category, message in get_flashed_messages(with_categories=True)]
    
    return jsonify({'id': cart_item.id, 'flash': flash_message}), 201



@api.route('/cart_items/<int:cart_item_id>', methods=['PUT'])
def update_cart_item(cart_item_id):
    data = request.get_json()
    cart_item = CartItem.query.get(cart_item_id)
    if not cart_item:
        return jsonify({'message': 'Cart item not found'}), 404
    cart_item.quantity = data['quantity']
    db.session.commit()
    return jsonify({'message': 'Cart item updated'})

@api.route('/cart_items/<int:cart_item_id>', methods=['DELETE'])
def delete_cart_item(cart_item_id):
    cart_item = CartItem.query.get(cart_item_id)
    if not cart_item:
        return jsonify({'message': 'Cart item not found'}), 404
    db.session.delete(cart_item)
    db.session.commit()
    return jsonify({'message': 'Cart item deleted'})


@api.route('/cart/<int:cart_id>/items', methods=['GET'])
def get_cart_items(cart_id):
    cart = Cart.query.get(cart_id)
    if not cart:
        return jsonify({'message': 'Cart not found'}), 404
    
    cart_items = CartItem.query.filter_by(cart_id=cart_id).all()
    items = [{
        'id': item.id,
        'product_id': item.product_id,
        'quantity': item.quantity,
        'product': {
            'name': Product.query.get(item.product_id).name,
            'price': Product.query.get(item.product_id).price
        }
    } for item in cart_items]
    
    return jsonify({'cart_id': cart_id, 'items': items})


@api.route('/cart/user/<int:user_id>', methods=['GET'])
def get_cart_by_user(user_id):
    cart = Cart.query.filter_by(user_id=user_id).first()
    if not cart:
        return jsonify({'message': 'Cart not found'}), 404
    return jsonify({
        'id': cart.id,
        'user_id': cart.user_id,
        'items': [{'product_id': item.product_id, 'quantity': item.quantity} for item in cart.items]
    })



# ----------------------
# ORDER ROUTES
# ----------------------

@api.route('/orders', methods=['POST'])
def create_order_debug():
    data = request.get_json()
    
    # Verifica que 'cart_id' esté presente en los datos
    if 'cart_id' not in data:
        return jsonify({'message': 'Missing cart_id in request data'}), 400

    cart_id = data['cart_id']

    # Obtener el carrito y verificar su existencia
    cart = Cart.query.get(cart_id)

    if not cart:
        return jsonify({'message': 'Cart not found'}), 404

    # Obtener los artículos del carrito
    cart_items = CartItem.query.filter_by(cart_id=cart_id).all()
    if not cart_items:
        return jsonify({'message': 'Cart is empty'}), 400

    # Calcular el total_amount basado en los precios de los productos
    total_amount = 0.0
    items_details = []
    for item in cart_items:
        product = Product.query.get(item.product_id)
        if not product:
            return jsonify({'message': f'Product with ID {item.product_id} not found'}), 404
        item_total = float(product.price * item.quantity)
        total_amount += item_total
        items_details.append({
            'product_id': item.product_id,
            'quantity': item.quantity,
            'price': float(product.price),
            'item_total': float(item_total)
        })
        
    # Crear la orden
    order = Order(
        user_id=cart.user_id,
        total_amount=total_amount,
        is_paid=False,  # Asumimos que la orden no está pagada inicialmente
        status='pending'  # Estado inicial de la orden
    )
    db.session.add(order)
    db.session.commit()
    
    #agregamos order items
    
    # Crear los OrderItems
    order_items_details = []
    for item in cart.items:
        product = Product.query.get(item.product_id)
        if not product:
            return jsonify({'message': f'Product with ID {item.product_id} not found'}), 404

        order_item = OrderItem(
            order_id=order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=product.price  # Precio del producto en la orden
        )
        db.session.add(order_item)
        order_items_details.append({
            "order_id": order.id,
            "product_id": item.product_id,
            "quantity": item.quantity,
            "price": product.price
        })
        

    db.session.commit()
    
    # Eliminar el carrito después de crear la orden
    db.session.delete(cart)
    db.session.commit()
    



    # Devolver la respuesta con los detalles de la orden y los artículos
    return jsonify({
        'cart_id': cart_id,
        'total_amount': float(total_amount),
        'items': items_details,
        'order_id': order.id,
        'order_items': order_items_details
        
    }), 201




@api.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({'message': 'Order not found'}), 404
    return jsonify({
        'id': order.id,
        'user_id': order.user_id,
        'total_amount': order.total_amount,
        'is_paid': order.is_paid,
        'status': order.status,
        'items': [{'product_id': item.product_id, 'quantity': item.quantity, 'price': item.price} for item in order.items]
    })

@api.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    data = request.get_json()
    order = Order.query.get(order_id)
    if not order:
        return jsonify({'message': 'Order not found'}), 404

    # Actualiza el estado y si está pagada
    if 'status' in data:
        order.status = data['status']
    if 'is_paid' in data:
        order.is_paid = data['is_paid']

    db.session.commit()
    return jsonify({'message': 'Order updated'})

@api.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({'message': 'Order not found'}), 404
    db.session.delete(order)
    db.session.commit()
    return jsonify({'message': 'Order deleted'})

