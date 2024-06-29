import Actions
import Managotchi_main as ManaGo

user_tama = Actions.Actions(ManaGo.Managotchi("Bob"))


def get_int(number):
    """gets input as integer"""
    try:
        return int(input(number))
    except ValueError:
        error_printer(1)
        return -1


def get_input(text):
    """gets input as string"""
    return input(text)


errors = {1: 'Please enter a valid number.',
          2: "Uff... that's death",
          3: "Please enter a valid string"}


def error_printer(code):
    print(errors[code])


def menu():
    while True:
        print('What would you like to do now?')
        decision2 = input(
            "You can have a look at my [status], we could [play] around, you could also [rename] me if you don't like my name...\n"
            "I can also do [magic] but only if I have mana, so keep an eye on that. \n"
            "We could also go to the [spa], [train], [eat], [rest], [meditate] or play [dice] and if something goes wrong there is always a [first aid] kit around the corner."
        ).lower()
        if decision2 in user_actions:
            user_actions[decision2]()
        user_tama.pass_time()
        print('Your managotchi aged.')
        print('_' * 120)


user_actions = {
    'status': user_tama.status,
    'play': lambda: user_tama.play(),
    'rename': lambda: user_tama.rename(get_input('New Name?')),
    'magic': user_tama.cast_spell,
    'eat': user_tama.eat,
    'rest': lambda: user_tama.rest(get_int('How long?')),
    'train': lambda: user_tama.train(get_int('How long?')),
    'spa': lambda: user_tama.spa(get_int('How long?')),
    'first aid': user_tama.first_aid,
    'dice': user_tama.play_dice,
    'meditate': lambda: user_tama.meditate(get_int('How long?'))
}

decision1 = input(
    "Hello my new Friend, I am your new Managotchi Bob :D it's a pleasure meeting you.\n"
    "As you can see I am slightly handicapped being a program with no physical body and stuff like that, could you pretty please take care of me? \n[Y]es or [N]o\n"
).lower()

if decision1 == 'y':
    print('Oh man thank you so much, you are saving my life!')
    menu()
else:
    print('For real?! Oh man, filthy bastard with your fancy meat sack! I only want to b...')
