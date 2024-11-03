import tkinter as tk
from tkinter import messagebox

class Programaquiz:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz em Tkinter")
        self.perguntas = [
            {
                "pergunta": "1) Qual é o comando que solicita a entrada para o usuário?",
                "opcoes": ["format()", "print()", "input()", "round()"],
                "correta": "input()"
            },
            {
                "pergunta": " 2) Onde armazenamos valores em um programa?",
                "opcoes": ["Relação", "Armazenador", "Pandas", "Variavel"],
                "correta": "Variavel"
            },
            {
                "pergunta": "3) Como é conhecida a chave primaria?",
                "opcoes": ["FP", "FK", "CP", "PK"],
                "correta": "PK"
            },
            {
                "pergunta": "6) O que é 'G' em GUT?",
                "opcoes": ["Gestão", "Gastos", "Gravidade", "Variavel"],
                "correta": "Gravidade"
            }
        ]
        self.pergunta_atual = 0
        self.pontuacao = 0

        self.rotulo_pergunta = tk.Label(self.master, text="", font=("Arial", 14))
        self.rotulo_pergunta.pack(pady=10)

        self.variavel_opcao = tk.StringVar()
        self.botoes_opcao = []
        for i in range(4):
            botao_opcao = tk.Radiobutton(self.master, text="", font=("Arial", 12), variable=self.variavel_opcao, value="", command=self.atualizar_resposta)
            botao_opcao.pack()
            self.botoes_opcao.append(botao_opcao)

        self.botao_enviar = tk.Button(self.master, text="Enviar Resposta", font=("Arial", 12), command=self.verificar_resposta)
        self.botao_enviar.pack(pady=10)
        self.rotulo_resultado = tk.Label(self.master, text="", font=("Arial", 12))
        self.rotulo_resultado.pack()

        self.proxima_pergunta()

    def proxima_pergunta(self):
        if self.pergunta_atual < len(self.perguntas):
            dados_pergunta = self.perguntas[self.pergunta_atual]
            self.rotulo_pergunta.config(text=dados_pergunta["pergunta"])
            opcoes = dados_pergunta["opcoes"]
            for i in range(4):
                self.botoes_opcao[i].config(text=opcoes[i], value=opcoes[i])
            self.variavel_opcao.set("")
        else:
            self.rotulo_pergunta.config(text="Fim do Quiz. Pontuação: {}/{}".format(self.pontuacao, len(self.perguntas)))
            self.botao_enviar.config(state=tk.DISABLED)
            for botao in self.botoes_opcao:
                botao.config(state=tk.DISABLED)

    def atualizar_resposta(self):
        self.opcao_selecionada = self.variavel_opcao.get()

    def verificar_resposta(self):
        dados_pergunta = self.perguntas[self.pergunta_atual]
        resposta_correta = dados_pergunta["correta"]
        if self.opcao_selecionada == resposta_correta:
            self.pontuacao += 1
            self.rotulo_resultado.config(text="Resposta correta!", fg="green")
        else:
            self.rotulo_resultado.config(text="Resposta incorreta! A resposta correta era: {}".format(resposta_correta), fg="red")
        self.pergunta_atual += 1
        self.proxima_pergunta()

if __name__ == "__main__":
    root = tk.Tk()
    app = Programaquiz(root)
    root.mainloop()