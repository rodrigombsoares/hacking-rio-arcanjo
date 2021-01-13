# Arcanjo - 2019
## Time 6 / Saúde
### Apresentação 

Quando se precisa levar uma criança à emergência hoje no Rio de Janeiro, além de todo o transporte e dificuldades para se encontrar os hospitais mais proximos e vazios, é necessário passar por um processo de check-in e triagem muitas vezes demorado que podem colocar uma vida em risco dependendo do grau da emergência. Além disso, mais de 50% dos casos atendidos na emergência não são casos emergenciais que poderiam estar sendo atendidos de outra forma, aumentando a fila para o atendimento e prolongando o tempo de espera. Outro fator que torna esse processo mais demorado é a realização do check-in  de maneira manual e previamente a triagem hospitalar, logo a criança que pode esta passando por um sério caso emergencial passa por um sério risco dado a espera prolongada. E os pais e responsáveis por essa criança passam por um transtorno maior do que o necessário, dada a ineficência do processo. 

### O Produto


#### Jornada do Usuário
<p align="center">
  <img src = "https://github.com/hackingrio/saude-2019-arcanjo/blob/master/docs/jornada-usuario.jpg?raw=true">
</p>


O Arcanjo é um bot de WhatsApp capaz de agilizar diversos processos durante o procedimento de atendimento de uma criança em uma emergência pediátrica. Com a nossa solução, quando o responsável pela criança decide levá-la até o hospital, durante o caminho de ida ele pode realizar uma pré triagem da criança, onde ele informa ao bot os diferentes sintomas que ela está sentindo. Por meio de algoritmos de Inteligência Artificial, o bot consegue classificar esses sintomas entre caso 'Urgente' ou caso 'Não Urgente', e já monta uma fila de atendimento de triagem após ser realizado o check-in. Esse processo dá mais transparência ao responsável do tempo de espera dentro do hospital além de possibilitar que ele tenha uma estimativa da sua posição na lista de espera para atendimento na triagem.

Após realizar esse procedimento, o bot, com conhecimento dos principais sintomas do paciente é capaz de sugerir hospitais próximos que possuem a especialidade necessária para tratar a criança, mostrando o tempo de espera de cada um. Além disso, tendo conhecimento da gravidade do caso do paciente o bot pode sugerir a realização de uma consulta caso identifique que o caso da criança não é tão grave. Isso auxilia na resolução de uma situação bastante comum de acontecer em serviços emergenciais para crianças, 70% das crianças que são atendidas na emergência não possuem um caso realmente urgente, o que é prejudicial a todas as crianças que realmente possuem estado urgente e estão na emergência. 

Depois disso, o responsável prossegue para a fase de check-in prévio à chegada no hospital, pedindo algumas documentações necessárias para atendimento, o que também permite agilizar o tempo de espera para check-in dentro do hospital, recebendo um QR Code para identificação quando chegar no hospital. Por meio desse QR Code, se é possível ter controle de todas as informações do paciente, podendo elas serem transmitidas desde o momento da informação dos sintomas na pré triagem, até o momento pós atendimento. Além disso, a utilização permite o controle do tempo de permanência do usuário dentro do hospital, possibilitando a medição do tempo de espera médio e um controle da produtividade dentro do hospital.

Após o atendimento, o bot manda uma mensagem de acompanhamento, onde ele sugere a marcação de consulta para a realização de exames de acompanhamento, garantindo o retorno do usuário ao hospital e minimizando a chance de reincidência na emergência.

#### Infraestrutura da Aplicação
<p align="center">
  <img src = "https://github.com/hackingrio/saude-2019-arcanjo/blob/master/docs/twil.png?raw=true">
</p>

### Informações adicionais 


##### RoadMap
<p align="center">
  <img src = "https://github.com/hackingrio/saude-2019-arcanjo/blob/master/docs/roadmap.jpg?raw=true">
</p>
