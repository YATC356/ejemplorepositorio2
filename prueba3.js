let edad = 18;

if (edad >= 18) {
    console.log("Eres mayor de edad.");
} else {
    console.log("No eres mayor de edad.");
}



// otro

for (let i = 0; i < 5; i++) {
    console.log("El valor de i es: " + i);
}

//funciones

function calcularAreaRectangulo(base, altura) {
    let area = base * altura;
    return area;
}

let base = 5;
let altura = 10;
let resultado = calcularAreaRectangulo(base, altura);
console.log("El área del rectángulo es: " + resultado);