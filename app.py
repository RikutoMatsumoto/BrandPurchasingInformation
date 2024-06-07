from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///PurchasingInformation.db'
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    TradeName = db.Column(db.String(50), nullable=False)
    BrandName = db.Column(db.String(50), nullable=False)
    CleaningFee = db.Column(db.String(50))
    Memo = db.Column(db.String(200))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        posts = Post.query.all()
        return render_template('index.html', posts=posts)

    else:
        TradeName = request.form.get('TradeName')
        BrandName = request.form.get('BrandName')
        CleaningFee = request.form.get('CleaningFee')
        Memo = request.form.get('Memo')
        new_post = Post(
            TradeName=TradeName, 
            BrandName=BrandName, 
            CleaningFee=CleaningFee, 
            Memo=Memo)

        db.session.add(new_post)
        db.session.commit()
        return redirect('/')


@app.route('/create')
def create():
    return render_template('create.html')


@app.route('/detail/<int:id>')
def read(id):
    post = Post.query.get(id)

    return render_template('detail.html', post=post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)