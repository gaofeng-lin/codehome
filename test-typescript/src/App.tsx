import React, { useEffect, useState } from 'react';

// class Square extends React.Component {
//   render() {
//     return (
//       <button className="square">
//         {/* TODO */}
//       </button>
//     );
//   }
// }

const Square = (props: any) => {

  const [squareval, Setsquareval] = useState(null);

  return (
          <button className="square" 
          onClick={()=> {
            // console.log('click')
            // Setsquareval(props.value);
            props.onClick()
          }}
          >
        {props.value}
      </button>
  )
}


const Board = ()=> {

  const [sArray, SetsArray] = useState(Array(9).fill(null));
  const [xIsNext, SetxIsNext] = useState(false);

  const handleClick = (i: any) => {
    const squares = sArray.slice();
    if (calculateWinner(squares) || squares[i]) {
      return;
    }
    squares[i] = xIsNext ? 'X' : 'O';
    SetxIsNext(!xIsNext)
    SetsArray(squares)
  }

  const renderSquare = (i: any)=> {
    return <Square value={sArray[i]} 
    onClick = {()=> {
      handleClick(i)
    }}
    />;
  }
  function calculateWinner(squares: any) {
    const lines = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],
      [0, 4, 8],
      [2, 4, 6],
    ];
    for (let i = 0; i < lines.length; i++) {
      const [a, b, c] = lines[i];
      if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
        return squares[a];
      }
    }
    return null;
  }
  // const status = 'Next player: X';
  const winner = calculateWinner(sArray);
  let status;
  if (winner) {
    status = 'Winner: ' + winner;
  } else {
    status = 'Next player: ' + (xIsNext ? 'X' : 'O');
  }
  return (
    <div>
    <div className="status">{status}</div>
    <div className="board-row">
      {renderSquare(0)}
      {renderSquare(1)}
      {renderSquare(2)}
    </div>
    <div className="board-row">
      {renderSquare(3)}
      {renderSquare(4)}
      {renderSquare(5)}
    </div>
    <div className="board-row">
      {renderSquare(6)}
      {renderSquare(7)}
      {renderSquare(8)}
    </div>
  </div>
  )
}


class Game extends React.Component {
  render() {
    return (
      <div className="game">
        <div className="game-board">
          <Board />
        </div>
        <div className="game-info">
          <div>{/* status */}</div>
          <ol>{/* TODO */}</ol>
        </div>
      </div>
    );
  }
}

export default Game;