Criei um flask aqui que simula o que é necessário para a comunicação. Nesse caso não tem botões, só as rotas mesmo.


http://127.0.0.1:5000/record
action: "start" para começar a gravar. "stop" para parar
is_audio_only: boolean. Para gravar só o audio.
phone_number: numero de telefone para o qual sera feita a ligação
meet_url: link do meet para começar um meet

if is_audio_only = true: é necessário passar o numero de telefone pois sera feita uma chamada telefonica.
if is_audio_only = false: é necessario passar o meet_url, pois sera feito um meet.

vale lembrar que no futuro, para começar as gravações, será utilizado a rota /record, mas para parar a gravação, sera feita: ou desligando a ligação, ou fechando o meet aberto. Mas para essa versão linux é necessário utilizar esta mesma rota para parar a gravação 