from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True      # displays runtime errors in the browser, too


@app.route("/", methods=["GET"])
def index():
    #displays main page
    return render_template("form.html")



@app.route("/", methods=["POST"])
def result():
    #returns welcome screen or shows any error messages
    user_name = request.form["user_name"]
    password = request.form["password"]
    password_retype = request.form["retype"]
    email = request.form["email"]

    #run through potential errors

    if user_name.strip() == "":
        error_name = "Please enter a Username"
        return render_template("form.html", error_name=error_name)
    
    if len(user_name) < 3 or len(user_name) > 20:
        error_name = "Please enter a Username between 3 and 20 characters in length"
        return render_template("form.html", error_name=error_name, user_name=user_name, email=email)

    if user_name.find(" ") != -1:
        error_name = "Please enter a valid username, spaces not allowed"
        return render_template("form.html", error_name=error_name, user_name=user_name, email=email)

    if password.strip() == "":
        error_pw1 = "Please enter a Password"
        return render_template("form.html", error_pw1=error_pw1, user_name=user_name, email=email)

    if password_retype.strip() == "":
        error_pw2 = "Please retype your password"
        return render_template("form.html", error_pw2=error_pw2, user_name=user_name, email=email)

    if password != password_retype:
        error_pw2 = "Original password and retype do not match, please retype passwords"
        return render_template("form.html", error_pw2=error_pw2, user_name=user_name, email=email)

    if email.strip() != "":
        if email.find(" ") != -1:
            error_email = "Please enter a valid email between 3 and 20 characters long, without spaces"
            return render_template("form.html", error_email=error_email, user_name=user_name, email=email)
        if len(email) < 3 or len(email) > 20:
            error_email = "Please enter a valid email between 3 and 20 characters long, without spaces"
            return render_template("form.html", error_email=error_email, user_name=user_name, email=email)
        if email.count(".") != 1 or email.count("@") != 1:
            error_email = "Please enter a valid email between 3 and 20 characters long, without spaces"
            return render_template("form.html", error_email=error_email, user_name=user_name, email=email)
        
    return render_template("success.html", user_name=user_name)


    


app.run()