# EstudePy
Nome do projeto: EstudePy


Calendário acadêmico - Organizador de Disciplinas, Períodos escolares, Acompanhamento de carga horaria e notas


 O EstudePy tem como objetivo oferecer aos estudantes uma ferramenta para organizar
 sua vida acadêmica e acompanhar seu desempenho ao longo do semestre.
 O EstudePy permite o gerenciamento de disciplinas, controle de frequência, registro de
 avaliações, calculo da média, anotações das disciplinas, além do agendamento de
 eventos escolares importantes.
 O Público-alvo são estudantes do ensino médio e até Universitários, que buscam uma
 forma eficiente de administrar seu tempo e manter o controle sobre a sua rotina de
 estudante.
 O problema que pretendemos resolver com o EstudePy é a dificuldade que muitos
 estudantes enfrentam em acompanhar as aulas, prazos, notas e faltas especialmente
 aqueles que estudam em uma escola que não oferece um sistema de organização e
 acompanhamento de suas notas.
 Usaremos Python para implentação do projeto, o armazenamento do banco de dados
 será local para que assim, a aplicação necessite de conexão a internet para funcionar, o
 software será o mais claro possível para que mesmo usuários leigos posam usufruir do
 software e terá a opções de tema claro ou escuro para conforto visual.


Requisitos funcionais
- O usuário deve ser capaz de registrar disciplinas com carga horaria, local de aula, dia(s) da semana e hora de aula
- ser capaz de marcar presença e registrar percentual máximo de falta que ele pode ter
- registrar avaliações e notas ligadas a disciplina
-visualização da carga horaria semanal
- escolher entre formas comuns de calculo de média para visualização de média final
- ter um espaço de anotações ligadas à disciplinas
-cadastrar eventos importantes e ter alguma notificação sobre
- registrar começo e fim de semestre




Requisitos não funcionais
- Interface Simples, Funcionalidades visíveis e de fácil acesso, auto explicativas
- Mínimo uso de janelas de interrupção/alertas (janelas pop-up)
- Opções dia/noite para conforto visual


Restrições
-Código em Python
-sistema local, sem integração



Banco de dados:
- Semestre\Ano
	-Categoria que enlaça todas as informações, usuário registra novo semestre/ano
	-Data de inicio\fim
	
	- Disciplina
		-Contem carga horaria, media, faltas, local e horário
		-Anotações relacionadas a disciplina

		-Nota
			-Contem tipo de media(aritmética, ponderada, nota mínima de PF) e as notas individuais

-Notas não relacionadas
	-Notificação (Opcional)
	
-Eventos 
	-Data e hora
	- Notificação (Opcional)




























