from fastapi import FastAPI, Depends, Query
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import models as db
import schemas as ss
import hashlib as hs

app = FastAPI()

oauth_scheme = OAuth2PasswordBearer(tokenUrl='token')

@app.get('/')
def home():
    return {'Data':'Home Page'}

@app.post('/token')
def token_generate(form_data : OAuth2PasswordRequestForm = Depends()):
    query = db.session.query(db.User_data).filter(db.User_data.user_name == form_data.username).first()
    print("..........",query)
    if query == None:
        return {'status': "user doesn't exist"}
    password = form_data.password.encode()
    result = hs.sha256(password)
    if result.hexdigest() == query.password:
        return {'access_token': form_data.username, 'token_type': 'bearer'}
    else:
        return {'status' : 'either username or password is incorrect'}

@app.get('/allowed')
def allowed_page(token: str = Depends(oauth_scheme)):
    return {'status': 'user logen in', 'username': token}

@app.post('/add_article')
def add_article(form_data: ss.Article_check):
    new_article = db.Article(title= form_data.title, body= form_data.body)
    db.session.add(new_article)
    db.session.commit()
    return {'status': 'success', 'id': new_article.identity}

@app.put('/update_data/{i}')
def update_data(form_data: ss.Article_check, i: int, token: str = Depends(oauth_scheme)):
    query = db.session.query(db.Article).filter(db.Article.identity == i).first()
    query.title = form_data.title
    query.body = form_data.body
    db.session.commit()
    return {'status':'changed'}

@app.post('/register_user')
def register_user(user : ss.User_details):
    password = user.password.encode()
    result = hs.sha256(password)
    new_user = db.User_data(user_name=user.user_name, password= result.hexdigest())
    db.session.add(new_user)
    db.session.commit()
    return {'status': 'user added successfully'}