import { languages } from 'templates/online_compiler/aceeditor.html'
let editor;
document.getElementById('editor').style.fontSize= "x-large"; 

window.onload = function(){
    editor = ace.edit("editor");
    editor.setTheme("ace/theme/monokai");
    editor.session.setMode("ace/mode/python");
}

function changeLanguage(){
    let language = document.querySelector("#languages");
    // let language = #languages.val();

    if(language == 'c' || language == 'cpp')editor.session.setMode("ace/mode/c_cpp");
    if(language == 'python')editor.session.setMode("ace/mode/python");
    if(language == 'java')editor.session.setMode("ace/mode/java");
}

function executeCode(){

    $.ajax({

        url: "http://127.0.0.1:8000/online_compiler",
        method: "POST",
        data: {
            language: $("#languages").val(),
            code: editor.getSession().getValue()
        },

        success: function(response){
            $(".output").text(response)
        }
    })
}