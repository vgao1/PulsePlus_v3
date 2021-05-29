var coll = document.getElementsByClassName("collapsible");
var team_names = "";
var i;
for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function () {
        var content = this.nextElementSibling;  //div element whose class="content"
        //if content is already shown, hide content when button is clicked
        
        if (content.style.display === "block") {
            content.style.display = "none";
            document.getElementById(this.innerText.trim() + "-up").classList.add("hide");
            document.getElementById(this.innerText.trim() + "-down").classList.remove("hide");
        }

        //show content
        else {
            content.style.display = "block";
            document.getElementById(this.innerText.trim() + "-down").classList.add("hide");
            document.getElementById(this.innerText.trim() + "-up").classList.remove("hide");
        }

    });
}

// Click on a close button to delete an added team name
var close = document.getElementsByClassName("close");
var j;
for (j = 0; j < close.length; j++) {
    close[j].onclick = function () {
        var div = this.parentElement;
        div.style.display = "none";
        team_names = team_names.replace(this.parentElement.innerText.slice(0, -1) + ",", "");
        document.getElementById("team_names").value = team_names;
    }
}

//If "Add" button is clicked, display name below previously added names (if any)
//add the most recently added team name to team_names variable
var add_Btn = document.getElementById("addBtn")
add_Btn.addEventListener("click", function () {
    var li = document.createElement("li");
    var inputValue = document.getElementById("team_name").value;
    var t = document.createTextNode(inputValue);
    //add background color and space between displayed team names
    li.setAttribute("style","background-color:rgb(240, 205, 10);margin-bottom:5px");
    li.appendChild(t);
    if (inputValue === '') {   //if the submitted team name has 0 characters
        alert("Please lengthen team name to 1 character or more (you are currently using 0 characters).");
    }
    if (inputValue !== '' && team_names.includes(inputValue + ",")) { //if the team name is already added
        alert("This team name is already added.");
    }
    else if (inputValue !== '') {   //if the team name hasn't been added
        document.getElementById("list_teams").appendChild(li);
        team_names += inputValue + ",";
    }
    document.getElementById("team_name").value = "";
    var span = document.createElement("SPAN");
    var txt = document.createTextNode("\u00D7");
    span.className = "close";
    span.appendChild(txt);
    li.appendChild(span);
    for (i = 0; i < close.length; i++) {
        close[i].onclick = function () {
            var div = this.parentElement;
            div.style.display = "none";
            team_names = team_names.replace(this.parentElement.innerText.slice(0, -1) + ",", "");
            document.getElementById("team_names").value = team_names;
        }
    }
    document.getElementById("team_names").value = team_names;
});

document.getElementById("setup-submit").addEventListener("click",function() {
    if ((document.getElementById("team_names").value.split(",").length - 1)<2){
        alert("Please add at least 2 team names!");
    }
    else {
        document.getElementById("team_name").required = false;
    }
})
