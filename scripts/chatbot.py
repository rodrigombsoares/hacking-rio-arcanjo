greeting_text = """
    Olá, me parece que você está passando
    por uma emergência. Informe os sintomas que 
    a criança está sentindo.
"""
receiveText()

after_triagem_warning = """
    Tem certeza que sua situação é uma emergência? Caso nao seja,
    e possivel marcar uma consulta pelo numero 21 993896258. Caso ainda
    queira ir a emergencia, digite Sim.
"""
receiveOption()
# case yes:

#     want_call = """
#         O número de telefone a ser ligado é:
#         21 993896258
#     """

after_triagem_hospitals = """
    Baseado nos sintomas apresentados, segue uma lista
    de hospitais mais próximos junto com os tempos
    estimados de espera que possuem os médicos que
    podem te auxiliar:
"""
showHospitalList()

check_in_text = """
    Para agilizarmos seu processo no hospital precisamos
    de algums informações.
"""

ask_name = "Qual o nome do responsável pela criança?"
receiveName()

ask_name_kid = "Qual o nome da criança?"
receiveKidName()

ask_CPF_kid = "Qual o CPF da criança?"
receiveKidCPF()

ask_number = "Qual o número do seguro-saúde?"
receiveKidNumber()

after_check_in -= """
    Pronto! Ao chegar no hospital apresente o
    QR Code abaixo na recepção, que seu check-
    in será concluído.
"""
sendQRCode()

after_consultation = """
    Não se esqueça de marcar
    sua consulta pós alta! Segue o número de 
    telefone para agilizar essa marcação:
    21 993986258
"""

goodbye = "Obrigado!"

