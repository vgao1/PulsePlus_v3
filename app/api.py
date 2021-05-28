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

def get_category(id):
    ques = []
    difficulty = ["easy", "medium", "hard"]
    amount = ["2", "2", "1"]
    for i in range(3):
        u = urllib.request.urlopen(trivia_link + "difficulty="+ difficulty[i] +"&amount=" + amount[i] + "&category=" + str(id))
        info = json.loads(u.read())
        if info["response_code"] == 0:
            for j in info["results"]:
                ques.append(j)
    return ques

if(__name__ == "__main__"):
    test = get_category(10)
    for i in test:
        print(i["question"])
        print(i["correct_answer"])
        print(i["difficulty"])
        print()

