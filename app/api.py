import urllib.request, json

trivia_link = "https://opentdb.com/api.php?"

# General Knowledge -> 9
# Entertainment: Books -> 10
# Entertainment: Film -> 11
# Entertainment: Music -> 12
# Entertainment: Musicals & Theatres -> 13
# Entertainment: Television -> 14
# Entertainment: Video Games -> 15
# Entertainment: Board Games -> 16
# Science & Nature -> 17
# Science: Computers -> 18
# Science: Mathematics -> 19
# Mythology -> 20
# Sports -> 21
# Geography -> 22
# History -> 23
# Politics -> 24
# Art -> 25
# Celebrities -> 26
# Animals -> 27
# Vehicles -> 28
# Entertainment: Comics -> 29
# Science: Gadgets -> 30
# Entertainment: Japanese Anime & Manga-> 31
# Entertainment: Cartoon & Animations-> 32

cats = { 9: "General Knowledge", 10: "Books", 11: "Films", 12: "Music", 13: "Musicals & Theatres",
        14: "Television", 15: "Video Games", 16: "Board Games", 17: "Nature",
        18: "Computers", 19: "Mathematics", 20: "Mythology", 21: "Sports",
        22: "Geography", 23: "History", 24: "Politics", 25: "Art", 26: "Celebrities",
        27: "Animals", 28: "Vehicles", 29: "Comics", 30: "Gadgets",
        31: "Japanese Anime & Manga", 32: "Cartoon & Animations" }

def get_questions(id):
    ques = []
    difficulty = ["easy", "medium", "hard"]
    amount = ["2", "2", "1"]
    for i in range(3):
        u = urllib.request.urlopen(trivia_link + "difficulty="+ difficulty[i] +"&amount=" + amount[i] + "&category=" + str(id + "&type=multiple"))
        info = json.loads(u.read())
        if info["response_code"] == 0:
            for j in info["results"]:
                q = {'question': j['question'], 'correct_answer': j['correct_answer'], 'incorrect_answers': j['incorrect_answers']}
                ques.append(q)
    return ques

def get_category(id):
    return cats.get(id)

if(__name__ == "__main__"):
    print(get_category(27))
    test = get_questions(10)
    for i in test:
        print(i["question"])
        print(i["correct_answer"])
        print(i["difficulty"])
        print()
