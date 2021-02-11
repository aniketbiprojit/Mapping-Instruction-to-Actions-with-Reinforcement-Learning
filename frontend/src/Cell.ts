export class Cell {
	block: HTMLElement

	piece_type: string
	color: string

	occupied = false
	constructor(block: HTMLElement) {
		this.block = block
	}

	mark() {
		if (this.occupied) {
			this.block.classList.add('dead')
		} else {
			this.block.classList.add('marked')
		}
	}

	unmark() {
		this.block.classList.remove('dead')
		this.block.classList.remove('marked')
	}

	update_from_server(board_elem) {
		if (board_elem['occupied']) {
			this.occupied = true
			this.piece_type = board_elem['piece_type']
			this.color = board_elem['color']

			this.block.innerHTML = this.color.toLowerCase()[0] + this.piece_type[0]
		} else {
			this.occupied = false
			this.piece_type = undefined
			this.color = undefined
			this.block.innerHTML = ''
		}
		this.block.setAttribute('data-occupied', this.occupied.toString())
		this.block.setAttribute('data-piece_type', this.piece_type)
		this.block.setAttribute('data-color', this.color)
	}
	// mark() {
	// 	this.marked = true
	// 	this.block.classList.add('marked')
	// }

	// unmark() {
	// 	this.marked = false
	// 	this.block.classList.remove('marked')
	// }
	// placeFood() {
	// 	this.food = true
	// 	this.block.classList.add('food')
	// }

	// eatFood() {
	// 	this.food = false
	// 	this.block.classList.remove('food')
	// }
}
