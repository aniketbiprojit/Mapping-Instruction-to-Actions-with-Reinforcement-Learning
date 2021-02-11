import App from './App.svelte'
import { Cell } from './Cell'

const rows = 8
const cols = 8
const size = 80
const updateTime = 150

let score = ''

let fired = false

var socket = (window as any).io('http://localhost:8080')
socket.on('connect', function () {
	console.log('connected')
	socket.emit('connected', { data: "I'm connected!" })
})

const app = new App({
	target: document.body,
	props: {
		// rows,
		// cols,
		handleKeyPress,
		clickHandler,
		score,
	},
})

const grid: Array<Array<Cell>> = Array.from(Array(rows), () => Array(cols))

function createCell(i: number, j: number) {
	const cell = document.createElement('div')
	cell.setAttribute('data-x', i.toString())
	cell.setAttribute('data-y', j.toString())
	cell.classList.add('cell')
	cell.style.height = (size - 2).toString() + 'px'
	cell.style.width = (size - 2).toString() + 'px'
	const p = document.createElement('p')
	// p.innerHTML = `${i},${j}`
	cell.appendChild(p)
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
	const board: Array<Array<any>> = JSON.parse(board_raw)
	for (let i = 0; i < rows; i++) {
		for (let j = 0; j < cols; j++) {
			grid[i][j].update_from_server(board[i][j])
		}
	}
	console.log(grid)
})

async function clickHandler(val: 'up' | 'down' | 'left' | 'right') {}

async function handleKeyPress(e: KeyboardEvent) {}

export default app
