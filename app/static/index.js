/**
 * Request to join a room.
 * This will redirect the home page to the game page with the token.
 */
function createRoom() {
  fetch("/game", { method: "POST" })
    .then(res => res.json())
    .then(token => window.location.replace(`/${token}`))
    .catch(err => console.log(err));
}

/**
 * Request to join a room.
 * This will redirect the home page to the game page with the token.
 */
function onJoin() {
  room_id = document.getElementById("game-id-field").value;

  fetch(`/game/${room_id}`, { method: "POST" })
    .then(res => res.json())
    .then(token => window.location.replace(`/${token}`))
    .catch(err => console.log(err));
}