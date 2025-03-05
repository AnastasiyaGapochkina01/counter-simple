from flask import Flask, render_template, request, session
import uuid

app = Flask(__name__)
app.secret_key = 'secret_key_here'  # Установите секретный ключ

visits = 0
unique_users = set()

@app.route('/', methods=['GET'])
def index():
    global visits, unique_users

    visits += 1

    if 'user_id' not in session:
        session['user_id'] = str(uuid.uuid4())
        unique_users.add(session['user_id'])

    return render_template('index.html', visits=visits, unique_users=len(unique_users))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
