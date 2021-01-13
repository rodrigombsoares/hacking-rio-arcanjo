from ..models import Session, Message, Patient, PatientSymptom
from datetime import datetime, timedelta
from ..utils.nlp import TextProcessor
from ..utils.qrcode import get_qrcode
from ..utils.bot import BotUtils
from time import sleep


def handle_message(message):
    from_ = message['From']
    body  = message['Body']
    msid = message['MessageSid']
    session = get_session(from_)
    step = get_step(session)
    prepare_next_step(step, body, from_, msid, session)


def get_session(income_phone):
    open_sessions = Session.objects.all().filter(
        ts_consultation_end = None,
        phone_number = income_phone
    )

    if open_sessions:
        open_session = open_sessions[0]
    else:
        open_session = None

    # open_session = []
    # for raw_session in raw_sessions:
    #     if datetime.now() - raw_session.ts_checkin < timedelta(1):
    #         open_sessions.append(raw_session)

    return open_session


def get_step(session):
    if session:
        messages = Message.objects.all().filter(session=session).order_by('-step')
        if messages:
            last_message = messages[0]
            return last_message.step + 1
    return 0 


def prepare_next_step(curr_step, body, income_phone, msid, session):
    is_urgent = False
    qrcode = None

    if curr_step == 0 or session == None:
        # Create next session
        session = Session(phone_number = income_phone)
        session.save()
        session = Session.objects.get(id=session.id)
        
    if curr_step == 1:
        processor = TextProcessor()
        symptoms_list = ['dor de cabeca', 'febre']
        for symtom in symptoms_list:
            patient_symptom = PatientSymptom(session=session, symptom=symtom)
            patient_symptom.save()
        
        is_urgent = processor.is_urgent(str(body))

    if curr_step == 2:
        session.guardian_name = str(body)
        session.save()

    if curr_step == 3:
        children_cpf = str(body)
        patient = Patient(cpf=children_cpf)
        patient.save()

        patient_symptoms = PatientSymptom.objects.all().filter(session=session)
        for patient_symptom in patient_symptoms:
            patient_symptom.patient = patient
            patient_symptom.save()

    if curr_step == 4:
        children_name = str(body)
        patient_symptom = PatientSymptom.objects.all().filter(session=session)[0]
        patient = patient_symptom.patient
        patient.name = children_name
        patient.save()

    if curr_step == 5:
        insurance_number = str(body)
        patient_symptom = PatientSymptom.objects.all().filter(session=session)[0]
        patient = patient_symptom.patient
        patient.insurance_number = insurance_number
        patient.save()
        qrcode = get_qrcode(session.id)

    # Create message
    message = Message(
        session = session,
        text = body,
        sid = msid,
        step = curr_step
    )
    message.save()

    print('Mom:', body)
    choose_answer(curr_step, is_urgent, qrcode, income_phone)


def choose_answer(step, is_urgent, qrcode, income_phone):
    media = qrcode

    if step == 0:
        messages = ['Olá, me parece que você está passando por uma emergência. Informe os sintomas que a criança está sentindo.']

    if step == 1: 
        message_p0 = "Aqui estão os hospitais mais próximos que possuem os médicos que podem te auxiliar e seus tempos estimados de espera: \n\n Hospital Quinta D'or - 2.7 km - Tempo de espera: 20 min \n Hospital Copa D'or - 10 km - Tempo de espera: 10 min \n Hospital Rios D'or - 24 km - Tempo de espera : 40 min"
        message_p1 = 'Para agilizarmos seu processo no hospital precisamos de algumas informações.'
        message_p3 = 'Primeiro, qual o nome do responsável pela criança?'
        
        if is_urgent:
            messages = [message_p0, message_p1, message_p3]
        if not is_urgent:
            message_p2 = 'Tem certeza que sua situação é uma emergência? Caso não seja, é possível marcar uma consulta pelo numero 21-993896258. Caso ainda queira ir a emergência, vamos precisar de algumas informações.'
            messages = [message_p0, message_p2, message_p3]
    
    if step == 2:
        messages = ['Qual é o CPF da criança?']
    
    if step == 3:
        messages = ['Qual é o nome da criança?']
    
    if step == 4:
        messages = ['Qual é o número do seguro-saúde?']
    
    if step == 5:
        messages = ['Pronto! Ao chegar no hospital apresente o QR Code acima na recepção, e seu check-in será concluído. \n*Atenção*: O QR Code só estará válido por um dia. Após isso ele será invalidado.']

    else:
        message = 'Desculpe, não entendi.'
    
    send_messages(messages, income_phone, media)


def send_messages(message_list, income_phone, media):
    bot_client = BotUtils()

    for message in message_list:
        bot_client.send_message(message, income_phone, media)
        sleep(0.5)
