from formula1.models import Constructor


def constructors(request):
    return {'constructors': Constructor.objects.all()}


"""def circuits(request):
    return {'circuits': Circuit.objects.all()}"""