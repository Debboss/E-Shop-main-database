from flask import Flask, render_template, request

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_username'
app.config['MYSQL_DB'] = 'your_database'

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/products')
def products_page():
    products = [
    {
        'name': 'Product A',
        'price': 29.99,
        'category': 'Electronics',
        'description': 'A high-quality electronic product with advanced features.',
        'image': 'https://img.global.news.samsung.com/in/wp-content/uploads/2022/03/SM-A536_Galaxy-A53-5G_Awesome-Peach_Front.jpg' 
    },
    {
        'name': 'Product B',
        'price': 49.99,
        'category': 'Clothing',
        'description': 'Stylish and comfortable clothing item for everyday wear.',
        'image': 'data:image/jpeg;base64,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'
    },
    {
        'name': 'Product C',
        'price': 9.99,
        'category': 'Home & Kitchen',
        'description': 'Useful and practical item for your home or kitchen.',
        'image': 'data:image/jpeg;base64,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'
    },
    {
        'name': 'Product D',
        'price': 99.99,
        'category': 'Fitness',
        'description': 'A fitness product to help you stay active and healthy.',
        'image': 'data:image/jpeg;base64,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'
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

@app.route('/subscription_plans')
def subscriptionPlans_page():
    plans = [
    {
        'name': 'Basic Plan',
        'price': 9.99,
        'duration': '1 month',
        'features': ['Basic features', 'Limited content access'],
    },
    {
        'name': 'Standard Plan',
        'price': 19.99,
        'duration': '3 months',
        'features': ['Standard features', 'Full content access', 'HD streaming'],
    },
    {
        'name': 'Premium Plan',
        'price': 29.99,
        'duration': '6 months',
        'features': ['Premium features', 'Ultra HD streaming', 'Offline downloads'],
    },
    {
        'name': 'Family Plan',
        'price': 39.99,
        'duration': '1 year',
        'features': ['All Premium features', 'Simultaneous streaming on multiple devices'],
    },
    ]

    return render_template('Subscription Plans/subscription_plans.html',plans=plans )

@app.route('/cart')
def cart_page():
    return render_template('cart/cart.html')

@app.route('/Login')
def login_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        #Connect to MySQL database
        mysql = mysql.connector.connect(
            host = app.config['MYSQL_HOST'],
            user = app.config['MYSQL_USER'],
            database =  app.config['MYSQL_DB']
        )

        # Execute SQL query to insert user's credentials
        cursor = mysql.cursor()
        insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(insert_query, (username, password))
        mysql.commit()  # Commit changes to the database
        cursor.close()
        mysql.close()

        return 'Signup successfull'
    return render_template('Login/login.html')

@app.route('/Sign Up')
def signUp_page():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        repeat_pass = request.form['repeat_pass']

        #Connect to MySQL database
        mysql = mysql.connector.connect(
            host = app.config['MYSQL_HOST'],
            user = app.config['MYSQL_USER'],
            database =  app.config['MYSQL_DB']
        )

        # Execute SQL query to insert user's credentials
        cursor = mysql.cursor()
        insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(insert_query, (username,email, repeat_pass, password))
        mysql.commit()  # Commit changes to the database
        cursor.close()
        mysql.close()

        return 'Signup successfull'
    return render_template('Sign Up/signUp.html')



if __name__ == '__main__':
    app.run(debug=True)
