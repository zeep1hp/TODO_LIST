import json

def  lecture():
    with open("todo.json", "r") as f:
        x= json.load(f)
        return x 
def sauvegarde():
    with open("todo.json","w") as f:
        json.dump(todo, f)

todo = lecture()

def ecrire_ue_notes():
    a = input("entre le nom d'une note\n==>")
    b = input("entre ta note\n==>")
    z={'nom':a,'notes':b}
    todo.append(z)
    sauvegarde()
    return True

def afficher_ue_notes():
    for element in todo:
        print(f"nom note: {element['nom']}")
    print("Entre le nom de la note que souhaite consulter")
    x=input("==>")
    for element in todo:
        if x == element['nom']:
            print(f"voici la note {element['nom']}:")
            print(element['notes'])
    return True

def supp_note():
    for element in todo:
        print(f"nom note: {element['nom']}")
    print("Entre le nom de la note que tu souhaite supprimer")
    x=input("==>")
    for element in todo:
        
        if x == element['nom']:
            todo.remove(element)
            sauvegarde()
    return True

def quittez():
    return False

menu= [{
    'indice':'1',
    'description':'créer une note',
    'func':ecrire_ue_notes
},{
    'indice':'2',
    'description':'afficher les notes',
    'func': afficher_ue_notes
},{
    'indice':'3',
    'description':'supprimer une note',
    'func': supp_note
},{
    'indice':'4',
    'description':'quittez',
    'func': quittez
}]

def menu_p():
    g=True
    while g:
        for element in menu:
            print(f"[{element['indice']}]  {element['description']}")
        print('Que veut tu faire ?')
        x=input("==>")
        for element in menu:
            if x == element['indice']:
                z=element['func']()
                if z is False:
                    g=False

menu_p()
