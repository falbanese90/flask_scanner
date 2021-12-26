from scan import app
from flask import render_template, redirect, url_for, flash
from scan.form import StockForm
import chart

@app.route('/', methods=['GET', 'POST'])
def home_page():
    form = StockForm()
    if form.validate_on_submit():
        equity = chart.Equity(form.stock.data)
        return render_template('data.html', equity=equity)
    return render_template('home.html', form=form)

@app.route('/data', methods=['GET', 'POST'])
def data_page():
    equity = equity
    return render_template('data.html')