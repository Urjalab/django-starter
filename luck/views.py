from django.shortcuts import render
import random
def guess_luck(request):

    guess = random.randint(3,6)
    user_guess = 4
    luck = False
    if user_guess == guess:
        luck = True
    context = {
        'result': luck
    }
    return render(
        request,
        'luck/index.html',
        context
    )