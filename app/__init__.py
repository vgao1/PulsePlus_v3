from flask import Flask, render_template, request
import api, json
import random

app = Flask(__name__)
#render home page
@app.route("/", methods=["GET", "POST"])
def root():
    return render_template("home.html")

#<Name of HTML form element>: (data type) <info stored>
#team_names: (string) team names separated by commas
#category: value of selected radio button for question category (int between 9 and 32, inclusive)
#score_rule: value of selected radio button for score rule (default or customized)
    #if customized option is checked, deduct (positive int) is # of points to deduct
    # for wrong answers. Default deduct is 1 point.
#selected_team: name of team answering a question
#answer: answer submitted by selected_team


#set up the board of cards
@app.route("/setup_cards", methods=["GET", "POST"])
def setup():
    #turn string of team names into a list
    teams = request.form.get("team_names").split(",")
    teams.pop()

    #initialize global variables
    global info
    global categories
    global questions
    global scores
    global score_rule
    global penalty

    #info is a dictionary: keys are question categories selected by user
    #values are lists containing true/false values where true means question has been answered already
    info = {}

    #categories is a list of question categories selected by user
    categories = []
    
    #questions is a list containing each card's question, incorrect and correct answers
    questions = []
    
    #scores is a dictionary: keys are team names and values are # of points earned by teams
    scores = {}
    for team in teams:
        scores[team] = 0

    #cats: local variable storing inputted categories from HTML form
    cats = request.form.getlist("category")
    
    for cat in cats:
        info[api.get_category(int(cat))] = [False] * 5
        questions.append(api.get_questions(int(cat)))
        categories.append(api.get_category(int(cat)))
    score_rule = request.form.get('score_rule')
    if (score_rule == "customized"):
        penalty = int(request.form.get('deduct'))
    return render_template("questions.html", teams=teams, info=info, categories=json.dumps(categories), clicked=json.dumps(info),scores=scores)

#get info about the selected card: clicked on status, question, answers
@app.route("/question", methods=["GET", "POST"])
def question():
    #name of buttons were formatted as <column>-<row>
    #column is the index of the column that the card was in
    #row is the index of the row that the card was in
    for col in range(0,5):
        for row in range(0,5):
            #if a button is clicked on
            if request.form.get(str(col)+"-"+str(row))!=None:
                #get question corresponding to position of card
                q = questions[col][row]

                #choices: answer choices of the question 
                choices = []
                choices.append(q["correct_answer"])
                for wrong_ans in q["incorrect_answers"]:
                    choices.append(wrong_ans)
                random.shuffle(choices) #shuffle answer choices
                info[categories[col]][row] = True   #if user submits an answer, change clicked on status to True
                return render_template('question.html',q=q,choices=choices,teams=list(scores.keys()), row = row, col = col)

#check if the submitted answer is correct
@app.route("/check_ans", methods=["GET", "POST"])
def answer():
    #stores the team that is answering the question
    team = request.form.get('team')

    #stores specific question that was clicked on
    col = int(request.form.get('col'))
    row = int(request.form.get('row'))
    q = questions[col][row]

    #stores the correct answer for the question that was chosen and stores the choice that the team chose
    correct_answer = q["correct_answer"]
    choice = request.form.get('answer')

    #checks if the choice was correct and awards points/deducts points based on scoring rules
    if (choice == correct_answer):
        scores[team] += (row + 1) * 100
    elif (score_rule == 'customized'):
        scores[team] -= penalty 
    return render_template("questions.html", teams=list(scores.keys()), info=info, categories=json.dumps(categories), clicked=json.dumps(info),scores=scores)

if(__name__ == "__main__"):
    app.debug = True
    app.run()
