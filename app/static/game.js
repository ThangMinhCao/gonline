let socket;

window.onload = () => {
  renderBoard();
  socket = io("http://127.0.0.1:5000/", { query: `game_id=${gameId}`});
  socket.on("move", (data) => {
    displayMove(...data.position, data.color)
  });
}

function renderBoard() {
  const board = document.getElementById("board")

  for (let i = 0; i < 19; i++) {
    for (let j = 0; j < 19; j++) {
      const cell = document.createElement("div");
      cell.id = `${i}-${j}`;
      cell.className = "cell"
      cell.addEventListener("click", () => onMove(i, j))

      board.appendChild(cell);
    }
  }

  renderPlayedMoves();
}

function renderPlayedMoves() {
  moves.forEach(([i, j, color]) => displayMove(i, j, color));
}

function onMove(i, j) {
  socket.emit("move", { i, j, player_id: playerId })
};

function displayMove(i, j, color) {
  const cell = document.getElementById(`${i}-${j}`);
  const piece = document.createElement("span");
  piece.className = "piece"
  piece.style.background = color;
  cell.appendChild(piece);
};