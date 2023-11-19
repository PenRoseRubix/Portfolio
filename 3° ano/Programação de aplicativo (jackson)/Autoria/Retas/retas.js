function ponto(x, y){
    var ponto = {x:x, y:y}
    return ponto
}
function reta(a,b){
    var coeficienteAngular = (b.y-a.y)/(b.x-a.x)
    var coeficienteLinear = (a.x*(-1*coeficienteAngular))+a.y
    if (Math.sign(coeficienteLinear) == -1){
        var formula = `y = ${coeficienteAngular}x${coeficienteLinear}`
    }else if(Math.sign(coeficienteLinear)== 1) {
        var formula = `y = ${coeficienteAngular}x+${coeficienteLinear}`
    }else{
        var formula = `y = ${coeficienteAngular}x`
    }

    var reta = {
        coeficienteAngular: coeficienteAngular,
        coeficienteLinear:coeficienteLinear,
        formula:formula
    }
    return reta 
}
function mediana(a,b){
   return ponto((a.x+ b.x)/2, (a.y+b.y)/2)
}
function seAlinhados(a,b,c){
    if (((a.x*b.y)+(a.y*c.x)+(b.x*c.y))-((b.y*c.x)+(a.y*b.x)+(a.x*c.y)) == 0 ){
        return true
    }
    return false
}
function distancia (a,b){
    return Math.sqrt((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y))
}
function getXof(reta,y){
    var x = (y - reta.coeficienteLinear)/reta.coeficienteAngular
    return x
}
function getYof(reta,x){
    var y = reta.coeficienteAngular*x + reta.coeficienteLinear
    return y
}
var pontoA = ponto(3,5)
var pontoB = ponto(2,3)
var pontoC = mediana(pontoA,pontoB)
var retaAB = reta(pontoA,pontoB)
var retaBC = reta(pontoB,pontoC)
var retaAC = reta(pontoA,pontoC)
console.log(seAlinhados(pontoA,pontoB,pontoC))
console.log(pontoA,pontoB,pontoC)
console.log(retaAB,retaBC,retaAC)
console.log(distancia(pontoA,pontoB))
console.log(getXof(retaAB,6))
console.log(getYof(retaAB,2))