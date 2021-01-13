from ..models import Session, PatientSymptom, Patient
from datetime import datetime
from django.forms.models import model_to_dict
from ..utils.bot import BotUtils


def consultation(session_id, start):
    try:
        session = Session.objects.get(id=int(session_id))
        if start:
            session.ts_consultation_start = datetime.now()

            patient_symptoms = PatientSymptom.objects.all().filter(session=session)
            patient = patient_symptoms[0].patient
            res = {
                'patient': model_to_dict(patient),
                'patient_symptoms': patient_symptoms.values(),
                'guardian': session.guardian_name
            }
        
        else:
            session.ts_consultation_end = datetime.now()
            bot = BotUtils()
            message = 'Não se esqueça de marcar sua consulta pós alta! Segue o número de telefone para agilizar essa marcação: 21 993986258'
            bot.send_message(message, session.phone_number, None)
            res = 'Sent confirmation'
            
        session.save()

        return res

    except Exception as e:
        print(e)
        return 'Id not found'