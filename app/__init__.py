from flask import Flask, render_template, request
import api

app = Flask(__name__)
#render home page
@app.route("/", methods=["GET", "POST"])
def root():
    return render_template("home.html")

info = {}

#<Name of HTML form element>: (data type) <info stored>
#team_names: (string) team names separated by commas
#category: value of selected radio button for question category (int between 9 and 32, inclusive)
#score_rule: value of selected radio button for score rule (default or customized)
    #if customized option is checked, deduct (positive int) is # of points to deduct
    # for wrong answers. Default deduct is 1 point.
@app.route("/setup_cards", methods=["GET", "POST"])
def setup():
    teams = request.form.get("team_names").split(",")
    teams.pop()
    cats = request.form.getlist("category")
    if not info:
        for cat in cats:
            info[api.get_category(int(cat))] = [False] * 5
    print(request.form["score_rule"])
    return render_template("questions.html", teams=teams, info=info)

if(__name__ == "__main__"):
    app.debug = True
    app.run()
