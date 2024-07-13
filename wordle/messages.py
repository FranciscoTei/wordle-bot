from json import dumps
START_TEXT:str = ""

CHUTES_DICT: dict = {
    1: ["chute1", "⬛️⬛️⬛️⬛️⬛️"],
    2: ["chute2", "⬛️⬛️⬛️⬛️⬛️"],
    3: ["chute3", "⬛️⬛️⬛️⬛️⬛️"],
    4: ["chute4", "⬛️⬛️⬛️⬛️⬛️"],
    5: ["chute5", "⬛️⬛️⬛️⬛️⬛️"],
    6: ["chute6", "⬛️⬛️⬛️⬛️⬛️"],
}

CHUTES = dumps(CHUTES_DICT)


CHUTE_INVALIDO: str = "A palavra deve conter 5 letras."

REGRAS = """<b>WORDLE </b>🔤<b>
</b>
📌 <b>Objeto do jogo:</b>

<code>Acertar a sequência de letras, formando a palavra antes determinada pelo bot.</code>

<b>🤓 Como jogar:</b>

• Inicialmente,o jogador deverá mandar /chute 'seu chute aqui' no privado do bot e enviar uma palavra de 5 letras.

○ <b>Palavra enviada:</b> Após o jogador ter enviado a palavra, o bot irá dizer quais letras pertencem a palavra misteriosa e quais letras estão no lugar certo daquela palavra.

<code>🟥 Letras incorretas, não tem na palavra.
🟨 Letras corretas, porém na posição errada.
🟩 Letras corretas e no local certo.</code>

○ <b>Novo chute:</b> Após o bot ter enviado a &quot;correção&quot; das letras, o jogador irá chutar uma nova palavra seguindo as dicas que ele obteve na primeira rodada.

• O jogador terá <b>seis tentativas</b> para adivinhar a palavra misteriosa, tendo a chance de ganhar mais pontos quanto menos chutes forem dados.

• Após o jogador acertar a palavra misteriosa ou esgotar as seis tentativas o jogador só poderá jogar novamente no dia seguinte.

<b>💰 Pontuação:</b>

<code>Um chute – 6 pontos
Dois chutes – 5 pontos
Três chutes – 4 pontos 
Quatro chutes – 3 pontos
Cinco chutes – 2 pontos
Seis chutes – 1 ponto</code>"""

keyboard_layout = """   🅀🅆🄴🅁🅃🅈🅄🄸🄾🄿
     🄰🅂🄳🄵🄶🄷🄹🄺🄻
         🅉🅇🄲🅅🄱🄽🄼"""

keyboard = {
    'Q': '🅀🆀', 'W': '🅆🆆', 'E': '🄴🅴', 'R': '🅁🆁', 'T': '🅃🆃', 'Y': '🅈🆈', 'U': '🅄🆄', 'I': '🄸🅸', 'O': '🄾🅾', 'P': '🄿🅿', 
    'A': '🄰🅰', 'S': '🅂🆂', 'D': '🄳🅳', 'F': '🄵🅵', 'G': '🄶🅶', 'H': '🄷🅷', 'J': '🄹🅹', 'K': '🄺🅺', 'L': '🄻🅻', 
    'Z': '🅉🆉', 'X': '🅇🆇', 'C': '🄲🅲', 'V': '🅅🆅', 'B': '🄱🅱', 'N': '🄽🅽', 'M': '🄼🅼'
}

keyboard_dict = {
    'Q': '🅀🅠', 'W': '🅆🅦', 'E': '🄴🅔', 'R': '🅁🅡', 'T': '🅃🅣', 'Y': '🅈🅨', 'U': '🅄🅤', 'I': '🄸🅘', 'O': '🄾🅞', 'P': '🄿🅟', 
    'A': '🄰🅐', 'S': '🅂🅢', 'D': '🄳🅓', 'F': '🄵🅕', 'G': '🄶🅖', 'H': '🄷🅗', 'J': '🄹🅙', 'K': '🄺🅚', 'L': '🄻🅛', 
    'Z': '🅉🅩', 'X': '🅇🅧', 'C': '🄲🅒', 'V': '🅅🅥', 'B': '🄱🅑', 'N': '🄽🅝', 'M': '🄼🅜'
}