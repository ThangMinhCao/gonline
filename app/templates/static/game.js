let socket = io("http://127.0.0.1:5000/");

window.onload = () => {
  socket.on("participation", (response) => {
    if (response["success"]) {
      console.log(response.message);
    } else {
      window.location.replace("/");
    }
  });

  socket.emit("join", { game_id: gameId });
};