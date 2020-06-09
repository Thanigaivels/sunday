const remote = require('electron').remote;
document.getElementById("close").addEventListener("click", function (e) {
  var window = remote.getCurrentWindow();
  window.close();
});

function chataiva(text) {
    userchat(text);
    var {PythonShell} = require('python-shell')
    var path = require("path")
    var options = {
      scriptPath : 'core/',
      args : [text]
    }
    let pyshell = new PythonShell('sundayText.py', options);
    pyshell.on('message', function(message) {
        aivachat(message);
    })
  }
var chatarea = document.getElementById("chatarea");
function userchat(text = "No msg given"){
    var box = document.createElement("div");
    box.setAttribute("class","user");
    box.innerHTML=text
    chatarea.appendChild(box);
    chatarea.scrollTop = chatarea.scrollHeight;
}
function aivachat(text = "No msg given"){
    var box = document.createElement("div");
    box.setAttribute("class","aiva");
    box.innerHTML=text
    chatarea.appendChild(box);
    chatarea.scrollTop = chatarea.scrollHeight;
}
var input = document.getElementById("input");
input.addEventListener("keydown", function (e) {
  if (e.keyCode === 13) {  //checks whether the pressed key is "Enter"
    data = input.value;
    input.value = "";
    chataiva(data);
  }
});
mic.addEventListener("click", function (e) {
var {PythonShell} = require('python-shell')
    var data;
    var options = {
      scriptPath : 'core/',
      args : []
    }
    let pyshell = new PythonShell('listen.py', options);
    pyshell.on('message', function(message) {
      data = message
      chataiva(data)
    })
    
});
aivachat("How may I help you?");