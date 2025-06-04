from django.shortcuts import render

def menu(request):
    teste = 123
    teste2 = 321
    teste3 = (teste) + (teste2)

    context = {
        'teste4': teste3,
        'teste': teste2,
    }

    return render(request, 'game/menu.html', context)

def game(request):

    
    return render(request, 'game/game.html')

