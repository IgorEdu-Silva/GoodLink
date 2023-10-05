from flask import Flask, render_template, redirect, request, flash
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'GoodLink'

loginOn = False

@app.route('/')
def home(): 
    return render_template('/index.html')

@app.route('/_homePage')
def homePage():
    if loginOn == True:
        return render_template("/homePage.html")
    elif loginOn == False:
        return redirect('/')

@app.route('/_login', methods=["POST"])
def login():
    emailLogin = request.form.get('email_login')
    passLogin = request.form.get('password_login')
    
    global loginOn

    with open('users.json') as usersTemp:
        users = json.load(usersTemp)

        cont = 0
        for user in users:

            cont += 1
            if user['emailLogin'] == emailLogin and user['passLogin'] == passLogin:
                loginOn = True
                return redirect("/_homePage")
            elif cont >= len(users):
                flash('User not find')
                return redirect("/")

@app.route('/_registro', methods=["POST"])
def registro():
    nameRegister = request.form.get('name_register')
    emailRegister = request.form.get('email_register')
    passRegister = request.form.get('password_register') 

    with open('users.json') as usersRead:
        users = json.load(usersRead)

    newUser = [
        {
            "nameRegister": nameRegister,
            "emailRegister": emailRegister,
            "passRegister": passRegister
        }
    ]

    users.append(newUser)

    print(users)

    with open('users.json', 'w') as usersTemp:
        json.dump(users, usersTemp, indent=4)

    return redirect("/")

# @app.route('/_reset_pass', methods=["POST"])
# def resetPass():
#     oldPass = request.form.get('old_pass')
#     newPass = request.form.get('new_pass')
#     confirmePass = request.form.get('confirme_pass')

if __name__ in "__main__":
    app.run(debug=True)