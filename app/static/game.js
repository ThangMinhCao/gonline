let socket;

window.onload = () => {
  renderBoard();
  socket = io("http://127.0.0.1:5000/", { query: `game_id=${gameId}` });

  socket.on("move", (data) => {
    displayMove(...data.position, data.color);

    if (data.is_finished) {
      document.getElementById("turn-status").textContent =
        data.next_player === playerId ? "You lose." : "You win.";
      socket.disconnect();
    } else {
      toggleGameStatus(data.next_player);
    }
  });

  if (isHost) {
    console.log("Waiting for player");
    socket.on("player_joined", (ready) => {
      if (ready) toggleStartButton("enable");
    });
  }

  socket.on("game_started", (nextPlayerId) => {
    toggleGameStatus(nextPlayerId);

    if (isHost) {
      toggleStartButton("disable");
      socket.off("player_joined");
    }
  });
};

function renderBoard() {
  const board = document.getElementById("board");

  for (let i = 0; i < 19; i++) {
    for (let j = 0; j < 19; j++) {
      const cell = document.createElement("div");
      cell.id = `${i}-${j}`;
      cell.className = "cell";
      cell.addEventListener("click", () => onMove(i, j));

      board.appendChild(cell);
    }
  }

  renderPlayedMoves();
}

function toggleGameStatus(nextPlayerId) {
  const turnStatus = document.getElementById("turn-status");
  const board = document.getElementById("board");
  if (nextPlayerId === playerId) {
    turnStatus.textContent = "Your turn.";
    board.style.pointerEvents = "all";
  } else {
    turnStatus.textContent = "Opponent's turn.";
    board.style.pointerEvents = "none";
  }
}

function toggleStartButton(state) {
  const button = document.getElementById("start-button");
  if (state === "disable") button.disabled = "disabled";
  else button.removeAttribute("disabled");
}

function onStart() {
  socket.emit("start_game", gameId);
}

function renderPlayedMoves() {
  moves.forEach(([i, j, color]) => displayMove(i, j, color));
}

function onMove(i, j, color) {
  socket.emit("move", { i, j, player_id: playerId });
}

function displayMove(i, j, color) {
  const cell = document.getElementById(`${i}-${j}`);
  const piece = document.createElement("span");
  piece.className = "piece";
  piece.style.background = color;
  cell.appendChild(piece);
}
