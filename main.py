import csv
import re

#dictionary of invalid letters for email addresses
replaceDictionary = {
    'ä': 'ae',
    'à': 'a',
    'â': 'a',
    'é': 'e',
    'è': 'e',
    'ê': 'e',
    'î': 'i',
    'ö': 'oe',
    'ô': 'o',
    'ü': 'ue',
    'û': 'u',
    'ù': 'u',
    'ß': 'ss'
    }

#generate email from 2 fields input
def nameToEmail(lastName, firstName):
    lastName = ''.join(lastName.split())
    lastName = replaceLetters(lastName)
    firstName = ''.join(firstName.split())
    firstName = replaceLetters(firstName)
    email = lastName + '.' + firstName + '@fh-swf.de'
    return email

#generate email from regex pattern input - not needed if .csv has seperate columns for first and last names
def nameToEmailRegex(name):
    nameRegex = re.compile(r'((\w*[\s-]*)*),\s((\w*[\s-]*)*)')
    data = nameRegex.search(name)
    lastName = data.group(1)
    lastName = ''.join(lastName.split())
    lastName = replaceLetters(lastName)
    firstName = data.group(3)
    firstName = ''.join(firstName.split())
    firstName = replaceLetters(firstName)
    email = lastName + '.' + firstName + '@fh-swf.de'
    return email

#replace invalid letters with entries from the replaceDictionary
def replaceLetters(word):
    for i in replaceDictionary.items():
        badLetter = i[0]
        replacedLetter = i[1]
        word = word.replace(badLetter, replacedLetter)
    return word


#main loop of the script
print('Dieses Script generiert aus der .csv der zur Prüfung angemeldeten Studenten eine für Moodle lesbare Tabellenversion zur automatischen Einschreibung für Prüfungskurse.')
print('Bitte stellen Sie sicher, dass die von Ihnen genutze .csv den Namen "liste.csv" trägt und nicht im Hintergrund geöffnet ist.')
enter = input('Möchten Sie das Programm starten? Bitte geben Sie "ja" oder "nein" ein und bestätigen Sie mit der Enter-Taste: ').lower()
if enter == 'ja':
    print('Vorgang wurde gestartet...')
    #reading input file
    inputFile = open('liste.csv')
    reader = csv.reader(inputFile, delimiter=';')
    #creating output file
    outputFile = open('moodle.csv', 'w', newline='')
    writer = csv.writer(outputFile)
    for row in reader:
        if reader.line_num == 1:
            continue
        lastName = str(row[2])
        lastName = lastName.lower()
        firstName = str(row[3])
        firstName = firstName.lower()
        email = nameToEmail(lastName, firstName)
        writer.writerow([email])
    print('Die neue Datei mit dem Namen "moodle.csv" wurde erfolgreich erstellt.')
    inputFile.close()
    outputFile.close()
elif enter == 'nein':
    print('Vorgang abgebrochen...')
else:
    print('Es konnte keine gültige Eingabe erkannt werden. Bitte starten Sie das Programm erneut...')

print('Sie können dieses Fenster nun schließen.')
exit()


