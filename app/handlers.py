from flask import Blueprint, render_template
from flask import current_app

site = Blueprint('site', __name__)


@site.route('/shopping_list')
def shopping_list_page():
    shopping_list = current_app.store.get_shopping_list()
    return render_template('dashboard.html', shopping_list=sorted(shopping_list.items()))


@site.route('/shopping_list/<int:shopping_id>')
def shopping_list_page(shopping_list_id):
    shopping_list = current_app.store.get_shopping_list(shopping_id)
    return render_template('login.html', shopping_list=shopping_list)    