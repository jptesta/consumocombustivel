

function calcular(){
    var valor1 = parseInt(document.getElementById('km').value);
    var valor2 = parseInt(document.getElementById('tanque').value);
    var valor3 = parseInt(document.getElementById('vlrpl').value);
    var valor4 = parseInt(document.getElementById('media').value);
    document.getElementById('media').value = valor1 / valor2;
    document.getElementById('totalcombustivel').value = valor3 * valor2;
    document.getElementById('vlrpkm').value = valor3 / valor4 ;
}

