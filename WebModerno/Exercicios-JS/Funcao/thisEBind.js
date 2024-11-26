const pessoa = {
    saudacao: 'Bom dia"',
    falar() {
        console.log(this.saudacao)
    }
}

pessoa.falar()
const falar = pessoa.falar
falar() //conflito entre paradigmas: funcional e 00

// bind amarra objeto a uma variável
const falarDePessoa = pessoa.falar.bind(pessoa)
falarDePessoa()

