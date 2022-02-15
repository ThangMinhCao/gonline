let socket;

window.onload = () => {
  /* Render the game board with played moves if available. */
  renderBoard();

  /* Connect to Socket.IO server. */
  socket = io(PUBLIC_URL, { query: `room_id=${gameId}` });

  /**
   * A listener for move emission.
   * Render details based on the move data and the game state to render.
   */
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

  /**
   * If this client is host, add a socket listener to enable the start button.
   */
  if (isHost) {
    console.log("Waiting for player");
    socket.on("player_joined", (ready) => {
      if (ready) {
        toggleStartButton("enable");
      }
    });
  }

  /**
   * If game start event is received,
   * the page's state is toggle to let players start.
   */
  socket.on("game_started", (nextPlayerId) => {
    toggleGameStatus(nextPlayerId);

    if (isHost) {
      toggleStartButton("disable");
      socket.off("player_joined");
    }
  });
};

/**
 * Create a square div for each 19x19 board cell.
 * The played moves are also rendered if available.
 */
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

/**
 * Enable the board and change state text depends on that
 * if this client is the next player or not.
 * @param {String} nextPlayerId
 */
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

/**
 * Toggle the make start button disabled or enabled.
 * @param {"disabled" | "enabled"} state 
 */
function toggleStartButton(state) {
  const button = document.getElementById("start-button");

  if (state === "disable") button.disabled = "disabled";
  else button.removeAttribute("disabled");
}

/**
 * Emit a start game request to the socket server.
 */
function onStart() {
  socket.emit("start_game", gameId);
}

/**
 * Display all the played moves on the board.
 * This function is for the case the player refresh the page.
 */
function renderPlayedMoves() {
  moves.forEach(([i, j, color]) => displayMove(i, j, color));
}

/**
 * Emit the move request to the socket server.
 * @param {number} i The coordinate respect to the vertical axis
 * @param {number} j The coordinate respect to the horizontal axis
 */
function onMove(i, j) {
  socket.emit("move", { i, j, player_id: playerId });
}

/**
 * Display a move on the board.
 * @param {number} i The coordinate respect to the vertical axis
 * @param {number} j The coordinate respect to the horizontal axis
 * @param {string} color The color of the piece
 */
function displayMove(i, j, color) {
  const cell = document.getElementById(`${i}-${j}`);
  const piece = document.createElement("span");

  piece.className = "piece";
  piece.style.background = color;
  cell.appendChild(piece);
}
