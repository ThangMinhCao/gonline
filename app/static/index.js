function createRoom() {
  fetch("/game", { method: "POST" })
    .then(res => console.log(res))
    // .then(token => window.location.replace(`/${token}`))
    .catch(err => console.log(err));
}

function onJoin() {
  game_id = document.getElementById("game-id-field").value;

  fetch(`/game/${game_id}`, { method: "POST" })
    .then(res => res.json())
    .then(token => window.location.replace(`/${token}`))
    .catch(err => console.log(err));
}