alleGäste = {'Alice': {'Äpfel': 5, 'Brätzel': 12},
	'Bob': {'Sandwiches': 5, 'Äpfel': 4}}

def insgesamt(Gäste, Gegenstände):
	anzahl = 0
	for  k, v in Gäste.items():
		anzahl = anzahl + v.get(Gegenstände,0)
	return anzahl

print('Äpfel ' + str(insgesamt(alleGäste, 'Äpfel')))
