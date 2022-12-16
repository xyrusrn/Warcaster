function deleteNote(noteId) {
    fetch("/delete-note", {
    method: 'POST',
    body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
        window.location.href = "/notes";
    });
}

function deleteChar(charId) {
    fetch("/delete-char", {
    method: 'POST',
    body: JSON.stringify({ charId: charId }),
    }).then((_res) => {
        window.location.href = "/character";
    });
}