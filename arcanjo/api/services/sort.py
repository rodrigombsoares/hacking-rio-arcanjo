from ..models import Session, PatientSymptom, Patient
from datetime import datetime
from django.forms.models import model_to_dict


def sort_start(session_id=None):
    try:
        session = Session.objects.get(id=int(session_id))
        session.ts_sorting = datetime.now()
        session.save()

        patient_symptoms = PatientSymptom.objects.all().filter(session=session)
        patient = patient_symptoms[0].patient
        res = {
            'patient': model_to_dict(patient),
            'patient_symptoms': patient_symptoms.values(),
            'guardian': session.guardian_name
        }

        return res

    except Exception as e:
        print(e)
        return 'Id not found'