from wordle.client import wordle_bot
from wordle.plugins.wordle import wordle_jogo
from wordle.messages import REGRAS
from pyrogram import filters, Client
from unidecode import unidecode


@wordle_bot.on_message(filters.command("regras"))
def comando_regras(client, message):
    wordle_bot.send_message(message.chat.id, REGRAS)


@wordle_bot.on_message(filters.command("ranking"))
def comando_regras(client, message):
    ranking = wordle_jogo.get_ranking()
    for score in ranking:
        print(score.user.name, score.pontos)
    wordle_bot.send_message(message.chat.id, REGRAS)


@wordle_bot.on_message(filters.command("perfil"))
def comando_perfil(client, message):
    usuario = wordle_jogo.get_user(message.from_user)
    if not usuario:
        usuario = wordle_jogo.create_user(message.from_user)
        usuario.save()
    score = usuario.score.get()
    position = wordle_jogo.get_position(score.pontos)

    perfil = f"""
<b>📍 Estes são seus dados pessoais:</b>

<b>Nome:</b> {usuario.name}
<b>Data de cadastro:</b> {usuario.created_at.strftime('%Y-%m-%d %H:%M:%S')}
<b>Tentativas:</b> {score.jogos}
<b>Acertos:</b> {score.vencidos}
<b>Falhas:</b> {score.perdidos}
<b>Desistências:</b> {score.desistencias}
<b>Pontuação:</b> {score.pontos}
<b>Posição:</b> {position}°"""
    wordle_bot.send_message(message.chat.id, perfil)


@wordle_bot.on_message(filters.private | filters.command("chute"))
def comando_nova_palavra(client, message):
    message.text = message.text.replace("/chute", '').strip()
    response = wordle_jogo.validate_guess(message.text)
    if not message.text:
        return
    if response['validate']:
        user = message.from_user
        if not wordle_jogo.check_new_user(user):
            wordle_jogo.create_user(user)

            wordle_bot.send_message(message.chat.id, 'Novo usuário cadastrado.\n\nPara ver seu perfil use /perfil.')
            wordle_bot.send_message(message.chat.id, 'Verificando palavra chutada.')

        response_guess = wordle_jogo.response_guess(user, unidecode(message.text.upper()))

        for response in response_guess:
            message.reply_text(response)
    elif not response['validate']:
        wordle_bot.send_message(message.chat.id, response['detail'])


