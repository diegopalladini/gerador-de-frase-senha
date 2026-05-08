function atualizarCombinacoes() {
    const slider = document.getElementById('quantidade');
    const spanContador = document.getElementById('contador-combinacoes');
    
    // Se por algum motivo o elemento não existir na página, não faz nada
    if (!slider || !spanContador) return;

    const qtd = slider.value;
    let texto = "";

    if (qtd == 3) {
        texto = "457 Bilhões de combinações. Equivalente a uma senha complexa de 8 caracteres sem símbolos.";
    } else if (qtd == 4) {
        texto = "3,5 Quadrilhões de combinações. Equivalente a uma senha complexa de 8 caracteres com símbolos.";
    } else if (qtd == 5) {
        texto = "27 Quintilhões de combinações. 4,5 vezes mais forte do que uma senha complexa de 8 caracteres com símbolos.";
    } else if (qtd == 6) {
        texto = "210 Sextilhões de combinações. 35.000 vezes mais forte do que uma senha complexa de 8 caracteres com símbolos.";
    } else if (qtd == 7) {
        texto = "1,6 Setilhões de combinações. 260 milhões de vezes mais forte do que uma senha de 8 caracteres com símbolos.";
    } else if (qtd == 8) {
        texto = "12,5 Octilhões de combinações. Nível de segurança inquebrável por milênios.";
    }

    spanContador.innerText = texto;
}

// Garante que o contador apareça assim que a página carregar
document.addEventListener('DOMContentLoaded', atualizarCombinacoes);