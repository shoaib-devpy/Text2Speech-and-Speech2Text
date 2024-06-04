function convertSpeechToText() {
    let audioFile = document.getElementById('audio-file').files[0];
    let formData = new FormData();
    formData.append('audio', audioFile);

    fetch('/speech_to_text', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(text => {
        document.getElementById('stt-result').innerText = text;
    })
    .catch(error => console.error('Error:', error));
}

function convertTextToSpeech() {
    let text = document.getElementById('text-to-convert').value;
    let voiceId = document.getElementById('voice-select').value;
    let formData = new FormData();
    formData.append('text', text);
    formData.append('voice_id', voiceId);

    fetch('/text_to_speech', {
        method: 'POST',
        body: formData
    })
    .then(response => response.blob())
    .then(blob => {
        let url = window.URL.createObjectURL(blob);
        let a = document.createElement('a');
        a.style.display = 'none';
        a.href = url;
        a.download = 'output.wav';
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
    })
    .catch(error => console.error('Error:', error));
}
