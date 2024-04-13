from flask import Flask, render_template, request
import mysql.connector
import hashlib

app = Flask(__name__)

# Connect to MySQL database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="DESKTOP-D1EGVS1-",
            user="root",
            login_database="login",  
            signup_database="sign_up"
        )
        return connection
    except mysql.connector.Error as error:
        print("Error connecting to MySQL database:", error)
        return None


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/products')
def products_page():
    products = [
    {
        'name': "Men's Shoes DN 23XX",
        'image': 'https://via.placeholder.com/200x200?text=Shoe',
        'price': 150.00,
        'discount_price': 133.00,
        'discount': '25% off',
        'category': "Men's Shoes",
        'description': 'New product for men with advanced features.',
        'image': 'https://img.global.news.samsung.com/in/wp-content/uploads/2022/03/SM-A536_Galaxy-A53-5G_Awesome-Peach_Front.jpg'
    },
    {
        'name': "Women's Shoes DN 23XX",
        'image': 'https://via.placeholder.com/200x200?text=Shoe2',
        'price': 100.00,
        'discount_price': 50.00,
        'discount': '50% off',
        'category': "Women's Shoes",
        'description': 'New product for women with stylish design.',
    },
]
    

    return render_template('products.html', products=products)

@app.route('/contact_us')
def contactUs_page():
    contact_info = [
    {
        'department': 'Sales',
        'email': 'sales@example.com',
        'phone': '+1 (555) 123-4567',
    },
    {
        'department': 'Support',
        'email': 'support@example.com',
        'phone': '+1 (555) 987-6543',
    },
    {
        'department': 'General Inquiries',
        'email': 'info@example.com',
        'phone': '+1 (555) 789-0123',
    },
    ]

    return render_template('contact_us.html', contact_info=contact_info)

subscription_plans = [
    {
        'name': 'Basic Plan',
        'price': 'Free',
        'duration': '1 month',
        'features': ['1 Account', 'Limited content access', 'Limited amount of items in wishlist', 'No discount on shipment fees',
                     'Limited eligibility for giveaways'],
    },
    {
        'name': 'Standard Plan',
        'price': 19.99,
        'duration': '3 months',
        'features': ['Multiple Accounts', 'Full content access', 'Unlimited items in wishlist', '50% discount on shipment fees',
                     'Eligibility for a majority of giveaways'],
    },
    {
        'name': 'Premium Plan',
        'price': 29.99,
        'duration': '6 months',
        'features': ['Unlimited Accounts', 'Full content access', 'Unlimited items in wishlist', 'No shipment fees',
                     'Eligibility for exclusive giveaways'],
    },
]

@app.route('/subscription_plans')
def subscriptionPlans_page():
    return render_template('Subscription Plans/subscription_plans.html', plans=subscription_plans)

@app.route('/cart')
def cart_page():
    return render_template('cart.html')

@app.route('/Login')
def login_page():
    if request.method == 'POST':
        # Retrieve form data
        username = request.form['username']
        password = request.form['password']

        # Hash the password (you should use a proper hashing algorithm)
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Insert data into the database
        connection = connect_to_database()
        if connection:
            try:
                cursor = connection.cursor()
                insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
                insert_values = (username, hashed_password)
                cursor.execute(insert_query, insert_values)
                connection.commit()
                cursor.close()
                connection.close()
                return "Account created successfully!"  
            except mysql.connector.Error as error:
                print("Error inserting data into MySQL database:", error)
                return "Error creating account"
        else:
            return "Error connecting to database"

    return render_template('Login/login.html')

@app.route('/Sign Up')
def signUp_page():
    if request.method == 'POST':
        # Retrieve form data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        repeat_password = request.form['repeat_password']

        # Check if passwords match
        if password != repeat_password:
            return "Passwords do not match. Please try again."

        # Hash the password (you should use a proper hashing algorithm)
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Insert data into the database
        connection = connect_to_database()
        if connection:
            try:
                cursor = connection.cursor()
                insert_query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
                insert_values = (username, email, hashed_password)
                cursor.execute(insert_query, insert_values)
                connection.commit()
                cursor.close()
                connection.close()
                return "Account created successfully!"  # You might want to redirect to a different page
            except mysql.connector.Error as error:
                print("Error inserting data into MySQL database:", error)
                return "Error creating account"
        else:
            return "Error connecting to database"

    return render_template('Sign Up/signUp.html')



if __name__ == '__main__':
    app.run(debug=True)
