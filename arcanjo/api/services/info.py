from ..models import Session, PatientSymptom, Patient
from datetime import datetime
from django.forms.models import model_to_dict


def checkin(session_id=None, post=False):
    if session_id:
        try:
            session = Session.objects.get(id=int(session_id))
            if post:
                session.ts_checkin = datetime.now()
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
        
    else:
        open_sessions = Session.objects.all().filter(ts_consultation_end=None)
        print(open_sessions)
        res = []
        for open_session in open_sessions:
            patient_symptoms = PatientSymptom.objects.all().filter(session=open_session)
            patient = patient_symptoms[0].patient
            one_res = {
                'symptoms': patient_symptoms.values(),
                'patient': model_to_dict(patient)
            }
            if open_session.ts_checkin:
                res.append(one_res)

        return res