function createRoom() {
  fetch("/game", { method: "POST" })
    .then(res => res.json())
    .then(roomId => window.location.replace(`/game/${roomId}`))
    .catch(err => console.log(err));
}