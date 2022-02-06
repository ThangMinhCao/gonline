window.onload = () => {
  let socket = io("http://127.0.0.1:5000/");
  const url = window.location.pathname;
  const gameId = url.substring(url.lastIndexOf("/") + 1);
  socket.on("participation", (message) => {
    console.log(message);
  });
  socket.emit("join", { game_id: gameId, player_name: "Unkown" });
};
