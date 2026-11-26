
from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# =====================================
# DATABASE CONFIGURATION
# =====================================

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'dev'
}

# =====================================
# DATABASE CONNECTION
# =====================================

def get_db_connection():
    return mysql.connector.connect(**db_config)


# =====================================
# GET REQUEST DATA
# Supports JSON, Form-data and Params
# =====================================

def get_request_data():
    return (
        request.get_json(silent=True)
        or request.form.to_dict()
        or request.args.to_dict()
    )


# =====================================
# 1. GET ALL USERS
# =====================================

@app.route('/users', methods=['GET'])
def get_users():

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()

        return jsonify(users), 200

    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500

    finally:
        cursor.close()
        conn.close()


# =====================================
# 2. GET USER BY ID
# =====================================

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute(
            "SELECT * FROM users WHERE id = %s",
            (user_id,)
        )

        user = cursor.fetchone()

        if user:
            return jsonify(user), 200

        return jsonify({'error': 'User not found'}), 404

    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500

    finally:
        cursor.close()
        conn.close()


# =====================================
# 3. POST - ADD NEW USER
# =====================================

@app.route('/users/add', methods=['POST'])
def add_user():

    data = get_request_data()

    name = data.get('name')
    email = data.get('email')
    age = data.get('age')
    city = data.get('city')

    if not name or not email:
        return jsonify({
            'error': 'Name and Email are required'
        }), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO users (name, email, age, city)
            VALUES (%s, %s, %s, %s)
            """,
            (name, email, age, city)
        )

        conn.commit()

        return jsonify({
            'message': 'User added successfully',
            'user_id': cursor.lastrowid
        }), 201

    except mysql.connector.Error as err:
        conn.rollback()
        return jsonify({'error': str(err)}), 500

    finally:
        cursor.close()
        conn.close()


# =====================================
# 4. PUT - UPDATE COMPLETE USER
# =====================================

@app.route('/users/update/<int:user_id>', methods=['PUT'])
def update_user(user_id):

    data = get_request_data()

    name = data.get('name')
    email = data.get('email')
    age = data.get('age')
    city = data.get('city')

    if not name or not email:
        return jsonify({
            'error': 'Name and Email are required'
        }), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            UPDATE users
            SET name = %s,
                email = %s,
                age = %s,
                city = %s
            WHERE id = %s
            """,
            (name, email, age, city, user_id)
        )

        if cursor.rowcount == 0:
            cursor.execute(
                "SELECT id FROM users WHERE id = %s",
                (user_id,)
            )

            if not cursor.fetchone():
                return jsonify({
                    'error': 'User not found'
                }), 404

        conn.commit()

        return jsonify({
            'message': 'User updated successfully',
            'user_id': user_id
        }), 200

    except mysql.connector.Error as err:
        conn.rollback()
        return jsonify({'error': str(err)}), 500

    finally:
        cursor.close()
        conn.close()


# =====================================
# 5. PATCH - PARTIAL UPDATE USER
# =====================================

@app.route('/users/patch/<int:user_id>', methods=['PATCH'])
def patch_user(user_id):

    data = get_request_data()

    if not data:
        return jsonify({
            'error': 'Provide at least one field to update'
        }), 400

    allowed_fields = ['name', 'email', 'age', 'city']

    update_fields = {
        key: value
        for key, value in data.items()
        if key in allowed_fields
    }

    if not update_fields:
        return jsonify({
            'error': 'No valid fields provided'
        }), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT id FROM users WHERE id = %s",
            (user_id,)
        )

        if not cursor.fetchone():
            return jsonify({
                'error': 'User not found'
            }), 404

        set_clause = ', '.join(
            f"{key} = %s" for key in update_fields
        )

        values = list(update_fields.values())
        values.append(user_id)

        query = f"""
            UPDATE users
            SET {set_clause}
            WHERE id = %s
        """

        cursor.execute(query, values)
        conn.commit()

        return jsonify({
            'message': 'User partially updated successfully',
            'user_id': user_id,
            'updated_fields': update_fields
        }), 200

    except mysql.connector.Error as err:
        conn.rollback()
        return jsonify({'error': str(err)}), 500

    finally:
        cursor.close()
        conn.close()


# =====================================
# 6. DELETE USER BY ID
# =====================================

@app.route('/users/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "DELETE FROM users WHERE id = %s",
            (user_id,)
        )

        if cursor.rowcount == 0:
            return jsonify({
                'error': 'User not found'
            }), 404

        conn.commit()

        return jsonify({
            'message': 'User deleted successfully',
            'user_id': user_id
        }), 200

    except mysql.connector.Error as err:
        conn.rollback()
        return jsonify({'error': str(err)}), 500

    finally:
        cursor.close()
        conn.close()


# =====================================
# 7. HOME ROUTE
# =====================================

@app.route('/', methods=['GET'])
def index():
    return jsonify({
        'message': 'Flask MySQL REST API is running',
        'status': 'success'
    }), 200


# =====================================
# 8. ENTRY POINT
# =====================================

if __name__ == '__main__':

    print("Available API Routes:")
    print(app.url_map)

    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
