async function analyzePassword(){

let password = document.getElementById("password").value;

let response = await fetch("/analyze",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({password:password})
});

let data = await response.json();

let result = `
Strength: ${data.strength}
<br>Score: ${data.score}/5
<br>Suggestions:
<ul>
`;

data.suggestions.forEach(s=>{
result += `<li>${s}</li>`;
});

result += "</ul>";

if(data.breached){
result += "<br style='color:red'>⚠ Password found in data breaches!";
}

document.getElementById("result").innerHTML = result;

}



async function generatePassword(){

let response = await fetch("/generate");

let data = await response.json();

document.getElementById("password").value = data.password;

}
