function send_req(data, id) {
    fetch('http://localhost:8001/dump', {
    // fetch('http://localhost:8001/ask', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'accept': 'application/json'
        },
        body: JSON.stringify({
            id: id,
            text: data
        })
    })
        .then((response) => response.json())
        .then((data) => {
            console.log("Success:", data);
        })
        .catch((error) => {
            console.error("Error:", error);
        });

}

const recognition = new webkitSpeechRecognition()
recognition.continuous = true
recognition.lang = 'de-DE'
recognition.start()

let activity = []

const min = 0;
const max = 1000000;
const token = Math.floor(Math.random() * (max - min + 1)) + min;
//console.log(c); // 16

recognition.onresult = event => {
    console.log(event)
    activity.push('Ended:' + event.timeStamp)
    //console.log(event.results.length)
    const transcript = event.results[event.results.length - 1][0].transcript;
    console.log(transcript);
    // event.results = [];
    send_req(transcript, token);
}

recognition.onspeechstart = event => {
    activity.push('Started:' + event.timeStamp)
}

//window.end = recognition.onend = event => {
// console.log(activity)
//}

/*
var SpeechRecognition = SpeechRecognition || webkitSpeechRecognition
var SpeechGrammarList = SpeechGrammarList || window.webkitSpeechGrammarList
var SpeechRecognitionEvent = SpeechRecognitionEvent || webkitSpeechRecognitionEvent

var diagnostic = document.querySelector('.output');
const recognition = new SpeechRecognition();
recognition.interimResults = true;

recognition.addEventListener('result', e => {
  const transcript = Array.from(e.results)
      .map(result => result[0])
      .map(result => result.transcript)
      .join('');
  console.log(transcript);
});

recognition.addEventListener('end', recognition.start);

recognition.onresult = function(event) {

  var sentence = event.results[0][0].transcript;
  diagnostic.textContent = 'Result received: ' + sentence + '.';

  console.log('Confidence: ' + event.results[0][0].confidence);
  setInterval(function() {
    console.log(transcript);
  }, 20000);

  send_req(sentence, 1);

}

recognition.start();
/*

/*
var recognition = new SpeechRecognition();
if (SpeechGrammarList) {
  // SpeechGrammarList is not currently available in Safari, and does not have any effect in any other browser.
  // This code is provided as a demonstration of possible capability. You may choose not to use it.
  var speechRecognitionList = new SpeechGrammarList();
  var grammar = '#JSGF V1.0; grammar colors; public <color> = ' + colors.join(' | ') + ' ;'
  speechRecognitionList.addFromString(grammar, 1);
  recognition.grammars = speechRecognitionList;
}
recognition.continuous = false;
recognition.lang = 'de-DE';
recognition.interimResults = false;
recognition.maxAlternatives = 1;

var diagnostic = document.querySelector('.output');
var bg = document.querySelector('html');
var hints = document.querySelector('.hints');

var colorHTML= '';
colors.forEach(function(v, i, a){
  console.log(v, i);
  colorHTML += '<span style="background-color:' + v + ';"> ' + v + ' </span>';
});
hints.innerHTML = 'Tap/click then say a color to change the background color of the app. Try ' + colorHTML + '.';

document.body.onclick = function() {
  recognition.start();
  console.log('Ready to receive a color command.');
}

recognition.onresult = function(event) {
  // The SpeechRecognitionEvent results property returns a SpeechRecognitionResultList object
  // The SpeechRecognitionResultList object contains SpeechRecognitionResult objects.
  // It has a getter so it can be accessed like an array
  // The first [0] returns the SpeechRecognitionResult at the last position.
  // Each SpeechRecognitionResult object contains SpeechRecognitionAlternative objects that contain individual results.
  // These also have getters so they can be accessed like arrays.
  // The second [0] returns the SpeechRecognitionAlternative at position 0.
  // We then return the transcript property of the SpeechRecognitionAlternative object
  var color = event.results[0][0].transcript;
  diagnostic.textContent = 'Result received: ' + color + '.';
  bg.style.backgroundColor = color;
  console.log('Confidence: ' + event.results[0][0].confidence);
}

recognition.onspeechend = function() {
  recognition.stop();
}

recognition.onnomatch = function(event) {
  diagnostic.textContent = "I didn't recognise that color.";
}

recognition.onerror = function(event) {
  diagnostic.textContent = 'Error occurred in recognition: ' + event.error;
}
*/