import App from './App.svelte'
import { Cell } from './Cell'

const rows = 8
const cols = 8
const size = 80
const updateTime = 150

let score = 0

let fired = false

var socket = (window as any).io('http://localhost:8080')
socket.on('connect', function () {
	console.log('connected')
	socket.emit('connected', { data: "I'm connected!" })
})

const app = new App({
	target: document.body,
	props: {
		score,
	},
})

const grid: Array<Array<Cell>> = Array.from(Array(rows), () => Array(cols))
let board: Array<Array<any>>
let moves: Array<Array<Array<number>>>

function enterMouse(i, j) {
	if (grid[i][j].occupied) {
		if (moves) {
			let available_moves = get_moves_from_cell(i, j)
			available_moves.forEach((move) => {
				const to = move[1]
				const cell = grid[to[0]][to[1]]
				cell.mark()
			})
		}
	}
}

function leaveMouse(i, j) {
	if (grid[i][j].occupied) {
		if (moves) {
			let available_moves = get_moves_from_cell(i, j)
			available_moves.forEach((move) => {
				const to = move[1]
				const cell = grid[to[0]][to[1]]
				cell.unmark()
			})
		}
	}
}
// funtion hoverHandler

function createCell(i: number, j: number) {
	const cell = document.createElement('div')
	cell.setAttribute('data-x', i.toString())
	cell.setAttribute('data-y', j.toString())
	cell.classList.add('cell')
	cell.style.height = (size - 2).toString() + 'px'
	cell.style.width = (size - 2).toString() + 'px'

	cell.addEventListener('mouseenter', (e) => {
		enterMouse(i, j)
	})

	cell.addEventListener('mouseleave', () => {
		leaveMouse(i, j)
	})

	const img = document.createElement('img')
	img.setAttribute('src', './images/blank.png')
	// p.innerHTML = `${i},${j}`
	cell.appendChild(img)
	return cell
}

function createGrid() {
	const grid_elem = document.getElementById('grid')
	grid_elem.style.height = (cols * size).toString() + 'px'
	grid_elem.style.width = (rows * size).toString() + 'px'
	for (let i = 0; i < rows; i++) {
		for (let j = 0; j < cols; j++) {
			const cell = createCell(i, j)

			grid[i][j] = new Cell(cell)
			grid_elem.appendChild(cell)
		}
	}
}

createGrid()

socket.on('init', (board_raw: string) => {
	board = JSON.parse(board_raw)
	update_board()

	socket.emit('get available moves', JSON.stringify(board))
})

socket.on('available moves', (data: any) => {
	moves = data
})

function get_update() {
	// console.log('get_update')
	socket.emit('get_update', JSON.stringify(board))
}

socket.on('update_board', (board_raw: string) => {
	socket.emit('get available moves', board_raw)
	board = JSON.parse(board_raw)
	update_board()
	// console.log(board)
})

function update_board() {
	for (let i = 0; i < rows; i++) {
		for (let j = 0; j < cols; j++) {
			grid[i][j].update_from_server(board[i][j])
		}
	}
}

function get_moves_from_cell(x: number, y: number) {
	return moves.filter((elem) => {
		return elem[0][0] === x && elem[0][1] === y
	})
}

document.getElementById('move')?.addEventListener('click', () => {
	get_update()
	score += 1
})

export default app
