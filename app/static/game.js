let socket = io("http://127.0.0.1:5000/");

function onMove(x, y) {
  console.log(x + ' ' + y);
};