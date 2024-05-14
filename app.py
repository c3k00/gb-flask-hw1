from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('category.html', categories=categories)

# Кортеж для обуви
shoes_data = (
    {
        'name': 'Ботинки',
        'description': 'Кожаные ботинки',
        'price': 79.99,
        'image': 'boots.jpg',
        'slug': 'boots'
    },
    {
        'name': 'Кроссовки',
        'description': 'Спортивные кроссовки',
        'price': 39.99,
        'image': 'sneakers.jpg',
        'slug': 'sneakers'
    }
)

# Кортеж для одежды
clothing_data = (
    {
        'name': 'Куртка',
        'description': 'Теплая куртка',
        'price': 50.99,
        'image': 'jacket.jpeg',
        'slug': 'jacket'
    },
    {
        'name': 'Футболка',
        'description': 'Хлопковая футболка',
        'price': 19.99,
        'image': 't-shirt.jpg',
        'slug': 't-shirt'
    }
)

# Категории
categories = [
    {
        'name': 'Обувь',
        'products': shoes_data
    },
    {
        'name': 'Одежда',
        'products': clothing_data
    }
]


@app.route('/products/<slug>')
def product_detail(slug):
    for category in categories:
        for product in category['products']:
            if product['slug'] == slug:
                return render_template('product_detail.html', product=product)
    return 'Product not found', 404

if __name__ == '__main__':
    app.run()