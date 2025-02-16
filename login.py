import customtkinter as ctk

# configuração-aparência
ctk.set_appearance_mode('dark')

#criação das funções
def validar_login():
    usuario= campo_usuario.get()
    senha= campo_senha.get()
    #validar se o usuario é 12334567890 e a senha 1234
    if usuario == '1234567890' and senha == '1234':
        resultado_login.configure(text='login feito com sucesso', text_color='green')
    else:
        resultado_login.configure(text='tente novamente', text_color='red')




#criação-de-janela-principal
api=ctk.CTk()
api.title('Sistema bancário')
api.geometry('300x300')



#criação-de-campos


#label
label_usuario=ctk.CTkLabel(api, text='CPF/CNPJ')
label_usuario.pack(pady=10)

#entry
campo_usuario=ctk.CTkEntry(api, placeholder_text='Digite o CPF', show='*')
campo_usuario.pack(pady=10)

#label
label_senha=ctk.CTkLabel(api, text='senha')
label_senha.pack(pady=10)

#entry 
campo_senha=ctk.CTkEntry(api, placeholder_text='Digite a senha', show='*')
campo_senha.pack(pady=10)

#button
botao_login=ctk.CTkButton(api,text='login',command=validar_login )
botao_login.pack(pady=10)
# feedback
resultado_login=ctk.CTkLabel(api, text='')
resultado_login.pack(pady=10)

#iniciar o loop de aplicação
api.mainloop()



