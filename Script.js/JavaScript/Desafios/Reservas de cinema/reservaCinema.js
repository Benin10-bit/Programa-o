class Cinema {
    constructor(rows, seatsPerRow) {
        this.seats = Array.from({ length: rows }, () =>
            Array.from({ length: seatsPerRow }, () => false)
        );
    }

    displaySeats() {
        console.log("Status das Cadeiras:");
        this.seats.forEach((row, rowIndex) => {
            console.log(`Fila ${rowIndex + 1}: ${row.map(seat => (seat ? "[X]" : "[ ]")).join(" ")}`);
        });
    }

    reserveSeat(row, seat) {
        if (row < 0 || row >= this.seats.length || seat < 0 || seat >= this.seats[row].length) {
            console.log("Erro: Assento inválido!");
            return;
        }

        if (this.seats[row][seat]) {
            console.log("Essa cadeira já está ocupada!");
        } else {
            this.seats[row][seat] = true;
            console.log("Cadeira reservada com sucesso!");
        }
    }

    releaseSeat(row, seat) {
        if (row < 0 || row >= this.seats.length || seat < 0 || seat >= this.seats[row].length) {
            console.log("Erro: Assento inválido!");
            return;
        }

        if (!this.seats[row][seat]) {
            console.log("Essa cadeira já está livre!");
        } else {
            this.seats[row][seat] = false;
            console.log("Reserva cancelada, cadeira agora está livre!");
        }
    }
}
