from datetime import date, datetime

def age_processor(request):
    if request.user.is_authenticated:
        fecha_nacimiento = request.user.birthday
        if fecha_nacimiento:
            birthdate = datetime.strptime(str(fecha_nacimiento), '%Y-%m-%d')
            edad = datetime.now().year - birthdate.year
            return {'edad': edad}
    return {'edad': None}





