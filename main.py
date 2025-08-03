import customtkinter as ctk

class MyFrame(ctk.CTkFrame):
    """
    Um frame reutilizável que agora usa o layout .grid() para posicionar os widgets.
    """
    def __init__(self, master, button_command, option_command, **kwargs):
        super().__init__(master, **kwargs)

        # --- MUDANÇA PRINCIPAL: De .pack() para .grid() ---

        # 1. Posiciona o OptionMenu na primeira linha (0) e primeira coluna (0)
        # sticky="w" alinha o widget à esquerda (West)
        self.optionmenu = ctk.CTkOptionMenu(self, 
                                            values=["Opção 1", "Opção 2"],
                                            command=option_command)
        self.optionmenu.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")
        self.optionmenu.set("Opção 2")

        # 2. Posiciona o Botão na segunda linha (1), abaixo do OptionMenu
        self.button = ctk.CTkButton(self, 
                                    text="Clique Aqui", 
                                    command=button_command)
        self.button.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")

        # 3. Posiciona o Botão 
        self.button = ctk.CTkButton(self, 
                                    text="Clique Aqui", 
                                    command=button_command)
        self.button.grid(row=1, column=3, padx=20, pady=(0, 20), sticky="w")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # --- Paleta de Cores (Paleta 1) ---
        self.COR_FUNDO_PRINCIPAL = "#F0F2F5"
        self.COR_FUNDO_SECUNDARIO = "#FFFFFF"
        self.COR_TEXTO_BOTAO = "#FFFFFF"
        self.COR_DESTAQUE_BOTAO = "#007BFF"
        
        # --- Configuração da Janela ---
        self.title("Layout com .grid()")
        self.geometry("1600x700")
        self.configure(fg_color=self.COR_FUNDO_PRINCIPAL)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # --- Criação do Frame ---
        self.my_frame = MyFrame(master=self,
                                button_command=self.button_callback,
                                option_command=self.optionmenu_callback,
                                fg_color=self.COR_FUNDO_SECUNDARIO)
        
        # Aplicando cores customizadas nos widgets dentro do frame
        self.my_frame.button.configure(fg_color=self.COR_DESTAQUE_BOTAO, 
                                       text_color=self.COR_TEXTO_BOTAO)
        self.my_frame.optionmenu.configure(fg_color=self.COR_DESTAQUE_BOTAO, 
                                            button_color=self.COR_DESTAQUE_BOTAO,
                                            text_color=self.COR_TEXTO_BOTAO)

        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    # --- Funções de Callback ---
    def button_callback(self):
        print("Botão foi clicado!")

    def optionmenu_callback(self, choice):
        print("Opção selecionada:", choice)


if __name__ == "__main__":
    app = App()
    app.mainloop()