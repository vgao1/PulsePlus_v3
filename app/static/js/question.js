var ans = document.getElementById("answer").value;
document.getElementById("next").addEventListener("click", function () {
    if (document.getElementById("selected_team").value != "0") {
        document.getElementById("team_select").className = "hide";
        document.getElementById("mcq").style.display = "block";
    }
    else {
        alert("Please select a team!");
    }
});

function update_ans(id) {
    if (ans.length > 0) {
        ans = "";
    }
    ans += document.getElementById(id).value;
    var all_ans = document.getElementsByClassName("choice");
    for (i = 0; i < all_ans.length; i++) {
        all_ans[i].style.backgroundColor = "rgb(15, 131, 185)";
        all_ans[i].style.color = "white";
    }
    document.getElementById(id).style.backgroundColor = "gold";
    document.getElementById(id).style.color = "black";
    console.log(ans);
}