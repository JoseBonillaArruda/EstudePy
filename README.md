# FaculPy
Projeto de Python de Organização Estudantil


Calendário acadêmico - Organizador de Disciplinas, Períodos escolares, Acompanhamento de carga horaria e notas


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




























