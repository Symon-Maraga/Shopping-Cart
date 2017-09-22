from flask import Flask

from handlers import site
from shopping_list import Shopping_list
from store import Store


def create_app():
    app = Flask(__name__)
    app.config.from_object('settings')
    app.register_blueprint(site)

    app.store = Store()
    app.store.add_shopping_list(Shopping_list(fullname='Ben Finkel', username='ben_finkel', email=ben_finkel@gmail.com, password=ben_finkel,))
    app.store.add_shopping_list(Shopping_list(fullname='Alice Murray', username='alice_murray', email=alice_murray@gmail.com, password=alice_murray))

    return app


def main():
    app = create_app()
    port = app.config.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()